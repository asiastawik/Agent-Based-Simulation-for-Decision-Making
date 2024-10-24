import numpy as np
import matplotlib.pyplot as plt

def simulate(L, x, N, p):
    t_max = 3000
    exit_count = 0
    
    for i in range(N):
        grid = np.random.choice([1, -1], size=L, p=[x, 1-x])
        
        for t in range(t_max):
            idx = np.random.randint(L)
            current_agent = grid[idx]
            left_neighbor = grid[(idx - 1) % L]
            right_neighbor = grid[(idx + 1) % L]
            
            if current_agent == 1:  # yes-agent
                if left_neighbor == -1 and right_neighbor == -1:
                    current_agent = -1
                elif (left_neighbor == -1 and right_neighbor == 1) or (right_neighbor == -1 and left_neighbor == 1):
                    if np.random.random() < p:
                        current_agent = 1
                    else:
                        current_agent = -1
                else:
                    current_agent = 1
            
            elif current_agent == -1:  # no-agent
                if left_neighbor == 1 and right_neighbor == 1:
                    current_agent = 1
                elif (left_neighbor == -1 and right_neighbor == 1) or (right_neighbor == -1 and left_neighbor == 1):
                    if np.random.random() < p:
                        current_agent = 1
                    else:
                        current_agent = -1
                else:
                    current_agent = -1
            
            grid[idx] = current_agent
            
            if np.sum(grid) == L or np.sum(grid) == -L:
                exit_count += 1
                break
    
    exit_probability = exit_count / N
    return exit_probability

L = 10
x = 0.5
N = 10 ** 5  # Configurations
p_step = 0.1
p_values = np.arange(0, 1 + p_step, p_step)

exit_probabilities = []

for p in p_values:
    exit_probability = simulate(L, x, N, p)
    exit_probabilities.append(exit_probability)
    
plt.plot(p_values, exit_probabilities)
plt.xlabel('Convincing Ability of Yes-Agents (p)')
plt.ylabel('Exit Probability (E)')
plt.title('Exit Probability E(p)')
plt.grid(True)
plt.show()

# Finding the minimum value of p for which all employees would agree to take the decision (positive consensus)
min_p_for_consensus = p_values[next(i for i, exit_prob in enumerate(exit_probabilities) if exit_prob == 1)]
print(f"Minimum p for consensus: {min_p_for_consensus}")
