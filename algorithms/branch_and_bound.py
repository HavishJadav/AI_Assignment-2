import heapq
import gymnasium as gym

def branch_and_bound(env_name="FrozenLake-v1"):
    env = gym.make(env_name, render_mode="ansi")
    start_state = env.reset()[0]
    goal_state = env.observation_space.n - 1

    queue = [(0, start_state, [])]  # cost, state, path
    visited = set()

    while queue:
        cost, state, path = heapq.heappop(queue)

        if state in visited:
            continue
        visited.add(state)

        new_path = path + [state]

        if state == goal_state:
            return new_path, cost

        for action in range(env.action_space.n):
            env.unwrapped.s = state
            next_state, reward, terminated, truncated, _ = env.step(action)

            if terminated and next_state != goal_state:
                continue

            if next_state not in visited:
                heapq.heappush(queue, (cost + 1, next_state, new_path))

    return None, float("inf")
