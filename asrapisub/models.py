# models.py
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
import binascii


class Server(object):

    def __init__(self, host_name=None, https=False, port=4040):

        self.__host_name = host_name
        self.__https = https
        self.__port = port

    @property
    def host_name(self):
        return self.__host_name

    @property
    def port(self):
        return self.__port

    @property
    def url(self):
        if self.__https:
            return "%s%s:%s/rest" % ("https://", self.host_name, self.port)
        else:
            return "%s%s:%s/rest" % ("http://", self.host_name, self.port)


class User(object):

    def __init__(self, user_name=None, password=None):
        self.__user_name = user_name
        self.__password = password

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return binascii.hexlify(self.__password.encode('utf-8')).decode('utf8')


class Artist(object):

    def __init__(self, artist):
        self.__artist = artist

    @property
    def albumCount(self):
        if "albumCount" in self.__artist:
            return self.__artist["albumCount"]

    @property
    def name(self):
        if "name" in self.__artist:
            return self.__artist["name"]

    @property
    def id(self):
        if "id" in self.__artist:
            return self.__artist["id"]

    @property
    def coverArt(self):
        if "coverArt" in self.__artist:
            return self.__artist["coverArt"]

    @property
    def album(self):
        album_list = []
        if "album" in self.__artist:
            for album in self.__artist["album"]:
                album_list.append(Album(album))
        return album_list


class Album(object):

    def __init__(self, album):
        self.__album = album

    @property
    def name(self):
        if "name" in self.__album:
            return self.__album["name"]

    @property
    def title(self):
        if "title" in self.__album:
            return self.__album["title"]
        else:
            return self.name

    @property
    def artist(self):
        if "artist" in self.__album:
            return self.__album["artist"]

    @property
    def artistId(self):
        if "artistId" in self.__album:
            return self.__album["artistId"]

    @property
    def id(self):
        if "id" in self.__album:
            return self.__album["id"]

    @property
    def coverArt(self):
        if "coverArt" in self.__album:
            return self.__album["coverArt"]

    @property
    def duration(self):
        if "duration" in self.__album:
            return self.__album["duration"]

    @property
    def songCount(self):
        if "songCount" in self.__album:
            return self.__album["songCount"]

    @property
    def song(self):
        song_list = []
        if "song" in self.__album:
            for song in self.__album["song"]:
                song_list.append(Song(song))
            return song_list


class Directory(object):

    def __init__(self, directory):
        self.__directory = directory

    @property
    def name(self):
        if "name" in self.__directory:
            return self.__directory["name"]

    @property
    def id(self):
        if "id" in self.__directory:
            return self.__directory["id"]

    @property
    def child(self):
        if "child" in self.__directory:
            child = []
            for element in self.__directory["child"]:
                child.append(Child(element))
            return child


class Folder(object):

    def __init__(self, folder):
        self.__folder = folder

    @property
    def name(self):
        if "name" in self.__folder:
            return self.__folder["name"]

    @property
    def id(self):
        if "id" in self.__folder:
            return self.__folder["id"]


class Song(object):

    def __init__(self, song):
        self.__song = song

    @property
    def parent(self):
        if "parent" in self.__song:
            return self.__song["parent"]

    @property
    def artist(self):
        if "artist" in self.__song:
            return self.__song["artist"]

    @property
    def year(self):
        if "year" in self.__song:
            return self.__song["year"]

    @property
    def album(self):
        if "album" in self.__song:
            return self.__song["album"]

    @property
    def created(self):
        if "created" in self.__song:
            return self.__song["created"]

    @property
    def isVideo(self):
        if "isVideo" in self.__song:
            return self.__song["isVideo"]

    @property
    def albumId(self):
        if "albumId" in self.__song:
            return self.__song["albumId"]

    @property
    def artistId(self):
        if "artistId" in self.__song:
            return self.__song["artistId"]

    @property
    def coverArt(self):
        if "coverArt" in self.__song:
            return self.__song["coverArt"]

    @property
    def title(self):
        if "title" in self.__song:
            return self.__song["title"]

    @property
    def suffix(self):
        if "suffix" in self.__song:
            return self.__song["suffix"]

    @property
    def type(self):
        if "type" in self.__song:
            return self.__song["type"]

    @property
    def duration(self):
        if "duration" in self.__song:
            return self.__song["duration"]

    @property
    def discnumber(self):
        if "discnumber" in self.__song:
            return self.__song["discnumber"]

    @property
    def path(self):
        if "path" in self.__song:
            return self.__song["path"]

    @property
    def size(self):
        if "size" in self.__song:
            return self.__song["size"]

    @property
    def bitRate(self):
        if "bitRate" in self.__song:
            return self.__song["bitRate"]

    @property
    def genre(self):
        if "genre" in self.__song:
            return self.__song["genre"]

    @property
    def id(self):
        if "id" in self.__song:
            return self.__song["id"]

    @property
    def track(self):
        if "track" in self.__song:
            return self.__song["track"]

    @property
    def contentType(self):
        if "contentType" in self.__song:
            return self.__song["contentType"]

    @property
    def isDir(self):
        if "isDir" in self.__song:
            return self.__song["isDir"]


class Video(object):

    def __init__(self, video):
        self.__video = video

    @property
    def parent(self):
        if "parent" in self.__video:
            return self.__video["parent"]

    @property
    def album(self):
        if "album" in self.__video:
            return self.__video["album"]

    @property
    def created(self):
        if "created" in self.__video:
            return self.__video["created"]

    @property
    def title(self):
        if "title" in self.__video:
            return self.__video["title"]

    @property
    def suffix(self):
        if "suffix" in self.__video:
            return self.__video["suffix"]

    @property
    def transcodedContentType(self):
        if "transcodedContentType" in self.__video:
            return self.__video["transcodedContentType"]

    @property
    def duration(self):
        if "duration" in self.__video:
            return self.__video["duration"]

    @property
    def path(self):
        if "path" in self.__video:
            return self.__video["path"]

    @property
    def size(self):
        if "size" in self.__video:
            return self.__video["size"]

    @property
    def bitRate(self):
        if "bitRate" in self.__video:
            return self.__video["bitRate"]

    @property
    def id(self):
        if "id" in self.__video:
            return self.__video["id"]

    @property
    def contentType(self):
        if "contentType" in self.__video:
            return self.__video["contentType"]

    @property
    def transcodedSuffix(self):
        if "transcodedSuffix" in self.__video:
            return self.__video["transcodedSuffix"]

    @property
    def isDir(self):
        if "isDir" in self.__video:
            return self.__video["isDir"]


class Index(object):

    def __init__(self, index):
        self.__index = index

    @property
    def name(self):
        if "name" in self.__index:
            return self.__index["name"]

    @property
    def id(self):
        if "id" in self.__index:
            return self.__index["id"]


class Element(object):
    pass


class Entry(object):

    def __init__(self, entry):
        self.__entry = entry

    @property
    def id(self):
        if "id" in self.__entry:
            return self.__entry["id"]

    @property
    def parent(self):
        if "parent" in self.__entry:
            return self.__entry["parent"]

    @property
    def isDir(self):
        if "isDir" in self.__entry:
            return self.__entry["isDir"]

    @property
    def title(self):
        if "title" in self.__entry:
            return self.__entry["title"]

    @property
    def album(self):
        if "album" in self.__entry:
            return self.__entry["album"]

    @property
    def artist(self):
        if "artist" in self.__entry:
            return self.__entry["artist"]

    @property
    def track(self):
        if "track" in self.__entry:
            return self.__entry["track"]

    @property
    def year(self):
        if "year" in self.__entry:
            return self.__entry["year"]

    @property
    def genre(self):
        if "genre" in self.__entry:
            return self.__entry["genre"]

    @property
    def coverArt(self):
        if "coverArt" in self.__entry:
            return self.__entry["coverArt"]

    @property
    def size(self):
        if "size" in self.__entry:
            return self.__entry["size"]

    @property
    def contentType(self):
        if "contentType" in self.__entry:
            return self.__entry["contentType"]

    @property
    def suffix(self):
        if "suffix" in self.__entry:
            return self.__entry["suffix"]

    @property
    def duration(self):
        if "duration" in self.__entry:
            return self.__entry["duration"]

    @property
    def bitRate(self):
        if "bitRate" in self.__entry:
            return self.__entry["bitRate"]

    @property
    def path(self):
        if "path" in self.__entry:
            return self.__entry["path"]

    @property
    def playCount(self):
        if "playCount" in self.__entry:
            return self.__entry["playCount"]

    @property
    def discNumber(self):
        if "discNumber" in self.__entry:
            return self.__entry["discNumber"]

    @property
    def create(self):
        if "create" in self.__entry:
            return self.__entry["create"]

    @property
    def albumId(self):
        if "albumId" in self.__entry:
            return self.__entry["albumId"]

    @property
    def artistId(self):
        if "artistId" in self.__entry:
            return self.__entry["artistId"]

    @property
    def type(self):
        if "type" in self.__entry:
            return self.__entry["type"]

    @property
    def username(self):
        if "username" in self.__entry:
            return self.__entry["username"]

    @property
    def minustesAgo(self):
        if "minustesAgo" in self.__entry:
            return self.__entry["minustesAgo"]

    @property
    def playerId(self):
        if "playerId" in self.__entry:
            return self.__entry["playerId"]

    @property
    def playerName(self):
        if "playerName" in self.__entry:
            return self.__entry["playerName"]


class Genre(object):

    def __init__(self, genre):
        self.__genre = genre

    @property
    def songCount(self):
        if "songCount" in self.__genre:
            return self.__genre["songCount"]

    @property
    def albumCount(self):
        if "albumCount" in self.__genre:
            return self.__genre["albumCount"]

    @property
    def value(self):
        if "value" in self.__genre:
            return self.__genre["value"]


class Child(object):

    def __init__(self, child):
        self.__child = child

    @property
    def album(self):
        if "album" in self.__child:
            return self.__child["album"]

    @property
    def artist(self):
        if "artist" in self.__child:
            return self.__child["artist"]

    @property
    def coverArt(self):
        if "coverArt" in self.__child:
            return self.__child["coverArt"]

    @property
    def created(self):
        if "created" in self.__child:
            return self.__child["created"]

    @property
    def genre(self):
        if "genre" in self.__child:
            return self.__child["genre"]

    @property
    def id(self):
        if "id" in self.__child:
            return self.__child["id"]

    @property
    def isDir(self):
        if "isDir" in self.__child:
            return self.__child["isDir"]

    @property
    def parent(self):
        if "parent" in self.__child:
            return self.__child["parent"]

    @property
    def playCount(self):
        if "playCount" in self.__child:
            return self.__child["playCount"]

    @property
    def title(self):
        if "title" in self.__child:
            return self.__child["title"]

    @property
    def year(self):
        if "year" in self.__child:
            return self.__child["year"]

    @property
    def suffix(self):
        if "suffix" in self.__child:
            return self.__child["suffix"]
