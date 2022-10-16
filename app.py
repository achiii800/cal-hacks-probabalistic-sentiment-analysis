from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


@app.route('/')
def index():
   return render_template('stonks.html')

@app.route('/ProcessorUserinfo/<string:userinfo>',methods=['POST'])
def ProcessUserInfo(userinfo):
   userinfo=json.loads(userinfo)
   username=userinfo
   print()
   print(username)
   print()
   return(username)


if __name__ == "__main__":
   app.run(debug=True)

