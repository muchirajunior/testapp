from flask import Flask,request,json,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://muchirajn@muchiradb:junior_12@muchiradb.postgres.database.azure.com:5432/testdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"]="34etrgfjkliop8iuyhg"

db=SQLAlchemy(app)
ma=Marshmallow(app)

class Users(db.Model):
       id=db.Column(db.Integer,primary_key=True)
       name=db.Column(db.String(100))
       email=db.Column(db.String(50))
       password=db.Column(db.String(20))

       def __init__(self,name,email,password):
              self.name=name
              self.email=email
              self.password=password

class UserSchema(ma.Schema):
       class Meta:
              fields=('name','email')

usershema=UserSchema(many=True)

@app.route("/")
def index():

   return {"app":"running"}

@app.route("/junior")
def junior():
  
   return {"name":"muchira junior!!!!!!!!"}

@app.route("/adduser",methods=["POST"])
def adduser():
       try:
           name=request.json['name']
           email=request.json['email']
           password=request.json['password']
          
           newuser=Users(name,email,password)

           db.session.add(newuser)
           db.session.commit()

           return {"feedback":"success"}
       except:
           return {"feedback":"failed"}

@app.route("/allusers")
def allusers():
       users=Users.query.all()
       users=usershema.dump(users)

       return usershema.jsonify(users)
 