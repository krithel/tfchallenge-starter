# Tech Forum Challenge Starter

This repository is designed to help you get started with submitting a bot for the AI challenge. The repository contains the following files:

- README.md - This file, acts as a walkthrough for creating, testing and uploading your first bot.
- my-first-bot.py - A simple bot to act as a starting point.
- local-runner.py - A game runner that will play your bot off against a sample opponent. This will let you ensure that your bot runs before uploading.
- opponent-bot.py - The opponent used by the local runner.

## Structure of a bot

When writing your bot, there are a few requirements to be aware of:

- Your bot must contain a `chooseMove(myMoves, opponentMoves)` function. This function should be at the root level of the python file, not inside a class. This function will be called everytime your bot makes a move. You can have any other functions within your class to help making a move.

- Your bot can import the basic python libraries, but cannot use external libraries (installed through `pip`). In the future, we will support basic data engineering libraries like `numpy`, `pandas` and `tensorflow` for creating ML-based bots.

- The main function `chooseMove` takes two parameters:
    - `myMoves` - A string array of all moves made by your bot so far
    - `opponentMoves` - A string array of all moves made by your opponent so far

- The `chooseMove` function should return one of `R`, `P` or `S` (capitalisation is important) to play the move Rock, Paper or Scissors respectively. The move histories are lists of those three strings.

## Testing your bot

Once you have a bot ready to go (or you are using the initial starter bot), you can test it locally before uploading. To test `my-first-bot.py` - simply run the command: `python local-runner.py` from this directory. The command will load `my-first-bot.py` and run it against `opponent-bot.py`, both found in the `scripts` directory.

If you want to run custom bots against each other, place them in the `scripts` folder, and change `local-runner.py`. Find the lines:
```
BASE_USER_SCRIPT = 'my-first-bot'
BASE_OPPONENT_SCRIPT = 'opponent-bot'
```

Change the values to point to your new scripts (without the `.py` extension)

## Uploading your bot

Once you have a bot that works locally - it's time to upload! Go to the [challenge site](https://tfbotchallenge-gcp.appspot.com/home/scripts) and log in. You will need a whitelisted account to be allowed to upload.

Once on the site, you can upload your script with a name and description of your choice. Once uploaded, the script will be validated server-side. This may take up to 10 minutes - once validated, your script will be labelled as active and will be ready to play in the daily tournaments.

