# configs/app.py
from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates',static_folder='../static')

@app.route('/')
def index():
    return render_template('front_pages/index.html')

@app.route('/planos_formacao')
def planos_formacao():
    return render_template('front_pages/planos_formacao.html')

@app.route('/legislacao')
def legislacao():
    return render_template('front_pages/legislacao.html')

@app.route('/upload_legislation', methods=['POST'])
def upload_legislation():
    # handle file and description upload
    return 

@app.route('/pessoal_docente')
def pessoal_docente():
    return render_template('front_pages/pessoal_docente.html')

@app.route('/upload_form', methods=['POST'])
def upload_form():
    
    # Handle saving logic
    return   # or another route

@app.route('/pessoal_acao_educativa')
def pessoal_acc_educativa():
    return render_template('front_pages/pessoal_acc_educativa.html')

@app.route('/contactos')
def contactos():
    return render_template('front_pages/contactos.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.html')