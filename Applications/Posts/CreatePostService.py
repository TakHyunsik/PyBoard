# Applications.Posts.CreatePostService.py
import __init__
from typing import Optional
from datetime import datetime
from result import Result

from Domains.Posts import Post, PostID, PostBuilder
from Domains.Posts.Repository import IInsertablePost


class CreatePostService:
    def __init__(
        self,
        insert_post_repo: IInsertablePost,
    ):
        assert issubclass(
            type(insert_post_repo), IInsertablePost
        ), "insert_post_repo must be a class that inherits from IInsertablePost."

        self.insert_post_repo = insert_post_repo

    def create(
        self,
        title: str,
        content: str,
        create_time: Optional[datetime] = None,
    ) -> Result[PostID, str]:
        """새로운 게시물을 생성합니다.

        Args:
            title (str): 게시물의 제목입니다.
            content (str): 게시물의 내용입니다.
            create_time (Optional[datetime], optional): 게시물을 생성한 시간입니다.
                기본값은 None이며, 현재 시간이 사용됩니다. Defaults to None.

        Returns:
            Result[PostID, str]: 게시물 생성에 성공하면 Ok를 반환하고, 새로운 게시물의 ID를 포함합니다.
                                실패하면 Err를 반환하고, 실패 이유를 문자열로 반환합니다.
        """
        post = (
            PostBuilder()
            .set_uuid()
            .set_title(title)
            .set_create_time(create_time)
            .set_content(content)
            .build()
        )
        print("create", post)
        return self.insert_post_repo.insert_post(post)
