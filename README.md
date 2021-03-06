# readme

This repo contains a simple environment for the fantastic "sushi go" card game. I cannot recommend this game enough.

## api

![](https://gym.openai.com/assets/docs/aeloop-138c89d44114492fd02822303e6b4b07213010bb14ca5856d2d49d6b62d88e53.svg)

The api is not done but it will mimic [the openai api](https://gym.openai.com/docs).

## internals

There is an internal state of the system which the agent does not get to see. All the state that is available to the agent will be passed via the observation variable.

![](/readme_imgs/internals1.png)

This will be the case for games with only two players but also for multiple players.

![](/readme_imgs/internals2.png)

The environment object is a mere wrapper around a `Deck`, `Game`, and multiple `Player` objects.

```
from sushigo.player import RandomPlayer
from sushigo.game import Game
from sushigo.deck import StandardDeck

p1 = RandomPlayer()
p2 = RandomPlayer()
game = Game(deck=StandardDeck(), players=[p1, p2])
```

This sets up the entire game. You can give it the `go` command to have it play a game. This will play a game and return a `GameResult` object. This is nice because this means you can run many simulations of the game.

```
game_result1 = game.simulate_game()
game_result2 = game.simulate_game()
game_result3 = game.simulate_game()
```


## building/testing

If you want to build and test you'll first need to install the package. This keeps the testing clean.

```
python setup.py install
pytest tests/*
```

## examples

If you want examples of the api, just look at the `vignette` folder. It contains python scripts that can be run from the command line.