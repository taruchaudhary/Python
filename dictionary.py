TaruMalik = {
    "Branch": "CS&IT", "Course":"Btech","Session":"2021-2025"
}
print(TaruMalik)
Tarumalik ={
    "Branch": "CSIT", "Course":"Btech","Session":"2021-2025","Branch":"CSE"
}
print(Tarumalik)
Tarumalik = {
    "Branch": "CSE","Course":"CSE","Year":"CSE","Session":"2021-2025"
}
print(Tarumalik)
print(len(Tarumalik))
print(type(Tarumalik))
x=Tarumalik.get("Branch")
y=Tarumalik["Session"]
print(x)
print(y)
z=Tarumalik.keys()
print(z)
a=Tarumalik.values()
print(a)
b=Tarumalik.items()
print(b)
thisdict={
    "name":"taru","branch":"csit","session":"2021-2025"
}
if "branch " in thisdict:
    print("yes")
    
else:
    print("no")
thisdict={
    "name":"taru","branch":"csit"
}
thisdict["branch"]="cse"
print(thisdict)
thisdict.update({"name":"malik"})
print(thisdict)
thisdict["color"]="red"
print(thisdict)
thisdict.pop("name")
print(thisdict)