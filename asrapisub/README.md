# ASR-API-SUB

Es un cliente para la api de subsonic creado en python3.
Se puede usar desde cualquier aplicacion en python3 con mucha facilidad.

## Usando ASR-API-SUB

        from asrapisub.rest import Api

        api = Api("user", "password", "host","https=False", port=4040, client="APP_NAME", client_version="VERSION")
        artists = api.get_artists()
        for artist in artists:
              print(artist.name)

## Funciones

| Funcion | Parametros | Descripcion |
| ------- | ---------- | ------------------------ |
| get_license | No | Devuelve un elemento de tipo [License](#lisence) |
| get_music_folders | No | Devuelve una lista de elementos de tipo [Folder](#folder) |
| get_indexes | id (`int`) (opcional) | Devuelve una lista de elementos de tipo [Index](#index) |
| get_music_directory | id (`int`) | Devuelve un elemento de tipo [Directory](#directory) |
| get_genres | No | Devuelve una lista de elementos de tipo [Genre](#genre) |
| get_artists | No | Devuelve una lista de elementos de tipo [Artist](#artist) |
| get_artist | id (`int`) | Devuelve un elemento de tipo [Artist](#artist) |
| get_album | id (`int`) | Devuelve un elemento de tipo [Album](#album) |
| get_song | id (`int`) | Devuelve un elemento de tipo [Song](#song) |
| get_videos | No | Devuelve una lista de elementos de tipo [Video](#video) |
| get_video_info | id (`int`) | Devuelve un elemento de tipo [VideoInfo](#videoinfo) |
| get_album_list | _type (`str`), size (`int`) | Devuelve una lista de elementos de tipo [Album](#album) |
| get_album_list2 | _type (`str`), size (`int`) | Devuelve una lista de elementos de tipo [Album](#album) |
| get_random_songs | size (opcional) | Devuelve una lista de elementos de tipo [Song](#song) |
| get_songs_by_genre | genre (`str`) | Devuelve una lista de elementos de tipo [Song](#song) |
| get_now_playing | No | Devuelve una lista de elementos de tipo [Entry](#entry) |

## Tipos de datos en ASR-API-SUB

#### Lisence:

| Parametro | Tipo |
| --------- | ---- |
| valid | `bool` |
| email | `str` |
| trialExpires | `str` |

#### Folder:

| Parametro | Tipo |
| --------- | ---- |
| name | `str` |
| id | `int` |

#### Index:

| Parametro | Tipo |
| --------- | ---- |
| Name | `str` |
| id | `int` |

#### Directory:

| Parametro | Tipo |
| --------- | ---- |
| name | `str` |
| id | `int` |
| child | `list` |

#### Genre:

| Parametro | Tipo |
| --------- | ---- |
| songCount | `int` |
| albumCount | `int` |
| value | `str` |

#### Artist:

| Parametro | Tipo |
| --------- | ---- |
| albumCount | `int` |
| name | `str` |
| id | `int` |
| coverArt | `str` |
| album | `Album (list)` |

#### Album:

| Parametro | Tipo |
| --------- | ---- |
| title | `str` |
| artist | `str` |
| artistId | `int` |
| id | `int` |
| coverArt | `str` |
| songCount | `int` |
| duration | `int` |
| songs | `Song (list)` |

#### Song:

| Parametro | Tipo |
| --------- | ---- |
| parent | `int` |
| artist | `str` |
| year | `int` |
| album | `str` |
| created | `str` |
| isVideo | `bool` |
| albumId | `int` |
| artistId | `int` |
| coverArt | `str` |
| title | `str` |
| suffix | `str` |
| type | `str` |
| duration | `int` |
| discnumber | `int` |
| path | `str` |
| size | `int` |
| bitRate | `int` |
| genre | `str` |
| id | `int` |
| track | `int` |
| contentType | `str` |
| isDir | `bool` |

### Entry

| Parametro | Tipo |
| --------- | ---- |
| id | `int` |
| parent | `int` |
| isDir | `bool` |
| title | `str` |
| album | `str` |
| artist | `str` |
| track | `int` |
| year | `int` |
| genre | `str` |
| coverArt | `str` |
| size | `int` |
| contentType | `str` |
| suffix | `str` |
| duration | `int` |
| bitRate | `int` |
| path | `str` |
| playCount | `int` |
| discNumber | `int` |
| create | `str` |
| albumId | `int` |
| artistId | `int` |
| type | `str` |
| username | `str` |
| minutesAgo | `int` |
| playerId | `int` |
| playerName | `str` |

## ASR-API-SUB Requiere

- python >= 3.5
