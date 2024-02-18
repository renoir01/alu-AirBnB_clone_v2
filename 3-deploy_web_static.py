#!/usr/bin/python3
"""
Write a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy:
"""
from fabric.api import *
from datetime import datetime
import os


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
    local("tar -czvf web_static_{0}.tgz web_static".format(date_str))
    local("mkdir -p ./versions/")
    local("mv *.tgz versions")
    path = local("cd ./versions/; readlink -f *.tgz", capture=True)
    return path


env.hosts = ["ubuntu@18.208.245.38", "ubuntu@54.146.197.24"]


def do_deploy(archive_path):
    """
    Prototype: def do_deploy(archive_path):
    Returns False if the file at the path archive_path doesn't exist
    The script should take the following steps:
    Upload the archive to the /tmp/ directory of the web server
    Uncompress the archive to the folder
    /data/web_static/releases/<archive filename without extension>
    on the web server Delete the archive from the web server
    Delete the symbolic link /data/web_static/current from the web server
    Create a new the symbolic link /data/web_static/current on the web server,
    linked to the new version of your code
    (/data/web_static/releases/<archive filename without extension>)
    All remote commands must be executed on your both web servers
    (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)
    Returns True if all operations have been done correctly,
    otherwise returns False You must use this script to deploy
    it on your servers: xx-web-01 and xx-web-02
    """
    if not os.path.exists(archive_path):
        return False
    archive = archive_path.split('/')[-1]
    filename_folder = archive.split('.')[0]
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{0}".format(filename_folder))
        run("tar -C /data/web_static/releases/{0} \
            -xzvf /tmp/{1}".format(filename_folder, archive))
        run("rm /tmp/{0}".format(archive))
        run("mv /data/web_static/releases/{0}/web_static/* \
            /data/web_static/releases/{1}/".format(filename_folder,
                                                   filename_folder))
        run("rm -rf \
            /data/web_static/releases/{0}/web_static".format(filename_folder))
        run("rm /data/web_static/current")
        run("ln -sf /data/web_static/releases/{0} \
            /data/web_static/current".format(filename_folder))
    except Exception:
        return False
    else:
        return True


def deploy():
    """
    Prototype: def deploy():
    The script should take the following steps:
    Call the do_pack() function and store the path
    of the created archive Return False if no archive
    has been created Call the do_deploy(archive_path)
    function, using the new path of the new archive
    Return the return value of do_deploy
    All remote commands must be executed on both of web
    your servers (using env.hosts = ['<IP web-01>', 'IP web-02']
    variable in your script) You must use this script to deploy
    it on your servers: xx-web-01 and xx-web-02
    """
    archive_path = do_pack()
    results = execute(do_deploy, archive_path=archive_path)
    return results
