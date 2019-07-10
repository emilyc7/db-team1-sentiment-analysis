import numpy as np
import torch
import pandas as pd


def read_txt(file_name, new_file_name):
    f = open(file_name, "r")
    fh = open(new_file_name, "w")
    f1 = f.readlines()
    i = 0
    for x in f1:
        while ord(x[0]) < 65:
            x = x[1:]
        while ord(x[len(x)-1]) < 65:
            print(x)
            x = x[:len(x)-1]
        print(x)
        x = x + "\n"
        fh.writelines(x)
        i = i + 1
        if i == 200000:
            break


def removeTwitterHandles(file_name, new_file_name):
    # df = pd.read_csv(file_name, header=None)
    # print(df[0])
    fh = open(new_file_name, "w")
    with open(file_name, encoding="utf-8") as f:
        for i, x in enumerate(f):
            x = x.split(",""", 1)
            num = x[0]
            text = x[1]
            print(i)
            if ord(text[0]) == 34:
                text = text[1:]
            if ord(text[len(text)-2]) == 34:
                text = text[:len(text)-2] + text[len(text)-1]
            if ord(text[0]) == 64:
                text = text.split(" ", 1)[1]
            line = num + "," + text
            fh.writelines(line)
            # i = i+1
    f.close()
    fh.close()


# read_txt("Fortune_Global500.txt", "Fortune_Global500_final.txt")
removeTwitterHandles("reduced_data-6.csv", "reduced_data-6.txt")
