from flask import Flask

meu_app = Flask(__name__)
@meu_app.route('/')
def inicio():
    return 'Olá, turma!. Sou o Flask'

if __name__ == "__main__":
    meu_app.run(port= 8000)
