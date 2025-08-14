from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-very-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///candidates.db'
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        candidate = Candidate(name=form.name.data, email=form.email.data)
        db.session.add(candidate)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('home'))
    return render_template('index.html', form=form)

@app.route('/api/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)