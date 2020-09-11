from flask import Flask,render_template

app = Flask(__name__)

#主页
@app.route('/home')
def home():
    return render_template("home.html")

#笔记（列表页面）
@app.route('/note')
def note():
    return render_template("category.html")

#照片，暂时只有一个页面,后面做成下拉框
@app.route('/photo')
def photo():
    return render_template("single-gallery.html")

#视频，暂时只有一个视频，后面做成下拉框
@app.route('/video')
def video():
    return render_template("single-video.html")

#作者，个人信息页面
@app.route('/author')
def author():
    return render_template("author-no-sidebar.html")

#联系方式和留言
@app.route('/board')
def board():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run()
