# Pygame Pong Game

This is a simple Pong game created using the Pygame library in Python. The game includes a paddle and a bouncing ball. The objective of the game is to keep the ball from falling off the screen by bouncing it back with the paddle.

## Getting Started

### Prerequisites

Before you can run this code, you need to have Python and Pygame installed on your system.

You can install Pygame using pip:

```
pip install pygame
```

### Running the Game

To run the game, simply execute the Python script:

```
python pong_game.py
```

## How to Play

- Use the **left arrow** key to move the paddle left.
- Use the **right arrow** key to move the paddle right.
- Try to keep the ball from falling off the bottom of the screen by bouncing it with the paddle.
- If the ball falls off the screen, the game will reset, and you can continue playing.

## Code Overview

Here is a brief overview of the code:

- We initialize Pygame and define some constants for the screen size, paddle size, and ball size.
- We set up the game window and create a clock to control the game's frame rate.
- The main game loop listens for user input and updates the position of the paddle and ball accordingly.
- Collisions with the walls and the paddle are detected, and the ball's direction is adjusted accordingly.
- The game continuously redraws the screen to reflect the updated positions of the paddle and ball.

## Controls

- **Left Arrow Key**: Move the paddle left.
- **Right Arrow Key**: Move the paddle right.
- **Close Window**: Click the close button on the game window to exit the game.

## Acknowledgments

This code is a simple demonstration of game development using the Pygame library. It serves as a basic starting point for creating more complex games.

Feel free to modify and expand upon this code to create your own unique Pong game or experiment with other game development concepts. Enjoy playing!
