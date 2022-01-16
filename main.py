import threading
import urllib.request

list=[]
list_filneNames=[]

class DownloadThread(threading.Thread):

    def __init__(self,obj, webUrlName,fileName):
        threading.Thread.__init__(self)
        self.obj = obj
        self.webUrlName = webUrlName
        self.fileName = fileName

    def getObj(self):
        return self.obj

    def run(self):
        # open a connection to a URL using urllib
        webUrl = urllib.request.urlopen(self.webUrlName)

        # get the result code and print it
        print("result code: " + str(webUrl.getcode()))

        # read the data from the URL and print it
        data = webUrl.read()

        data = data.decode("utf-8")

        f = open(self.fileName, "w")
        f.write(data)
        f.close()


class DecryptThread(threading.Thread):

    def __init__(self,obj,fileName):
        threading.Thread.__init__(self)
        self.obj = obj
        self.fileName = fileName

    def getObj(self):
        return self.obj

    def run(self):
        f=open(self.fileName)
        result = f.read()
        result1=""
        # traverse text
        for i in range(len(result)):
            char = result[i]

            # Encrypt uppercase characters
            if (char.isupper()):
                result1 += chr((ord(char) - 8 - 65) % 26 + 65)

            # Encrypt lowercase characters
            elif(char.islower()):
                result1 += chr((ord(char) - 8 - 97) % 26 + 97)
            else:
                result1+=char

        list.append(result1)
        list_filneNames.append(self.fileName)

class Combiner():
    def __init__(self,fileName, list):
        self.fileName = fileName
        self.list = list
        f=open(self.fileName,"w")
        for l in list:
            f.write(l)
            f.write('\n')

        f.close()




def startInstanceThread():

    thread1 = DownloadThread(1,"https://advancedpython.000webhostapp.com/s1.txt","s1.txt")
    print("1 - STARTING INSTANCE OF THREAD.....")
    thread1.start() # starts the thread


    print("2 - STARTING INSTANCE OF THREAD.....")
    thread2 = DownloadThread(1,"https://advancedpython.000webhostapp.com/s2.txt","s2.txt")
    thread2.start() # starts the thread


    print("3 - STRARTING INSTANCE OF THREAD.....")
    thread3 = DownloadThread(1,"https://advancedpython.000webhostapp.com/s3.txt","s3.txt")
    thread3.start() # starts the thread

    thread1.join()
    thread2.join()
    thread3.join()

def startInstanceDecryptionThread():
    myDecryptInstance1 = DecryptThread(1, "s1.txt")
    myDecryptInstance1.start()

    myDecryptInstance2 = DecryptThread(1, "s2.txt")
    myDecryptInstance2.start()

    myDecryptInstance3 = DecryptThread(1, "s3.txt")
    myDecryptInstance3.start()

    myDecryptInstance1.join()
    myDecryptInstance2.join()
    myDecryptInstance3.join()

if __name__ == '__main__':
    startInstanceThread()
    startInstanceDecryptionThread()
    Combiner = Combiner("s_final.txt",list)
    print("The order of the texts:")
    print(list_filneNames)