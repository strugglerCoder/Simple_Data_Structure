setVar={"A","B","C","D"}
print(setVar)
setVar.add("Z")
print(setVar)
print(setVar.copy())
setVar.discard("B")
print(setVar)

setVar2=(1,2,3,4,5)
print(setVar2)

setVar.union(setVar2)
print(setVar)
