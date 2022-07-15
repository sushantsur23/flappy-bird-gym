import time
import flappy_bird_gym
import numpy as np


env = flappy_bird_gym.make("FlappyBird-v0")

obs = env.reset()
while True:
    # Next action:
    # (feed the observation to your agent here)
    # action = env.action_space.sample()  # env.action_space.sample() for a random action
    action = np.random.choice([0,1])  # env.action_space.sample() for a random action

    # Processing:
    obs, reward, done, info = env.step(action)
    print(type(info["score"]))
    break
    # Rendering the game:
    # (remove this two lines during training)
    env.render()
    time.sleep(1 / 30)  # FPS
    
    # Checking if the player is still alive
    if done:
        break

env.close()