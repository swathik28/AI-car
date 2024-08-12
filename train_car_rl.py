from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from car_rl_env import CarRLEnv

# Create the custom environment
env = CarRLEnv()
check_env(env, warn=True)

# Define the RL model
model = PPO("CnnPolicy", env, verbose=1)

# Train the model
model.learn(total_timesteps=10000)  # Adjust the timesteps as needed

# Save the model
model.save("car_rl_model")
