import random
import matplotlib.pyplot as plt

def MakeCoords(x, y):
    coords = tuple()
    for i in range(y + 1):
        for j in range(x + 1):
            coords += ((j, i),)
    return coords

def FindAdjacentNode(current_node, max_x, max_y):
    x, y = current_node
    list1 = ["a", "b"] # a = x change, b = y change
    list2 = ["p", "q"] # p = add, q = subtract
    change = random.choice(list1)
    operation = random.choice(list2)
    
    if change == "a":
        if operation == "p" and x != max_x:
            x += 1
        elif operation == "q" and x != 0:
            x -= 1
    else:
        if operation == "p" and y != max_y:
            y += 1
        elif operation == "q" and y != 0:
            y -= 1
    return (x, y)

def VisualiseStep(coords, path, start_node, end_node):
    plt.clf()
    x_vals = [coord[0] for coord in coords]
    y_vals = [coord[1] for coord in coords]
    
    plt.scatter(x_vals, y_vals, color='lightgray', s=15)
    plt.scatter(*start_node, color='green', s=80, label='Start')
    plt.scatter(*end_node, color='red', s=80, label='End')
    
    if path:
        path_x = [p[0] for p in path]
        path_y = [p[1] for p in path]
        plt.plot(path_x, path_y, color='blue', linewidth=2)
    
    plt.legend()
    plt.title("Pathfinding Progress")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.pause(0.05) # update every 0.05 seconds

def FindPath(coords, max_x, max_y):
    path = []
    start_node = random.choice(coords)
    end_node = random.choice(coords)
    while end_node == start_node:
        end_node = random.choice(coords)
    plt.ion() # turn on interactive mode
    
    k = 0
    current_node = start_node
    step = 0
    while current_node != end_node:
        adjacent_node = FindAdjacentNode(current_node, max_x, max_y)
        if adjacent_node == current_node or adjacent_node in path:
            k += 1
        else:
            if adjacent_node != start_node:
                current_node = adjacent_node
                path.append(current_node)
                VisualiseStep(coords, path, start_node, end_node)
        step += 1
        if k > 100:
            path.clear()
            current_node = start_node
            k = 0
    
    print(f"It took {step} steps to find the path between {start_node} and {end_node}")
    plt.ioff() # turn off interactive mode
    plt.show()
    return path

if __name__ == "__main__":
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))
    coords = MakeCoords(x, y)
    path = FindPath(coords, x, y)
