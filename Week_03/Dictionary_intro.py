ascars = {"Ford": "Mustang", "Mazda" : "Miata", "Scion" : "FR-S",
          "Subaru" : "BRZ", "Dodge" : "Challenger", "Nissan" : "370Z",
          "Chevy" : "Camaro", "Hyundai" : "Genesis Coupe",
          "MINI Cooper" : "Roadster"}

print(ascars) #(a)
print(ascars["Nissan"]) #(b)
print(ascars["Chevy"]) #(c)
ascars["MINI Cooper"] = "Coupe" #(d)
print(ascars)
for value in ascars.values():
    print(value, end = ' ')

print() #(e)

for key in ascars.keys():
    print(key, end = ' ')

print() #(f)
