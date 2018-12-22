# utils.py
#
# Copyright (C) 2018 - Lesly Cintra
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import json
import urllib.request
from datetime import time

from . import operations_dict
from . import parameters_dict
from .core.exceptions import ApiError


class JSon(object):

    def __init__(self, __object, url):
        self.url = url
        self.object = __object

    def json_text(self):
        json_byte = urllib.request.urlopen(self.url).read()
        return trate_json_text(json_byte.decode("utf_8"), self.object.connection.client)

    @property
    def header(self):
        sub_header = "subsonic-response"
        json_init = json.loads(self.json_text())
        header = json_init[sub_header]
        if header["status"] == "ok":
            return header
        else:
            error = header["error"]
            raise ApiError("Error Code: %s --> %s" % (error["code"], error["message"]))


def build_url(operation, base_url, user_name, password, client_version, client, params=None):
    url_base = (base_url + operations_dict[operation] + "u=" + user_name + "&p=enc:" +
                password + "&v=" + str(client_version) + "&c=" + client + "&f=jsonp")
    for key in params.keys():
        url_base += parameters_dict[key] + str(params[key])
    return url_base + "&callback=%s" % client


def convert_to_time(secons):
    hours = secons // 3600
    minutes = secons % 3600
    secons_ = minutes % 60
    minutes = minutes // 60
    return time(hours, minutes, secons_)


def replace_spaces(text):
    return text.replace(" ", "%20")


def trate_json_text(jtext, app_name):
    json_text_lines = jtext.splitlines()
    json_text_lines[0] = json_text_lines[0].replace("%s(" % app_name, "")
    json_text_lines[-1] = json_text_lines[-1].replace(");", "")
    json_trate = ""
    for line in json_text_lines:
        json_trate += "%s\n" % line
    return json_trate
