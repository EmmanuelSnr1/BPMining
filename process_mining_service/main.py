from flask import Flask
from api.process_discovery import process_discovery_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(process_discovery_bp, url_prefix='/api/process_discovery')

@app.route('/')
def home():
    return 'PROCESS MINING SERVER IS RUNNING'


if __name__ == '__main__':
    app.run(debug=True)



