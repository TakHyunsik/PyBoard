# IoC.InMemory.Posts.py
import __init__
from typing import Optional, List, Tuple, Dict
from result import Result, Ok, Err

from Domains.Posts.Repository import *
from Domains.Posts import Post, PostID, PostIDBuilder, PostBuilder

from icecream import ic

post_memory: Dict[str, Post] = {}


class InMemorySelectPostStorage(ISelectablePost):
    def __init__(self):
        self.posts = post_memory

    def get_post_by_post_id(self, post_id: PostID) -> Optional[Post]:
        """주어진 게시물 ID에 해당하는 게시물을 반환합니다.

        Args:
            post_id (PostID): 게시물을 식별하는 고유한 ID입니다.

        Returns:
            Optional[Post]: 주어진 ID에 해당하는 게시물 객체를 반환합니다.
                            만약 해당 ID에 해당하는 게시물이 존재하지 않는 경우 None을 반환합니다.
        """
        return self.posts.get(post_id.get_id())

    def get_posts_by_reverse_sequence(
        self,
        page=0,
        size=10,
    ) -> Result[Tuple[int, List[Post]], str]:
        """역순으로 정렬된 페이지별 게시물 목록을 가져옵니다.

        Args:
            page (int, optional): 가져올 페이지의 번호입니다. 기본값은 0입니다.
            size (int, optional): 페이지당 게시물 수입니다. 기본값은 10입니다.

        Returns:
            Result[Tuple[int, List[Post]], str]:
                게시물 목록을 가져오는 데 성공하면 Ok를 반환하고,
                (전체 게시물 수, 현재 페이지의 게시물 목록)로 구성된 튜플을 반환합니다.
                가져오기에 실패하면 Err을 반환하고, 실패 이유를 문자열로 반환합니다.
        """
        posts_list = list(self.posts.values())
        total_count = len(posts_list)
        # start_index와 end_index를 계산하여 리스트의 일부를 가져옵니다.
        start_index = max(total_count - (page + 1) * size, 0)
        end_index = max(total_count - page * size, 0)
        posts_on_page = posts_list[start_index:end_index][::-1]  # 역순으로 반환
        try:
            return Ok((total_count, posts_on_page))
        except:
            return Err("out of range")


class InMemoryInsertPostStorage(IInsertablePost):
    def __init__(self):
        self.posts = post_memory

    def insert_post(self, post: Post) -> Result[PostID, str]:
        new_post = PostBuilder(
            uuid=post.id.uuid,
            seq=len(self.posts) + 1,
            title=post.title,
            content=post.content,
            create_time=post.create_time,
        ).build()
        self.posts[post.get_id()] = new_post
        return Ok(new_post.id)


__all__ = [
    "post_memory",
    "InMemoryInsertPostStorage",
    "InMemorySelectPostStorage",
]
