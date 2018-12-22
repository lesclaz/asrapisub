from asrapisub.rest import Api


def convert_tab(tab_count):
    lo = ""
    for _ in list(range(tab_count)):
        lo += "    "
    return lo


def search(__element, tab_count):
    if __element.isDir:
        file.write("%sDirectorio: %s\n" % (convert_tab(tab_count), __element.title))
        __tab_count = tab_count + 1
        for directory in api.get_music_directory(__element.id).child:
            search(directory, __tab_count)
    else:
        file.write("%sArchivo: %s[%s]\n" % (convert_tab(tab_count), __element.title, __element.suffix))


api = Api("admin", "empresarioles9507", "127.0.0.1")
print(api.version)
__license = api.get_license()
if __license.valid:
    part_message = "es valida.\nPropietario:%s\nExpira:%s" % (__license.email, __license.trialExpires)
else:
    part_message = "no es valida"
print("La licencia %s" % part_message)
folders = api.get_music_folders()

file = open("file", "a")

for folder in folders:
    file.write("Folder: %s\n" % folder.name)
    indexes = api.get_indexes(folder.id)
    for index in indexes:
        file.write("    Index: %s\n" % index.name)
        music_directory = api.get_music_directory(index.id)
        for element in music_directory.child:
            search(element, 2)
