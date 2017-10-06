from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def home():
    return ("hola mundo")

@app.route('/parm')
def parametro():
    p1 = request.args.get('param1','no hay nada')
    p2 = request.args.get('param2','no hay nada')
    return ('Los parametros son {} {}'.format(p1,p2))

# validation de entrada de url
@app.route('/validation/<name>')
@app.route('/validation/<name>/<lastname>')
def validation(name ='Error al ingresar nombre',lastname='Error al ingresar apellido'):
    #return ('Tu nombre {} {}'.format(name, lastname))
    return render_template('index.html',name= name)


@app.route('/landing')
def landing():
    list_project = {
        'python':'proyecto django',
        'laravel':'Blog',
        'nodejs':'Sistema Ventas',
        'android':'Juego'
    }

    return render_template('project.html', projects = list_project)

if __name__ =='__main__':
    app.run(debug=True, port=8000)
