import sys

# We encode the knowledge a player has from the game in a dictionary `player` as follows:
# - player["grid"] encodes the grid the player is playing with
# - player["history"] encodes the history of moves player by the player
# - player["boat"] keeps track of the damages on each boat of the player
# - player["nboat"] keeps track of the number of undestroyed boats on the board
# 
# Each boat is represented by one letter :
#
# - the carrier (size 5) is denoted with letter C
# - the battle ship (size 4) is denoted with letter B
# - the destroyer (size 3) is denoted with letter D
# - the submarine (size 3) is denoted with letter S
# - the patrol boat (size 2) is denoted with letter P

# More details now:
# - player["grid"] is a 10x10 string list such that player["grid"][i][j] is:
#   - "." if the cell (i,j) is empty
#   - "x" if the cell contains a boat that has been hit by the other player
#   - "C" (resp "N","D","S","P") if the carrier is at position (i,j) and has not yet been hit. 
# - player["history"] is a 10x10 string list such that player["history"][i][j] is:
#   - "?" if the player has not yet shot at position (i,j)
#   - "M" if the player has shot at position (i,j) and missed
#   - "H" if the player has shot at position (i,j) and hit
# - player["boat"] is a dictionary such that player["boat"][L] is the number of cells not hit for the boat denoted by letter L. For example, at start, player["boat"]["C"] is 5 because the carrier is unhit and has size 5. If the other player hits the carrier once, then player["boat"]["C"] is decreased to 4.

# Here are some general values for the game

boatSizes = {"C":5, "B":4, "D":3, "S":3, "P":2}
gridsize  = 10

def checkGrid(grid):
    """
    Input: `grid` is a string (gridsize × gridsize) list.
    Output: True if it represents a valid grid and False otherwise.
    It checks that every boat are on the board, with the right number of cells and are positionned in one vertical or horizontal block
    
    For example, a grid
        ...C..BBBB
        ...C......
        ...C......
        ...C......
        ...C......
        DDD.....PP
        ..........
        .....S....
        .....S....
        .....S....
    is valid while
        ...C..BBBB
        ..........
        ...C......
        ...C......
        ...C......
        DDDC....PP
        ..........
        .....S....
        .....S....
        .....S....
    is not valid, since the carrier is not contiguous.
    """
    
    
    dBoatPos = {}
    dPosBoat = {}

    if len(grid) != gridsize:
        return False
        
    for i,l in enumerate(grid):
        if len(l) != gridsize:
            return False
        for j,v in enumerate(l):
            if v in boatSizes.keys():
                if v not in dBoatPos:
                    dBoatPos[v] = []
                dBoatPos[v].append((i,j))
                dPosBoat[(i,j)] = v
            elif v != ".":
                return False
                
    if dBoatPos.keys() != boatSizes.keys():
        return False

    for v in dBoatPos.keys():
        if len(dBoatPos[v]) != boatSizes[v]:
            return False
        dBoatPos[v].sort()
        if len(dBoatPos[v]) > 1:
            orientation = 0
            if dBoatPos[v][0][0] == dBoatPos[v][1][0]:
                orientation = 0
            elif dBoatPos[v][0][1] == dBoatPos[v][1][1]:
                orientation = 1
            else:
                return False
 
            for k in range(len(dBoatPos[v])-1):
                if (dBoatPos[v][k][1-orientation]+1 != dBoatPos[v][k+1][1-orientation]) or\
                   (dBoatPos[v][k][orientation] != dBoatPos[v][k+1][orientation]):
                    return False
    return True

def mkGridFromString(s):
    """
    Builds the grid from a string of the form. Returns a (gridsize × gridsize) array. 
        ...C..BBBB
        ...C......
        ...C......
        ...C......
        ...C......
        DDD.....PP
        ..........
        .....S....
        .....S....
        .....S....
    Trailing empty lines are allowed.
    """

    return [[c for c in row] for row in s.strip("\n").split("\n")]

def mkGridFromPos(boatPos):
    grid = [["." for i in range(gridsize)] for j in range(gridsize)]
    for v in boatPos:
        for (i,j) in boatPos[v]:
            grid[i][j]=v
    return grid

def mkPlayer(grid):
    """Input: `grid` is a (gridsize × gridsize) list representing the
    player's grid (ideally created through mkGridFromPos or
    mkGridFromString functions.

    Output: A dictionary describing a player as explained in the
    beginning of the file, initialized with grid `grid`. If the grid is
    not valid, it raises ValueError exception.
    """
    player = {}
    if checkGrid(grid):
        player["grid"] = grid
        player["history"] = [["?" for i in range(gridsize)] for j in range(gridsize)]
        player["boat"] = boatSizes.copy()
        player["nboat"] = len(boatSizes)

        return player
    else:
        raise ValueError

def updateShoot(player, coord):
    """Input: `player` is a dictionary representing a player and
    `coord` a tuple of size 2 representing a cell in the board.
    
    Output: Returns 0 if the shot missed (no boat at position `coord`), 1 if it hits a boat and 2 if it sinks a boat.

    Side effect: Updates player["boat"] if the shot hit.  Raise ValueError is coord is not valid. 
    """
    (i,j) = coord
    if i>=gridsize or j>=gridsize:
        raise ValueError

    v = player["grid"][i][j]
    if v in player["boat"]:
        player["grid"][i][j] = "x"
        player["boat"][v] -= 1
        if player["boat"][v] == 0:
            player["nboat"] -= 1
            return 2
        else:
            return 1
    else:
        return 0

def shootAt(player1, player2, coord):
    """Input: `player1` and `player2` are two dicts representing two
    players. `coord` a tuple of size 2 representing a cell in the
    board.

    Output: Returns 0 if the shot from player1 to player2 missed (no
    boat at position `coord`), 1 if it hits a boat and 2 if it sinks a
    boat.

    Side effect: updates the history of player1 and the boat states of player2.
    """
    (i,j) = coord
    if i>=gridsize or j>=gridsize:
        raise ValueError

    r = updateShoot(player2, coord) 

    if r==0:
        player1["history"][i][j] = "M" 
    elif r>0:
        player1["history"][i][j] = "H"
        
    return r
    
def playerStr(player):
    colidx = ' '.join([chr(j) for j in range(65, 65+gridsize)])
    tbl = (len(colidx)+3)

    state = "="*tbl+"\t\t"+"="*tbl+"\n"
    state += "     GRILLE JOUEUR    \t\t    GRILLE ADVERSE  \n"
    state += "="*tbl+"\t\t"+"="*tbl+"\n"
    state += f" |{colidx} \t\t |{colidx}\n"
    state += "-"*tbl+"\t\t"+"-"*tbl+"\n"

    for i in range(gridsize):
        state += f"{i}|"

        for j in range(gridsize):
            state += player["grid"][i][j]+" "
                    
        state += "\t\t"
        state += f"{i}|"

        for j in range(gridsize):
            state += player["history"][i][j]+" "
        state += "\n"
    state += "="*tbl+"\t\t"+"="*tbl+"\n"

    return state


def parseCoord(c):
    if len(c) != 2 or c[0] not in [chr(j) for j in range(65, 65+gridsize)] or int(c[1]) not in range(gridsize):
        raise ValueError
    else:
        return (int(c[1]), ord(c[0])-ord("A"))



def parseArg(args):
    if (len(args) != 3):
        print(f"{args[0]} grille1.txt grille2.txt")
        exit(0)
    else:
        players = []
        for i in range(1,3):
            with open(args[i]) as g:
                grid = mkGridFromString(g.read())
                players.append(mkPlayer(grid))
        return players

def get_boat_info(grid):
    visited = [[False]*gridsize for _ in range(gridsize)]
    boat_info = []

    for i in range(gridsize):
        for j in range(gridsize):
            if visited[i][j]:
                continue

            cell = grid[i][j]
            if cell not in boatSizes and cell != "x":
                continue

            letter = None
            if cell in boatSizes:
                letter = cell
            elif cell == "x":
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < gridsize and 0 <= nj < gridsize:
                        if grid[ni][nj] in boatSizes:
                            letter = grid[ni][nj]
                            break
            if letter is None:
                continue

            size = boatSizes[letter]

            orientation = None
            if j + size <= gridsize and all(grid[i][j + k] in [letter, "x"] for k in range(size)):
                orientation = "H"
                coords = [(i, j + k) for k in range(size)]
            elif i + size <= gridsize and all(grid[i + k][j] in [letter, "x"] for k in range(size)):
                orientation = "V"
                coords = [(i + k, j) for k in range(size)]
            else:
                continue

            for x, y in coords:
                visited[x][y] = True
            boat_info.append((i, j, letter, orientation, size))

    return boat_info


def grid_to_html(grid, mask=False):
    image_map = {
        "C": "ship1.png",
        "B": "ship2.png",
        "D": "ship3.png",
        "S": "ship4.png",
        "P": "ship5.png",
        "x": "fire.png",
        "H": "fire.png",
        "M": "missed.png",
        "?": "fogofwar.png",
        ".": "free.png"
    }
    boat_info = get_boat_info(grid)
    
    water_html = '''<div class="layer water">
        ''' + '\n        '.join([''.join(['<img src="images/free.png">' for _ in range(gridsize)]) for _ in range(gridsize)]) + '''
    </div>'''
    
    ships_html = '''<div class="layer ships">
        ''' + '\n        '.join([
        f'''<div class="cell ship" style="grid-column: {y+1} / span {size}; grid-row: {x+1};">
            <img src="images/{image_map[letter]}" class="ship-img">
        </div>''' if orientation == "H" else 
        f'''<div class="cell ship" style="grid-column: {y+1}; grid-row: {x+1} / span {size};">
            <img src="images/{image_map[letter]}" class="ship-img vertical">
        </div>'''
        for (x, y, letter, orientation, size) in boat_info
    ]) + '''
    </div>'''
    
    effects_html = '''<div class="layer effects">
        ''' + '\n        '.join([
        f'''<div class="cell">
            {'<img src="images/fire.png">' if cell in ["x", "H"] else 
             '<img src="images/missed.png">' if cell == "M" else 
             '<img src="images/fogofwar.png">' if mask and cell not in ["M", "H"] else ''}
        </div>'''
        for i in range(gridsize)
        for j, cell in enumerate(grid[i])
    ]) + '''
    </div>'''
    
    return f'''<div class="board">
        {water_html}
        {ships_html}
        {effects_html}
    </div>'''

def generate_html(player0, player1):
    html_template = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Joueur {num}</title>
    <link rel="stylesheet" href="main.css">
    <link rel="stylesheet" href="joueur{num}.css">
</head>
<body>
    <h1>Joueur {num}</h1>
    <div class="boards">
        <div class="player-board">
            <h2>Votre Plateau</h2>
            {player_grid}
        </div>
        <div class="enemy-board">
            <h2>Plateau Adversaire</h2>
            {enemy_grid}
        </div>
    </div>
</body>
</html>'''

    with open("joueur0.html", "w") as f:
        f.write(html_template.format(
            num=0,
            player_grid=grid_to_html(player0["grid"]),
            enemy_grid=grid_to_html(player0["history"], mask=True)
        ))

    with open("joueur1.html", "w") as f:
        f.write(html_template.format(
            num=1,
            player_grid=grid_to_html(player1["grid"]),
            enemy_grid=grid_to_html(player1["history"], mask=True)
        ))

def main():
    players = parseArg(sys.argv)  
    current_player = 0

    generate_html(players[0], players[1])  

    while True:
        print(f"JOUEUR {current_player}")
        print(playerStr(players[current_player]))

        while True:
            c = input("Où voulez-vous tirer (ex A0, q pour quitter)? ").strip().upper()
            if c == "Q":
                print("Fin du jeu.")
                return
            try:
                (i, j) = parseCoord(c)
                break
            except ValueError:
                print("Coordonnées non valides. Essayez encore.")

        result = shootAt(players[current_player], players[1 - current_player], (i, j))
        if result == 0:
            print("Raté !")
        elif result == 1:
            print("Touché !")
        elif result == 2:
            print("Coulé !")

        if players[1 - current_player]["nboat"] == 0:
            print(f"Joueur {current_player} gagne !")
            break

        generate_html(players[0], players[1])

        current_player = 1 - current_player

if __name__ == "__main__":
    main()
