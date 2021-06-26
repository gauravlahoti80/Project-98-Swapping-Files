import pyttsx3

input_speak = pyttsx3.init()

def swapFile():
    input_speak.say("Enter the path of the file to swap: ")
    input_speak.runAndWait()
    file1 = str(input("Enter the path of the file to swap: "))

    input_speak.say("Enter the path where you need to swap: ")
    input_speak.runAndWait()
    file2 = str(input("Enter the path where you need to swap: "))

    if  file1 == file2:
        input_speak.say("You have entered same file names. change and try again.")
        input_speak.runAndWait()
        print("You have entered same file names. Change and try again.")
        swapFile()

    with open(file1 , 'r') as a:
        data_a = a.read()
    with open(file2 , 'r') as b:
        data_b = b.read()
    with open(file1 , 'w') as a:
        a.write(data_b)
    with open(file2 , 'w') as b:
        b.write(data_a)

swapFile()
