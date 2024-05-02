import sys
from pathlib import Path

now_path = Path(__file__).resolve().parent
root_path = now_path.parent.parent

if not (str(root_path) in sys.path):
    sys.path.append(str(root_path))

from Domains.Posts.Post import (
    Post,
    PostBuilder,
    PostID,
    PostIDBuilder,
)

__all__=[
    "Post",
    "PostBuilder",
    "PostID",
    "PostIDBuilder",
]