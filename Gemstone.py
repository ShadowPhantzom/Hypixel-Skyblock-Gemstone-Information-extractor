import re

def GemstoneCheckerV4(ItemLore):
    
    symbols = '❤|❈|☘|✎|⸕|✧|❁|❂|☠|α|⚔'

    # Hash map gemstones
    gemstones = {
    'ruby': ['c', '❤'],
    'amethyst': ['5', '❈'],
    'jade': ['a', '☘'],
    'sapphire': ['b', '✎'],
    'amber': ['6', '⸕'],
    'topaz': ['e', '✧'],
    'jasper': ['d', '❁'],
    'opal': ['f', '❂'],
    'onyx': ['8', '☠'],
    'aquamarine': ['3', 'α'],
    'citrine': ['4', '☘'],
    'peridot': ['2', '☘']
    }

    # Hash map Qualitys
    qualitys = {
    'rough': 'f',
    'flawed': 'a',
    'fine': '9',
    'flawless': '5',
    'perfect': '6'
    }


    data = []   # stores data of all gemstones
    unlocked = 0    # counts amount of unlocked slots
    gemstone = []   # all gemstones applyed are stored here
    quality = []    # all qualitys of gemstones are stored here

    data = re.findall(r'§(\w)\[§(\w)(' + symbols + r')§(\w)\]', ItemLore)   # searches ItemLore for Gemstone slots
    
    for current in data:    # goes trough every gemstone seperatly. If there arent any it skips the loop

        if not re.findall(r"\('8', '8', '(" + symbols + r")', '8'\)", str(current)): # checks if the current gemstone slot is locked. If yes it goes to the next one
            
            if re.findall(r"\('8', '7', '(" + symbols + r")', '8'\)", str(current)): # checks if there are any unlocked slots.
                unlocked = unlocked + 1 # counts how many unlocked slots there are
            else:

                # check what gemstones are applyed
                for i, gemstone_cur in enumerate(gemstones.values()):
                    if current[1] == gemstone_cur[0] and current[2] == gemstone_cur[1]:
                        gemstone.append(list(gemstones.keys())[i])
                        
                        
                        #check the qualitys of the gemstones
                        for i, quality_cur in enumerate(qualitys.values()):
                            if current[0] == quality_cur and current[3] == quality_cur:
                                quality.append(list(qualitys.keys())[i])
                                

    return unlocked, gemstone, quality  #returns all values
