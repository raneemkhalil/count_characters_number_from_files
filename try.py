
def main():
    l = {}
    files_list = ['file.txt', 'file1.txt', 'file2.txt']
    count = 0
    for f in files_list:
        file = open(f, 'r', encoding='UTF-8')
        while 1:
            c = file.read(1)
            if not c: break
            i = ord(c)
            count = count + 1
            if i not in l:
                l[i] = 1
            else:
                l[i] = l[i] + 1
        file.close()

    for i in l:
        c = chr(i)
        print(c, l[i], " the rate: ", (l[i]/count))

if __name__ == "__main__":
    main()

