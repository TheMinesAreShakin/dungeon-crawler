# Battle Game:

## Housekeeping Functionality:

### Main Menu:
- quit
- start

### Loop Menu:
- show menu of basic options every loop
- options:
    - attack
    - check gold
    - check lvl
    - quit

### Death / Kill handling:
- send to menu on death
- on kill
    - give player new opponent

## Player and Opponent

### Both fighters (aka Entity):
- both fighters have hp, defense, gold, exp, and attack
- hp is health points and vary depending on type
- def varies and determines the hit number needed to successfully hit
- att is attack and is a range that is randomly chosen from
- should have a gold amount that is rewarded to the entity that kills them
- exp is rewarded to the killer
    - if a persistent world is created it would then be possible for a player to level up go back and kill a monster to get their levels back


### Player:
- Player attack should have a base range that can be raised with different types of weapons
- player should have a base dmg for unarmed strikes
    - unarmed dmg should be
- player should have exp and level scaling based on exp
    - level should change the player's hp, att, and def


### Opponent:
- should have a list of attacks with their own att and dmg values
    - list should be standardized so that it can be loaded from a file for different opponent types
    - dmg should be a range of reasonable numbers based on the attack type and if the opponent has a weapon
- opponent should have a list of possible item drops

## Items:

### Weapons:
- weapons should have a attBonus and dmg stat
- attBonus will be a bonus on top of the base att of the player
- dmg will replace the player's unarmed attack dmg


## MVP:
- basic Main menu (quit / start)
- loop menu
- entity class to be inherited from
- player class
    - att base range
    - unarmed dmg
    - gold (0 starting)
- opp class
    - one opp with attacks and gold drop
- death state handling
- victory (kill opp) handling
    - recycle the same opp over and over
- gold transfer on death