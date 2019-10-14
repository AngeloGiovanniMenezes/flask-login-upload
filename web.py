from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, make_response, jsonify
import os

app = Flask(__name__)


@app.route("/upload", methods=["GET", "POST"])
def upload_video():

    if request.method == "POST":

        arquivo = request.files["file"]

        print("Arquivo Carregado")
        print(arquivo)

        res = make_response(jsonify({"mensagem": "Arquivo carregado"}), 200)

        return res

    return render_template("upload.html")
    
@app.route('/')
def home():

    if not session.get('logado'):
        return render_template('login.html')
    else:
        return redirect('upload')

@app.route('/login', methods=['POST'])
def do_admin_login():

    if request.form['usuario'] and request.form['senha'] == 'root':
        session['logado'] = True
    else:
        flash('Senha Errada,')
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
