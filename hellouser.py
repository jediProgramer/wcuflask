from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hellouser.html', name = user)

if __name__ == '__main__':
   app.run(debug = True)