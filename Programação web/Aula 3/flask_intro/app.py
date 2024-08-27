from flask import Flask, render_template 
#cara que ira renderizar o html mexendo nas informações do python
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', titulo="Pagina Inicial", usuario="Godofredo")
@app.route('/controle_fluxo_condicionais')
def controle_fluxo_condicionais():
    usuario ={
        'nome': 'Gustavo',
        'idade': 4,
        'cidade': 'jaragua do sul',
        'premium': True
    }
    return render_template('controle_fluxo_condicionais.html', usuario=usuario)

if __name__ == "__main__":
    app.run(debug=True)
