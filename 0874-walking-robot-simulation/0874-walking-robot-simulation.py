class Solution(object):
    def robotSim(self, commands, obstacles):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        curr_pos = [0,0]
        res = 0
        curr_dir = 0
        obstacle_map = {}
        for obs in obstacles:
            if obs[0] not in obstacle_map:
                obstacle_map[obs[0]] = set()
            obstacle_map[obs[0]].add(obs[1])
        
        for command in commands:
            if command == -1:
                curr_dir = (curr_dir + 1) % 4
                continue
            
            if command == -2:
                curr_dir = (curr_dir -1) % 4
                if curr_dir == -1:
                    curr_dir == 3
                continue

            direction = directions[curr_dir]
            for steps in range(command):
                nextx = curr_pos[0] + direction[0]
                nexty = curr_pos[1] + direction[1]

                if nextx in obstacle_map and nexty in obstacle_map[nextx]:
                    break
                curr_pos[0] = nextx
                curr_pos[1] = nexty
            
            res = max(res, curr_pos[0] * curr_pos[0] + curr_pos[1] * curr_pos[1])
        return res