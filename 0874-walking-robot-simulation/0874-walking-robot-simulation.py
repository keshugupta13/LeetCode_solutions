class Solution(object):
    def robotSim(self, commands, obstacles):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # North, East, South, West
        curr_pos = [0, 0]  # Use a list to store current position
        res = 0
        curr_dir = 0
        
        # Create a dictionary to map x-coordinates to a set of y-coordinates of obstacles
        obstacle_map = {}
        for obs in obstacles:
            if obs[0] not in obstacle_map:
                obstacle_map[obs[0]] = set()
            obstacle_map[obs[0]].add(obs[1])
        
        for command in commands:
            if command == -1:
                # Turn right
                curr_dir = (curr_dir + 1) % 4
                continue
            if command == -2:
                # Turn left
                curr_dir = (curr_dir - 1) % 4
                if curr_dir == -1:
                    curr_dir = 3
                continue

            direction = directions[curr_dir]
            for step in range(command):
                nextx = curr_pos[0] + direction[0]
                nexty = curr_pos[1] + direction[1]
                
                # Check if the next position is an obstacle
                if nextx in obstacle_map and nexty in obstacle_map[nextx]:
                    break  # Stop moving if an obstacle is encountered
                
                curr_pos[0] = nextx
                curr_pos[1] = nexty

            # Calculate the maximum Euclidean distance squared
            res = max(res, curr_pos[0] * curr_pos[0] + curr_pos[1] * curr_pos[1])
        
        return res






        