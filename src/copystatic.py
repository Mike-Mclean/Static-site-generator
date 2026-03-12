import os
import shutil

def dir_copy(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)

    if not os.path.exists(source):
        raise Exception("Source paths do not exist")

    for item in os.listdir(source):
        item_path = os.path.join(source, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, destination)
        else:
            new_destination = os.path.join(destination, item)
            os.mkdir(new_destination)
            dir_copy(item_path, new_destination)
            