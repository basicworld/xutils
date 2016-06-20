# -*- coding: utf-8 -*-
"""
common functions
"""

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
# set basedir
XUTILSDIR = os.path.split(os.path.realpath(__file__))[0]
sys.path.insert(0, XUTILSDIR)

# try:
#     from xcsv import CsvWriter
# except ImportError as e:
#     print("Warning: cannot import CsvWriter")

# try:
#     from xcsv import CsvReader
# except ImportError as e:
#     print("Warning: cannot import CsvWriter")

# try:
#     from ximage import imageGetter
# except ImportError as e:
#     print("Warning: cannot import CsvWriter")

# from xbuild import builDir
# from xtree import Tree
# from xlog import logger
# from xtime import createTimeFromStr
# from xtime import createTimeFromDatetimeClass

# try:
#     from xlsx import XlsxReader
# except ImportError as e:
#     print("Warning: cannot import CsvWriter")

# try:
#     from xlsx import XlsxWriter
# except ImportError as e:
#     print("Warning: cannot import CsvWriter")
