#!/usr/bin/python3
"""
Write a Fabric script that generates
a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo,
using the function do_pack.
"""
import fabric.api as fab
from datetime import datetime


def do_pack():
    """
    Prototype: def do_pack():
    All files in the folder web_static must
    be added to the final archive
    All archives must be stored in the folder versions
    (your function should create this folder if it doesn't exist)
    The name of the archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz
    The function do_pack must return the archive path
    if the archive has been correctly generated.
    Otherwise, it should return None
    """
    date_obj = datetime.now()
    date_str = date_obj.isoformat()
    char_rem = "-:.T"
    count = 0
    try:
        while char_rem[count] in date_str:
            date_str = date_str.split(char_rem[count])
            date_str = "".join(date_str)
            count += 1
    except IndexError:
        pass
    fab.local("tar -czvf web_static_{0}.tgz web_static".format(date_str))
    fab.local("mkdir -p ./versions/")
    fab.local("mv *.tgz versions")
    path = fab.local("cd ./versions/; readlink -f *.tgz", capture=True)
    return path
