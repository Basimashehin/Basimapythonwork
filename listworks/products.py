mobiles=[
    [1000,"samsungA52","4g","AMOLED",27000,"samsung",12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung",20],
    [1002, "redminote10", "4g", "led", 17000, "redmi",50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi",70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung",1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung",34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung",7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung",89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung",0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple",0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus",67]

]

#

# total mobiles

print(f"total number of mobile = {len(mobiles)}")


# q1 total number of out_of_stock mobiles

out_of_stock=[fw for fw in mobiles if fw[-1]==0]
print(out_of_stock)


# q2 total stock
stock=[fw[6] for fw in mobiles]
print(f"total stock is {sum(stock)}")

# q3 print mobiles available in range 20k to 30k
in_range=[fw for fw in mobiles if fw[4] in range(20000,30001)]
print(in_range)

# q4 print all 5g phone
fiveg=[fw for fw in mobiles if fw[2]=="5g"]
print(fiveg)

# q5 print samsung mobiles
samsung=[fw for fw in mobiles if fw[5]=="samsung"]
print(samsung)

# q6 print costly mobile
cost=[fw[4] for fw in mobiles]
costly=max(cost)
costly_mob=[mob for mob in mobiles if mob[4]==costly]
print(costly_mob)

# q7 prin low cost mobiles

cost=[fw[4] for fw in mobiles]
lowcost=min(cost)
lowcost_mob=[mob for mob in mobiles if mob[4]==lowcost]
print(lowcost_mob)

# q8 print all mobiles having stock >10
mob=[fw for fw in mobiles if fw[-1]>10]
print(mob)

# q9 count of mobiles having dispaly amoled
mobamoled=[mob for mob in mobiles if mob[3]=="AMOLED"]
print(mobamoled)
print("next")
# q10 sort mobiles based on price order by desc
#
# mobiles.sort(reverse=True,key=lambda mob:mob[4])
# print(mobiles)
# # q11 sort mobiles based on avl stock oredr by desc
# mobiles.sort(key= lambda  mob:mob[-1])
# print(mobiles)

#low cost mobile
cheapmob=min(mobiles,key=lambda  mob: mob[4])
print(cheapmob)
# q12 is there any mobile available at rs 10000 ?
mob_ten=[True if mob[4]==10000  else False for mob in mobiles ]
print("yes" if True in mob_ten else "not available")
# q12 list all mobiles having same price