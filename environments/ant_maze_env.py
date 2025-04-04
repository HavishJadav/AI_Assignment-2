import gymnasium as gym

def ant_maze_env():
    env = gym.make("Taxi-v3", render_mode="ansi")
    return env
