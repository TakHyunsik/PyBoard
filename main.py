# main.py
import __init__
from flask import Flask, render_template, request, redirect, url_for

flask_path = __init__.root_path
print(flask_path / "templates")
# APP init
app = Flask(
    __name__,
    # static_folder= str(flask_path/"Views"/"static"),
    template_folder=str(flask_path / "templates"),
)


# 루트 라우트
@app.route("/")
def index():
    return redirect(url_for("create_post_form"))


# 게시물 생성을 위한 폼 페이지 라우트
@app.route("/create_post", methods=["GET"])
def create_post_form():
    return render_template("create_post.html")


# 게시물 생성 처리 라우트
@app.route("/create_post", methods=["POST"])
def create_post():
    title = request.form["title"]
    content = request.form["content"]
    # 여기서는 게시물을 생성하는 로직을 추가할 수 있습니다. (데이터베이스에 저장 등)
    # 이 예제에서는 생성된 데이터를 콘솔에 출력합니다.
    print(f"Title: {title}, Content: {content}")
    # 생성이 완료되면 홈 페이지로 리다이렉트합니다.
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
