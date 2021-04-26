from flask import Flask
from flask import url_for, redirect, render_template, request

import pymysql
from DataStore.GAB_MySQL import GAB_MySQL

import make_pic



dns = {
    "host": "localhost",
    "user": "sora",
    "password": "monster",
    "db": "good_anime_bu"
}

con = GAB_MySQL(**dns)

app = Flask(__name__)


@app.after_request
def add_header(r):
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Contorl'] = 'public, max-age=0'
        return r



@app.route("/")
def main():
    #dbから情報（テーブル）のあるcoolを取ってくる
    cool_list = con.all_cool()

    html = render_template("main.html", cool_list=cool_list)

    return html


@app.route("/anime/<string:cool>", methods=["POST", "GET"])
def all_cool(cool): 

    if request.method == "POST":

        anime_num = con.count_cool_anime(cool)
        anime_check_list = request.form.getlist("anime")

        #tempファイルとして画像生成したい
        cool_view = con.select_cool(cool)[1]
        tmpdir = make_pic.make_user_pic(cool, cool_view, anime_num,anime_check_list)

        #html = render_template("generator_result.html", path=tmpdir, cool=cool)

        #return redirect(url_for("gen_result", cool=cool))

        return render_template("generator_result.html", path=tmpdir+"/", cool=cool)

        #return html

        

    #cool_list = con.all_cool()
    result = con.select_cool(cool)

    if request.method == "GET":
        anime_num = con.count_cool_anime(cool)
        pic_path = "../../static/"+cool+"/"
        html = render_template("anime_generator.html", path=pic_path, cool=result, anime_num=anime_num)
        
        return html

    #if cool in cool_list:
    #    pic_path = ("static/"+cool+"/")
    #    html = render_template("anime_generator.html", path=pic_path)

    #    return html


#@app.route("/anime/user/<string:cool>/result", methods=["POST","GET"])
#def gen_result(cool):
    #data_dir = "../../../user/"+cool
    #data_dir = "../../../static/user/"+cool
    #return render_template("generator_result.html",path=data_dir, cool=cool)



if __name__ =="__main__":
    app.run(debug=True)
