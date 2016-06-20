# -*- coding: utf-8 -*-
"""
"""
import datetime
import time


def createTimeFromStr(inputTime='',
                      inputFormat='%Y-%m-%d %H:%M',
                      outputFormat='%Y-%m-%d %H:%M',
                      timeAdd=0,
                      addUnit='minutes'):
    if inputTime:
        inputTime = time.strptime(inputTime, inputFormat)
        inputTime = datetime.datetime(*inputTime[:6])
    else:
        inputTime = datetime.datetime.now()
    return createTimeFromDatetimeClass(inputTime,
                                       outputFormat,
                                       timeAdd,
                                       addUnit)


def createTimeFromDatetimeClass(inputTime,
                                outputFormat='%Y-%m-%d %H:%M',
                                timeAdd=0,
                                addUnit='minutes'):
    """
    todo: addUnit
    """
    if timeAdd:
        if addUnit == 'minutes':
            timeAdd = 60 * timeAdd
            timedelta = datetime.timedelta(seconds=timeAdd)
    else:
        timedelta = datetime.timedelta(seconds=0)
    outputTime = inputTime + timedelta
    return datetime.datetime.strftime(outputTime, outputFormat)


timestamp = lambda: unicode(int(time.time()))

if __name__ == '__main__':
    print createTimeFromStr('')
