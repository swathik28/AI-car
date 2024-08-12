import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pygame
from car_simulation import Car, Track, window_width, window_height, window, black, clock

class CarRLEnv(gym.Env):
    def __init__(self):
        super(CarRLEnv, self).__init__()
        self.action_space = spaces.Discrete(4)  # [Accelerate, Decelerate, Turn Left, Turn Right]
        self.observation_space = spaces.Box(low=0, high=255, shape=(window_height, window_width, 3), dtype=np.uint8)
        self.car = Car(window_width // 2, window_height // 2)
        self.track = Track()
        self.track.add_line((100, 100), (700, 100))
        self.track.add_line((700, 100), (700, 500))
        self.track.add_line((700, 500), (100, 500))
        self.track.add_line((100, 500), (100, 100))
        self.checkpoints = [(700, 100), (700, 500), (100, 500), (100, 100)]
        self.current_checkpoint = 0
        self.prev_x = self.car.x
        self.prev_y = self.car.y
        self.done = False
        print("Environment initialized.")

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        if seed is not None:
            np.random.seed(seed)
        self.car = Car(window_width // 2, window_height // 2)
        self.current_checkpoint = 0
        self.prev_x = self.car.x
        self.prev_y = self.car.y
        self.done = False
        print("Environment reset.")
        return self._get_observation(), {}

    def step(self, action):
        print(f"Action taken: {action}")
        self.car.update(action)
        reward = self._get_reward()
        obs = self._get_observation()
        self.done = self._check_done()
        terminated = self.done
        truncated = False  # You can add your condition for truncation if necessary
        print(f"Step taken. Reward: {reward}, Done: {self.done}")
        return obs, reward, terminated, truncated, {}

    def render(self, mode='human'):
        print("Rendering environment.")
        window.fill(black)
        self.track.draw(window)
        self.car.draw(window)
        pygame.display.update()
        clock.tick(30)  # Limit frame rate to 30 FPS

    def _get_observation(self):
        obs = pygame.surfarray.array3d(window)
        obs = np.rot90(obs, 3)
        obs = np.fliplr(obs)
        return obs

    def _get_reward(self):
        # Reward function to incentivize moving forward and reaching checkpoints
        if self.car.x < 100 or self.car.x > 700 or self.car.y < 100 or self.car.y > 500:
            return -1.0  # Negative reward for going out of track

        checkpoint_x, checkpoint_y = self.checkpoints[self.current_checkpoint]
        distance_to_checkpoint = np.sqrt((self.car.x - checkpoint_x) ** 2 + (self.car.y - checkpoint_y) ** 2)

        if distance_to_checkpoint < 50:  # Threshold to consider reaching a checkpoint
            self.current_checkpoint = (self.current_checkpoint + 1) % len(self.checkpoints)
            return 10.0  # Larger reward for reaching a checkpoint

        distance_moved = np.sqrt((self.car.x - self.prev_x) ** 2 + (self.car.y - self.prev_y) ** 2)
        self.prev_x = self.car.x
        self.prev_y = self.car.y
        return 0.1 + distance_moved * 0.01  # Small positive reward for moving forward

    def _check_done(self):
        # Check if car is out of track boundaries
        if self.car.x < 0 or self.car.x > window_width or self.car.y < 0 or self.car.y > window_height:
            return True
        if self.car.x < 100 or self.car.x > 700 or self.car.y < 100 or self.car.y > 500:
            return True
        return False
