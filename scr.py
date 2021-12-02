from multiprocessing import Lock as thread_lock
from multiprocessing import cpu_count, current_process
from multiprocessing import Process, Manager
from subprocess import DEVNULL, Popen, check_call
from threading import Thread
from hashlib import sha1
from platform import machine as osprocessor
from re import sub
from socket import socket
import requests
from time import time, sleep, strptime, ctime
from datetime import datetime
from random import randint
from os import execl, mkdir, _exit
import sys
import os
import json
import cpuinfo
from pathlib import Path
from random import choice
from signal import SIGINT, signal
from locale import LC_ALL, getdefaultlocale, getlocale, setlocale
from configparser import ConfigParser
from colorama import init, Fore, Style, Back
from configparser import ConfigParser
configparser = ConfigParser()
init()


def Banner():
    data = """
            [0;33;5;43;103m. . . . . . . [0;33;5;41;101m.[0;33;5;43;103m [0;31;5;41;101m [0;33;5;41;101m. [0;33;5;43;103m.[0;31;5;41;101m [0;33;5;41;101m.[0;33;5;43;103m [0;31;5;41;101m [0;33;5;43;103m.[0;33;5;41;101m [0;33;5;43;103m. . . . . . . [0m
            [0;33;5;43;103m. [0;33;5;41;101m [0;37;5;43;103mX[0;33;5;43;103m [0;33;5;41;101m [0;37;5;43;103mX[0;33;5;43;103m [0;33;5;41;101m [0;37;5;43;103mX[0;33;5;41;101m    [0;33;5;43;103m [0;31;5;41;101m [0;33;5;41;101m [0;37;5;43;103mX[0;33;5;41;101m  [0;33;5;43;103m [0;31;5;41;101m [0;33;5;41;101m [0;33;5;43;103m [0;31;5;41;101m [0;37;5;43;103mX[0;31;5;41;101m [0;33;5;41;101m [0;33;5;43;103m [0;33;5;41;101m [0;37;5;43;103mX[0;1;31;91;5;43;103m8[0;33;5;43;103m [0;33;5;41;101m [0;37;5;43;103mX[0;33;5;43;103m [0;33;5;41;101m [0;37;5;43;103mX[0;33;5;43;103m [0;1;33;93;5;41;101m8[0m
            [0;33;5;43;103m. [0;37;5;43;103mX[0;33;5;43;103m  [0;37;5;43;103mX[0;1;31;91;5;43;103m88[0;1;33;93;5;41;101m8[0;33;5;41;101m [0;37;5;43;103mX[0;33;5;41;101m [0;37;5;43;103m@[0;31;5;41;101m [0;35;5;41;101m [0;1;33;93;47m8[0;33;5;41;101m [0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8[0;33;5;41;101m [0;37;5;41;101m8[0;1;31;91;5;43;103m8[0;33;5;41;101m [0;37;5;41;101m8[0;33;5;41;101m [0;1;31;91;5;43;103m88[0;37;5;41;101m8[0;33;5;41;101m [0;37;5;43;103mX[0;33;5;41;101m [0;33;5;43;103m [0;37;5;41;101m@[0;37;5;43;103m:[0;33;5;43;103m  [0;37;5;43;103mX[0;1;31;91;5;43;103m@[0;33;5;43;103m [0;37;5;43;103mS[0m
            [0;33;5;43;103m. [0;1;33;93;5;41;101m8[0;33;5;43;103m [0;1;33;93;5;41;101m8[0;33;5;43;103m [0;31;5;41;101m [0;33;5;41;101m [0;37;5;43;103m8[0;31;5;41;101m [0;33;5;41;101m [0;1;31;91;5;43;103m8[0;33;5;41;101m [0;37;5;43;103m@[0;31;5;41;101m [0;1;33;93;5;41;101m@8[0;33;5;41;101m [0;37;5;43;103m8[0;33;5;41;101m [0;1;31;91;5;43;103m8[0;37;5;41;101m@[0;1;31;91;5;43;103m88[0;1;33;93;5;41;101m8[0;37;5;41;101m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m88[0;1;33;93;5;41;101m@8[0;33;5;41;101m [0;37;5;43;103mS[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8[0;37;5;43;103mX[0;1;31;91;5;43;103m@[0;37;5;43;103m%[0;1;31;91;5;43;103m8[0;33;5;43;103m [0m
            [0;33;5;43;103m. [0;37;5;43;103mX[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m8[0;33;5;41;101m [0;37;5;43;103m8[0;31;5;41;101m [0;33;5;41;101m [0;1;31;91;5;43;103m8[0;33;5;41;101m [0;1;31;91;5;43;103m8[0;33;5;41;101m [0;1;33;93;5;41;101m@@[0;33;5;41;101m [0;37;5;43;103m8[0;33;5;41;101m [0;1;33;93;5;41;101m8888[0;33;5;41;101m [0;37;5;43;103m8[0;33;5;41;101m [0;1;31;91;5;43;103m@[0;1;33;93;5;41;101m88[0;37;5;41;101m8[0;1;31;91;5;43;103m888[0;1;33;93;5;41;101m@88[0;37;5;43;103mS[0;1;31;91;5;43;103m@[0;33;5;43;103m [0;1;31;91;5;43;103m@[0;37;5;43;103mS[0m
            [0;33;5;43;103m.[0;1;31;91;5;43;103m8[0;33;5;43;103m [0;31;5;41;101m [0;37;5;41;101m8[0;1;33;93;5;41;101m@[0;31;5;41;101m [0;1;33;93;5;41;101m8@[0;37;5;41;101m8[0;1;33;93;5;41;101m8[0;37;5;41;101m8[0;1;31;91;5;43;103m8[0;1;31;91;47mX[0;1;31;91;5;43;103m8[0;1;31;91;47mX[0;1;33;93;5;41;101m8[0;1;33;93;47m@[0;1;33;93;5;41;101m@[0;1;33;93;47mS[0;37;5;41;101m8[0;37;5;43;103m8[0;1;33;93;5;41;101m8@[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m@[0;37;5;41;101m8[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m88[0;37;5;41;101m8[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m8[0;37;5;43;103m8[0;1;33;93;5;41;101mX8[0;1;31;91;5;43;103m8[0;37;5;43;103mX[0;1;31;91;5;43;103mX[0;33;5;43;103m [0m
            [0;33;5;43;103m. [0;35;5;41;101m [0;1;33;93;5;41;101m8[0;33;5;41;101m [0;1;33;93;5;41;101m8[0;37;5;41;101m8[0;1;33;93;5;41;101m@[0;33;5;41;101m [0;1;33;93;5;41;101m8@X[0;37;5;47;107m8          :[0;1;37;97;47m [0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m88[0;1;31;91;5;43;103m88[0;1;33;93;5;41;101m888[0;1;31;91;5;43;103m88[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8[0;37;5;43;103mX[0;1;31;91;5;43;103m@[0m
            [0;33;5;43;103m.[0;33;5;41;101m [0;1;33;93;47m8[0;31;5;41;101m [0;1;33;93;5;41;101m8[0;37;5;41;101m@[0;1;33;93;5;41;101m@@8[0;37;5;41;101m8[0;1;33;93;5;41;101m@X[0;37;5;47;107m8;     ..  . t[0;1;37;97;47m [0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m88[0;37;5;43;103m8[0;1;33;93;5;41;101m@[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m8[0;37;5;43;103m8[0;1;33;93;5;41;101m@[0;1;31;91;5;43;103m88@[0;37;5;43;103mS[0m
            [0;33;5;43;103m.[0;31;5;41;101m [0;33;5;41;101m [0;1;31;91;5;43;103m8[0;33;5;41;101m [0;1;33;93;5;41;101m8X[0;37;5;41;101m8[0;1;33;93;5;41;101m@XXX[0;1;31;91;47m@[0;37;5;47;107m8[0;37;5;43;103m8[0;1;37;97;47m [0;37;5;47;107m8[0;1;31;91;5;43;103m8[0;37;5;47;107m8[0;1;33;93;5;41;101m8[0;1;31;91;47m@[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8[0;37;5;47;107m88;.S[0;37;5;43;103m8[0;1;33;93;5;41;101mX8[0;1;31;91;5;43;103m8[0;1;31;91;47m8[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8[0;37;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8[0;37;5;43;103m%[0m
            [0;33;5;41;101m.[0;33;5;43;103m [0;31;5;41;101m [0;37;5;41;101m8[0;1;31;91;5;43;103m8[0;37;5;41;101m@[0;1;33;93;5;41;101m@XX@[0;37;5;41;101m8[0;1;33;93;5;41;101m8[0;37;5;47;107m88 %:   :[0;37;5;43;103m8[0;1;33;93;5;41;101mS@[0;1;31;91;5;43;103m8[0;37;5;47;107m@  8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m88888[0;1;33;93;5;41;101m88[0;37;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m@[0m
            [0;33;5;41;101m. [0;37;5;43;103mX[0;31;5;41;101m [0;1;33;93;5;41;101m8XX@[0;37;5;41;101m8[0;1;33;93;5;41;101m8@@[0;37;5;43;103m8[0;1;35;95;5;47;107m@[0;1;37;97;5;43;103m8[0;37;5;47;107m8[0;1;33;93;5;47;107m8[0;1;35;95;5;47;107m8[0;1;33;93;5;47;107m8[0;37;5;47;107mS .[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m88[0;37;5;43;103m8[0;37;5;47;107m:.:[0;37;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m888[0;37;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m888[0;37;5;43;103mX[0m
            [0;33;5;41;101m.[0;1;31;91;5;43;103m8[0;31;5;41;101m [0;1;31;91;5;43;103m8[0;33;5;41;101m [0;1;33;93;5;41;101m8[0;37;5;41;101m8[0;1;33;93;5;41;101m8@@@XXXSSS@X[0;1;31;91;5;43;103m8[0;37;5;47;107m  ;[0;1;33;93;5;41;101m888[0;37;5;47;107m8; 8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8[0;37;5;43;103m8[0;1;33;93;5;41;101mX8[0;37;5;43;103m8[0;1;33;93;5;41;101m8[0;37;5;43;103m@[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8[0m
            [0;33;5;41;101m.[0;1;33;93;5;41;101m88[0;37;5;41;101m8[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m@@@@[0;37;5;41;101m8[0;1;33;93;5;41;101m8888888888[0;37;5;47;107m; @[0;1;31;91;5;43;103m88[0;1;33;93;5;41;101m8[0;37;5;47;107m8t:[0;1;33;93;5;47;107m@[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m8[0;37;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m888@[0;37;5;43;103mX[0m
            [0;33;5;41;101m.[0;1;31;91;5;43;103m8[0;33;5;41;101m [0;1;31;91;5;43;103m8[0;37;5;41;101m8[0;1;33;93;5;41;101m@@[0;37;5;41;101m8[0;1;33;93;5;41;101m88888888[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8[0;37;5;47;107m88 8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m88[0;37;5;47;107m8:.[0;1;33;93;5;47;107m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m888@@[0;37;5;43;103m8[0;1;31;91;5;43;103m888[0m
            [0;33;5;41;101m.[0;33;5;43;103m [0;33;5;41;101m [0;1;33;93;5;41;101m88@8888[0;37;5;41;101m8[0;1;31;91;5;43;103m8[0;37;5;47;107m8...:.SX.8[0;1;31;91;5;43;103m888[0;37;5;47;107m8S.X[0;1;31;91;5;43;103m88[0;37;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m@[0;37;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8@[0;37;5;43;103m8[0;1;31;91;5;43;103m@[0m
            [0;33;5;43;103m.[0;31;5;41;101m [0;37;5;43;103m8[0;33;5;41;101m [0;1;31;91;5;43;103m8[0;37;5;41;101m8[0;1;33;93;5;41;101m8888[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m@[0;37;5;47;107m8; ....%[0;1;33;93;5;47;107m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m8[0;37;5;47;107m8@  [0;1;33;93;5;47;107m8[0;1;31;91;5;43;103m888@88[0;37;5;43;103m@[0;1;31;91;5;43;103m8@@[0;37;5;43;103mS[0m
            [0;33;5;43;103m.[0;33;5;41;101m [0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m8888[0;37;5;41;101m8[0;1;31;91;5;43;103m8[0;37;5;41;101m8[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m8[0;37;5;43;103m8[0;37;5;47;107m8[0;1;31;91;5;43;103m8[0;37;5;47;107m8[0;37;5;43;103m8[0;37;5;47;107m8[0;37;5;43;103m88[0;1;33;93;5;41;101m8[0;37;5;47;107m8[0;1;37;97;5;43;103m8[0;37;5;47;107m8@ :[0;1;33;93;5;47;107m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8@[0;37;5;43;103m8[0;1;31;91;5;43;103m8[0;37;5;43;103m8[0;1;31;91;5;43;103m88X[0;37;5;43;103m8[0;1;31;91;5;43;103m@S[0m
            [0;33;5;43;103m.[0;37;5;43;103mS[0;1;33;93;5;41;101m8[0;37;5;41;101m8[0;1;33;93;5;41;101m88[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m88[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m88[0;37;5;47;107m8t  .% [0;1;35;95;5;47;107mt[0;37;5;47;107m   :S[0;1;33;93;5;47;107m8[0;1;31;91;5;43;103m88@@8888X[0;37;5;43;103m8[0;1;31;91;5;43;103m8X[0;37;5;43;103mS[0;1;31;91;5;43;103mS[0m
            [0;33;5;43;103m. [0;1;31;91;5;43;103m88[0;1;33;93;5;41;101m8[0;37;5;41;101m8[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m888[0;37;5;43;103m8[0;1;33;93;5;41;101mS[0;37;5;47;107m888888888[0;1;33;93;5;47;107mX[0;37;5;47;107m8[0;1;31;91;5;43;103m@@88@[0;37;5;43;103m8[0;1;31;91;5;43;103m8[0;37;5;43;103m8[0;1;31;91;5;43;103m8[0;37;5;43;103m8[0;1;31;91;5;43;103m8@@[0;37;5;43;103mX[0;1;31;91;5;43;103mX%[0;37;5;43;103m%[0m
            [0;33;5;43;103m. [0;37;5;43;103m@[0;1;31;91;5;43;103m88[0;1;33;93;5;41;101m88[0;1;33;93;47m8[0;1;33;93;5;41;101m@8@8888[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8888[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m88@@[0;37;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8@8@@[0;37;5;43;103m@[0;1;31;91;5;43;103m@XS[0;37;5;43;103mX[0;1;31;91;5;43;103mS[0;33;5;43;103m [0m
            [0;33;5;43;103m.[0;1;31;91;5;43;103m8[0;33;5;43;103m [0;37;5;43;103m@S[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m888[0;37;5;43;103m8[0;1;33;93;5;41;101m@[0;1;31;91;5;43;103m8888888888@@@@88X[0;37;5;43;103m8[0;1;31;91;5;43;103m8X[0;37;5;43;103m8[0;1;31;91;5;43;103m8X[0;37;5;43;103mX[0;1;31;91;5;43;103mS[0;37;5;43;103mS[0;1;31;91;5;43;103mSS[0;37;5;43;103mS[0m
            [0;33;5;43;103m. [0;1;33;93;5;41;101m8[0;33;5;43;103m [0;1;31;91;5;43;103m8[0;37;5;43;103m@S[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m88[0;1;31;91;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m88888888@@@[0;37;5;43;103m8[0;1;31;91;5;43;103m8[0;37;5;43;103m8[0;1;31;91;5;43;103m8@@[0;37;5;43;103m8[0;1;31;91;5;43;103m8XS[0;37;5;43;103mX[0;1;31;91;5;43;103mX[0;37;5;43;103m%[0;1;31;91;5;43;103mX[0;37;5;43;103m%[0;1;31;91;5;43;103mSS[0m
            [0;33;5;43;103m. [0;37;5;43;103m@[0;1;31;91;5;43;103m8[0;37;5;43;103mS[0;1;31;91;5;43;103mSS[0;37;5;43;103mXS[0;1;31;91;5;43;103m88[0;37;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m88888@@[0;37;5;43;103m8[0;1;31;91;5;43;103m88888[0;37;5;43;103m8[0;1;31;91;5;43;103m8X@[0;37;5;43;103mX[0;1;31;91;5;43;103mS[0;37;5;43;103mX[0;1;31;91;5;43;103mS%%%%[0;37;5;43;103mX[0;1;31;91;5;43;103m%[0m
            [0;33;5;43;103m.[0;1;31;91;5;43;103m8[0;33;5;43;103m [0;1;31;91;5;43;103m@[0;37;5;43;103m%[0;1;31;91;5;43;103mS[0;37;5;43;103m%[0;1;31;91;5;43;103mXS[0;37;5;43;103m@[0;1;31;91;5;43;103mSX[0;37;5;43;103m8[0;1;31;91;5;43;103m8[0;37;5;43;103m8[0;1;31;91;5;43;103m8[0;37;5;43;103m8[0;1;33;93;5;41;101m8[0;37;5;43;103m8[0;1;33;93;5;41;101m8[0;1;31;91;5;43;103m8@[0;37;5;43;103m8[0;1;31;91;5;43;103m8[0;37;5;43;103m8[0;1;31;91;5;43;103m@X[0;37;5;43;103m@[0;1;31;91;5;43;103mS[0;37;5;43;103mX[0;1;31;91;5;43;103mS%S[0;37;5;43;103mS[0;1;31;91;5;43;103mS[0;37;5;43;103mX[0;1;31;91;5;43;103m%[0;37;5;43;103mS[0;1;31;91;5;43;103mX[0;37;5;43;103mt[0m
            """
    return data



def handler(signal_received, frame):
    """
    Nicely handle CTRL+C exit
    """
    if current_process().name == "MainProcess":
        PrintBlocks(
            get_string("sigint_detected")
            + Style.NORMAL
            + Fore.RESET
            + get_string("goodbye"),
            "warning")
    _exit(0)


class Settings:
    """
    Class containing default miner and server settings
    """
    ENCODING = "UTF8"
    SEPARATOR = ","
    VER = 2.74
    DATA_DIR = "STG"
    TRANSLATIONS_FILE = "/string.json"
    SETTINGS_FILE = "/Settings.cfg"

    SOC_TIMEOUT = 15
    REPORT_TIME = 50
    DONATE_LVL = 0

    BLOCK = " ‖ "
    PICK = ""
    COG = " @"
    if os.name != "nt" or bool(os.name == "nt" and os.environ.get("WT_SESSION")):
        # Windows' cmd does not support emojis, shame!
        PICK = " ⛏"
        COG = " ⚙"


class MiningAlgorithms:
    def DUCOS1(last_h: str, exp_h: str, diff: int, eff: int):
        time_start = time()
        base_hash = sha1(last_h.encode('ascii'))

        for nonce in range(100 * diff + 1):
            temp_h = base_hash.copy()
            temp_h.update(str(nonce).encode('ascii'))
            d_res = temp_h.hexdigest()

            if eff != 0:
                if nonce % 5000 == 0:
                    sleep(eff / 100)

            if d_res == exp_h:
                time_elapsed = time() - time_start
                hashrate = nonce / time_elapsed
                return [nonce, hashrate]

        return [0, 0]



class Client:
    """
    Class helping to organize socket connections
    """
    def connect(pool: tuple):
        global s
        s = socket()
        s.settimeout(Settings.SOC_TIMEOUT)
        s.connect((pool))

    def send(msg: str):
        sent = s.sendall(str(msg).encode(Settings.ENCODING))
        return True

    def recv(limit: int = 128):
        data = s.recv(limit).decode(Settings.ENCODING).rstrip("\n")
        return data

    def fetch_pool():
        """
        Fetches best pool from the /getPool API endpoint
        """
        while True:
            PrintBlocks(" " + get_string("connection_search"),
                         "warning", "net0")
            try:
                response = requests.get(
                    "https://server.duinocoin.com/getPool").json()
                if response["success"] == True:
                    NODE_ADDRESS = response["ip"]
                    NODE_PORT = response["port"]
                    return (NODE_ADDRESS, NODE_PORT)
                elif "message" in response:
                    PrintBlocks(f"Warning: {response['message']}"
                                 + ", retrying in 15s", "warning", "net0")
                    sleep(10)
                else:
                    raise Exception(
                        "no response - IP ban or connection error")
            except Exception as e:
                PrintBlocks(f"Error fetching mining node: {e}"
                             + ", retrying in 15s", "error", "net0")
                sleep(15)




def get_prefix(symbol: str, val: float, accuracy: int):
    """
    H/s, 1000 => 1 kH/s
    """
    if val >= 1_000_000_000_000:  # Really?
        val = str(round((val / 1_000_000_000_000), accuracy)) + " T"
    elif val >= 1_000_000_000:
        val = str(round((val / 1_000_000_000), accuracy)) + " G"
    elif val >= 1_000_000:
        val = str(round((val / 1_000_000), accuracy)) + " M"
    elif val >= 1_000:
        val = str(round((val / 1_000))) + " k"
    else:
        val = str(round(val)) + " "
    return val + symbol



def periodic_report(start_time, end_time,
                    shares, hashrate, uptime):
    """
    Displays nicely formated uptime stats
    """
    seconds = round(end_time - start_time)
    PrintBlocks(get_string("periodic_mining_report")
                 + Fore.RESET + Style.NORMAL
                 + get_string("report_period")
                 + str(seconds) + get_string("report_time")
                 + get_string("report_body1")
                 + str(shares) + get_string("report_body2")
                 + str(round(shares/seconds, 1))
                 + get_string("report_body3")
                 + get_string("report_body4")
                 + str(get_prefix("H/s", hashrate, 2))
                 + get_string("report_body5")
                 + str(int(hashrate*seconds))
                 + get_string("report_body6")
                 + get_string("total_mining_time")
                 + str(uptime), "success")

def calculate_uptime(start_time):
    """
    Returns seconds, minutes or hours passed since timestamp
    """
    uptime = time() - start_time
    if uptime <= 59:
        return str(round(uptime)) + get_string("uptime_seconds")
    elif uptime == 60:
        return str(round(uptime // 60)) + get_string("uptime_minute")
    elif uptime >= 60:
        return str(round(uptime // 60)) + get_string("uptime_minutes")
    elif uptime == 3600:
        return str(round(uptime // 3600)) + get_string("uptime_hour")
    elif uptime >= 3600:
        return str(round(uptime // 3600)) + get_string("uptime_hours")


def PrintBlocks(message :str = None, states: str = "success", senders: str = "sys0"):
    if senders.startswith("net"):
        bg_color = Back.BLUE
    elif senders.startswith("cpu"):
        bg_color = Back.YELLOW
    elif senders.startswith("sys"):
        bg_color = Back.GREEN

    if states == "success":
        fg_color = Fore.GREEN
    elif states == "error":
        fg_color = Fore.RED
    else:
        fg_color = Fore.YELLOW

    with thread_lock():
        print(Fore.WHITE + "\033[35;1m[" + datetime.now().strftime(Style.DIM + "\033[36;1m%H:%M:%S" + "\033[35;1m] ")
              + Style.BRIGHT + bg_color + " " + senders + " "
              + Back.RESET + " " + fg_color + message.strip())



def MiningPrint(id, type, accept, reject, hashrate, total_hashrate, computetime, diff, ping, back_color):
    total_hashrate = get_prefix("H/s", total_hashrate, 2)
    diff = get_prefix("", int(diff), 0)

    if type == "accept":
        share_str = get_string("accepted")
        fg_color = Fore.GREEN
    elif type == "block":
        share_str = get_string("block_found")
        fg_color = Fore.YELLOW
    else:
        share_str = get_string("rejected")
        fg_color = Fore.RED

    with thread_lock():
        print(Fore.WHITE + datetime.now().strftime(Style.DIM + "%H:%M:%S ")
              + Fore.WHITE + Style.BRIGHT + back_color + Fore.RESET
              + " cpu" + str(id) + " " + Back.RESET
              + fg_color + Settings.PICK + share_str + Fore.RESET
              + str(accept) + "/" + str(accept + reject) + Fore.YELLOW
              + " (" + str(round(accept / (accept + reject) * 100)) + "%)"
              + Style.NORMAL + Fore.RESET
              + " ∙ " + str("%04.1f" % float(computetime)) + "s"
              + Style.NORMAL + " ∙ " + Fore.BLUE + Style.BRIGHT
              + str(total_hashrate) + Fore.RESET + Style.NORMAL
              + Settings.COG + f" diff {diff} ∙ " + Fore.CYAN
              + f"ping {(int(ping))}ms")


def get_string(string_name):
    """
    Gets a string from the language file
    """
    if string_name in lang_file["english"]:
        return lang_file["english"][string_name]
    else:
        return "String not found: " + string_name

class Miner:
    def greeting():
        diff_str = get_string("net_diff_short")
        if user_settings["start_diff"] == "LOW":
            diff_str = get_string("low_diff_short")
        elif user_settings["start_diff"] == "MEDIUM":
            diff_str = get_string("medium_diff_short")

        current_hour = strptime(ctime(time())).tm_hour
        greeting = get_string("greeting_back")
        if current_hour < 12:
            greeting = get_string("greeting_morning")
        elif current_hour == 12:
            greeting = get_string("greeting_noon")
        elif current_hour > 12 and current_hour < 18:
            greeting = get_string("greeting_afternoon")
        elif current_hour >= 18:
            greeting = get_string("greeting_evening")

        print(Banner())

        if lang != "english":
            print(Style.DIM + Fore.YELLOW + Settings.BLOCK
                  + Style.NORMAL + Fore.RESET + lang.capitalize()
                  + " translation: " + Fore.YELLOW
                  + get_string("translation_autor"))

        try:
            print(Style.DIM + Fore.YELLOW + Settings.BLOCK
                  + Style.NORMAL + Fore.RESET + "CPU: " + Style.BRIGHT
                  + Fore.YELLOW + str(user_settings["threads"])
                  + "x " + str(cpu["brand_raw"]))
        except:
            print(Style.DIM + Fore.YELLOW + Settings.BLOCK
                  + Style.NORMAL + Fore.RESET + "CPU: " + Style.BRIGHT
                  + Fore.YELLOW + str(user_settings["threads"])
                  + "x threads")

        if os.name == "nt" or os.name == "posix":
            print(Style.DIM + Fore.YELLOW
                  + Settings.BLOCK + Style.NORMAL + Fore.RESET
                  + get_string("donation_level") + Style.BRIGHT
                  + Fore.YELLOW + str(user_settings["donate"]))

        print(Style.DIM + Fore.YELLOW + Settings.BLOCK
              + Style.NORMAL + Fore.RESET + get_string("algorithm")
              + Style.BRIGHT + Fore.YELLOW + user_settings["algorithm"]
              + Settings.COG + " " + diff_str)

        if user_settings["identifier"] != "None":
            print(Style.DIM + Fore.YELLOW + Settings.BLOCK
                  + Style.NORMAL + Fore.RESET + get_string("rig_identifier")
                  + Style.BRIGHT + Fore.YELLOW + user_settings["identifier"])

        print(Style.DIM + Fore.YELLOW + Settings.BLOCK
              + Style.NORMAL + Fore.RESET + str(greeting)
              + ", " + Style.BRIGHT + Fore.YELLOW
              + str(user_settings["username"]) + "!\n")

    def preload():
        """
        Creates needed directories and files for the miner
        """
        global lang_file
        global lang

        if not Path(Settings.DATA_DIR).is_dir():
            mkdir(Settings.DATA_DIR)

        with open(Settings.DATA_DIR + Settings.TRANSLATIONS_FILE, "r",
                  encoding=Settings.ENCODING) as file:
            lang_file = json.load(file)

        try:
            if not Path(Settings.DATA_DIR + Settings.SETTINGS_FILE).is_file():
                lang = "english"
            else:
                try:
                    configparser.read(Settings.DATA_DIR
                                      + Settings.SETTINGS_FILE)
                    lang = configparser["PC Miner"]["language"]
                except Exception:
                    lang = "english"
        except Exception as e:
            print("Error with lang file, falling back to english: " + str(e))
            lang = "english"

    def load_cfg():
        """
        Loads miner settings file or starts the config tool
        """
        if not Path(Settings.DATA_DIR + Settings.SETTINGS_FILE).is_file():
            print(get_string("basic_config_tool")
                  + Settings.DATA_DIR
                  + get_string("edit_config_file_warning")
                  + "\n"
                  + get_string("dont_have_account")
                  + Fore.YELLOW
                  + get_string("wallet")
                  + Fore.RESET
                  + get_string("register_warning"))

            username = input(get_string("ask_username") + Style.BRIGHT)
            if not username:
                username = choice(["revox", "Bilaboz", "JoyBed", "Connor2"])

            algorithm = "DUCO-S1"

            intensity = None
            intensity = sub(r"\D", "",
                input(Style.NORMAL + get_string("ask_intensity") + Style.BRIGHT))

            if not intensity:
                intensity = 95
            elif float(intensity) > 100:
                intensity = 100
            elif float(intensity) < 1:
                intensity = 1

            threads = sub(r"\D", "",
                          input(Style.NORMAL + get_string("ask_threads")
                                + str(cpu_count()) + "): " + Style.BRIGHT))
            if not threads:
                threads = cpu_count()

            if int(threads) > 8:
                threads = 8
                PrintBlocks(
                    Style.BRIGHT
                    + get_string("max_threads_notice"))
            elif int(threads) < 1:
                threads = 1

            print(Style.BRIGHT
                  + "1" + Style.NORMAL + " - " + get_string("low_diff")
                  + "\n" + Style.BRIGHT
                  + "2" + Style.NORMAL + " - " + get_string("medium_diff")
                  + "\n" + Style.BRIGHT
                  + "3" + Style.NORMAL + " - " + get_string("net_diff"))
            start_diff = sub(r"\D", "",
                             input(Style.NORMAL + get_string("ask_difficulty")
                                   + Style.BRIGHT))
            if start_diff == "1":
                start_diff = "LOW"
            elif start_diff == "3":
                start_diff = "NET"
            else:
                start_diff = "MEDIUM"

            rig_id = input(Style.NORMAL + get_string("ask_rig_identifier")
                           + Style.BRIGHT)
            if rig_id.lower() == "y":
                rig_id = str(input(Style.NORMAL + get_string("ask_rig_name")
                                   + Style.BRIGHT))
            else:
                rig_id = "None"

            donation_level = '0'
            if os.name == 'nt' or os.name == 'posix':
                donation_level = input(Style.NORMAL
                                       + get_string('ask_donation_level')
                                       + Style.BRIGHT)

            donation_level = sub(r'\D', '', donation_level)
            if donation_level == '':
                donation_level = 1
            if float(donation_level) > int(5):
                donation_level = 5
            if float(donation_level) < int(0):
                donation_level = 0

            configparser["PC Miner"] = {
                "username":    username,
                "intensity":   intensity,
                "threads":     threads,
                "start_diff":  start_diff,
                "donate":      int(donation_level),
                "identifier":  rig_id,
                "algorithm":   algorithm,
                "language":    lang,
                "soc_timeout": Settings.SOC_TIMEOUT,
                "report_sec":  Settings.REPORT_TIME,
                "discord_rp":  "y"}

            with open(Settings.DATA_DIR + Settings.SETTINGS_FILE,
                      "w") as configfile:
                configparser.write(configfile)
                print(Style.RESET_ALL + get_string("config_saved"))

        configparser.read(Settings.DATA_DIR
                          + Settings.SETTINGS_FILE)
        return configparser["PC Miner"]

    def m_connect(id, pool):
        retry_count = 0
        while True:
            try:
                if retry_count > 3:
                    pool = Client.fetch_pool()
                    retry_count = 0

                socket_connection = Client.connect(pool)
                POOL_VER = Client.recv(5)

                if id == 0:
                    Client.send("MOTD")
                    motd = Client.recv(512).replace("\n", "\n\t\t")

                    PrintBlocks("MOTD: " + Fore.RESET + Style.NORMAL
                                 + str(motd), "success", "net" + str(id))

                    if float(POOL_VER) <= Settings.VER:
                        PrintBlocks(get_string("connected") + Fore.RESET
                                     + Style.NORMAL +
                                     get_string("connected_server")
                                     + str(POOL_VER) + ", " + pool[0] + ":"
                                     + str(pool[1]) + ")", "success",
                                     "net" + str(id))
                    else:
                        PrintBlocks(get_string("outdated_miner")
                                     + str(Settings.VER) + ") -"
                                     + get_string("server_is_on_version")
                                     + str(POOL_VER) + Style.NORMAL
                                     + Fore.RESET +
                                     get_string("update_warning"),
                                     "warning", "net" + str(id))
                        sleep(5)
                break
            except Exception as e:
                PrintBlocks(get_string('connecting_error')
                             + Style.NORMAL + f' (connection err: {e})',
                             'error', 'net0')
                retry_count += 1
                sleep(10)
    def mine(id: int, user_settings: list,
             pool: tuple,
             accept: int, reject: int,
             hashrate: list,
             single_miner_id: str):
        """
        Main section that executes the functionalities from the sections above.
        """

        using_algo = get_string("using_algo")
        PrintBlocks(get_string("mining_thread") + str(id)
                     + get_string("mining_thread_starting")
                     + Style.NORMAL + Fore.RESET + using_algo + Fore.YELLOW
                     + str(user_settings["intensity"])
                     + "% " + get_string("efficiency"),
                     "success", "sys"+str(id))

        last_report = time()
        r_shares, last_shares = 0, 0
        while True:
            try:
                Miner.m_connect(id, pool)
                while True:
                    try:
                        while True:
                            job_req = "JOB"
                            Client.send(job_req
                                        + Settings.SEPARATOR
                                        + str(user_settings["username"])
                                        + Settings.SEPARATOR
                                        + str(user_settings["start_diff"]))

                            job = Client.recv().split(Settings.SEPARATOR)
                            if len(job) == 3:
                                break
                            else:
                                PrintBlocks(
                                    "Node message: " + str(job[1]),
                                    "warning")
                                sleep(3)

                        while True:
                            time_start = time()
                            back_color = Back.YELLOW

                            eff = 0
                            eff_setting = int(user_settings["intensity"])
                            if 99 > eff_setting >= 90:
                                eff = 0.005
                            elif 90 > eff_setting >= 70:
                                eff = 0.1
                            elif 70 > eff_setting >= 50:
                                eff = 0.8
                            elif 50 > eff_setting >= 30:
                                eff = 1.8
                            elif 30 > eff_setting >= 1:
                                eff = 3

                            result = MiningAlgorithms.DUCOS1(
                                    job[0], job[1], int(job[2]), eff)
                            computetime = time() - time_start

                            hashrate[id] = result[1]
                            total_hashrate = sum(hashrate.values())
                            while True:
                                Client.send(f"{result[0]}"
                                            + Settings.SEPARATOR
                                            + f"{result[1]}"
                                            + Settings.SEPARATOR
                                            + "Official PC Miner"
                                            + f" {Settings.VER}"
                                            + Settings.SEPARATOR
                                            + f"{user_settings['identifier']}"
                                            + Settings.SEPARATOR
                                            + Settings.SEPARATOR
                                            + f"{single_miner_id}")

                                time_start = time()
                                feedback = Client.recv(
                                ).split(Settings.SEPARATOR)
                                ping = (time() - time_start) * 1000

                                if feedback[0] == "GOOD":
                                    accept.value += 1
                                    MiningPrint(id, "accept",
                                                accept.value, reject.value,
                                                result[1], total_hashrate,
                                                computetime, job[2], ping,
                                                back_color)

                                elif feedback[0] == "BLOCK":
                                    reject.value += 1
                                    MiningPrint(id, "block",
                                                accept.value, reject.value,
                                                result[1], total_hashrate,
                                                computetime, job[2], ping,
                                                back_color)

                                elif feedback[0] == "BAD":
                                    reject.value += 1
                                    MiningPrint(id, "reject",
                                                accept.value, reject.value,
                                                result[1], total_hashrate,
                                                computetime, job[2], ping,
                                                back_color)

                                if id == 0:
                                    end_time = time()
                                    elapsed_time = end_time - last_report
                                    if elapsed_time >= Settings.REPORT_TIME:
                                        r_shares = accept.value - last_shares
                                        uptime = calculate_uptime(
                                            mining_start_time)
                                        periodic_report(last_report, end_time,
                                                        r_shares,
                                                        sum(hashrate.values()),
                                                        uptime)
                                        last_report = time()
                                        last_shares = accept.value
                                break
                            break
                    except Exception as e:
                        PrintBlocks(get_string("error_while_mining")
                                     + " " + str(e), "error", "net" + str(id))
                        sleep(5)
                        break
            except Exception as e:
                pass

Miner.preload()
p_list = []
mining_start_time = time()
if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()

    cpu = cpuinfo.get_cpu_info()
    accept = Manager().Value("i", 0)
    reject = Manager().Value("i", 0)
    hashrate = Manager().dict()

    signal(SIGINT, handler)
    user_settings = Miner.load_cfg()
    Miner.greeting()
    fastest_pool = Client.fetch_pool()

    """
    Generate a random number that's used only to
    make the wallets display one miner with many threads
    instead of many separate miners clogging it up
    (like it was before release 2.7.3)
    """
    single_miner_id = randint(0, 2811)
    threads = int(user_settings["threads"])
    if threads > 8:
        threads = 8
        PrintBlocks(Style.BRIGHT
                     + get_string("max_threads_notice"))

    for i in range(threads):
        p = Process(target=Miner.mine,
                    args=[i, user_settings,
                          fastest_pool, accept, reject,
                          hashrate, single_miner_id])
        p_list.append(p)
        p.start()
        sleep(0.05)

    for p in p_list:
        p.join()
