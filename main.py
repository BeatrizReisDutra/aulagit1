from flask import Flask, render_template

meu_app = Flask(__name__)
@meu_app.route('/')
def inicio():
    return render_template('base.html')

if __name__ == "__main__":
    meu_app.run(port= 8000)
