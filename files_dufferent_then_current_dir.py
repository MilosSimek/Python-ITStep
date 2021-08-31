import os
print(os.getcwd())
#os.chdir("Python_code")


file = open(os.path.join("Text", "slovnik1.txt"), 
    encoding="utf-8")

ovoce = file.read()

print(ovoce)

file.close()
