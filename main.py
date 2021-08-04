import random
import sys
import os
import time
playerMoves = 0
global apAmmount
global spAmmount
global hpAmmount


def clear():
    time.sleep(2)
    os.system('clear')


#super.__init__(self,name,attack,defense,health)


class Monster:

    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    def monsterStats(self):
        print("The Monsters Stats are:")
        print("Attack " + str(self.attack))
        print("Health " + str(self.health))

    def monsterAttack(self):
        return str(self.attack)

    def monsterHealth(self):
        return str(self.health)

    def monsterAlive(self):
        return self.health > 0


class Item:

    def __init__(self, name, attack, defense, health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health

    def itemStats(self):
        print("name: " + self.name)
        print("attack: " + str(self.attack))
        print("defense: " + str(self.defense))
        print("health: " + str(self.health))


class Weapon(Item):

    def __init__(self, name, attack):
        super.__init__(self, name, attack)

    def itemStats(self):
        print("Name: " + str(self.name))
        print("attack: " + str(self.attack))


class Shield(Item):

    def __init__(self, name, defense):
        super.__init__(self, name, defense)

    def itemStats(self):
        print("name: " + str(self.name))
        print("defense: " + str(self.defense))


class Armor(Item):

    def __init__(self, name, armor):
        super.__init__(self, name, armor)

    def itemStats(self):
        print("Name: " + str(self.name))
        print("Defense: + " + str(self.armor))

    def armorDefense(self):
        self.armor


class attackPotion(Item):

    def __init__(self, bonusAttack):
        super.__init__(self, bonusAttack)

    def itemStats(self):
        print("Potion type: Attack")
        print("attack: " + str(self.bonusAttack))


class shieldPotion(Item):

    def __init__(self, bonusDefense):
        super.__init__(self, bonusDefense)

    def itemStats(self):
        print("Potion type: Defesne")
        print("attack: " + str(self.bonusDefense))


class healthPotion(Item):

    def __init__(self, bonusHealth):
        super.__init__(self, bonusHealth)

    def itemStats(self):
        print("Potion type: Attack")
        print("attack: " + str(self.bonusHealth))


class Player:

    def __init__(self, attack, shield, health):
        self.attack = attack
        self.shield = shield
        self.health = health

    '''
  def playerStatsTut(self):
   print( "current stats are:")
   print("attack " + str(self.attack))
   print("shield " + str(self.shield))
   print("health " + str(self.health))
  '''

    def playerStats(self):
        global apAmmount
        global spAmmount
        global hpAmmount
        print("Your Current Stats are:")
        print("Attack " + str(self.attack))
        print("Shield " + str(self.shield))
        print("Health " + str(self.health))
        print("Potions: Attack(" + str(apAmmount) + ") Defense(" +
              str(spAmmount) + ")  Health(" + str(hpAmmount) + ")")

    def playerAlive(self):
        return self.health > 0


class Move:

    def attack(pAttack, mHealth, mAttack, pHealth):
        global playerMoves
        print("You deal " + str(pAttack) + " damage")
        mHealth -= pAttack
        mon1.health = mHealth
        print("Monsters Health is now: " + str(mHealth))
        if (mHealth > 0):
            print("")
            print("The Monster attacks!")
            pHealth -= mAttack
            player.health = pHealth
            print("Your health is now: " + str(player.health))
            print("")
        playerMoves = playerMoves + 1

    def blocknShield(mAttack, pHealth, mHealth):
        global playerMoves
        print("You don't have a shield!")
        print("You take: " + str(mAttack) + " damage")
        pHealth -= mAttack
        player.health = pHealth
        print("Your Health is now: " + str(player.health))
        if (player.health == 0 or player.health < 0):
            print("GAME OVER")
            sys.exit(0)
        print("")
        playerMoves = playerMoves + 1

    def blockwShield(mAttack, sDefense, pHealth, mHealth):
        global playerMoves
        print("The monster attacks!")
        mon1.attack = mAttack
        mon1.health = mHealth
        player.shield = sDefense
        player.health = pHealth
        difference = mAttack - sDefense
        if (mAttack > sDefense):
            print("You take: " + str(difference) + " damage")
            pHealth -= difference
            if (pHealth == 0 or pHealth < 0):
                print("GAME OVER")
                sys.exit(0)
            print("Your health is now: " + str(pHealth))
            diffmDamage = 0.5 * player.shield
            mHealth -= diffmDamage
            print("The Monster takes: " + str(diffmDamage) + " damage")
            print("The Monsters health is now: " + str(mHealth))
            print("")
            mon1.health = mHealth
            player.health = pHealth
        if (mAttack < sDefense):
            print("You block all damage!")
            diffdamage = sDefense - mAttack
            print("The Monster takes: " + str(diffdamage) + " damage")
            print("The Monsters health is now: " + str(mHealth))
            print("")
        if (mAttack == sDefense):
            print("You block all damage!")
            diffmDamage = 0.5 * player.shield
            mHealth -= diffmDamage
            print("The Monster takes: " + str(diffmDamage) + " damage")
            print("The Monsters health is now: " + str(mHealth))
            print("")
            mon1.health = mHealth
            playerMoves = playerMoves + 1

    def useAttackPotion(pAttack, pHealth, mAttack):
        global playerMoves
        global apAmmount
        global attackMoves
        global origAttack
        if (apAmmount > 0):
            playerMoves = playerMoves + 1
            attackMoves = playerMoves
            origAttack = player.attack
            player.attack = player.attack * 1.5
            apAmmount -= 1
            print("Your Attack is now: " + str(player.attack))
        else:
            print("You have no Attack potions left!")
            pHealth -= mAttack
            print("You take: " + str(mon1.attack) + " damage")
            print("your health is now: " + str(player.health))
            print("")

    def useShieldPotion(pShield, pHealth, mAttack):
        global playerMoves
        global spAmmount
        global origShield
        global shieldMoves
        if (spAmmount > 0):
            playerMoves = playerMoves + 1
            shieldMoves = playerMoves
            origShield = player.shield
            player.shield = player.shield * 1.5
            spAmmount -= 1
            print("Your Shield is now: " + str(player.shield))
        else:
            print("You have no Attack potions left!")
            pHealth -= mAttack
            print("You take: " + str(mon1.attack) + " damage")
            print("your health is now: " + str(player.health))
            print("")

    def useHealthPotion(pHealth, mAttack):
        global playerMoves
        global hpAmmount
        if (hpAmmount > 0):
            playerMoves = playerMoves + 1
            player.health = player.health * 1.5
            print("Your Health is now: " + str(player.health))
            print("")
            hpAmmount -= 1
        else:
            print("You have no Health potions left!")
            pHealth -= mAttack
            print("You take: " + str(mon1.attack) + " damage")
            print("your health is now: " + str(player.health))
            print("")

    def keepSword(pAttack, sAttack):
        print("You chose to keep the Sword!")
        pAttack = 0
        pAttack = sAttack + 1
        print("Your new attack is: " + str(pAttack))
        player.attack = pAttack

    def keepShield(pDefense, sDefense):
        print("You chose to keep the shield!")
        pDefense = 0
        pDefense += sDefense
        print("Your new denfense is: " + str(sDefense))
        player.shield = pDefense

    def keepArmor(pHealth, aArmor):
        print("You chose to keep the Armor!")
        aHealth = aArmor + pHealth
        pHealth = aHealth
        print("Your new health is: " + str(pHealth))
        player.health = pHealth


class game:

    def maingame(pAttack, pHealth, pShield, mAttack, mHeath):
        global attackMoves
        global shieldMoves
        while (mon1.health > 0):
            fof = input("Block attack or potion? ")
            if (fof == 'attack'):
                Move.attack(player.attack, mon1.health, mon1.attack,
                            player.health)
                if (mon1.health == 0 or mon1.health < 0):
                    break
                if (player.health == 0 or player.health < 0):
                    print("GAME OVER")
                    sys.exit(0)
            elif (fof == 'block'):
                if (player.shield == 0):
                    Move.blocknShield(mon1.attack, player.health, mon1.health)
                if (player.shield > 0):
                    Move.blockwShield(mon1.attack, player.shield, player.health,
                                      mon1.health)
                if (player.health == 0 or player.health < 0):
                    print("GAME OVER")
                    sys.exit(0)
            elif (fof == 'potion'):
                print(
                    "To use potions, enter the full name (attack potion, shield potion, health potion)"
                )
            elif (fof == 'attack potion'):
                Move.useAttackPotion(player.attack, player.health, mon1.attack)
                if (player.health == 0 or player.health < 0):
                    print("GAME OVER")
                    sys.exit(0)
            elif (fof == 'shield potion'):
                Move.useShieldPotion(player.shield, player.health, mon1.attack)
                if (player.health == 0 or player.health < 0):
                    print("GAME OVER")
                    sys.exit(0)
            elif (fof == 'health potion'):
                Move.useHealthPotion(player.health, mon1.attack)
                if (player.health == 0 or player.health < 0):
                    print("GAME OVER")
                    sys.exit(0)
            else:
                player.health -= mon1.attack
                print("You failed to make a move!")
                print("You take " + str(mon1.attack) + " damage!")
                print("Your health is now: " + str(player.health))
                if (player.health == 0 or player.health < 0):
                    break
            if (playerMoves == (attackMoves + 3)):
                player.attack = origAttack
                print("Your attack potion has worn off!")
                print("Your attack is now: " + str(player.attack))
                print("")
            if (playerMoves == (shieldMoves + 3)):
                player.shield = origShield
                print("Your shield potion has worn off!")
                print("Your attack is now: " + str(player.shield))
                print("")

    def endofRoom():
        if (mon1.health == 0 or mon1.health < 0):
            print("The Monster is killed!")
            player.health += mon1.attack
            print("You gain: +" + str(mon1.attack) + " health")
            clear()
        if (player.health == 0 or player.health < 0):
            print("GAME OVER")
            sys.exit(0)
        clear()


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


class Art:

    def swordArt():
        print("                            /()")
        print("                           / /")
        print("                          / /")
        print(
            "             /============| |------------------------------------------,"
        )
        print(
            "          {=| / / / / / /|()}     }     }     }                        >"
        )
        print(
            "             \============| |------------------------------------------'"
        )
        print("                         \ \ ")
        print("                           \ \ ")
        print("                            \()")
        print("")
        print("")

    def shieldArt():
        print("          |`-._/\_.-`|")
        print("          |    ||    |")
        print("          |___o()o___|")
        print("          |__((<>))__|")
        print("          \   o\/o   /")
        print("           \   ||   /")
        print("            \  ||  /")
        print("             '.||.'")
        print("               ``")
        print("")
        print("")


'''----------------------------------------------------------------------------------'''
missItem = 0
import pyfiglet
from pyfiglet import Figlet
custom_fig = Figlet(font='larry3d')
print(custom_fig.renderText('  10 Rooms'))

time.sleep(2)
print("                          Created by Sam C and Hammad A")

time.sleep(2)
for x in range(6):
    print("")

userName = input("Before we begin what is your name? ")
clear()
print("Welcome to 10 Rooms " + userName + ".")
fof = input(
    "You are lost in a dark room and hear nosies around you. Do you run, or fight? "
)

if (fof == 'run'):
    print("There is nowhere to go!")
    print("You see a monster and you must fight!")
elif (fof == 'fight'):
    print("You see a monster and prepare yourself for the fight")
else:
    while (fof != 'run' or fof != 'fight'):
        fof = input("Do you run or fight? ")
        if (fof == 'run'):
            print("There is nowhere to go!")
            print("You see a monster and you must fight!")
            break
        if (fof == 'fight'):
            print("You see a monster and prepare yourself for the fight")
            break
'''----------------------------------------------------------------------------------'''

clear()

print("Welcome to the Tutorial:")
print("")
print("If you attack, the monster gets a chance to attack you back")
print(
    "If you block, you can stop incoming damage, and even deal some back to the monster"
)
print("At the end of each room you get one attack worth of health back")
print("")
print(
    "There are three types of potions in the game: Attack, Shield, and Health")
print(
    "Each one raises that particular stat by 50% for three turns (excpet for health which  stays)"
)
print("")

advance = input("Are you ready? ")
if (advance == 'yes'):
    print("")
    print_slow("PREPARE FOR AN EPIC BATTLE!")
elif (advance == 'no'):
    print("But its time to fight!")
else:
    print("Sorry, it's time to fight!")

clear()

#Creating player
player = Player(1, 0, 4)
mon1 = Monster(15, 1)

#Giving Player potions
apAmmount = 1
hpAmmount = 1
spAmmount = 0

import pyfiglet
from pyfiglet import Figlet
custom_fig = Figlet(font='larry3d')
print(custom_fig.renderText('   10 Rooms'))

print("Welcome to the Tutorial Room:")
print("----------------------------------")
Player.playerStats(player)
print("----------------------------------")
Monster.monsterStats(mon1)
print("----------------------------------")

#main game
game.maingame(player.attack, player.health, player.shield, mon1.attack,
              mon1.health)
game.endofRoom()

#first item and pick up/ leave
woodSword = Item('toothpick', 1, 0, 0)
Art.swordArt()
print("While walking you find a wood sword!")
print("----------------------------------")
print("Its stats are:")
woodSword.itemStats()
print("----------------------------------")

print("Your current attack is: " + str(player.attack))
keep = input("Would you like to keep it? ")
if (keep == 'yes'):
    Move.keepSword(player.attack, woodSword.attack)
elif (keep == 'no'):
    print("ok, but you will probably want it")
else:
    print("You will not keep the item")

clear()
'''The Main Game Loop'''
'''----------------------------------------------------------------------------------'''

import pyfiglet
from pyfiglet import Figlet
custom_fig = Figlet(font='larry3d')
print(custom_fig.renderText('  10 Rooms'))

print("You have advanced to Room 1!")
mon1 = Monster(random.randrange(2, 3), random.randrange(2, 4))
player.health = 5

print("----------------------------------")
Player.playerStats(player)
print("----------------------------------")
Monster.monsterStats(mon1)
print("----------------------------------")

game.maingame(player.attack, player.health, player.shield, mon1.attack,
              mon1.health)
game.endofRoom()

#random chance for the weapon
rng = random.randrange(1, 3)
if (rng == 1):
    stonesword = Item('Quickfang', 3, 0, 0)
    Art.swordArt()
    print("While walking you find a new sword!")
    print("----------------------------------")
    print("Its stats are:")
    stonesword.itemStats()
    print("----------------------------------")

    print("Your current attack is: " + str(player.attack))
    keep = input("Would you like to keep it? ")
    if (keep == 'yes'):
        Move.keepSword(player.attack, stonesword.attack)
    elif (keep == 'no'):
        print("You will not keep the item")
        print("")
    else:
        print("You will not keep the item")
else:
    missItem = missItem + 1

clear()

armortest = Item('OG Iron Man Armor', 0, 0, 2)
print("While walking you find armor!")
print("----------------------------------")
print("Its stats are:")
armortest.itemStats()
print("----------------------------------")

keep = input("Would you like to keep it? ")
if (keep == 'yes'):
    Move.keepArmor(player.health, armortest.health)
elif (keep == 'no'):
    print("Ok, but you will probably need it!")
else:
    print("You will not keep the item")

clear()

wShield = Item('Wooden Shield', 0, 3, 0)
Art.shieldArt()
print("While walking you find a shield!")
print("----------------------------------")
print("Its stats are:")
wShield.itemStats()
print("----------------------------------")

print("Your current defense is: " + str(player.shield))
keep = input("Would you like to keep it? ")
if (keep == 'yes'):
    Move.keepShield(player.shield, wShield.defense)
elif (keep == 'no'):
    print("Ok, but you will probably need it!")
else:
    print("You will not keep the item")
'''----------------------------------------------------------------------------------'''

clear()

import pyfiglet
from pyfiglet import Figlet
Custom_fig = Figlet(font='larry3d')
print(custom_fig.renderText('  10 Rooms'))

print("You have advanced to Room 2!")
mon1 = Monster(random.randrange(5, 8), random.randrange(3, 4))

print("----------------------------------")
Player.playerStats(player)
print("----------------------------------")
Monster.monsterStats(mon1)
print("----------------------------------")

game.maingame(player.attack, player.health, player.shield, mon1.attack,
              mon1.health)
game.endofRoom()

rng = random.randrange(1, 4)
if (rng == 1):
    apAmmount += 1
    print("While walking you find an Attack potion")
    time.sleep(1)
    print("you now have: " + str(apAmmount) + " attack potions")
    time.sleep(1)

rng = random.randrange(1, 3)
if (rng == 1):
    scsword = Item('The Scarlet Sword', random.randrange(3, 5), 0, 0)
    Art.swordArt()
    print("While walking you find a new sword!")
    print("----------------------------------")
    print("Its stats are:")
    scsword.itemStats()
    print("----------------------------------")

    print("Your current attack is: " + str(player.attack))
    keep = input("Would you like to keep it? ")
    if (keep == 'yes'):
        Move.keepSword(player.attack, scsword.attack)
    else:
        print("You will not keep the item")
else:
    missItem = missItem + 1
'''----------------------------------------------------------------------------------'''
clear()

import pyfiglet
from pyfiglet import Figlet
Custom_fig = Figlet(font='larry3d')
print(custom_fig.renderText('  10 Rooms'))

print("You have advanced to Room 3!")
mon1 = Monster(random.randrange(5, 9), random.randrange(3, 5))

print("----------------------------------")
Player.playerStats(player)
print("----------------------------------")
Monster.monsterStats(mon1)
print("----------------------------------")

game.maingame(player.attack, player.health, player.shield, mon1.attack,
              mon1.health)
game.endofRoom()

rng = random.randrange(1, 4)
if (rng == 1):
    spAmmount += 1
    print("While walking you find an Shield potion")
    time.sleep(1)
    print("you now have: " + str(spAmmount) + " shield potions")
    time.sleep(1)

rng = random.randrange(1, 3)
if (rng == 1):
    hShield = Item('Wakandan Shield', 0, random.randrange(4, 5), 0)
    Art.shieldArt()
    print("While walking you find a new Shield!")
    print("----------------------------------")
    print("Its stats are:")
    hShield.itemStats()
    print("----------------------------------")

    print("Your current defense is: " + str(player.shield))
    keep = input("Would you like to keep it? ")
    if (keep == 'yes'):
        Move.keepShield(player.shield, hShield.defense)
    else:
        print("You will not keep the item")
else:
    missItem = missItem + 1

clear()

rng = random.randrange(1, 2)
if (rng == 1):
    scsword = Item('The Scarlet Sword', random.randrange(3, 5), 0, 0)
    Art.swordArt()
    print("While walking you find a new sword!")
    print("----------------------------------")
    print("Its stats are:")
    scsword.itemStats()
    print("----------------------------------")

    print("Your current attack is: " + str(player.attack))
    keep = input("Would you like to keep it? ")
    if (keep == 'yes'):
        Move.keepSword(player.attack, scsword.attack)
    else:
        print("You will not keep the item")
else:
    missItem = missItem + 1
'''----------------------------------------------------------------------------------'''
clear()

import pyfiglet
from pyfiglet import Figlet
Custom_fig = Figlet(font='larry3d')
print(custom_fig.renderText('  10 Rooms'))

print("You have advanced to Room 4!")
mon1 = Monster(random.randrange(6, 10), random.randrange(4, 6))

print("----------------------------------")
Player.playerStats(player)
print("----------------------------------")
Monster.monsterStats(mon1)
print("----------------------------------")

game.maingame(player.attack, player.health, player.shield, mon1.attack,
              mon1.health)
game.endofRoom()

rng = random.randrange(1, 4)
if (rng == 1):
    hpAmmount += 1
    print("While walking you find a Health potion")
    time.sleep(1)
    print("you now have: " + str(hpAmmount) + " health potions")
    time.sleep(1)

rng = random.randrange(1, 2)
if (rng == 1):
    hShield = Item('Guardian Shield', 0, random.randrange(4, 5), 0)
    Art.shieldArt()
    print("While walking you find a new Shield!")
    print("----------------------------------")
    print("Its stats are:")
    hShield.itemStats()
    print("----------------------------------")

    print("Your current defense is: " + str(player.shield))
    keep = input("Would you like to keep it? ")
    if (keep == 'yes'):
        Move.keepShield(player.shield, hShield.defense)
    else:
        print("You will not keep the item")
else:
    missItem = missItem + 1

clear()

rng = random.randrange(1, 2)
if (rng == 1):
    scsword = Item('The Scarlet Sword', random.randrange(4, 5), 0, 0)
    Art.swordArt()
    print("While walking you find a new sword!")
    print("----------------------------------")
    print("Its stats are:")
    scsword.itemStats()
    print("----------------------------------")

    print("Your current attack is: " + str(player.attack))
    keep = input("Would you like to keep it? ")
    if (keep == 'yes'):
        Move.keepSword(player.attack, scsword.attack)
    else:
        print("You will not keep the item")
else:
    missItem = missItem + 1
'''----------------------------------------------------------------------------------'''
clear()

import pyfiglet
from pyfiglet import Figlet
Custom_fig = Figlet(font='larry3d')
print(custom_fig.renderText('  10 Rooms'))

print("You have advanced to Room 5!")
mon1 = Monster(random.randrange(9, 13), random.randrange(5, 7))

print("----------------------------------")
Player.playerStats(player)
print("----------------------------------")
Monster.monsterStats(mon1)
print("----------------------------------")

game.maingame(player.attack, player.health, player.shield, mon1.attack,
              mon1.health)
game.endofRoom()

rng = random.randrange(1, 2)
if (rng == 1):
    hShield = Item('Hylian Shield', 0, random.randrange(4, 5), 0)
    Art.shieldArt()
    print("While walking you find a new Shield!")
    print("----------------------------------")
    print("Its stats are:")
    hShield.itemStats()
    print("----------------------------------")

    print("Your current defense is: " + str(player.shield))
    keep = input("Would you like to keep it? ")
    if (keep == 'yes'):
        Move.keepShield(player.shield, hShield.defense)
    elif (keep == 'no'):
        print("Ok, but you will probably want it!")
    else:
        print("You will not keep the item")
else:
    missItem = missItem + 1
'''----------------------------------------------------------------------------------'''
clear()

import pyfiglet
from pyfiglet import Figlet
Custom_fig = Figlet(font='larry3d')
print(custom_fig.renderText('  10 Rooms'))

print("You have advanced to Room 6!")
mon1 = Monster(random.randrange(11, 15), random.randrange(6, 8))

print("----------------------------------")
Player.playerStats(player)
print("----------------------------------")
Monster.monsterStats(mon1)
print("----------------------------------")

game.maingame(player.attack, player.health, player.shield, mon1.attack,
              mon1.health)
game.endofRoom()

armortest = Item('Armor of the Champions', 0, 0, random.randrange(4, 5))
print("While walking you find armor!")
print("----------------------------------")
print("Its stats are:")
armortest.itemStats()
print("----------------------------------")

keep = input("Would you like to keep it? ")
if (keep == 'yes'):
    Move.keepArmor(player.health, armortest.health)
elif (keep == 'no'):
    print("Ok, but you will probably need it!")
else:
    print("You will not keep the item")
'''----------------------------------------------------------------------------------'''
clear()

import pyfiglet
from pyfiglet import Figlet
Custom_fig = Figlet(font='larry3d')
print(custom_fig.renderText('  10 Rooms'))

print("You have advanced to Room 7!")
mon1 = Monster(random.randrange(8, 10), random.randrange(5, 7))

print("----------------------------------")
Player.playerStats(player)
print("----------------------------------")
Monster.monsterStats(mon1)
print("----------------------------------")

game.maingame(player.attack, player.health, player.shield, mon1.attack,
              mon1.health)
game.endofRoom()

rng = random.randrange(1, 4)
if (rng == 1):
    apAmmount += 1
    print("While walking you find an Attack potion")
    time.sleep(1)
    print("you now have: " + str(apAmmount) + " attack potions")
    time.sleep(1)

rng = random.randrange(1, 3)
if (rng == 1):
    scsword = Item('Worldline Zero', random.randrange(6, 8), 0, 0)
    Art.swordArt()
    print("While walking you find a new sword!")
    print("----------------------------------")
    print("Its stats are:")
    scsword.itemStats()
    print("----------------------------------")

    print("Your current attack is: " + str(player.attack))
    keep = input("Would you like to keep it? ")
    if (keep == 'yes'):
        Move.keepSword(player.attack, scsword.attack)
    elif (keep == 'no'):
        print("Ok, but you will probably want it!")
    else:
        print("You will not keep the item")
else:
    missItem = missItem + 1
'''----------------------------------------------------------------------------------'''
clear()

import pyfiglet
from pyfiglet import Figlet
Custom_fig = Figlet(font='larry3d')
print(custom_fig.renderText('  10 Rooms'))

print("You have advanced to Room 8!")
mon1 = Monster(random.randrange(9, 12), random.randrange(6, 9))

print("----------------------------------")
Player.playerStats(player)
print("----------------------------------")
Monster.monsterStats(mon1)
print("----------------------------------")

game.maingame(player.attack, player.health, player.shield, mon1.attack,
              mon1.health)
game.endofRoom()

rng = random.randrange(1, 4)
if (rng == 1):
    spAmmount += 1
    print("While walking you find a Shield potion")
    time.sleep(1)
    print("you now have: " + str(spAmmount) + " shield potions")
    time.sleep(1)

rng = random.randrange(1, 2)
if (rng == 1):
    hShield = Item('Aegis Shield', 0, random.randrange(6, 8), 0)
    Art.shieldArt()
    print("While walking you find a new Shield!")
    print("----------------------------------")
    print("Its stats are:")
    hShield.itemStats()
    print("----------------------------------")

    print("Your current defense is: " + str(player.shield))
    keep = input("Would you like to keep it? ")
    if (keep == 'yes'):
        Move.keepShield(player.shield, hShield.defense)
    elif (keep == 'no'):
        print("Ok, but you will probably want it!")
    else:
        print("You will not keep the item")
else:
    missItem = missItem + 1

clear()

rng = random.randrange(1, 2)
if (rng == 1):
    scsword = Item('Energy Sword', random.randrange(6, 8), 0, 0)
    Art.swordArt()
    print("While walking you find a new sword!")
    print("----------------------------------")
    print("Its stats are:")
    scsword.itemStats()
    print("----------------------------------")

    print("Your current attack is: " + str(player.attack))
    keep = input("Would you like to keep it? ")
    if (keep == 'yes'):
        Move.keepSword(player.attack, scsword.attack)
    elif (keep == 'no'):
        print("Ok, but you will probably want it!")
    else:
        print("You will not keep the item")
else:
    missItem = missItem + 1

clear()

rng = random.randrange(1, 2)
if (rng == 1):
    hShield = Item('GREATSHIELD OF ARTORIAS', 0, random.randrange(6, 8), 0)
    Art.shieldArt()
    print("While walking you find a new Shield!")
    print("----------------------------------")
    print("Its stats are:")
    hShield.itemStats()
    print("----------------------------------")

    print("Your current defense is: " + str(player.shield))
    keep = input("Would you like to keep it? ")
    if (keep == 'yes'):
        Move.keepShield(player.shield, hShield.defense)
    elif (keep == 'no'):
        print("Ok, but you will probably want it!")
    else:
        print("You will not keep the item")
else:
    missItem = missItem + 1
'''----------------------------------------------------------------------------------'''
clear()

import pyfiglet
from pyfiglet import Figlet
Custom_fig = Figlet(font='larry3d')
print(custom_fig.renderText('  10 Rooms'))

print("You have advanced to Room 9!")
mon1 = Monster(random.randrange(10, 12), random.randrange(7, 9))

print("----------------------------------")
Player.playerStats(player)
print("----------------------------------")
Monster.monsterStats(mon1)
print("----------------------------------")

game.maingame(player.attack, player.health, player.shield, mon1.attack,
              mon1.health)
game.endofRoom()

rng = random.randrange(1, 4)
if (rng == 1):
    hpAmmount += 1
    print("While walking you find a Health potion")
    time.sleep(1)
    print("you now have: " + str(hpAmmount) + " health potions")
    time.sleep(1)

rng = random.randrange(1, 2)
if (rng == 1):
    scsword = Item('The Holy Avenger Sword', random.randrange(7, 8), 0, 0)
    Art.swordArt()
    print("While walking you find a new sword!")
    print("----------------------------------")
    print("Its stats are:")
    scsword.itemStats()
    print("----------------------------------")

    print("Your current attack is: " + str(player.attack))
    keep = input("Would you like to keep it? ")
    if (keep == 'yes'):
        Move.keepSword(player.attack, scsword.attack)
    elif (keep == 'no'):
        print("Ok, but you will probably want it!")
    else:
        print("You will not keep the item")
else:
    missItem = missItem + 1
'''----------------------------------------------------------------------------------'''

clear()

print("You enter the final room")
time.sleep(2)
print("The air goes cold and you quietly shiver")
time.sleep(2)
print("Suddently the ground shakes!")
time.sleep(2)
print("A massive beast with 12 Arms rises up!")
time.sleep(2)
contin = input("This is the final confrontation! Are you ready? ")
if (contin == 'yes'):
    print("alright " + userName + ", lets do this")
else:
    print("Sorry " + userName + ". This monster waits for no man!")
'''----------------------------------------------------------------------------------'''
clear()
print("Congratulations " + userName + "! You were able to beat the game in: " +
      str(playerMoves) + " moves!")
print("You missed out on: " + str(missItem) + " possible items")
time.sleep(3)
print("")
print("")
print(
    "10 rooms in infinatnly replayable. Go back again and see how quick you can beat it, or how many items you can get!"
)
print("")

print_slow(
    "Special Thanks to the repl.it community for helping me out in coding and development"
)

print("")
print("")

time.sleep(4)

custom_fig = Figlet(font='big')
print(custom_fig.renderText('Thanks for    Playing!'))
time.sleep(10)
sys.exit()
