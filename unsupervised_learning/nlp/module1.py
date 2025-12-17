def write_textfile(filename):
    filename += '.txt'
    file = open(filename,'w')
    while True:
        sent = input("Enter a Paragraph : ")
        if sent == "":
            break
        else:
            file.write(sent + '\n')
            print("Data stored Successfully ! ")
        file.close()
    return file

# f = input("Enter file name : ")
# write_textfile(f)


# def read_textfile(filename):
#     filename += '.txt'
#     file = open(filename,'r')

#     if file:
#         content = file.read()
#         print(content)
#         file.close()
#     else:
#         print("File not found! ")

    # return file.read()
# f = input("Enter file name : ")
# read_textfile(f)


def read_textfile(filename):
    filename += '.txt'
    try:
        with open(filename, 'r') as file:
            return file.read()   # ✅ RETURN STRING
    except FileNotFoundError:
        print("File not found!")
        return ""

