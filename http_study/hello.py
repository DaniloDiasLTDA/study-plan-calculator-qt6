from flask import Flask, request, render_template

app = Flask(__name__, template_folder='./templates')


@app.route('/')
def index():
    # todo: helphcheck
    return 'Index Page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        try:
            # json_study.parse()
            raise Exception('NotImplemented')
        except Exception as e:
            print('Error: ' + str(e))
            return render_template("500_generic.html",), 500
    else:
        return 'NotImplemented'
