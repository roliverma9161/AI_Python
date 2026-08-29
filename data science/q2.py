def q_learning_update(state, action, reward, next_state):
#Defines a function to update the Q-value for a given (state, action, reward, next_state)
#This function follows the Q-learning update rule:
#Q(s,a)←Q(s,a)+α[R+γ maxQ(s',a')-Q(s,a)]
best_next_action = np.argmax(Q[next_state, :])
#Find the Best Next Action.Finds the action with the highest Q-value in next_state.
#why?:Q-learning is an off-policy algorithm that assumes the agent will follow the best policy
#in the future.
print(best_next_action)