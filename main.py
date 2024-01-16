from flask import Flask, render_template, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, AnyOf, EqualTo
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = '12345678'


class LoginForm(FlaskForm):
    username = StringField('email', validators=[InputRequired(), Email(message='Email не правильний.')])
    password = PasswordField('password', validators=[
        InputRequired(message='Пароль обов\'язковий для заповнення.'),
        Length(min=5, max=10, message='Пароль повинен бути від 5 до 10 символів.'),
        AnyOf(['secret', 'password'], message='Не правильний пароль.')
    ])
    password1 = PasswordField('password2', validators=[
        InputRequired(message='Пароль повинен будти однаковий, як минулий.'),
        Length(min=5, max=10, message='Пароль повинен бути від 5 до 10 символів.'),
        AnyOf(['secret', 'password'], message='Не правильний пароль.'),
        EqualTo('password', message='Паролі повинні співпадати.')
    ])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        session['username'] = username
        return render_template('home.html', username=username)
    return render_template('index.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)