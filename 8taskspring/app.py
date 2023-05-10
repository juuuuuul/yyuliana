
import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")


@app.route('/')
@app.route('/main', methods= ['POST', 'GET'])
def hello_name():
    if request.method == 'POST':
        name_param=request.form.get('name')

    elif request.method == 'GET':
        name_param=request.args.get('name')

    if name_param is None:
        name_param="Гость"

    return flask.render_template(
        'myprogramm.html',
        name=name_param,
        method=request.method
    )

if __name__ == '__main__':
   app.run(debug = True)
