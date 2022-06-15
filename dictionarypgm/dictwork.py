# student={"rolno":1000,"name":"ram","class":"12","div":"2a"}
#
# print(student["name"])
# print(student["rolno"])


car={"name":"swift",
     "colour":"grey",
     "brand":"maruthi",
     "make":2005,
     "fuel":"petrol",
     "price":"9lk",
     "no_of_airbags":1
     }
print(car["no_of_airbags"])
car["no_of_airbags"]=2
print(car)

print(car["brand"])
print(car["fuel"])
print(car["price"])
print("transmission_type" in car)
car["transmission_type"]="manuel"
print(car)
print("gear_type" in car)
car["gear_type"]="abs"
print(car)
