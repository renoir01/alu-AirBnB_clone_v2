#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy:
"""
from fabric.api import *
import os


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
