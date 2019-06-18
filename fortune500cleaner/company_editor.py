
def read_txt(file_name, new_file_name):
    f = open(file_name, "r")
    fh = open(new_file_name, "w")
    f1 = f.readlines()
    for x in f1:
        while ord(x[0]) < 65:
            x = x[1:]
        while ord(x[len(x)-1]) < 65:
            x = x[:len(x)-1]
        print(x)
        x = x + "\n"
        fh.writelines(x)


read_txt("Fortune_Global500.txt", "Fortune_Global500_final.txt")