import gymnasium as gym

def frozen_lake_env():
    env = gym.make("FrozenLake-v1", render_mode="ansi")
    return env