Title: nginx + gunicorn + supervisior + flask 部署 python web
Date: 2015-09-13 10:00
Modified: 2015-09-13 10:00
Category: it
Tags: python,web,nginx,gunicorn,supervisior,flask
Slug: deploy-python-web
Author: caimaoy


# 简介

- 最近离职休假，在家研究 python 的 web 框架
- 本来是要来 tornado 的，但是因为 Falsk 文档更为齐全，并且更易上手，所以先来了flask
- 做了一个小 web 之后就想发布，看了一下官方文档说了 Heroku 云服务和其他的 VPS，于是上Heroku 上面去折腾了一番
- 除了 git 和 Heroku 自己的东西，中间在启动的时候有如下代码：

```
web: gunicorn gettingstarted.wsgi --log-file -
```

- gunicorn 是什么？
- 继续 google 发现了一套比较通用的部署 python web app 的解决方案
- nginx + gunicorn + supervisior + flask 来吧在本地折腾一番吧

# 大体介绍

## 创建一个项目

```
mkdir myproject
```

## 创建 python 虚拟环境
- virtualenv is a tool to create isolated Python environments.
- 不同项目完全隔离的 python 虚拟环境

```
mkdir myproject
cd myproject
virtualenv venv
```

- 使用 venv 环境

```
source venv/bin/activate
```

## 安装 python web 框架 flask

- Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD licensed!
- 使用 pip 安装 flask

```
pip install flask
```

- mpapp.py 文件

```
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
if __name__ == '__main__':
    app.debug = True
    app.run()
```

- 启动flask
```
python myapp.py
```

- 正常情况下可以在浏览器中访问 <http://127.0.0.1:5000> 查看到 hello world

## 使用 gunicorn 部署 python web
- Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.
- 安装 gunicorn
```
pip install gunicorn
```

- pip 是用于 python 的包管理工具
- 我们现在在这个项目中又安装了新的 python 库，所以我们需要记录在 requirements.txt 文件中
- 这样方便方便别人部署

```
pip freeze > requirements.txt
```

- 当我们安装好 gunicorn 之后，需要用 gunicorn 启动 flask
- 注意 flask 里面的name 里面的代码启动了 app.run()
- 这个含义是用 flask 自带的服务器启动 app
- 这里我们使用了 gunicorn，myapp.py 就等同于一个库文件，被 gunicorn 调用

```
gunicron -w4 -b0.0.0.0:8000 myapp:app
```

- 此时，我们需要用 8000 的端口进行访问，原先的5000 并没有启用
- 其中 gunicorn 的部署中，-w 表示开启多少个 worker
- b 表示 gunicorn 开发的访问地址
- 想要结束 gunicorn 只需执行 pkill gunicorn
- 有时候还的 ps 找到 pid 进程号才能 kill
- 可是这对于一个开发来说，太过于繁琐，因此出现了另外一个神器---supervisor
- 一个专门用来管理进程的工具，还可以管理系统的工具进程
- 到此 python web 应用 可以正常使用
- 之后的进程管理和 nginx 部署还够写很多，之后再见
