import pyautogui
import time
import pydirectinput as pdi
import sys


def main():
    
    time.sleep(2)
    print(pyautogui.position())
    top = True
    topBattleLocation = ((342, 259, 202, 131))
    topPokemonLocation = ((598, 170, 194, 147))
    topBattleStart = "topBattle.png"
    topFightButton = ((382, 411))


    bottomBattleStart = "bottomBattle.png"
    bottomBattleLocation = ((341, 780, 204, 131))
    bottomPokemonLocation = (579, 645, 219, 167)
    bottomFightButton = (383, 905)
    
    while True:
        if top == True:
            account(topBattleStart, topBattleLocation, topPokemonLocation, topFightButton)
            top = not top
            pyautogui.click(935, 753)
            
            
        else:
            account(bottomBattleStart, bottomBattleLocation, bottomPokemonLocation, bottomFightButton)
            top = not top
            pyautogui.click(941, 275)
        
        


                
def account(startPokemon, startPokeArea, pokeArea, fightButton):
        count = 0
        step = 0
        while True:
            battle_start = pyautogui.locateOnScreen(startPokemon, region=startPokeArea, confidence=0.9)
            if battle_start == None:
                move()
                step += 1
    
            else:
                pdi.keyUp("d")
                time.sleep(1.8)
                if identify(pokeArea):
                    attack(fightButton)
                    count = 0
                    break
                else:
                    count +=1
            print(count, step)
            if count >= 3 or step >= 30:
                    sys.exit("exit")



def attack(fight_button):
    pyautogui.moveTo(fight_button)
    
    for i in range(2):
        pyautogui.click()
    time.sleep(0.32)
    pyautogui.click()


def move():
        pdi.keyDown("d")
        time.sleep(0.2)
        pdi.keyDown("a")
        time.sleep(0.3)
        pdi.keyUp("a")

def identify(pokemonArea):
    common_pokemon = [ 
                      "beautifly.png", "fearow.png", "butterfree.png", "pidgeot.png", "marill.png",
                      
                      
                      "delibird.png", "stantler.png","cryogonal.png",

                      "cubchoo.png", "bergmite.png", "dewgong.png", "vanillite.png",

                      "snorunt.png", "swinub.png", "snover.png", "spheal.png"
                      
                      ]
    for pokemon in common_pokemon:
        mon = pyautogui.locateOnScreen(pokemon, region=pokemonArea, confidence=0.96)
        print(mon)
        if mon != None:
             return True
        
    return False

if __name__ == "__main__":
     main()

