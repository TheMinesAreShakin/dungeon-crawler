

class Entity:


    def __init__(self, hp=0, defense=0, attack=0, gold=0, exp=0):
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.gold = gold
        self.exp = exp

    
    def __str__(self):
        return f"HP: {self.hp}\n"\
            f"Defense: {self.defense}\n"\
            f"Attack: {self.attack}\n"\
            f"Gold: {self.gold}\n"\
            f"EXP: {self.exp}\n"

    
    def set_hp(self, newHp):
        self.hp = newHp

    def get_hp(self):
        return self.hp

    def set_defense(self, newDefense):
        self.defense = newDefense

    def get_defense(self):
        return self.defense

    def set_attack(self, newAttack):
        self.attack = newAttack

    def get_attack(self):
        return self.attack

    def set_gold(self, newGold):
        self.gold = newGold

    def get_gold(self):
        return self.gold

    def set_exp(self, newExp):
        self.exp = newExp

    def get_exp(self):
        return self.exp