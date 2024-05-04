# main.py
import __init__
from typing import Dict
from datetime import datetime
from math import ceil
from flask import Flask, render_template, request, redirect, url_for

from result import Result, Ok, Err
from icecream import ic

from Domains.Posts import Post
from Applications.Posts import *
from IoC.container import Container, post_memory

flask_path = __init__.root_path / "Flask"
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
    return redirect(url_for("get_posts", page=1))


# 게시글 리스트 조회
@app.route("/post/list/<int:page>", methods=["GET"])
def get_posts(page):
    # 페이지 번호를 이용하여 해당 페이지의 게시글 리스트를 조회하고 HTML 파일을 렌더링하여 클라이언트에게 반환
    size = 3
    page = max(page - 1, 0)
    match Container().read_post_service().read_posts_by_reverse_sequence(
        page=page, size=size
    ):
        case Ok((post_num, post_list)):
            return render_template(
                "post_list.html",
                posts=post_list,
                page=page + 1,
                total_pages=ceil(post_num / size),
            )
        case Err(msg):
            return render_template("error.html", error=msg), 400
        case err:
            print(err, ":get_post", page)
            return render_template("error.html", error="Error"), 404


# 게시글 상세 조회
@app.route("/post/detail/<post_id>", methods=["GET"])
def get_post(post_id):
    match Container().read_post_service().read_post_by_post_id(post_id=post_id):
        case post if isinstance(post, Post):
            return render_template("post_detail.html", post=post)
        case _:
            return render_template("error.html", error="Post not found"), 404


# 게시물 생성을 위한 폼 페이지 라우트
@app.route("/create_post", methods=["GET"])
def create_post_form():
    return render_template("post_create.html")


# 게시물 생성 처리 라우트
@app.route("/create_post", methods=["POST"])
def create_post():
    title = request.form["title"]
    content = request.form["content"]
    create_time = datetime.now()

    # 여기서는 게시물을 생성하는 로직을 추가할 수 있습니다. (데이터베이스에 저장 등)
    create_post_service = Container().create_post_service()

    match create_post_service.create(
        title=title, content=content, create_time=create_time
    ):
        case Ok(pid):
            # 생성이 완료되면 홈 페이지로 리다이렉트합니다.
            return redirect(url_for("index"))
        case Err(msg):
            return render_template("error.html", error=msg), 400


def init_post():
    create_post = Container().create_post_service()
    match create_post.create(
        title="첫번째 글",
        content="이것을 보았다는 것은 게시판이 잘 만들어 졌다는 것입니다.",
    ):
        case Ok(pid):
            pass

    match create_post.create(
        title="두번째 글",
        content="이것을 보았다는 것은 테스트를 잘 진행하고 있다는 것입니다.",
    ):
        case Ok(pid):
            pass

    match create_post.create(
        title="세번째 글",
        content="이것을 보았다는 것은 할짓이 드럽게도 없다는 것입니다.",
    ):
        case Ok(pid):
            pass


if __name__ == "__main__":
    init_post()
    app.run(debug=True)
