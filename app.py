from flask import Flask, render_template, request, redirect, url_for
from pony.orm import db_session, select
from models import db, Roupa

app = Flask(__name__)

@app.route('/')
@db_session
def index():
    roupas = select(r for r in Roupa)[:]
    return render_template('index.html', roupas=roupas)

@app.route('/adicionar', methods=['GET', 'POST'])
@db_session
def adicionar_roupa():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        tamanho = request.form['tamanho']
        
        Roupa(nome=nome, categoria=categoria, tamanho=tamanho)
        db.commit()
        return redirect(url_for('index'))
    
    return render_template('add_item.html')

if __name__ == '__main__':
    app.run(debug=True)
