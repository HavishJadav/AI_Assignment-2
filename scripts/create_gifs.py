import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import gymnasium as gym
import imageio
from algorithms.ida_star import ida_star

# Create environment
env = gym.make("Taxi-v3", render_mode="rgb_array")
frames = []

# Run the algorithm to get the path
path, cost = ida_star(env)

# Re-run environment and record frames by setting the agent to each state
for state in path:
    env.reset()
    env.unwrapped.s = state
    frame = env.render()
    frames.append(frame)

# Save GIF
imageio.mimsave("results/ida_star.gif", frames, fps=2)
print("GIF saved as results/ida_star.gif")
