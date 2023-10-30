from flask import Flask, jsonify
from injector import inject, Injector, singleton
from domain.user import User
from application.user_repository import UserService, InMemoryUserRepository

# Set up the Injector instance
def configure(binder):
    binder.bind(UserService, to=UserService, scope=singleton)

injector = Injector([configure])

app = Flask(__name__)
app.config['INJECTOR'] = injector

@app.route('/ping')
def ping():
    return 'pong'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)