from datetime import datetime
from flaskblog import db  # 匯入 SQLAlchemy 的資料庫實例

# 定義 User 類別，表示使用者
class User(db.Model):  # 繼承 SQLAlchemy 的 Model 類別
    # 使用者 ID，主鍵，整數類型
    id = db.Column(db.Integer, primary_key=True)
    # 使用者名稱，字串長度限制為 20，必填且唯一
    username = db.Column(db.String(20), unique=True, nullable=False)
    # 電子郵件，字串長度限制為 120，必填且唯一
    email = db.Column(db.String(120), unique=True, nullable=False)
    # 頭像檔案名稱，字串長度限制為 20，必填，預設為 'default.jpg'
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # 密碼，字串長度限制為 60，必填
    password = db.Column(db.String(60), nullable=False)
    # 與 Post 表的關聯關係，用於獲取該使用者的所有文章
    posts = db.relationship('Post', backref='author', lazy=True)

    # 定義物件的字串表示形式
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# 定義 Post 類別，表示文章
class Post(db.Model):  # 繼承 SQLAlchemy 的 Model 類別
    # 文章 ID，主鍵，整數類型
    id = db.Column(db.Integer, primary_key=True)
    # 文章標題，字串長度限制為 100，必填
    title = db.Column(db.String(100), nullable=False)
    # 發布日期，DateTime 類型，必填，預設值為當前 UTC 時間
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # 文章內容，Text 類型，必填
    content = db.Column(db.Text, nullable=False)
    # 與 User 表的關聯，指向 user.id，必填
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # 定義物件的字串表示形式
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
