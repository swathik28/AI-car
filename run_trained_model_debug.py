from car_rl_env import CarRLEnv

# Create the environment
env = CarRLEnv()

# Reset the environment
obs, _ = env.reset()

# Render the environment for a few steps
for _ in range(100):
    # Take a random action
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    env.render()
    if terminated or truncated:
        obs, _ = env.reset()
