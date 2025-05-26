class MazeEnvironment:
    def __init__(self,maze):

        self.start, self.goal= self.pos_start_goal(maze)
        self.maze = maze

    def pos_start_goal(self, maze):
        start = None
        goal = None
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 'g':
                    goal = (i,j)
                if maze[i][j] == 's':
                    start = (i,j)

        return start, goal

    def get_neighbors(self,pos):

        actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for action in actions:
            new_x = pos[0] + action[0]
            new_y = pos[1] + action[1]

            # se está dentro do tabuleiro
            if 0 <= new_x < len(self.maze) and 0 <= new_y < len(self.maze[0]):
                cell = self.maze[new_x][new_y]
                # se é um posição livre
                if cell == '0' or cell == 0 or cell == 'g':
                    neighbors.append((new_x, new_y))

        return neighbors

class Environment:
    def __init__(self,G={},start=[],goal=[]):
        if G:
            self.G=G
        else:
            self.G = {'A':['B','C'],
                 'B':['D','E'],
                 'C':['F'],
                 'D':[],
                 'E':[],
                 'F':['G','H'],
                 'G':[],
                 'H':[]}
        if not start:
            self.start = 'A'
        else:
            self.start = start
        
        if not goal:
            self.goal = 'G'
        else:
            self.goal = goal

    def get_neighbors(self,state):
        return self.G[state]

if __name__ == '__main__':

    env = Environment()

    print(env.G)
    print(env.goal)
    print(env.start)

    print(env.get_neighbors('A'))

    print(env.get_neighbors('F'))




        


       