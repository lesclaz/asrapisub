# __init__.py
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


APP_NAME = 'asrapisub'
VERSION = '1.0'

# Dict of operations
operations_dict = {"ping": "/ping.view?",
                   "get_genres": "/getGenres?",
                   "get_song": "/getSong?",
                   "get_license": "/getLicense?",
                   "get_indexes": "/getIndexes?",
                   "get_artists": "/getArtists.view?",
                   "get_artist": "/getArtist.view?",
                   "get_music_folders": "/getMusicFolders.view?",
                   "get_music_directory": "/getMusicDirectory.view?",
                   "get_album": "/getAlbum.view?",
                   "get_album_list": "/getAlbumList.view?",
                   "get_album_list2": "/getAlbumList2.view?",
                   "get_random_songs": "/getRandomSongs.view?",
                   "get_songs_by_genre": "/getSongsByGenre?",
                   "get_now_playing": "/getNowPlaying?",
                   "get_videos": "/getVideos.view?",
                   "get_starred": "/getStarred?"}

# Dict of protocols
protocols_dict = {"HTTP": "http://",
                  "HTTPS": "https://"}

parameters_dict = {"id": "&id=",
                   "type": "&type=",
                   "size": "&size=",
                   "genre": "&genre=",
                   "search": "&search=",
                   "musicFolderId": "&musicFolderId="}
