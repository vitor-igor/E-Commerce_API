from flask import Flask

app = Flask(__name__)

# Rota raiz (página inicial) e a função executada ao requisitar
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug = True)