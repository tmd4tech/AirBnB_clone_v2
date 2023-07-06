#!/usr/bin/python3
"""a script to pack static content into a tarball
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """packages all contents from web_static into .tgz archive
    """
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    result = local('tar -czvf versions/web_static_{}.tgz web_static'
                   .format(now))
    if result.failed:
        return None
    else:
        return result
