class GameCharacter:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def increase_level(self):
        self.level += 1
        self.attack *= 1.1
        self.health *= 1.1


character1 = GameCharacter('John', 4, 100, 40, 10)
character2 = GameCharacter('Ben', 2, 50, 20, 20)

for round_num in range(1, 4):
    print(f"Раунд {round_num}")
    damage1 = character1.attack - character2.defense
    if damage1 < 0:
        damage1 = 0
    character2.damage(damage1)
    print(f"{character1.name} атакует {character2.name} и наносит {damage1} урона")
    damage2 = character2.attack - character1.defense
    if damage2 < 0:
        damage2 = 0
    character1.damage(damage2)
    print(f"{character2.name} атакует {character1.name} и наносит {damage2} урона")

if character1.health > character2.health:
    print(f"Победитель: {character1.name}")
    print(f"Проигравший: {character2.name}")
elif character2.health > character1.health:
    print(f"Победитель: {character2.name}")
    print(f"Проигравший: {character1.name}")
else:
    print("Ничья")