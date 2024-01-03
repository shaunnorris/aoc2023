import os

def read_file_lines(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    else:
        print("no input file found")
        return False

def test_read_file_lines(tmp_path):
    # Create a temporary file and write some content to it
    test_file = tmp_path / "test_file.txt"
    with open(test_file, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3")

    # Use the function to read the file's content
    result = read_file_lines(test_file)
    assert result == ["Line 1", "Line 2", "Line 3"]
    badresult = read_file_lines('should_not_exist.txt')
    assert badresult == False
    
def transpose(strings):
    zipped = zip(*strings)
    transposed = [''.join(group) for group in zipped]
    return transposed


def test_in_grid():
    testgrid = ['abc', 'def', 'ghi']
    assert in_grid(testgrid, (0,0)) == True
    assert in_grid(testgrid, (1,1)) == True
    assert in_grid(testgrid, (2,2)) == True
    assert in_grid(testgrid, (3,3)) == False
    assert in_grid(testgrid, (0,3)) == False
    assert in_grid(testgrid, (3,0)) == False
    assert in_grid(testgrid, (-1,0)) == False
    assert in_grid(testgrid, (0,-1)) == False
    
def in_grid(grid, coord):
    """Return True if coord is in the grid, False otherwise"""
    x, y = coord
    if x < 0 or y < 0:
        return False
    try:
        grid[y][x]
        return True
    except IndexError:
        return False