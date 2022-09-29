#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  # импорт из математической библиотеки
import numpy  # импорт из библиотеки
import matplotlib.pyplot as mpp  # импорт из библиотеки в Python project

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':  # питон проверяет и запускает файлы
    arguments = numpy.arange(0, 200, 0.1)  # задаёт координаты для графика
    mpp.plot(  # строит график
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]  # задаёт функцию
    )
    mpp.show()  # выводит график
