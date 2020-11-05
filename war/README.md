# Game: WAR

## Rules

Each player starts with a _startingHand_ of cards; for example - 10 cards with the values 1-10.

Players then play a card each from their hand, with the highest card played winning that player a point. This is repeated until all cards in the hand have been played. The winner is the player who won the most points.

## Implementation Rules

2 players face off in a **game** of War.

1 **game** consists of a number of **rounds** of War.

The winner of each **round** is the player with the most points won during that **round**. The winner of the whole **game** is the player who won the most rounds

## Development of a Player

To participate, a player script (or _bot_) needs to be written in Python, using version **3.x.x**

### Requirements

The script should contain a function, called **chooseCard**; with the definition given below.

```python
def chooseCard(availableCards, currentRoundState, historicGameState):
```

This function needs to return an **index** with the selected card. See below for more details on how to do that

### Information available to the player

The function definition given above passes in 3 pieces of information that can be used to write a script...

- `availableCards` - the cards that the player has in his hand

This will be a `List` containing the value of each card in the Player's hand currently, in ascending order. For example, at the start of the round this might be `[1,2,3,4,5,6,7,8,9,10]`. If you play the card `5` in the first round, then the next time your function is called this list will contain `[1,2,3,4,6,7,8,9,10]`.

**IMPORTANT:** the return value from your `chooseCard` function should be an **index** of a card in this array. So in the above example, if you wanted to return the `5` card, your function would use `return 4` - i.e. the card at position 4 in the List.

- `currentRoundState` - the state of the current round of War

This is an object containing all the information for the current round. It has `startingHand`, which is a `List` of the cards each player started with at the start of the round - for example `[1,2,3,4,5,6,7,8,9,10]`.
It also has `myPlayedCards` and `oppPlayedCards`; which are both `List` objects. These contain all of the cards played so far in the round by your bot and your opponent.

- `historicGameState` - the historic information for all of the previous rounds of War in this game

This object contains information for all of the previous rounds of War in this game. This is for the more advanced script and provides more historical information which could be used to create a stategy.
The object will contain two `List` objects; `myHistory` and `oppHistory`.

As an example, `oppHistory` might contain the following `[ [1,2,3,4,5], [5,4,3,2,1] ]` - which would indicate in the first round of War, your opponent played the cards `1, 2, 3, 4, 5` in ascending order. Then the in the second round of War, your opponent changed tactics and played the cards `5, 4, 3, 2, 1` instead.

### Development tips

#### How to run your scripts

This starter kit comes with `my-first-bot`; which you can modify to start writing your very first War bot. We also provide you a simple opponent bot, `opponent-bot`, for you to fight against - these are both found in the `/scripts` directory. To run this, execute the following from this directory...

```
python local-runner.py
```

#### Changing scripts

If you want to run your bot against another opponent; or you want to rename your script (useful for keeping different versions and builds to play with) then this is easily done. 
All scripts should run from the root of the `/scripts` folder, so you should copy and paste any opponent scripts etc into here.

Then, open `local-runner.py` and find the following lines near the top

```python
SCRIPT_USER = 'my-first-bot'
SCRIPT_OPP = 'opponent-bot'
```
... you can then change these to match the new filenames (no .py needed).

#### Debug logging in your script

You can log out the contents of `currentRoundState` using `print(currentRoundState)`. This might be useful to see the structure of the information you get back, as well as the cards your opponent has played.

#### Debug round-by-round logging

The `local-runner.py` script won't show you the historical results for a match; only who won what. You can turn it on by finding the following lines and setting to `True`:

```python
ROUND_BY_ROUND_LOG = False
```

#### Changing the number of rounds

By default; the number of rounds is set to `ROUNDS_PER_GAME = 10`.

For the _real thing_ this will be `1000`. But should you wish to do some finer grained debugging, you might want to change the number of rounds to something smaller.

As with the above, this is done by finding the line in `local-runner.py`

```python
ROUNDS_PER_GAME = 10
```

#### Hints 

Check out the opponent bots - they are well commented and contain a lot of the common moves - like checking what your opponent played last time; searching for a card of a specific number to play, that kind of thing. 
