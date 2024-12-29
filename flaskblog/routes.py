from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

# 模擬文章數據，用於測試
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# 路由 - 主頁
@app.route("/")
@app.route("/home")
def home():
    # 渲染 home.html，並將模擬的文章數據傳遞到模板
    return render_template('home.html', posts=posts)

# 路由 - 關於頁面
@app.route("/about")
def about():
    # 渲染 about.html，並傳遞 title 參數
    return render_template('about.html', title='About')

# 路由 - 註冊頁面
@app.route("/register", methods=['GET', 'POST'])
def register():
    # 創建註冊表單實例
    form = RegistrationForm()
    if form.validate_on_submit():
        # 如果表單通過驗證，顯示成功消息並重定向到主頁
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    # 渲染 register.html，並將表單傳遞到模板
    return render_template('register.html', title='Register', form=form)

# 路由 - 登入頁面
@app.route("/login", methods=['GET', 'POST'])
def login():
    # 創建登入表單實例
    form = LoginForm()
    if form.validate_on_submit():
        # 模擬登入驗證邏輯
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            # 如果驗證成功，顯示成功消息並重定向到主頁
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            # 如果驗證失敗，顯示錯誤消息
            flash('Login Unsuccessful. Please check username and password', 'danger')
    # 渲染 login.html，並將表單傳遞到模板
    return render_template('login.html', title='Login', form=form)
