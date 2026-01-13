# Monty Hall problem

https://en.wikipedia.org/wiki/Monty_Hall_problem

Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

## What

The suggestion is to change from your initial pick to increse your chances. That didn's sond intuitive to me, and seems like to other people too.

But running the simulation, the chance is 67% if you switch each time from the initial pick.

There are two simulations:
- MontyHall - where I force switch from the initial choice
- OneOfTwo - where I randomly pick one of two left options (host pick one of three with the goat)

Output of 100000 runs with force switching from the initial choice:

```
MontyHall: Total wins: 66658 out of 100000 with probability 0.67
OneOfTwo: Total wins: 50169 out of 100000 with probability 0.50
```

In case where I do not force switchin and let randomly decide if I want to switch, the chance drops down to 50%.

Output of 100000 runs where we randomly decide to switch.
```
MontyHall: Total wins: 50075 out of 100000 with probability 0.50
OneOfTwo: Total wins: 49894 out of 100000 with probability 0.50
```

## Code

### To run

```
python run.py
```

### Modify

Easily modify output logging, number of iterations and the forced switching.

Change the variables in the `run.py`.

```
ITERATIONS = 100000 
FORCE_SWITCH = False
LOG_LEVEL = logging.INFO
```
