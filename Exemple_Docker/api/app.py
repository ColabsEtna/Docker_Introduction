from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://db_user:db_password@db:5432/db_name'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    return 'API is running!'

@app.route('/users')
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append({'id': user.id, 'username': user.username, 'email': user.email})
    return jsonify(user_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
