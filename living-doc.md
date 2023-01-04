# living-doc.md

# Aibou

A tentative summary of the aibou project.

## Summary

Aibou is a CLI, turn-based, RPG game where the player commands their partner
monster to defeat 3 bosses. The boss battle system is turn-based combat 
where the partner and boss monster use attacks to lower the eachother's 
hitpoints. However, commanding attacks require a subtask where the player 
is prompted and has to press the correct key (a quick-time event) a number of 
times before damage is calculated and dealt. After winning a boss battle, 
except the final boss, the partner undergoes metamorphosis which changes the
physical appearance of the partner and gives it new attacks.

## Battling

### Hitpoints

Hitpoints (HP) is the health of a monster. Attacks are used by monsters to
lower HP to 0 or below to defeat opposing monsters.

### Attacking

Attacks have 2 primary components. First, the attack has a relative damage
value, plainly called 'damage'. Next, there is the 'skill' component of an
attack which indicates the relative difficulty of performing the max damage.
As a general rule, damage is proportional to skill, so that high damage attacks
will also have high skill. Altogether, the acutal amount of hitpoints
subtracted from the opponent after an attack is the plain 'damage' value
multiplied by the performance on the quick-time event skill test (percentage).

For example, an attack called 'blitz' has both high damage and high skill.
The 'damage' value equals 100, and if the player scores 100% on the skill test,
then the amount of HP subtracted from the opponent will be the full 100HP. If
the player misses 1 out of the 10 quick-time events, then their skill test 
score is 90%. Therefore, the amount of HP subtracted from the opponent is 
100HP * 0.9 = 90HP.

## Art

The game runs solely via the command line, and all monsters are depicted by 
ASCII text art ([Examples](https://fsymbols.com/text-art/))

___________________________¶¶¶¶¶¶¶¶¶¶¶  
__________________________¶¶11¶¶11¶¶¶¶¶¶ 
_________________________¶¶¶¶11¶¶1¶11¶¶¶¶ 
_____¶¶¶¶¶_______________¶¶¶¶¶11¶11¶11¶¶¶¶ 
___¶¶¶¶¶¶¶¶¶_______________¶¶¶¶¶1¶1¶11¶1¶¶¶ 
__¶¶1111111¶¶_________________¶¶¶¶¶1¶1¶¶1¶¶¶ 
_¶¶11111¶1¶1¶¶¶_________________¶¶¶1¶1¶¶1¶¶¶¶
¶¶111¶¶¶¶1¶¶11¶__________________¶¶¶¶11¶1¶¶¶¶
_¶¶¶¶¶¶¶¶1¶¶11¶¶_________________¶¶¶¶1¶11¶1¶¶
_¶¶0¶___¶11¶¶11¶¶_________________¶¶¶¶¶11¶1¶¶
_¶______¶1¶¶¶111¶_________________¶_¶¶¶11¶1¶¶
_¶¶_____¶11¶¶¶11¶¶_______________¶¶_¶¶¶1¶1¶1¶
__¶____¶¶11¶_¶¶¶1¶_______________¶__¶1¶¶¶1¶1¶
__¶¶¶¶¶¶¶11¶_¶¶¶¶¶¶_____________¶¶_¶¶1¶¶1¶1¶¶
___¶___¶¶1¶¶____¶¶¶¶¶_________¶¶¶__¶¶1¶¶¶1¶¶¶
___¶__¶¶¶1¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶___¶¶11¶¶1¶1¶¶
___¶_¶¶¶11¶___________¶¶¶¶¶¶_____¶¶11¶¶1¶11¶¶
_____¶¶1¶¶¶____________________¶¶¶11¶¶11¶¶¶¶¶
____¶¶111¶¶_____________¶¶¶¶¶¶¶¶111¶¶111¶¶¶¶ 
____¶¶¶1111¶______¶¶¶¶¶¶¶¶¶¶111111¶¶111¶¶¶¶ 
____¶¶¶¶1111¶___¶¶¶¶111111111¶¶¶¶¶¶111¶¶¶ 
____¶¶¶¶¶¶1¶¶__¶¶¶1111¶11¶¶¶¶11¶1111¶¶¶¶ 
____¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶111111111¶¶¶¶ 
_____¶¶¶¶¶¶¶¶¶¶¶1¶11¶111¶¶111111¶¶¶¶ 
______¶¶111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶ 
_______¶¶¶¶¶¶¶¶¶____________¶¶¶¶ 
________¶1¶¶1¶¶¶¶_____________¶¶¶ 
________¶1¶¶1¶¶_¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶ 
________¶1¶11¶¶___¶¶111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
________¶1111¶¶____¶¶1111¶¶¶¶¶¶¶__¶111¶¶¶¶ 
________¶1¶11¶¶______¶¶¶¶¶¶_____¶__¶¶111¶¶¶ 
________¶1¶11¶¶_______¶¶¶¶___¶¶¶_¶__¶¶11¶¶¶¶ 
________¶1¶¶1¶¶_________¶¶___¶¶¶__¶__¶¶1¶¶¶¶ 
________¶11¶1¶¶_________¶¶___¶¶¶___¶__¶11¶¶¶ 
________¶11¶1¶¶_________¶¶¶____¶¶___¶__¶¶¶¶¶ 
________¶¶1¶1¶¶_________¶¶¶¶____¶¶¶__¶_¶¶¶ 
________¶¶1¶1¶¶________¶¶¶¶¶¶¶____¶¶__¶¶¶¶ 
_____¶¶¶¶1111¶¶______¶¶¶¶¶¶¶¶¶¶¶_____¶_¶¶¶ 
___¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶111¶¶111¶¶¶¶_¶¶¶¶¶¶ 
___¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 


### Metamorphosis 

After winning a boss battle, the player's partner monster undergoes 
metamorphosis which changes the partner's appearance and grants new attacks.

## Development

1. A CLI-based UI which allows the user to perform all game actions from start
to finish.
    a. Proper display and sizing for monsters and text
    b. Navigation of attack choices
2. Damage calculation logic that coordinates with user's performance in the
quick-time event
    a. Effective input recognitition

### To-do

- [x] Store art in individual text files and write code to easily handle monster
 conversion.
- [ ] Create a handler for easy config of monster attacks. For example, attacks
could be read from some sort of master data file that contains all monsters'
attacks.

- [ ] Add an `attacks` attribute to monster's that gets the attacks from a file.

### Handling input

- *Keyboard* module allows reading user input without having to press enter

### Game distribution

- *cx_Freeze* module can create standalone executables that allow the user to
run the program without having python or the pacakges installed.

### Colored text

- termcolor package's colored function works for coloring characters
- rich package for color and layout

### Potential add-on features

#### Defensive quick-time events

The user can reduce the damage received from boss attacks by passing 
quick-time events.
