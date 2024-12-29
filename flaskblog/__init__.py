from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 創建 Flask 應用實例
app = Flask(__name__)

# 配置 Flask 應用的密鑰（用於加密 session 資料和其他安全相關操作）
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# 配置資料庫 URI，這裡使用 SQLite，資料庫文件名為 site.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# 初始化 SQLAlchemy，將資料庫與 Flask 應用連接
db = SQLAlchemy(app)

# 從 flaskblog 模組中導入 routes（路由設定和功能實現）
from flaskblog import routes
