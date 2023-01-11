from task_read_write_21 import RandomWordsGenerator
import Classesnotes



newObject = RandomWordsGenerator("I am somename")
#print (newObject.somename)

test_file2 = [i for i in newObject.file1]
print (type(newObject.file1))


f = open("file1.txt", "r")
#print(f.read())
