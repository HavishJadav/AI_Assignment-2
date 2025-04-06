import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gymnasium as gym
from algorithms.branch_and_bound import branch_and_bound
import imageio

# Run algorithm
path, cost = branch_and_bound(env_name="FrozenLake-v1")

# Check if path was found
if path is None:
    print("No solution found by the algorithm.")
    exit()

# Set up environment for rendering (RGB frames for GIF)
env = gym.make("FrozenLake-v1", render_mode="rgb_array", is_slippery=False)
env.reset()

# Capture frames
frames = []
for state in path:
    env.unwrapped.s = state
    frame = env.render()
    frames.append(frame)

# Save as GIF
imageio.mimsave("bnb_frozenlake.gif", frames, duration=0.8)
print("GIF saved as bnb_frozenlake.gif")
