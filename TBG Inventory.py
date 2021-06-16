#Weapon and Armor inventory
Weapon = ['knife', 'shotgun', 'pistol','sniper rifle','Rocket Launcher']
Armor = ['C.golden armor', 'D.golden armor', 'B.golden armor', 'D.golden armor', 'A.golden armor',  'A.golden armor',  'D.golden armor']
print(f"\n You have {Weapon} in the Inventory.") #Weapon Check
print(f" You have {Armor} in the Inventory.") #Armor Check

#Add
Weapon.append('sword') #Add Weapon
Armor.append('G.golden armor') #Add Armor
print(f"\n You pick up sword, now you have {Weapon} in the Inventory.")
print(f" You pick up G.golden armor, now you have {Armor} in the Inventory.")
#Put something into Inventory
Weapon.insert(0, 'grenade') #Put grenade at the first position Inventory
print(f"\n You pick up a grenade, now you have {Weapon} in the Inventory.")
Armor.insert(2, 'trash') #Put grenade at the third position Inventory
print(f" You pick up a trash, now you have {Armor} in the Inventory.")

#Delete
del Weapon[1] #delete 'knife'
del Armor[2] #delete 'trash'
print("\n You dropped a weapon.")
print("\n You throw away the trash.")
print(f"\n {Weapon}") #weapon check
print(f" {Armor}") #armor check
popped_Weapon = Weapon.pop(2) #delete 'pistol'
used_armor = 'B.golden armor'#remove 'B.golden armor'
Armor.remove(used_armor)

print("\n You lost a Weapon.")
print(f" You lost {popped_Weapon}.")

print("\n You used a armor.")
print(f" {used_armor} had broken!")

#Sort and reverse
Weapon.sort() #sort weapon
print(f"\n You have organized your Inventory.(sort by Name↑)\n{Weapon}")
Weapon.sort(reverse=True) #reverse weapon
print(f"\n You have organized your Inventory.(sort by Name↓)\n{Weapon}")

print(f"\n You have organized your Inventory.(sort by Level↑)\n {sorted(Armor)}")
Armor.sort() #sort armor
Armor.reverse() #reverse armor
print(f"\n You have organized your Inventory.(sort by Level↓)\n {Armor}")

#len
print(f"\n You have {len(Weapon)} weapons now.") #len weapon
print(f"\n You have {len(Armor)} armors now.") #len armor