from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
  return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
           def main():
             r = request.form.get("name")
             return(render_temmplate("main.htlm",r=r))

@app.route("/main",methods=["GET","POST"])
           def main():
           return(render_temmplate("image.GPT.htlm",r=r))
if __name__ == "__main__":
  app.run()
