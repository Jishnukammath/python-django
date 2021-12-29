# coding_challenge_6 : file operation
# file write

file=open("demo.txt","w")
file.write("hello ...!!")

file.close()

# file read

file1=open("demo.txt","r")
content=file1.read()
print(content)
file1.close()


# file append

file2=open("demo.txt","a")
file2.write("\nhai ...")
file2.write("\navodha_python ...")

file2.close()