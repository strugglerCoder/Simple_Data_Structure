listVar = ["A","B","C","D"]
print(listVar)
listVar[1]="z"
print(listVar)
add_e=listVar.append("e")      #add "e" in listVar at last pos
print(listVar)
print(add_e)                   # print none
listVar.insert(2,'s')          #add "s" at pos 2
print(listVar)
listVar.remove("A")    
print(listVar)
del listVar[1]                 #delete value at pos 1 
print(listVar)
listVar.clear()                #delete whole listVar
print(listVar)
