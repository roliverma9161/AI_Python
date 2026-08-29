import numpy as np
import random

num_states = 6
num_action = 2
rewards = np.array([-1, -1, -1, -1, -1, 10]) 
Q = np.zeros((num_states, num_action))
alpha = 0.1
gamma = 0.9
epsilon = 0.2


def get_next_state(state, action):
    if action == 0: 
        return max(0, state - 1)
    else: 
        return min(num_states - 1, state + 1)


num_episodes = 1000

for episode in range(num_episodes):
    state = 0

    while state != num_states - 1:  
        
        if random.uniform(0, 1) < epsilon:
            action = random.choice([0, 1])  
        else:
            action = np.argmax(Q[state])  

        
        next_state = get_next_state(state, action)

        
        reward = rewards[next_state]

        Q[state, action] = Q[state, action] + alpha * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )


        state = next_state

print("Trained Q-Table:")
print(Q)
