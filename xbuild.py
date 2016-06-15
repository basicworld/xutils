# -*- coding: utf-8 -*-
"""
build dir
"""
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def builDir(dirName='./', fileName=''):
    """
    create dir to make sure os.path.isdir(dirName) = True
    """
    # dirName = os.path.abspath(dirName)
    dirName = unicode(dirName)
    fileName = unicode(fileName)
    if not os.path.isdir(dirName):
        os.makedirs(dirName)
    return(os.path.join(dirName, fileName) if fileName else dirName)
