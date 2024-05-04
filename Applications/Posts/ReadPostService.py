import __init__
from typing import Optional, Tuple, List
from result import Result, Ok

from Domains.Posts import Post, PostID, PostIDBuilder
from Domains.Posts.Repository import ISelectablePost

from icecream import ic


class ReadPostService:
    def __init__(
        self,
        get_post_repo: ISelectablePost,
    ):
        assert issubclass(
            type(get_post_repo), ISelectablePost
        ), "get_post_repo must be a class that inherits from ISelectablePost."

        self.get_post_repo = get_post_repo

    def read_post_by_post_id(
        self,
        post_id: str,
    ) -> Optional[Post]:
        match PostIDBuilder().set_str_uuid(post_id).map(lambda b: b.build()):
            case Ok(id):
                post_id = id
            case err:
                ic(err)
                return None

        assert isinstance(post_id, PostID), "Type of post_id is PostID. Not Converted"
        return self.get_post_repo.get_post_by_post_id(post_id=post_id)

    def read_posts_by_reverse_sequence(
        self,
        page=0,
        size=10,
    ) -> Result[Tuple[int, List[Post]], str]:
        return self.get_post_repo.get_posts_by_reverse_sequence(
            page=page,
            size=size,
        )
