from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f"""<h1>Show de Horror!!!<br><h2>Parece ruim mais é bom<br>"""