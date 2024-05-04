# IoC.container.py
import __init__
from dependency_injector import containers, providers

from Domains.Posts.Repository import IInsertablePost
from Domains.Posts import Post
from Applications.Posts import *
from IoC.InMemory.Posts import *

class Container(containers.DeclarativeContainer):
    
    insertable_post_repo = providers.Singleton(
        InMemoryInsertPostStorage
    )

    selectable_post_repo = providers.Singleton(
        InMemorySelectPostStorage
    )

    create_post_service = providers.Factory(
        CreatePostService,
        insert_post_repo=insertable_post_repo,
    )

    read_post_service = providers.Factory(
        ReadPostService,
        get_post_repo=selectable_post_repo,        
    )
