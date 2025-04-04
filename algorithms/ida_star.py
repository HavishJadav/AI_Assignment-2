import gymnasium as gym

# Heuristic: Manhattan distance from taxi to destination
def heuristic(state):
    taxi_row, taxi_col, dest_row, dest_col = decode_state(state)
    return abs(taxi_row - dest_row) + abs(taxi_col - dest_col)


# Helper to decode Taxi-v3 state
def decode_state(state):
    env = gym.make("Taxi-v3")
    return env.unwrapped.decode(state)

def is_goal_state(state):
    # Taxi-v3 ends when passenger is dropped off
    return state in goal_states

def ida_star():
    global goal_states
    env = gym.make("Taxi-v3", render_mode="ansi")
    initial_state, _ = env.reset()

    # Get all terminal goal states
    goal_states = set()
    for s in range(env.observation_space.n):
        taxi_row, taxi_col, pass_loc, dest_idx = decode_state(s)
        if pass_loc == 4:  # Passenger has been dropped off
            goal_states.add(s)

    def dfs(path, g, bound, visited):
        node = path[-1]
        f = g + heuristic(node)

        if f > bound:
            return f

        if is_goal_state(node):
            return "FOUND"

        visited.add(node)

        min_threshold = float('inf')
        for action in range(env.action_space.n):
            env.unwrapped.s = node
            next_state, _, terminated, _, _ = env.step(action)

            if next_state in visited:
                continue

            path.append(next_state)
            t = dfs(path, g + 1, bound, visited)

            if t == "FOUND":
                return "FOUND"

            if t < min_threshold:
                min_threshold = t

            path.pop()

        return min_threshold

    bound = heuristic(initial_state)
    path = [initial_state]

    while True:
        visited = set()
        t = dfs(path, 0, bound, visited)

        if t == "FOUND":
            return path, len(path) - 1  # Cost is number of steps

        if t == float('inf'):
            return None, float('inf')

        bound = t
