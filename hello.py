from flask import Flask, render_template, request
import pymysql,language,db

app = Flask(__name__)

@app.route("/", methods =['POST','GET'])
def hello():
	html = render_template('index.html')
	return html


@app.route("/send", methods=["POST"])
def lang():
	get_value = request.form.get("bunsyo")
	lang = language.language(get_value)
	db_init(lang.run(),get_value)
	return render_template("send.html",lang=get_value,score=lang.run())


def db_init(score,value):
	DB = db.db(score,value)
	DB.db_table_insert(score,value)
	


if __name__ == "__main__":
	app.run(debug=True)


