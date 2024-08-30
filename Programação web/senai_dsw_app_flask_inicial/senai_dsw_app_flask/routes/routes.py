from flask import render_template, request, redirect, url_for, session, flash
from forms.forms import ContatoForm  # Importa o formulário
import os 

def configurar_rotas(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/Web-Forms', methods=['GET', 'POST'])
    def web_form():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            idade = request.form['idade']
            mensagem = request.form['mensagem']
            
            # Aqui você pode processar os dados do formulário, 
            #como salvar em um banco de dados ou enviar um e-mail.
            print(f"Nome: {nome}, Email: {email}, Idade: {idade}, Mensagem: {mensagem}")
            
            return redirect(url_for('obrigado_1'))
        
        return render_template('web_forms.html')

    @app.route('/Web-Forms-WTF', methods=['GET', 'POST'])
    def web_forms_wtf():
        formulario = ContatoForm()
        if formulario.validate_on_submit():
            contato = {
                'nome': formulario.nome.data,
                'email': formulario.email.data,
                'idade': formulario.idade.data,
                'mensagem': formulario.mensagem.data
            }
            
            session['contato'] = contato # Armazena os dados na sessão
        
            return redirect(url_for('obrigado_2'))        
        
        return render_template('web_forms_wtf.html', formulario=formulario)

    @app.route('/upload-arquivo', methods=['GET', 'POST'])
    def upload_arquivo():
        if request.method == 'POST':
            if 'arquivo' not in request.files:
                flash('Nenhum arquivo foi selecionado.')
                return redirect(url_for('upload_arquivo'))
            
            arquivo = request.files['arquivo']
            
            if arquivo.filename== '':
                flash('Nenhum arquivo foi selecionado')
                return redirect(url_for('upload_arquivo'))
            
            if arquivo:
                nome_arquivo = arquivo.filename
                caminho_arquivo = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)
                try:
                    arquivo.save(caminho_arquivo)
                    flash(f'Arquivo {nome_arquivo} enviado')
                    
                except Exception as e:
                    flash(f'Erro ao salvar o arquivo meu mano: {e}')
                return redirect(url_for('upload_arquivo'))
            
            #se o metodo for get renderiza a pagina de upload :b   
            
            
        return render_template('upload_arquivo.html')

    @app.route('/CRUD-Simples')
    def crud_simples():
        return render_template('crud_simples.html')

    @app.route('/CRUD-SQL')
    def crud_sql():
        return render_template('crud_sql.html')

    @app.route('/CRUD-SQLAlchemy')
    def crud_sqlalchemy():
        return render_template('crud_sqlalchemy.html')
    
    @app.route('/sobre')
    def sobre():
        return render_template('sobre.html')

    @app.route('/contato')
    def contato():
        return render_template('contato.html')
    
    @app.route('/obrigado-1')
    def obrigado_1():
        return render_template('obrigado_1.html')
    
    @app.route('/obrigado-2')
    def obrigado_2():
        contato = session.get('contato', None)  # Recupera os dados da sessão
        if contato is None:
            # Redireciona para a página do formulário se não houver dados
            return redirect(url_for('web_forms_wtf'))
        # Limpa a sessão após o uso
        session.clear()
        return render_template('obrigado_2.html', contato=contato)
