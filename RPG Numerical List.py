#Weapon and Armor and Food inventory
Weapon = ['knife', 'shotgun', 'pistol','sniper rifle','Rocket Launcher'] #Weapon inventory
Armor = ['C.golden armor', 'D.golden armor', 'B.golden armor', 'D.golden armor', 'A.golden armor',  'A.golden armor',  'D.golden armor'] #Armor inventory
Food = ['Apple Juice', 'Chicken Soup', 'Cheese Pizza', 'Beef Buger', 'French Fries'] #Food inventory

print("Available Weapon:") #Weapon Numerical List
i = 0 #set the Numerical to 0
for weapon in Weapon[:]:
    i= i+1 #each item will let the Numerical List + 1 
    print(f"{i}. {weapon.title()}") #print Numerical + Armor
    
print("Available Armor:") #Armor Numerical List
i = 0 #set the Numerical to 0
for armor in Armor[:]:
    i= i+1 #each item will let the Numerical List + 1 
    print(f"{i}. {armor.title()}") #print Numerical + Armor
    
print("Available Food:") #Food Numerical List
i = 0 #set the Numerical to 0
for food in Food[:]:
    i= i+1 #each item will let the Numerical List + 1 
    print(f"{i}. {food.title()}") #print Numerical + Food
    
