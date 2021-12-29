# file read

file1=open("demo.txt","r")
content=file1.read()
print(content)
file1.close()


# file write


file2=open("demo1.txt","w")
file2.write("hello ...!!")

file2.close()


# file append

file3=open("demo3.txt","a")
file3.write("hai ...")
file3.write("jishnukammath ...")
file3.close()