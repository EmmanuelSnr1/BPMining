from flask import jsonify

def create_error_response(message, code=400):
    return jsonify({'error': message}), code
