from entity import Entity

e = Entity()

print(str(e))

e.set_attack(1)
e.set_defense(2)
e.set_exp(3)
e.set_gold(4)
e.set_hp(5)

print(e.get_attack())
print(e.get_defense())
print(e.get_exp())
print(e.get_gold())
print(e.get_hp())

print(str(e))

p = Entity(10, 9, 8, 7, 6)

print(str(p))