from flask import Flask, render_template, jsonify, request, redirect, url_for
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time

app=Flask(__name__)

ENV='dev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://eunamewfsidzet:3dc1416abf5e68aca5f4dec3695b6f57153fa05655c027fabfe186c3b0b6cf7b@ec2-50-17-21-170.compute-1.amazonaws.com:5432/d5ukkd9etal4nu'

db = SQLAlchemy(app)
#db.create_all()

class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(200))
    name = db.Column(db.String(200))
    password = db.Column(db.String(200))
    create_time = db.Column(db.DateTime,default=datetime.now)
    status = db.Column(db.Integer)

    def __init__(self, id, nickname, name, password,create_time,status):
        self.id = id
        self.nickname = nickname
        self.name = name
        self.password = password
        self.create_time=create_time
        self.status = status

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def user_create():
    return render_template('users.html')


@app.route('/insert_user',methods=["POST"])
def insert_user():
    req = request.get_json()
    req['create_time']=datetime.now()
    print(req)
    user = users(id=req['id'], nickname=req['nickname'],name=req['name'],password=req['password'],create_time=req['create_time'],status=req['status'])
    db.session.add(user)
    db.session.commit()
    return req

@app.route('/admin/users',methods=["GET"])
def show_all():
    all_user = users.query.all()
    json={}
    return all_user

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
    db.create_all()
    app.debug=True
    app.run() 