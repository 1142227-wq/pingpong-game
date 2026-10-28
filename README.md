# Ping Pong Game

A simple two-player **Ping Pong** game built with Python and Pygame. Two players control paddles on opposite sides of the screen and try to hit the ball past their opponent to score points.

## Features

- Local two-player gameplay on one keyboard
- Paddle movement with collision detection against the top and bottom walls
- A moving ball that bounces off paddles and walls
- Automatic scoring when the ball passes either side of the screen
- Ball reset to the center after each point
- Live score display and a 60 FPS game loop

## Requirements

- Python 3
- [Pygame](https://www.pygame.org/)

Install Pygame:

```bash
python -m pip install pygame
```

## Run the Game

1. Keep `main.py` in your project folder.
2. Open a terminal in that folder.
3. Run:

```bash
python main.py
```

A **500 × 500** window titled **Ping Pong** will open.

## Controls

| Player | Move up | Move down |
| --- | --- | --- |
| Player 1 (left) | `W` | `S` |
| Player 2 (right) | `↑` | `↓` |

Close the game window to exit.

## How to Play

1. Player 1 controls the left paddle; Player 2 controls the right paddle.
2. Keep the ball in play by moving your paddle to intercept it.
3. The ball bounces off the paddles and the top and bottom walls.
4. If the ball leaves the **left** side, Player 2 scores one point.
5. If the ball leaves the **right** side, Player 1 scores one point.
6. After a point, the ball returns to the center and play continues.

There is currently **no winning-score limit**; the game runs until the window is closed.

## Project Structure

```text
project/
├── main.py      # Game logic, rendering, and input handling
└── README.md    # Project documentation
```

## Code Overview

### `Paddle` class

Creates a **10 × 80** paddle, moves it up or down at **5 pixels per frame** using assigned keys, prevents movement through the top and bottom walls, and draws the paddle in cyan.

### `Ball` class

Creates a **10 × 10** red ball with initial horizontal and vertical speeds of **4 pixels per frame**. Its `update()` method handles movement and collisions. Its `reset()` method places the ball at the center and reverses its horizontal direction after a score.

### Main game loop

The loop processes quit events, reads player controls, updates the ball, checks for scoring, redraws the black background and game objects, displays the white score, and limits the frame rate to **60 FPS**.

## Possible Improvements

- Add a start screen and a game-over screen
- Add a winning score or match timer
- Increase ball speed as rallies get longer
- Add sound effects and a pause function
- Add a single-player mode with an AI paddle

## License

No license has been specified for this project.
