"""Flood-fill to count chambers in a cave.
CS 210 project.
<Your name here>, <date>
Credits: Thalia Hundt
"""
import doctest
import config
import cave
import cave_view

#def fill(cavern: list[list[str]], row_i: int, col_i: int):
    #"""Pour water into cell at row_i, col_i"""
    #cavern[row_i][col_i] = cave.WATER
    #cave_view.fill_cell(row_i, col_i)
        
def scan_cave(cavern: list[list[str]]) -> int:
    """Scan the cave for air pockets.  Return the number of
    air pockets encountered.

    >>> cavern_1 = cave.read_cave("data/tiny-cave.txt")
    >>> scan_cave(cavern_1)
    1
    >>> cavern_2 = cave.read_cave("data/cave.txt")
    >>> scan_cave(cavern_2)
    3
    """
    air_row = 0
    for row_i in range(len(cavern)):
        for col_i in range(len(cavern[0])):
            if cavern[row_i][col_i] == cave.AIR:
                air_row += 1
                fill(cavern, row_i, col_i)
                cave_view.change_water()
    return air_row

def fill(cavern: list[list[str]], row_i: int, col_i: int):
    """Fill the whole chamber around cavern[row_i][col_i] with water
    """
    if 0 > row_i or row_i >= len(cavern) or 0 > col_i or col_i >= len(cavern[0]) or cavern[row_i][col_i] != cave.AIR:
        return True
    cavern[row_i][col_i] = cave.WATER
    cave_view.fill_cell(row_i, col_i)
    fill(cavern, row_i + 1 , col_i) 
    fill(cavern, row_i - 1 , col_i)
    fill(cavern, row_i, col_i + 1)
    fill(cavern, row_i, col_i - 1)
        
def main():
    doctest.testmod()
    cavern = cave.read_cave(config.CAVE_PATH)
    cave_view.display(cavern, config.WIN_WIDTH, config.WIN_HEIGHT)
    chambers = scan_cave(cavern)
    cave_view.prompt_to_close()
    print(f"Found {chambers} chambers")
    
    
if __name__ == "__main__":
    main()
