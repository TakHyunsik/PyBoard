from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
from typing import Optional, Self, Union
from result import Result, Ok, Err
from uuid import UUID, uuid4

from Commons.helpers import check_hex_string


class ID(metaclass=ABCMeta):
    @abstractmethod
    def get_id(self) -> str: ...
    @abstractmethod
    def get_seq(self) -> Optional[int]: ...


class IIDBuilder(metaclass=ABCMeta):
    @abstractmethod
    def set_uuid(self, uuid_hex: Optional[str] = None) -> Result[Self, str]: ...
    @abstractmethod
    def set_seq(self, seq: int) -> Self: ...

@dataclass
class IDBuilder(IIDBuilder):
    uuid: Optional[UUID] = None
    seq: Optional[int] = None

    def set_seq(self, seq: int) -> Self:
        assert isinstance(seq, int), "Type of seq is int."
        assert self.seq is None, "The sequence is already set."
        assert seq >= 0, "seq >= 0"

        self.seq = seq
        return self
    
    def set_str_uuid(self, uuid: str) -> Result[Self, str]:
        assert self.uuid is None, "The uuid_hex is already set."
        assert check_hex_string(uuid), "The uuid_hex is not in hex format."
        if not check_hex_string(uuid):
            return Err("not hex format")
        try:
            self.uuid = UUID(hex=uuid)
        except:
            return Err("Not Convert UUID")
        return Ok(self)

    def set_uuid(self, uuid: Optional[UUID] = None) -> Self:
        assert self.uuid is None, "The uuid is already set."
        match uuid:
            case None:
                self.uuid = uuid4()
            case id if isinstance(id, UUID):
                self.uuid = id
            case _:
                assert False, "Type of uuid is not str."

        return self
