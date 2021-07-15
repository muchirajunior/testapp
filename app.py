from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():

   return {"app":"running"}

@app.route("/junior")
def junior():
   
   return {"route":"junior!!!!!!!!"}

# app.run()
