import pygame
from stable_baselines3 import PPO
from car_rl_env import CarRLEnv

# Initialize Pygame
pygame.init()

# Create the environment
env = CarRLEnv()

# Load the trained model
print("Loading the trained model...")
model = PPO.load("car_rl_model")
print("Model loaded successfully.")

# Test the trained model
print("Resetting the environment...")
obs, _ = env.reset()
print("Environment reset. Starting the test loop.")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    action, _states = model.predict(obs, deterministic=True)
    print(f"Predicted action: {action}")
    obs, reward, terminated, truncated, info = env.step(action)
    print(f"Observation: {obs.shape}, Reward: {reward}, Terminated: {terminated}, Truncated: {truncated}")
    env.render()
    if terminated or truncated:
        print("Episode terminated or truncated. Resetting environment.")
        obs, _ = env.reset()

print("Test loop completed.")
pygame.quit()
