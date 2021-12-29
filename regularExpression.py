import re

pattern=r"jishnu kammath"

if re.match(pattern,"jishnu kammath is a devolopper"):
    print("matched")
else:
    print("not match")



if re.search(pattern,"he is a devoloper of python django ,his name is jishnu kammath"):
    print("is matched")
else:print("not match")



num=r"[A-Z] [0-9] [a-z]"
if re.search(num,"A5e"):
    print("matched")
else:print("not match")