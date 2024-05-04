# Domains.Posts.Pepository.py
import __init__
from abc import ABC, abstractmethod
from typing import Optional, List, Tuple
from result import Result

from Domains.Posts import Post, PostID

class ISelectablePost(ABC):
    
    @abstractmethod
    def get_post_by_post_id(self, post_id: PostID) -> Optional[Post]: 
        """주어진 게시물 ID에 해당하는 게시물을 반환합니다.

        Args:
            post_id (PostID): 게시물을 식별하는 고유한 ID입니다.

        Returns:
            Optional[Post]: 주어진 ID에 해당하는 게시물 객체를 반환합니다.
                            만약 해당 ID에 해당하는 게시물이 존재하지 않는 경우 None을 반환합니다.
        """
        ...

    @abstractmethod
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
        ...

class IInsertablePost():
    @abstractmethod
    def insert_post(self, post:Post) -> Result[PostID, str]: ...