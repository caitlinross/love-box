import datetime
import json
from json import JSONEncoder
import dateutil.parser


class Message:
    def __init__(
        self,
        message: str,
        fontsize: int = 48,
        image: bool = False,
        modified=None,
    ) -> None:
        self.message: str = message
        self.fontsize: int = fontsize
        self.image: bool = image
        if modified == None:
            self.modified: str = DateTimeEncoder().encode(datetime.datetime.utcnow())
        else:
            self.modified: str = json.loads(modified, object_hook=DecodeDateTime)
        self.modified = self.modified.replace('"', '')

    def __str__(self) -> str:
        return "Message: " + self.message + "\nModified: " + str(self.modified)


class DateTimeEncoder(JSONEncoder):
    def default(self, obj) -> datetime.datetime:
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


def DecodeDateTime(dict) -> dict:
    if "modified" in dict:
        dict["modified"] = dateutil.parser.parse(dict["modified"])
        return dict
