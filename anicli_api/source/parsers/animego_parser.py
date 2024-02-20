# Auto generated code by ssc_gen
# WARNING: Any manual changes made to this file will be lost when this
# is run again. Do not edit this file unless you know what you are doing.

from __future__ import annotations  # python 3.7, 3.8 comp
import re
from typing import Any, Union

from parsel import Selector, SelectorList

_T_DICT_ITEM = dict[str, Union[str, list[str]]]
_T_LIST_ITEMS = list[dict[str, Union[str, list[str]]]]


class _BaseStructParser:
    def __init__(self, document: str):
        self.__raw__ = document
        self.__selector__ = Selector(document)
        self._cached_result: Union[_T_DICT_ITEM, _T_LIST_ITEMS] = {}

    def _pre_validate(self, document: Selector) -> None:
        # pre validate entrypoint, contain assert expressions
        pass

    def parse(self):
        """run parser"""
        self._pre_validate(self.__selector__)
        self._start_parse()
        return self

    def view(self) -> Union[_T_DICT_ITEM, _T_LIST_ITEMS]:
        """get parsed values"""
        return self._cached_result

    def _start_parse(self):
        """parse logic entrypoint"""
        pass


class OngoingView(_BaseStructParser):
    """Get all available ongoings from main page

        GET https://animego.org

        OngoingView view() item signature:

    {
        "url": "String",
        "title": "String",
        "thumbnail": "String",
        "episode": "String",
        "dub": "String"
    }
    """

    def __init__(self, document: str):
        super().__init__(document)
        self._cached_result: _T_LIST_ITEMS = []

    def _pre_validate(self, doc: Selector) -> None:
        var_0 = doc
        var_1 = var_0.css("title")
        var_2 = var_1.css("::text").get()
        assert re.search(r"Смотреть Аниме онлайн", var_2)
        return

    def _part_document(self) -> SelectorList:
        doc = self.__selector__
        var_0 = doc
        var_1 = var_0.css(".border-bottom-0.cursor-pointer")
        return var_1

    def _start_parse(self):
        self._cached_result.clear()
        for part in self._part_document():
            self._cached_result.append(
                {
                    "url": self._parse_url(part),
                    "title": self._parse_title(part),
                    "thumbnail": self._parse_thumbnail(part),
                    "episode": self._parse_episode(part),
                    "dub": self._parse_dub(part),
                }
            )

    def view(self) -> _T_LIST_ITEMS:
        return self._cached_result

    def _parse_url(self, doc: Selector):
        """ongoing page"""

        var_0 = doc
        var_1 = var_0.attrib["onclick"]
        var_2 = var_1.lstrip("location.href=")
        var_3 = var_2.strip("'")
        var_4 = "https://animego.org{}".format(var_3)
        return var_4

    def _parse_title(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".last-update-title")
        var_2 = var_1.css("::text").get()
        return var_2

    def _parse_thumbnail(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".lazy")
        var_2 = var_1.attrib["style"]
        var_3 = var_2.lstrip("background-image: url(")
        var_4 = var_3.rstrip(");")
        return var_4

    def _parse_episode(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".text-truncate")
        var_2 = var_1.css("::text").get()
        var_3 = re.search(r"(\d+)\s", var_2)[1]
        return var_3

    def _parse_dub(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".text-gray-dark-6")
        var_2 = var_1.css("::text").get()
        var_3 = var_2.replace(")", "")
        var_4 = var_3.replace("(", "")
        return var_4


class SearchView(_BaseStructParser):
    """Get all search results by query

        GET https://animego.org/search/anime
        q={QUERY}

        SearchView view() item signature:

    {
        "title": "String",
        "thumbnail": "String",
        "url": "String"
    }
    """

    def __init__(self, document: str):
        super().__init__(document)
        self._cached_result: _T_LIST_ITEMS = []

    def _part_document(self) -> SelectorList:
        doc = self.__selector__
        var_0 = doc
        var_1 = var_0.css(".row > .col-ul-2")
        return var_1

    def _start_parse(self):
        self._cached_result.clear()
        for part in self._part_document():
            self._cached_result.append(
                {
                    "title": self._parse_title(part),
                    "thumbnail": self._parse_thumbnail(part),
                    "url": self._parse_url(part),
                }
            )

    def view(self) -> _T_LIST_ITEMS:
        return self._cached_result

    def _parse_title(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".text-truncate a")
        var_2 = var_1.attrib["title"]
        return var_2

    def _parse_thumbnail(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".lazy")
        var_2 = var_1.attrib["data-original"]
        return var_2

    def _parse_url(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".text-truncate a")
        var_2 = var_1.attrib["href"]
        return var_2


class AnimeView(_BaseStructParser):
    """Anime page information

        GET https://animego.org/anime/eksperimenty-leyn-1114

        AnimeView view() item signature:

    {
        "title": "String",
        "description": "Array['String']",
        "thumbnail": "String",
        "id": "String",
        "raw_json": "String"
    }
    """

    def __init__(self, document: str):
        super().__init__(document)
        self._cached_result: _T_DICT_ITEM = {}

    def _pre_validate(self, doc: Selector) -> None:
        var_0 = doc
        var_1 = var_0.css("title")
        var_2 = var_1.css("::text").get()
        assert re.search(r".* смотреть онлайн .*", var_2)
        return

    def _start_parse(self):
        self._cached_result.clear()
        self._cached_result["title"] = self._parse_title(self.__selector__)
        self._cached_result["description"] = self._parse_description(self.__selector__)
        self._cached_result["thumbnail"] = self._parse_thumbnail(self.__selector__)
        self._cached_result["id"] = self._parse_id(self.__selector__)
        self._cached_result["raw_json"] = self._parse_raw_json(self.__selector__)

    def view(self) -> _T_DICT_ITEM:
        return self._cached_result

    def _parse_title(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".anime-title h1")
        var_2 = var_1.css("::text").get()
        return var_2

    def _parse_description(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css(".description")
        var_2 = var_1.css("::text").getall()
        var_3 = " ".join(var_2)
        return var_3

    def _parse_thumbnail(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css("#content img")
        var_2 = var_1.attrib["src"]
        return var_2

    def _parse_id(self, doc: Selector):
        """anime id required for next requests (for DubberView, Source schemas)"""

        var_0 = doc
        var_1 = var_0.css(".br-2 .my-list-anime")
        var_2 = var_1.attrib["id"]
        var_3 = var_2.lstrip("my-list-")
        return var_3

    def _parse_raw_json(self, doc: Selector):
        """DEV key: for parse extra metadata"""

        var_0 = doc
        var_1 = var_0.css("script[type='application/ld+json']")
        var_2 = var_1.css("::text").get()
        return var_2


class DubbersView(_BaseStructParser):
    """Representation dubbers in {id: 'dubber_id', name: 'dubber_name'}

        Prepare:
          1. get id from Anime object
          2. GET 'https://animego.org/anime/{Anime.id}/player?_allow=true'
          3. extract html from json by ['content'] key
          4. OPTIONAL: unescape HTML

        DubbersView view() item signature:

    {
        "key": "String",
        "value": "String"
    }
    """

    def __init__(self, document: str):
        super().__init__(document)
        self._cached_result: _T_DICT_ITEM = {}

    def _pre_validate(self, doc: Selector) -> None:
        var_0 = doc
        assert var_0.css("#video-dubbing .mb-1").get()
        return

    def _part_document(self) -> SelectorList:
        doc = self.__selector__
        var_0 = doc
        var_1 = var_0.css("#video-dubbing .mb-1")
        return var_1

    def _start_parse(self):
        self._cached_result.clear()
        for part in self._part_document():
            self._cached_result[self._parse_key(part)] = self._parse_value(part)

    def view(self) -> _T_DICT_ITEM:
        return self._cached_result

    def _parse_key(self, doc: Selector):
        """dubber id"""

        var_0 = doc
        var_1 = var_0.attrib["data-dubbing"]
        return var_1

    def _parse_value(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css("span")
        var_2 = var_1.css("::text").get()
        var_3 = var_2.strip("\n")
        var_4 = var_3.strip(" ")
        var_5 = var_4.rstrip("\n")
        return var_5


class EpisodeView(_BaseStructParser):
    """Representation episodes

        Prepare:
          1. get id from Anime object
          2. GET 'https://animego.org/anime/{Anime.id}/player?_allow=true'
          3. extract html from json by ['content'] key
          4. OPTIONAL: unescape HTML

        EpisodeView view() item signature:

    {
        "num": "String",
        "title": "String",
        "id": "String"
    }
    """

    def __init__(self, document: str):
        super().__init__(document)
        self._cached_result: _T_LIST_ITEMS = []

    def _pre_validate(self, doc: Selector) -> None:
        var_0 = doc
        assert var_0.css("#video-carousel .mb-0").get()
        return

    def _part_document(self) -> SelectorList:
        doc = self.__selector__
        var_0 = doc
        var_1 = var_0.css("#video-carousel .mb-0")
        return var_1

    def _start_parse(self):
        self._cached_result.clear()
        for part in self._part_document():
            self._cached_result.append(
                {
                    "num": self._parse_num(part),
                    "title": self._parse_title(part),
                    "id": self._parse_id(part),
                }
            )

    def view(self) -> _T_LIST_ITEMS:
        return self._cached_result

    def _parse_num(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.attrib["data-episode"]
        return var_1

    def _parse_title(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.attrib["data-episode-title"]
        return var_1

    def _parse_id(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.attrib["data-id"]
        return var_1


class SourceView(_BaseStructParser):
    """representation videos

        Prepare:
          1. get num and id from Episode

          2.

          GET https://animego.org/anime/series
          dubbing=2&provider=24&episode={Episode.num}id={Episode.id}

          3. extract html from json by ["content"] key

          4. OPTIONAL: unescape document

        SourceView view() item signature:

    {
        "title": "String",
        "url": "String",
        "data_provider": "String",
        "data_provide_dubbing": "String"
    }
    """

    def __init__(self, document: str):
        super().__init__(document)
        self._cached_result: _T_LIST_ITEMS = []

    def _part_document(self) -> SelectorList:
        doc = self.__selector__
        var_0 = doc
        var_1 = var_0.css("#video-players > span")
        return var_1

    def _start_parse(self):
        self._cached_result.clear()
        for part in self._part_document():
            self._cached_result.append(
                {
                    "title": self._parse_title(part),
                    "url": self._parse_url(part),
                    "data_provider": self._parse_data_provider(part),
                    "data_provide_dubbing": self._parse_data_provide_dubbing(part),
                }
            )

    def view(self) -> _T_LIST_ITEMS:
        return self._cached_result

    def _parse_title(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.css("::text").get()
        return var_1

    def _parse_url(self, doc: Selector):
        var_0 = doc
        var_1 = var_0.attrib["data-player"]
        var_2 = "https:{}".format(var_1)
        return var_2

    def _parse_data_provider(self, doc: Selector):
        """player id"""

        var_0 = doc
        var_1 = var_0.attrib["data-provider"]
        return var_1

    def _parse_data_provide_dubbing(self, doc: Selector):
        """dubber id"""

        var_0 = doc
        var_1 = var_0.attrib["data-provide-dubbing"]
        return var_1
