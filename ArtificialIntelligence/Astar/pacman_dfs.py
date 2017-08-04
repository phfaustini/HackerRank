# https://www.hackerrank.com/challenges/pacman-dfs

def dfs( r, c, pacman_r, pacman_c, food_r, food_c, grid):
    stack = []
    stack.append((pacman_r, pacman_c))
    explored = []
    path = {}
    path[pacman_r, pacman_c] = (-1, -1)
    while len(stack) > 0:
        v = stack.pop()

        if v not in explored:
            explored.append(v)
            
            if v[0] - 1 >= 0 and grid[v[0]-1][v[1]] != '%': # UP
                stack.append((v[0]-1, v[1]))
                if (v[0]-1, v[1]) not in path: path[(v[0]-1, v[1])] = v
                
            if v[1] - 1 >= 0 and grid[v[0]][v[1] - 1] != '%': # LEFT
                stack.append((v[0], v[1]-1))
                if (v[0], v[1]-1) not in path: path[(v[0], v[1]-1)] = v
                
            if v[1] + 1 < c and grid[v[0]][v[1] + 1] != '%': # RIGHT
                stack.append((v[0], v[1]+1))
                if (v[0], v[1]+1) not in path: path[(v[0], v[1]+1)] = v
                
            if v[0] + 1 < r and grid[v[0] + 1][v[1]] != '%': # DOWN
                stack.append((v[0]+1, v[1]))
                if (v[0]+1, v[1]) not in path: path[(v[0]+1, v[1])] = v

            if v[0] == food_r and v[1] == food_c:
                break

    print(len(explored) )
    for i in explored:
        print(i[0], i[1])

    order = []
    father = (food_r, food_c)
    while father != (-1, -1):
        order.append(father)
        father = path[father]

    i = len(order) -1
    print(i)
    while i >= 0:
        print(order[i][0], order[i][1])
        i-=1




if __name__ == "__main__":
    pacman_r, pacman_c = [ int(i) for i in input().strip().split() ]
    food_r, food_c = [ int(i) for i in input().strip().split() ]
    r,c = [ int(i) for i in input().strip().split() ]

    grid = []
    for i in range(0, r):
        grid.append(input().strip())

    dfs(r, c, pacman_r, pacman_c, food_r, food_c, grid)