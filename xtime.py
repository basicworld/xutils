# -*- coding: utf-8 -*-
"""
"""
import datetime
import time


def createTimeFromStr(inputTime,
                      inputFormat='%Y-%m-%d %H:%M',
                      outputFormat='%Y-%m-%d %H:%M',
                      timeAdd=0,
                      addUnit='minutes'):
    inputTime = time.strptime(inputTime, inputFormat)
    inputTime = datetime.datetime(*inputTime[:6])
    if timeAdd:
        if addUnit == 'minutes':
            timeAdd = 60 * timeAdd
            timedelta = datetime.timedelta(seconds=timeAdd)
    else:
        timedelta = datetime.timedelta(seconds=0)
    outputTime = inputTime + timedelta
    return datetime.datetime.strftime(outputTime, outputFormat)


def createTimeFromDatetimeClass(inputTime,
                                outputFormat='%Y-%m-%d %H:%M',
                                timeAdd=0,
                                addUnit='minutes'):
    if timeAdd:
        if addUnit == 'minutes':
            timeAdd = 60 * timeAdd
            timedelta = datetime.timedelta(seconds=timeAdd)
    else:
        timedelta = datetime.timedelta(seconds=0)
    outputTime = inputTime + timedelta
    return datetime.datetime.strftime(outputTime, outputFormat)


if __name__ == '__main__':
    print createTimeFromStr('2016-06-13 09:56')
