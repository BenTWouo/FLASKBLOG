from flaskblog import app
# 從 flaskblog 模組中匯入 Flask 應用實例 app

# 檢查是否以主程序運行
if __name__ == '__main__':
    # 啟動 Flask 應用
    app.run(debug=True)
    # debug=True 開啟調試模式，允許即時重新加載和錯誤追蹤
