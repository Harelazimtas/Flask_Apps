from flask import Flask, render_template, jsonify, request, redirect, url_for
import json

app=Flask(__name__)

ENV='dev'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def user_create():
    return render_template('users.html')


@app.route('/insert_user',methods=["POST"])
def insert_user():
    req = request.get_json()
    print(req)
    return render_template("users.html")

@app.route('/admin/users',methods=["GET"])
def show_all():

    return render_template("show_user.html")

#@app.route('/submit',methods=['POST'])
#def submit():
#    if request.method=='POST':
#        Id=request.form['Id']
#        nickname=request.form['nickname']
 #       name=request.form['name']
  #      password=request.form['password']
   #     create_time=request.form['create_time']
    #    status=request.form['status']
     #   print(Id," ",name)
      #  return render_template('index.html')

if __name__== "__main__":
    app.debug=True
    app.run() 