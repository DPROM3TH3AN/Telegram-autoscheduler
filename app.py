from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from telethon import TelegramClient
import os
from dotenv import load_dotenv
from datetime import datetime
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Initialize Telegram client
client = TelegramClient('telegram_scheduler_session',
                       int(os.getenv('API_ID')),
                       os.getenv('API_HASH'))

# Database models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class ScheduledMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    groups = db.Column(db.Text, nullable=False)  # JSON string of group IDs
    schedule_time = db.Column(db.DateTime, nullable=False)
    repeat_type = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='pending')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/groups')
@login_required
def groups():
    async def get_groups():
        groups = []
        async for dialog in client.iter_dialogs():
            if dialog.is_group or dialog.is_channel:
                groups.append({
                    'id': dialog.id,
                    'name': dialog.name,
                })
        return groups
    
    groups = client.loop.run_until_complete(get_groups())
    return jsonify(groups)

@app.route('/schedule', methods=['POST'])
@login_required
def schedule_message():
    data = request.json
    
    # Validate inputs
    if not data.get('message') or not data.get('groups'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Create scheduled message
    scheduled_msg = ScheduledMessage(
        user_id=current_user.id,
        message=data['message'],
        groups=json.dumps(data['groups']),
        schedule_time=datetime.fromisoformat(data['schedule_time']),
        repeat_type=data.get('repeat_type', 'one-time')
    )
    
    db.session.add(scheduled_msg)
    db.session.commit()
    
    return jsonify({'status': 'success', 'id': scheduled_msg.id})

@app.route('/messages')
@login_required
def get_messages():
    messages = ScheduledMessage.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': msg.id,
        'message': msg.message,
        'groups': json.loads(msg.groups),
        'schedule_time': msg.schedule_time.isoformat(),
        'status': msg.status
    } for msg in messages])

def create_app():
    with app.app_context():
        db.create_all()
    return app

if __name__ == '__main__':
    create_app()
    client.start()
    app.run(debug=False)