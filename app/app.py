from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>🚀 Deploy via Render com CI/CD</h1><p>Aplicação Flask funcionando!</p>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)