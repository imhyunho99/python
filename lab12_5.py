"""
movie.txt에 저장돤 내용을 읽어 movie 객체를 만든후 이를 movie.p에 bi 형태로 저장하라
"""
from pickle import *

infile = open("movie.txt", "r")
newfile = open("my_movies", "wb")
while True:
    string = infile.readline()
    m = string.split(", ")
    if not string:
        break
    if m[1] in "\n":
        m[1] = m[1][0:len(m[1]) - 2]
    print(m,end = "")
