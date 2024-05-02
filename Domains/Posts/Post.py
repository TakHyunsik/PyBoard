import __init__
from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
from typing import Optional, Self
from datetime import datetime
from uuid import UUID, uuid4

from Domains.ID import ID, IDBuilder


@dataclass(frozen=True)
class PostID(ID):
    uuid: UUID
    seq: Optional[int]

    def get_id(self) -> str:
        return self.uuid.hex

    def get_seq(self) -> Optional[int]:
        return self.seq


@dataclass(frozen=True)
class Post(ID):
    id: PostID
    title: str
    content: str
    create_time: datetime
    
    def get_id(self) -> str:
        return self.id.get_id()
    
    def get_seq(self) -> Optional[int]:
        return self.id.get_seq()
    

class PostIDBuilder(IDBuilder):
    def build(self) -> PostID:
        assert isinstance(self.uuid, UUID), "You didn't set the uuid."
        assert isinstance(self.seq, int) or self.seq is None, "Type of seq is INT or None."

        return PostID(
            uuid=self.uuid,
            seq=self.seq,
        )

@dataclass
class PostBuilder(IDBuilder):
    title: Optional[str]=None
    content: Optional[str]=None
    create_time: Optional[datetime]=None

    def set_id(self, id:PostID)->Self:
        assert self.uuid is None, "id alredy set."
        assert isinstance(id, PostID), "Type of id is PostID."
        assert isinstance(id.uuid, UUID), "Type of id is PostID."
        
        self.uuid = id.uuid
        self.seq = id.seq
        return self

    def set_title(self, title:str)->Self:
        assert self.title is None, "title alredy set."
        assert isinstance(title, str), "Type of title is str."
        
        self.title = title
        return self
    
    def set_content(self, content:str)->Self:
        assert self.content is None, "content alredy set."
        assert isinstance(content, str), "Type of content is str."
        
        self.content = content
        return self
    
    def set_create_time(self, create_time:Optional[datetime]=None)->Self:
        assert self.create_time is None, "create_time alredy set."
        if create_time is None:
            create_time = datetime.now()           
        
        assert isinstance(create_time, datetime), "Type of create_time is datetime."
        
        self.create_time = create_time
        return self
    
    def build(self)->Post:
        assert isinstance(self.uuid, UUID), "You didn't set the uuid."
        assert isinstance(self.seq, int) or self.seq is None, "Type of seq is INT or None."
        assert isinstance(self.title, str) , "title not set. plz str."
        assert isinstance(self.content, str) , "content not set. plz str."
        assert isinstance(self.create_time, datetime) , "create_time not set. plz datetime."

        return Post(
            id = PostID( uuid=self.uuid, seq=self.seq),
            title= self.title,
            content= self.content,
            create_time= self.create_time,
        )
    # def set_aaa(self, aaa:bbb)->Self:
    #     assert self.aaa is None, "aaa alredy set."
    #     assert isinstance(aaa, bbb), "Type of aaa is bbb."
        
    #     self.aaa = aaa
    #     return self