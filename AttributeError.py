# AttributeError.py

from app import create_app  # 导入create_app
from app.models import Role, User
from app.extensions import db

app = create_app()  # 创建应用


@app.shell_context_processor  # Flask内置的shell上下文装饰器
def make_shell_context():
    return dict(db=db, Role=Role, User=User)  # 返回包含所有模型的字典


@app.cli.command()  # Flask集成了click，我们可以使用它的命令来轻松创建命令行命令
def deploy():
    """Deploy the application"""
    Role.insert_role()


if __name__ == '__main__':
    app.run(debug=True)  # 运行应用，并开启调试模式
