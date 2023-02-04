# How to play Aibou

## Objective

The objective of Aibou is to win battles. A battle is won when the opposing 
monster's healthpoints (**HP**) are less than or equal to 0. Conversely, a battle is 
lost when the user's monster (partner monster) loses all of their healthpoints.

## Game mechanics

### Moves and turns

Each turn the user and the opposing AI will select a move that can affect each 
other. Some examples are damaging, healing, and status moves. Moves are carried 
out in a sequential and cyclic manner: partner, boss, partner, boss, etc. At the 
moment, there is no speed stat and the partner monster always moves first to 
start the battle.

### Quick-time-events (QTEs)

After selecting a move, you will be thrown into a quick-time-event (QTE). 
During the QTE phase, random keys will appear in the window at various positions. 
As the prompt at the bottom says, "Press the key!" 
to pass the QTE with a success status. Failure to press the correct key in the 
time window will result in a fail. The number of key-pressing events and time 
alotted for each QTE varies depending on the move selected. Passing QTEs is the 
essential to ensure your moves are used to their full potential.

### Damage

Damaging moves directly lower a monster's HP. Each damaging move has a base 
power that is multiplied by the percentage of QTEs passed. For example, the move 
**bite** has a base power of 60 and a total of 2 QTEs. If bite is selected and 
2/2 QTEs are passed, then the move will deal the full damage, reducing the 
opposing monster's HP by 60. However, if only 1/2 QTEs are passed, then bites 
resultant damage will be 30 (1/2 * 60). Another factor in damage calculation 
could be the **status** of the partner or boss monster.

### Healing

Some moves can directly or indirectly heal a monster. For example, the move 
**honeyslurp** can heal up to 75HP for the user. Similar to damaging moves, the 
amount healed is dependent on the ratio of QTEs passed out of the total QTEs for 
the move; honeyslurp has 5 QTEs and a base heal amount of 75. Indirect healing 
moves include, but are not limited to, lifesteal moves that both deal damage to 
the opposing monster and heal the move user at the same time.

### Status

A **status** is an effect placed on a monster than can be either beneficial or 
harmful. Statuses usually have a duration that can be decremented over time. 
The event that decrements a status duration varies. 
**Evading** is an example of a positive status that benefits the monster 
posessing the evading status by granting the chance of dodging incoming attacks. 
At the moment, the evading status will only decrement after an opposing monster 
tries to land an attack. So, the evading status is not guarunteed to decrement 
after a turn as may be expected.


## Battle controls

Move prompts are numbered. To select an attack press the key that corresponds to 
the move number, then press ENTER to confirm. During the QTE phase, the correct 
key only needs to be pressed once; ENTER does not need to be pressed during QTEs. 
Furthermore, pressing the incorrect key will not result in 
a failure; the only thing that matters is presssing the *correct* key within 
the time window.

## FAQ

### I passed all QTEs, why did my move fail?

Non-damaging moves, such as moves that set an Evading status, often have a set 
efficacy lower than 100%. For example, the move **evade** from **babybee** has 
a base 80% efficacy and there are 5 QTEs associated with the move. If all 5 QTEs 
are passed, then the max efficacy (80% * 100%) for the move will be used in 
choosing whether the move succeeds or fails. On the other hand if only of 
1/5QTEs are successful, then the change of **evade** succeeding is 80% * 20% 
which is only 16%. Non-damaging or **status** moves are typically very powerful 
and can have long lasting effects; for this reason, the risk is that they do not 
have 100% efficacy.
