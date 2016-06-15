# -*- coding: utf-8 -*-
"""
save image
"""
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from cStringIO import StringIO
import os
import purl  # pip
import requests  # pip
from PIL import Image  # pip
from xbuild import builDir


def imageGetter(url, saveDir='', saveName=''):
    """
    download img from url, save to saveDir
    @saveDir path to save img
    usage:
    >>> url = 'http://www.itprofessor.cn/media/media.jpg'
    >>> imageGetter(url)
    """
    response = requests.get(url.strip())
    img = Image.open(StringIO(response.content)) if response.ok else None
    if isinstance(img, Image.Image):
        path = purl.URL(url).path()
        if not saveName:
            saveName = os.path.splitext(path.strip('/').replace('/', '_'))[0]
        img.save(builDir((saveDir if saveDir else './'),
                         '%s.%s' % (saveName, img.format.lower())))
        return True
    else:
        raise TypeError('not a image url: %s' % url)


if __name__ == '__main__':

    url = 'http://www.itprofessor.cn/media/media.jpg'
    imageGetter(url, 'test', 'myimg')
