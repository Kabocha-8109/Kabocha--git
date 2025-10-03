# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/hola")
def hola():
    return 'HOLA 1239788787878'

@app.route('/user/<string:username>', methods=['GET'])
def show_user_name(username):
    print ('type(username)=> ', type(username))
    return 'String => {} '.format(username)

@app.route('/user/<int:id>', methods=['GET'])
def show_user_id(id):
    print ('type(id)=> ', type(id))
    return 'int => {} '.format(id)

@app.route('/user/<float:version>', methods=['GET'])
def show_user_version(version):
    print ('type(version)=> ', type(version))
    return 'float => {} '.format(version)

@app.route('/appinfo')
def show_appinfo():
    return '<html><body><h1>APPINFO</h1></body></html>'

@app.route('/htmlinfo')
def show_htmlinfo():
    return render_template('home.html', text='jerry')

@app.route('/appinfo/appinfo')
def Appinfo():
    appio = {
        'app_id':'25.1001',
        'app_name':'Flask'
    }
    return render_template('home.html', AppInfo=appio)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)