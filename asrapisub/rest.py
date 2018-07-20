# rest.py
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

from . import APP_NAME
from . import VERSION
from .connect import Connection
from .models import Album
from .models import Artist
from .models import Directory
from .models import Element
from .models import Entry
from .models import Folder
from .models import Genre
from .models import Index
from .models import Server
from .models import Song
from .models import User
from .models import Video
from .utils import JSon
from .utils import build_url


class Api(object):

    def __init__(self, user_name, password, host, https=False, port=4040, client=APP_NAME,
                 client_version=VERSION):
        server = Server(host, https=https, port=port)
        user = User(user_name, password)
        self.connection = Connection(server, user, client, client_version)

    @property
    def version(self):
        url = self.generate_url("ping")
        return self.get_header(url)["version"]

    def generate_url(self, operation, params=None):
        if params is None:
            params = {}
        return build_url(operation, self.connection.server.url,
                         self.connection.user.user_name,
                         self.connection.user.password,
                         self.connection.client_version, self.connection.client,
                         params=params)

    @staticmethod
    def get_header(url):
        request = JSon(url)
        return request.header

    def get_license(self):
        url = self.generate_url("get_license")
        header = self.get_header(url)
        __license = header["__license"]
        element = Element()
        if __license["valid"]:
            element.valid = True
        else:
            element.valid = False
        if "email" in __license:
            element.email = __license["email"]
        if "trialExpires" in __license:
            element.trialExpires = __license["trialExpires"]
        return element

    def get_music_folders(self):
        url = self.generate_url("get_music_folders")
        folders = []
        header = self.get_header(url)
        music_folders_ = header["musicFolders"]
        music_folder = music_folders_["musicFolder"]
        for folder in music_folder:
            folders.append(Folder(folder))
        return folders

    def get_indexes(self, _id=None):
        indexes_list = []
        url = self.generate_url("get_indexes", params={"id": _id})
        header = self.get_header(url)
        indexes = header["indexes"]
        index = indexes["index"]
        for element in index:
            for element_ in element["artist"]:
                indexes_list.append(Index(element_))

        return indexes_list

    def get_music_directory(self, _id):
        url = self.generate_url("get_music_directory", params={"id": _id})
        header = self.get_header(url)
        directory = header["directory"]
        return Directory(directory)

    def get_genres(self):
        url = self.generate_url("get_genres")
        genre_list = []
        header = self.get_header(url)
        genres = header["genres"]
        if "genre" in genres:
            for genre in genres["genre"]:
                genre_list.append(Genre(genre))
        return genre_list

    def get_artists(self):
        artist_list = []
        url = self.generate_url("get_artists")
        header = self.get_header(url)
        artists = header["artists"]
        index = artists["index"]
        for indexed in index:
            for artist in indexed["artist"]:
                artist_list.append(Artist(artist))
        return artist_list

    def get_artist(self, _id):
        url = self.generate_url("get_artist", params={"id": _id})
        header = self.get_header(url)
        artist = header["artist"]
        return Artist(artist)

    def get_album(self, _id):
        url = self.generate_url("get_album", params={"id": _id})
        header = self.get_header(url)
        return Album(header["album"])

    def get_song(self, _id):
        url = self.generate_url("get_song", params={"id": _id})
        header = self.get_header(url)
        return Song(header["song"])

    def get_videos(self):
        video_list = []
        url = self.generate_url("get_videos")
        header = self.get_header(url)
        videos = header["videos"]
        if "video" in videos:
            for video in videos["video"]:
                video_list.append(Video(video))
        return video_list

    def get_video_info(self, _id):
        url = self.generate_url("get_video_info", params={"id": _id})
        header = self.get_header(url)
        video_info = header["videoInfo"]
        element = Element()
        element.id = video_info["id"]
        element.audioTrack = []
        for _audio_track in video_info["audioTrack"]:
            audio_track = Element()
            audio_track.id = _audio_track["id"]
            audio_track.name = _audio_track["name"]
            audio_track.languageCode = _audio_track["languageCode"]
            element.audioTrack.append(audio_track)
        return element

    def get_album_list(self, _type, size=15):
        __album_list = []
        url = self.generate_url("get_album_list", params={"size": size,
                                                          "type": _type})
        header = self.get_header(url)
        album_list = header["albumList"]
        if "album" in album_list:
            for album in album_list["album"]:
                __album_list.append(Album(album))
        return __album_list

    def get_album_list2(self, _type, size=15):
        album_list = []
        url = self.generate_url("get_album_list2", params={"size": size,
                                                           "type": _type})
        header = self.get_header(url)
        album_list2 = header["albumList2"]
        if "album" in album_list2:
            for album in album_list2["album"]:
                album_list.append(Album(album))
        return album_list

    def get_random_songs(self, size=15):
        song_list = []
        url = self.generate_url("get_random_songs", params={"size": size})
        header = self.get_header(url)
        random_songs = header["randomSongs"]
        if "song" in random_songs:
            for song in random_songs["song"]:
                song_list.append(Song(song))
        return song_list

    def get_songs_by_genre(self, genre=None):
        song_list = []
        url = self.generate_url("get_songs_by_genre", params={"genre": genre})
        header = self.get_header(url)
        songs_by_genre = header["songsByGenre"]
        if "song" in songs_by_genre:
            for song in songs_by_genre["song"]:
                song_list.append(Song(song))
        return song_list

    def get_now_playing(self):
        entry_list = []
        url = self.generate_url("get_now_playing")
        header = self.get_header(url)
        now_playing = header["nowPlaying"]
        if "entry" in now_playing:
            for entry in now_playing["entry"]:
                entry_list.append(Entry(entry))
        return entry_list

    def get_starred(self, music_folder_id=None):
        element_list = []
        params = {}
        if music_folder_id:
            params["musicFolderId"] = music_folder_id
        url = self.generate_url("get_starred", params=params)
        header = self.get_header(url)
        starred = header["starred"]
        if "artist" in starred:
            for artist in starred["artist"]:
                element_list.append(Artist(artist))
        if "album" in starred:
            for album in starred["album"]:
                element_list.append(Album(album))
        if "song" in starred:
            for song in starred["song"]:
                element_list.append(Song(song))
        return element_list
