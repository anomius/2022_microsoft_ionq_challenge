# Welcome to IonQ + Microsoft Joint Challenge @ MIT iQuHACK 2022! #QuantumTicTacToe

![](Assets/Header.jpg)

[Michael Kougang](https://github.com/RoyalWeden), [Henry Atkins](https://github.com/henry-dev-atkins), [Ananya Shukla](https://github.com/ShuklaAnanya), [Swaraj Purohit](https://github.com/anomius)
-------------------------------------------------------------

****

The game we will be quantizing today is none other than the infamous tic tac toe! Here, “Quantizing” a game simply means introducing quantum effect into the game. 
For those who have never heard of it, Tic tac toe is a 2-player strategy game, where players take turns to place their marking(either “O” or “X”) on a 3x3 board. The goal is to form a straight line from 3 markings, which can be straight or diagonal.

Our qubit tic tac toe is the extension of Schoridnger’s cat — but instead of 1 box, we have 9 boxes with 9 cats inside. Before opening the box and performing a measurement, you can perform all sorts of unitary operations on the box as long as it is non-destructive. The goal is to keep 3 cats alive in a straight line. Why does this happen to our poor cat? Well. who knows, let’s just "shut up and play the game"!

### Instructions
----------------------------------------------------
0. In X's turn, X applies an X (pauli) and H (Hadamard) gate on the chosen
   cell.
1. In O's turn, O applies a H gate on the cell of choice.
2. To select the cell to claim, type an integer (0-8) when prompted. 
   X's cells are labelled 1, and O's cells are labelled 0.
3. Players may take their turn on existing cells
   to change its state.
4. To entangle two cells, players can apply the
   CX gate to two cells through the command
   CX (first cell) (second cell). e.g. CX 4 5.
5. When a player wants to use the current state
   of the board to get results, they can measure it
   with 'm'. Warning: only play this if you think you'll win!
6. Have fun!

### <u>How to win</u>
----------------------------------------------------

When a measurement occurs, the one with a win state in classical tic tac toe wins.

###  The Board
----------------------------------------------------

``` bash
┌───┬───┬───┐
│ 0 │ 1 │ 2 │
├───┼───┼───┤
│ 3 │ 4 │ 5 │
├───┼───┼───┤
│ 6 │ 7 │ 8 │
└───┴───┴───┘
```


### Sample Runthrough
![output1](https://user-images.githubusercontent.com/98439884/151698210-b056e381-efc5-45c0-8050-2ac67d797072.jpg)
![output2](https://user-images.githubusercontent.com/98439884/151698223-23ecd482-aa39-4204-86fa-f82983f386e8.jpg)
![output3](https://user-images.githubusercontent.com/98439884/151698233-06060373-ab7d-4ff9-9b31-27db4562fe03.jpg)
![output4](https://user-images.githubusercontent.com/98439884/151698239-353c9e60-e4b6-4f98-90d4-f40117abe4f7.jpg)
![output5](https://user-images.githubusercontent.com/98439884/151698242-9c9e1a85-64d1-4634-9a06-f96d14f4fe17.jpg)


``` bash
git clone https://github.com/RoyalWeden/2022_microsoft_ionq_challenge.git
cd 2022_microsoft_ionq_challenge
./setup.sh
```

### Bibliography
----------------------------------------------------

1) https://medium.com/@toohonlin/develop-quantum-mechanics-intuition-through-quantum-game-qubit-tic-tac-toe-d9814bc927dc
2) https://www.researchgate.net/publication/338113536_Quantum_Tic-Tac-Toe_A_Hybrid_of_Quantum_and_Classical_Computing

### Team Experience at iQuHACK 2022
Our experience as a team at the Interdisciplinary Quantum Hackathon 2022 by MIT has been a great learning experience. Through the expert sessions and talks with industry specials and leading researchers, we became even more motivated and enlightened. This hackathon has given us an wonderful platform to exercise our knowledge in the field of quantum computation and computer programming to work on something unique, fulfilling, and fun. We are extremely grateful for opportunity given by the iQuHack Staff and are utmost sure that this hackathon has motivated us to contribute our time and effort as a part of the future quantum workforce.

## Link to the presentation:
