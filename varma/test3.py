
class file_append:


    def append(self,string1):
        self.string1 = string1
        with open("file12.txt","a") as f1:
            f1.write("\n"+self.string1)

string1 = input()
varma = file_append()
varma.append(string1)
