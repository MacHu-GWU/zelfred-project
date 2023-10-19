# -*- coding: utf-8 -*-

import typing as T
import dataclasses


SEP = "____"


class QueryParser:
    """
    Utility class that can parse string to query.
    """

    def __init__(
        self,
        delimiter: T.Union[str, T.List[str]] = " ",
    ):
        if isinstance(delimiter, str):
            self.delimiter = [
                delimiter,
            ]
        else:
            self.delimiter = delimiter

    def parse(self, s: str) -> "Query":
        """
        Convert string query to structured query object.

        :param s: a string.
        """
        for sep in self.delimiter:
            s = s.replace(sep, SEP)
        parts = s.split(SEP)
        trimmed_parts = [c.strip() for c in parts if c.strip()]
        return Query(
            raw=s,
            parts=parts,
            trimmed_parts=trimmed_parts,
        )


DEFAULT_QUERY_PARSER = QueryParser()


@dataclasses.dataclass
class Query:
    """
    Structured query object. This is very useful to parse the input of UI handler.

    :param parts: the parts of query string split by delimiter
    :param trimmed_parts: similar to parts, but each part is white space stripped
    """

    raw: str = dataclasses.field()
    parts: T.List[str] = dataclasses.field()
    trimmed_parts: T.List[str] = dataclasses.field()

    @classmethod
    def from_str(cls, s: str, parser=DEFAULT_QUERY_PARSER):
        return parser.parse(s)
