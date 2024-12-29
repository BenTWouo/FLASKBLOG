from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# 定義註冊表單類別
class RegistrationForm(FlaskForm):
    # 使用者名稱欄位，必填，長度需在 2 到 20 個字元之間
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    # 電子郵件欄位，必填，必須符合電子郵件格式
    email = StringField('Email', validators=[DataRequired(), Email()])
    # 密碼欄位，必填
    password = PasswordField('Password', validators=[DataRequired()])
    # 確認密碼欄位，必填，必須與密碼欄位的值一致
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # 提交按鈕
    submit = SubmitField('Sign Up')

# 定義登入表單類別
class LoginForm(FlaskForm):
    # 電子郵件欄位，必填，必須符合電子郵件格式
    email = StringField('Email', validators=[DataRequired(), Email()])
    # 密碼欄位，必填
    password = PasswordField('Password', validators=[DataRequired()])
    # 記住我選項，布林值
    remember = BooleanField('Remember Me')
    # 提交按鈕
    submit = SubmitField('Login')
