tupleVar=("A","B","C","D","E","F","G","H","I")
print(tupleVar[1])
print(tupleVar.index("A"))

if "A" in tupleVar:
    print("Yes")

tupleVar[2]="Z"
print(tupleVar)        #error bcz we cannot change values in tuple
