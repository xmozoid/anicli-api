# autogenerated by ssc-gen DO NOT_EDIT
from __future__ import annotations
import re
from typing import TypedDict, Union
from parsel import Selector, SelectorList

T_AniboomPage = TypedDict("T_AniboomPage", {"data_parameters": str, "hls": str, "dash": str})


class AniboomPage:
    """Extract MPD and M3U8 urls

        Required `referer="https://animego.org/` HEADER

        USAGE:
            1. GET <PLAYER_LINK> (e.g. https://aniboom.one/embed/6BmMbB7MxWO?episode=1&translation=30)
            2. PARSE. If pre-unescape response before parse - css selector may not find attribute
            3. For video playing, url required next headers:

            - Referer="https://aniboom.one/"
            - Accept-Language="ru-RU"  # INCREASE DOWNLOAD SPEED with this static value
            - Origin="https://aniboom.one"
        ISSUES:
            - 403 Forbidden if request sent not from CIS region
            - KEYS SHOULD BE STARTED IN Title case else hls/mpd links returns 403 error
            - Sometimes, aniboom backend missing MPD key and returns M3U8 url. Check this value before usage:

            https://github.com/vypivshiy/ani-cli-ru/issues/29

            Expected json signature (LOOK at dash.src and hls.src keys):

            { ...
            "dash":"{"src":"https:.../abcdef.mpd",        "type":"application\\/dash+xml"}",
            "hls":"{"src":"https:...\\/master_device.m3u8",
            "type":"application\\/x-mpegURL"}"

            ... }

            MAYBE returns this:

             { ...
            "dash":"{"src":"https:...master_device.m3u8",        "type":"application\\/dash+xml"}",
            "hls":"{"src":"https:...master_device.m3u8",
            "type":"application\\/x-mpegURL"}"

            ... }





    {
        "data_parameters": "String",
        "hls": "String",
        "dash": "String"
    }"""

    def __init__(self, document: Union[str, SelectorList, Selector]):
        self._doc = Selector(document) if isinstance(document, str) else document

    def _parse_data_parameters(self, value: Selector) -> str:
        value1 = value.css("#video")
        value2 = value1.css("::attr(data-parameters)").get()
        value3 = value2.replace("\\", "")
        value4 = value3.replace("&quot;", '"')
        return value4

    def _parse_hls(self, value: Selector) -> str:
        value1 = value.css("#video")
        value2 = value1.css("::attr(data-parameters)").get()
        value3 = value2.replace("\\", "")
        value4 = value3.replace("&quot;", '"')
        value5 = re.search('"hls":"{"src":"(https?.*?\\.m3u8)"', value4)[1]
        return value5

    def _parse_dash(self, value: Selector) -> str:
        value1 = value.css("#video")
        value2 = value1.css("::attr(data-parameters)").get()
        value3 = value2.replace("\\", "")
        value4 = value3.replace("&quot;", '"')
        value5 = re.search('"dash":"{"src":"(https?.*?\\.(?:mpd|m3u8))"', value4)[1]
        return value5

    def parse(self) -> T_AniboomPage:
        return {
            "data_parameters": self._parse_data_parameters(self._doc),
            "hls": self._parse_hls(self._doc),
            "dash": self._parse_dash(self._doc),
        }
