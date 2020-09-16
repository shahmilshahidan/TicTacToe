# tictactoe
## About
This is my first pygame project. There are several components that made up this game: 3X3 grid, X and O and player status (Win, Lose or Draw).
## Installation for Mac
Visit [pygame](https://www.pygame.org/wiki/GettingStarted) to install the python game engine. If not familiar with Python Package Installer, visit [pip](https://pypi.org/project/pip/).
```
pip install pygame
```
If there are any issues running the command above, try these commands instead:
```
python3 -m pip install -U pygame==2.0.0.dev6 --user
```
For any Python users that are using virtualenv in their environment,
```
# create a virtualenv called 'anenv' and use it.
python3 -m virtualenv anenv
. ./anenv/bin/activate
# venvdotapp helps the python be a mac 'app'. So the pygame window can get focus.
python -m pip install venvdotapp
venvdotapp
python -m pip install pygame
```
For Anaconda users, use pythonw instead of python
## Installation for Windows
```
py -m pip install -U pygame --user
```
## Installation for Unix Systems
Ubuntu/Debian/Mint:
```
sudo apt-get install python3-pygame
```
Fedora/Red hat:
```
sudo yum install python3-pygame
```
Arch/Manjaro:
```
sudo pamac install python-pygame
```
## Usage
```
python3 board.py
```
The game will appear in a separate window.
## How to play
Use mouse to hover around the game board. Click on the square to place X or O. The first player to have three O's or X's in either the same row, column or diagonally wins the game. If there are no such occurrence, then a draw is called.
