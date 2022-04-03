from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    var = "Game, advinhe o número correto"
    if request.method == "GET":
        return render_template("index.html", var=var)
    else:
        numero = 0
        palpite = int(request.form.get("name"))

        if palpite == numero:
            return '<h1>Resultado: Você ganhou</h1>'
        else:
            return '<h1>Resultado: Não foi dessa vez</h1>'


@app.route('/sobre')
def sobre():
    return 'Sobre'


@app.route('/<string:nome>')
def error(nome):
    var = f'A página {nome} não existe!'
    return render_template("error.html", var=var)


if __name__ == '__main__':
    app.run()
