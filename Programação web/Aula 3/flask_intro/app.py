from flask import Flask, render_template 
#cara que ira renderizar o html mexendo nas informações do python
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', titulo="Pagina Inicial", usuario="Godofredo")

if __name__ == "__main__":
    app.run(debug=True)
