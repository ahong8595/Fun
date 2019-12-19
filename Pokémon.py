from random import randint
import random


# object class for types
class Type:
    def __init__(self, name): # each variable is a list of types
        self.name = name
        self.weakA = []  # types the Type cannot hit very effectively
        self.neutralA = []  # types the Type can hit neutrally
        self.superA = []  # types the Type can hit super-effectively
        self.noA = []  # types the Type has no effect on
        self.weakD = []  # types the Type cannot defend effectively
        self.neutralD = []  # types the Type can defend neutrally
        self.superD = []  # types the Type can defend effectively
        self.noD = []  # types the Type can resist

    def getName(self):
        return self.name

    def getWeakA(self):
        return self.weakA

    def getNeutralA(self):
        return self.neutralA

    def getSuperA(self):
        return self.superA

    def getNoA(self):
        return self.noA

    def getWeakD(self):
        return self.weakD

    def getNeutralD(self):
        return self.neutralD

    def getSuperD(self):
        return self.superD

    def getNoD(self):
        return self.noD


# class for each move in the game
class Move:
    def __init__(self, name, power, accuracy, type):  # Moves have a name, power, accuracy, and type
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.type = type

    def getName(self):
        return self.name
    def getPower(self):
        return self.power

    def getAccuracy(self):
        return self.accuracy

    def getType(self):
        return self.type

    def damage(self, level, attack, defense, power, user, opponent):  # calculates damage
        ran = random.uniform(0.85, 1.00)
        if randint(0, 10000) < 625:  # checks for critical hit
            crit = 1.5
        else:
            crit = 1.0
        if self.getType().getName() == user.getType().getName():  # checks for STAB
            STAB = 1.5
        else:
            STAB = 1.0
        TypeB = effectiveness(self.type, opponent)
        return (((((2 * level / 5) + 2) * power * (attack / defense)) / 50) + 2) * crit * ran * STAB * TypeB


# creates Pokémon object
class Pokémon:
    def __init__(self, name, hp, level, type, attackPower, defensePower, moveSet):
        self.name = name
        self.hp = hp
        self.level = level
        self.type = type
        self.attackPower = attackPower
        self.defensePower = defensePower
        self.moveSet = moveSet

    def getName(self):
        return self.name

    def getHP(self):
        return self.hp

    def getAttackPower(self):
        return self.attackPower

    def getDefensePower(self):
        return self.defensePower

    def getLevel(self):
        return self.level

    def getType(self):
        return self.type

    def getMoveSet(self):
        return self.moveSet

    def attack(self, move1, opponent):  # attacks an opponent
        counter = 0
        for move in self.moveSet:
            if move1.getName() == move.getName():
                acc = randint(0, 100)
                if move1.getAccuracy() > acc:
                    print("The attack hit")
                    damage = move1.damage(self.level, self.attackPower, opponent.defensePower, move1.power, self, opponent)
                    print("Total damage is " + str(int(damage)) + " damage")
                    if opponent.hp - int(damage) < 0:
                        print(opponent.name + " fainted")
                    else:
                        print(opponent.name + " has " + str(opponent.hp - int(damage)) + " HP left")
                else:
                    print("The attack missed.")
            else:
                counter = counter + 1
        if counter == 4:
            print("This move does not exist")



# creating each type through instantiation of each object
normal = Type("normal")
fight = Type("fight")
flying = Type("flying")
poison = Type("poison")
ground = Type("ground")
rock = Type("rock")
bug = Type("bug")
ghost = Type("ghost")
steel = Type("steel")
fire = Type("fire")
water = Type("water")
grass = Type("grass")
electric = Type("electric")
psychic = Type("psychic")
ice = Type("ice")
dragon = Type("dragon")
dark = Type("dark")
fairy = Type("fairy")

# try to make this more concise, takes a lot of space but required for each combination
# defining normal's type match-ups
normal.getNeutralA().extend([normal, fight, flying, poison, ground, bug, fire, water, grass, electric, psychic, ice, dragon, dark, fairy])
normal.getWeakA().extend([rock, steel])
# superA
normal.getNoA().extend([ghost])
normal.getNeutralD().extend([normal, flying, poison, ground, rock, bug, steel, fire, water, grass, electric, psychic, ice, dragon, dark, fairy])
normal.getWeakD().extend([fight])
# weakD
normal.getNoD().extend([ghost])

# defining fighting's type match-ups
fight.getNeutralA().extend([fight, ground, fire, water, grass, electric, dragon])
fight.getWeakA().extend([flying, poison, bug, psychic, fairy])
fight.getSuperA().extend([normal, rock, steel, ice, dark])
fight.getNoA().extend([ghost])
fight.getNeutralD().extend([normal, fight, poison, ground, ghost, steel, fire, water, grass, electric, ice, dragon])
fight.getWeakD().extend([flying, psychic, fairy])
fight.getSuperD().extend([rock, bug, dark])
# noD

# defining flying's type match-ups
flying.getNeutralA().extend([normal, flying, poison, ground, ghost, fire, water, psychic, ice, dragon, dark, fairy])
flying.getWeakA().extend([rock, steel, electric,])
flying.getSuperA().extend([fight, bug, grass])
# noA
flying.getNeutralD().extend([normal, flying, poison, ghost, steel, fire, water, psychic, dragon, dark, fairy])
flying.getWeakD().extend([rock, electric, ice])
flying.getSuperD().extend([fight, bug, grass])
# noD

# defining poison's type match-ups
poison.getNeutralA().extend([normal, fight, flying, bug, fire, water, electric, psychic, ice, dragon, dark])
poison.getWeakA().extend([poison, ground, rock, ghost])
poison.getSuperA().extend([grass, fairy])
poison.getNoA().extend([steel])
poison.getNeutralD().extend([[normal, flying, rock, ghost, steel, fire, water, electric, ice, dragon, dark]])
poison.getWeakD().extend([ground, psychic])
poison.getSuperD().extend([fight, poison, bug, grass, fairy])
# noD

# defining ground type match-ups
ground.getNeutralA().extend([normal, fight, ground, ghost, water, psychic, ice, dragon, dark, fairy])
ground.getWeakA().extend([bug, grass])
ground.getSuperA().extend([flying])
ground.getNoA().extend([])
ground.getNeutralD().extend([normal, fight, flying, ground, bug, ghost, steel, fire, psychic, dragon, dark, fairy])
ground.getWeakD().extend([water, grass, ice])
ground.getSuperD().extend([poison, rock])
ground.getNoD().extend([electric])

# defining rock's type match-ups
rock.getNeutralA().extend([normal, poison, rock, ghost, water, grass, electric, psychic, dragon, dark, fairy])
rock.getWeakA().extend([fight, ground, steel])
rock.getSuperA().extend([flying, bug, fire, ice])
# noA
rock.getNeutralD().extend([rock, bug, ghost, electric, psychic, ice, dragon, dark, fairy])
rock.getWeakD().extend([fight, ground, steel, water, grass])
rock.getSuperD().extend([normal, flying, poison, fire])
# noD

# defining bug's type match-ups
bug.getNeutralA().extend([normal, ground, rock, bug, water, electric, ice, dragon])
bug.getWeakA().extend([fight, flying, poison, ghost, steel, fire, fairy])
bug.getSuperA().extend([grass, psychic, dark])
# noA
bug.getNeutralD().extend([normal, poison, bug, ghost, steel, water, electric, psychic, ice, dragon, dark, fairy])
bug.getWeakD().extend([flying, rock, fire])
bug.getSuperD().extend([fight, ground, grass])
# noD

# defining ghost's type match-ups
ghost.getNeutralA().extend([fight, flying, poison, ground, rock, bug, steel, fire, water, grass, electric, ice, dragon, fairy])
ghost.getWeakA().extend([dark])
ghost.getSuperA().extend([ghost, psychic])
ghost.getNoA().extend([normal])
ghost.getNeutralD().extend([flying, ground, steel, rock, bug, steel, fire, water, grass, electric, ice, dragon, fairy])
ghost.getWeakD().extend([ghost, dark])
ghost.getSuperD().extend([poison, bug])
ghost.getNoD().extend([normal, fight])

# defining steel type match-ups
steel.getNeutralA().extend([normal, fight, flying, poison, ground, bug, ghost, grass, psychic, dragon, dark])
steel.getWeakA().extend([rock, ice, fairy])
steel.getSuperA().extend([steel, fire, water, electric])
# noA
steel.getNeutralD().extend([ghost, water, electric, dark])
steel.getWeakD().extend([fight, ground, fire])
steel.getSuperD().extend([normal, flying, rock, bug, steel, grass, psychic, ice, dragon, fairy])
steel.getNoD().extend([poison])

# defining fire type match-ups
fire.getNeutralA().extend([normal, fight, flying, poison, ground, ghost, electric, psychic, dark, fairy])
fire.getWeakA().extend([rock, water, fire, dragon])
fire.getSuperA().extend([bug, grass, steel, ice])
# noA
fire.getNeutralD().extend([normal, fight, flying, poison, ghost, electric, psychic, dragon, dark])
fire.getWeakD().extend([ground, rock, water])
fire.getSuperD().extend([bug, steel, fire, grass, ice, fairy])
# noD

# defining water type match-ups
water.getNeutralA().extend([normal, fight, flying, poison, bug, ghost, steel, electric, psychic, ice, dark, fairy])
water.getWeakA().extend([water, grass, dragon])
water.getSuperA().extend([ground, rock, fire])
# noA
water.getNeutralD().extend([normal, fight, flying, poison, ground, rock, bug, ghost, psychic, dragon, dark, fairy])
water.getWeakD().extend([grass, electric])
water.getSuperD().extend([steel, fire, water, ice])
# noD

# defining grass type match-ups
grass.getNeutralA().extend([normal, fight, ghost, electric, psychic, ice, dark, fairy])
grass.getWeakA().extend([flying, poison, bug, steel, fire, grass, dragon])
grass.getSuperA().extend([ground, rock, water])
# noA
grass.getNeutralD().extend([normal, fight, rock, ghost, steel, psychic, dragon, dark, fairy])
grass.getWeakD().extend([flying, poison, bug, fire, ice])
grass.getSuperD().extend([ground, water, grass, electric])
# noD

# defining electric type match-ups
electric.getNeutralA().extend([normal, fight, poison, rock, bug, ghost, steel, fire, psychic, ice, dark, fairy])
electric.getWeakA().extend([grass, electric, dragon])
electric.getSuperA().extend([flying, water])
electric.getNoA().extend([ground])
electric.getNeutralD().extend([normal, fight, poison, rock, bug, ghost, fire, water, grass, psychic, ice, dragon, dark, fairy])
electric.getWeakD().extend([ground])
electric.getSuperD().extend([flying, steel, electric])
# noD

# defining psychic type match-ups
psychic.getNeutralA().extend([normal, flying, rock, ground, bug, ghost, fire, water, grass, electric, ice, dragon, fairy])
psychic.getWeakA().extend([steel, psychic])
psychic.getSuperA().extend([fight, poison])
psychic.getNoA().extend([dark])
psychic.getNeutralD().extend([normal, flying, poison, ground, rock, steel, fire, water, grass, electric, ice, dragon, fairy])
psychic.getWeakD().extend([bug, ghost, dark])
psychic.getSuperD().extend([fight, psychic])
# noD

# defining ice type match-ups
ice.getNeutralA().extend([normal, fight, poison, rock, bug, ghost, electric, psychic, dark, fairy])
ice.getWeakA().extend([steel, fire, water, ice])
ice.getSuperA().extend([flying, ground, grass, dragon])
# noA
ice.getNeutralD().extend([normal, flying, poison, ground, bug, ghost, water, grass, electric, psychic, dragon, dark, fairy])
ice.getWeakD().extend([fight, rock, steel, fire])
ice.getSuperD().extend([ice])
# noD

# defining dragon type match-ups
dragon.getNeutralA().extend([normal, fight, flying, poison, ground, rock, bug, ghost, fire, water, grass, electric, psychic, ice, dark])
dragon.getWeakA().extend([steel])
dragon.getSuperA().extend([dragon])
dragon.getNoA().extend([fairy])
dragon.getNeutralD().extend([normal, fight, flying, poison, ground, rock, bug, ghost, steel, psychic, dark])
dragon.getWeakD().extend([ice, dragon, fairy])
dragon.getSuperD().extend([fire, water, grass, electric])
# noD

# defining dark type match-ups
dark.getNeutralA().extend([normal, flying, poison, ground, rock, bug, steel, fire, water, grass, electric, ice, dragon])
dark.getWeakA().extend([fight, dark, fairy])
dark.getSuperA().extend([ghost, psychic])
# noA
dark.getNeutralD().extend([normal, flying, poison, ground, rock, steel, fire, water, grass, electric, ice, dragon])
dark.getWeakD().extend([fight, bug, fairy])
dark.getSuperD().extend([ghost, dark])
dark.getNoD().extend([psychic])

# defining fairy type match-ups
fairy.getNeutralA().extend([normal, flying, ground, rock, bug, ghost, water, grass, electric, psychic, ice, fairy])
fairy.getWeakA().extend([poison, steel, fire])
fairy.getSuperA().extend([fight, dragon, dark])
fairy.getNoA().extend([])
fairy.getNeutralD().extend([normal, flying, ground, rock, ghost, fire, water, grass, electric, psychic, ice, fairy])
fairy.getWeakD().extend([poison, steel])
fairy.getSuperD().extend([fight, bug, dark])
fairy.getNoD().extend([dragon])


# tests to see how effective a move is
def effectiveness(typeMove, opponent):
    for t in opponent.getType().getWeakD():
        if t.getName() == typeMove.getName():  # super-effective
            print("Super-effective")
            return 2.0
    for t in opponent.getType().getSuperD():
        if t.getName() == typeMove.getName():  # neutral
            print("Not very effective")
            return 0.5
    for t in opponent.getType().getNeutralD():  # not very effective
        if t.getName() == typeMove.getName():
            print("Normal damage")
            return 1.0
    for t in opponent.getType().getNoD():
        if t.getName() == typeMove.getName():  # no effect
            print("It had no effect")
            return 0
    return 1000000000


#list of pokémon and list of moves
pokémonList = []
moveList = []


# instantiation of some moves
flamethrower = Move("flamethrower", 90, 100, fire)  # (name, power, accuracy, type)
razorLeaf = Move("razor leaf", 65, 95, grass)
surf = Move("surf", 90, 100, water)
brickBreak = Move("brickBreak", 70, 100, fight)
thunder = Move("thunder", 120, 80, electric)
waterPulse = Move("water pulse", 60, 100, water)
aquaTail = Move("aqua tail", 90, 90, water)
ironTail = Move("iron tail", 90, 90, steel)
hyperBeam = Move("hyper beam", 120, 100, normal)


# instantiation of some Pokémon
charmander = Pokémon("Charmander", 100, 50, fire, 70, 30, [flamethrower, razorLeaf, surf, brickBreak])  # (name, HP, level, type, attack, defense, moveSet)
squirtle = Pokémon("Squirtle", 100, 50, water, 30, 70, [flamethrower, razorLeaf, surf, brickBreak])
machop = Pokémon("Machop", 100, 50, fight, 100, 20, [flamethrower, razorLeaf, surf, brickBreak])
bidoof = Pokémon("Bidoof", 100, 50, normal, 30, 40, [flamethrower, razorLeaf, surf, brickBreak])
pikachu = Pokémon("Pikachu", 80, 50, electric, 80, 20, [flamethrower, razorLeaf, surf, brickBreak])
blastoise = Pokémon("Blastoise", 200, 50, water, 120, 80, [waterPulse, aquaTail, ironTail, hyperBeam])

pokémonList.extend([charmander, squirtle, machop, bidoof, pikachu, blastoise])
# some actions
x = True
while x:
    slot = 1
    check = 0
    input1 = input("Choose a Pokémon")
    for poke in pokémonList:
        if input1 == poke.getName():
            check = 1
            print("")
            index = pokémonList.index(poke)
            for moves in pokémonList[index].getMoveSet():
                print(str(slot) + ". " + moves.getName())
                slot = slot + 1
            moveChoice = input("Pick a move")
            print("")
            print(blastoise.getMoveSet()[int(moveChoice) - 1].getName())
            blastoise.attack(blastoise.getMoveSet()[int(moveChoice) - 1], squirtle)

    if check == 0:
        print("Invalid name")
    else:
        x = False








