# app.py

from app import create_app  # 导入create_app

app = create_app()  # 创建应用

if __name__ == '__main__':
    app.run(debug=True)  # 运行应用，并开启调试模式
