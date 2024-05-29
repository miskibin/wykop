from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, HttpUrl


class Source(BaseModel):
    label: str
    url: HttpUrl
    type: str
    type_id: int


class Rank(BaseModel):
    position: Optional[int] = None
    trend: int


from pydantic import validator, HttpUrl


class User(BaseModel):
    username: str
    gender: Optional[str]
    company: bool
    avatar: Optional[HttpUrl]
    status: str
    color: str
    verified: bool
    rank: Rank
    blacklist: bool
    follow: bool
    note: bool
    online: bool

    @validator("avatar", pre=True)
    def empty_str_to_none(cls, v):
        return v or None


class Photo(BaseModel):
    key: str
    label: str
    mime_type: str
    url: HttpUrl
    size: int
    width: int
    height: int


class Media(BaseModel):
    photo: Optional[Photo]
    embed: Optional[dict]


class Votes(BaseModel):
    up: int
    down: int
    count: int = 0


from pydantic import BaseModel
from typing import Optional, List, Dict


class WykopItem(BaseModel):
    id: int
    slug: str
    author: User
    created_at: datetime
    voted: int
    adult: bool
    tags: List[str]
    favourite: Optional[bool]
    parent: Optional[Dict]
    votes: Votes
    editable: bool
    deletable: bool
    comments: Dict
    resource: str
    actions: Dict
    archive: bool

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        validate_assignment = True
        use_enum_values = True
        validate_all = True
        max_anystr_length = 2**20
        anystr_strip_whitespace = True
        anystr_lower = True

    @property
    def url_if_exists(self):
        return getattr(getattr(self, "source", {}), "url", None)

    @property
    def desc_or_content(self):
        return getattr(self, "description", getattr(self, "content", ""))

    def __str__(self):
        return (
            f"{self.desc_or_content}\n\n{self.url_if_exists}\n{self.tags}\n\n{80*'='}"
        )


class WykopLink(WykopItem):
    title: str
    description: str
    source: Source
    published_at: Optional[str]
    hot: bool
    media: Media


class WykopEntry(WykopItem):
    content: str
    device: Optional[str]
    media: Optional[Media]  # Assuming Media might be simpler or just a photo
