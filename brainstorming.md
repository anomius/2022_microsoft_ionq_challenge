# Quantum Tic Tac Toe

The game we will be quantizing today is none other than the infamous tic tac toe!“Quantizing” a game simply means introducing quantum effect into the game. 
For those who have never heard of it, Tic tac toe is a 2-player strategy game, where players take turns to place their marking(either “O” or “X”) on a 3x3 board. The goal is to form a straight line from 3 markings.

Our qubit tic tac toe is the extension of Schoridnger’s cat — but instead of 1, we have 9 black boxes with 9 cats inside. Before opening the box(performing measurement), you can perform all sorts of operations(unitary operation) in the box as long as it is non-destructive. The goal is to keep 3 cats alive in a straight line (or dead if you are dead inside). Why does this happen to our poor cat? Well. who knows, let’s just "shut up and play the game"!

A Player has 3 types of move:

-   Measure it will collapse every quantum state on the board.
-   A quantum play i.e  one can place his gates on the board on non finalized state.
-   The CNOT gate to entangle the results that is to capture the point.

### <u>How to win</u>

When a measurement occurs the one with a win state in classical tic tac toe wins.

###  The Board

``` bash
┌───┬───┬───┐
│ 0 │ 1 │ 2 │
├───┼───┼───┤
│ 3 │ 4 │ 5 │
├───┼───┼───┤
│ 6 │ 7 │ 8 │
└───┴───┴───┘
```





### Bibliography
1) https://medium.com/@toohonlin/develop-quantum-mechanics-intuition-through-quantum-game-qubit-tic-tac-toe-d9814bc927dc
