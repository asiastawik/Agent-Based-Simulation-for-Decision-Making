import numpy as np
import matplotlib.pyplot as plt

def simulate(L, x, N, p):
    t_max = 10 ** 4
    exit_count = 0
    
    for i in range(0, N):
        t = 0
        grid = np.random.choice([1, -1], size=L, p=[x, 1-x])
       
        while t < t_max:
            t += 1
    
            for i in range(L):
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
                if np.sum(grid) == L:
                    exit_count += 1
                break
    
        exit_probability = exit_count / N
        
    return exit_probability

L = 50
x = 0.5
N = 10 ** 5  # Configurations
step = 0.01  # Step size for p

p = []
p_value = 0.4
while p_value <= 0.6:
    p.append(round(p_value, 2))
    p_value += step
    
# p = []
# p_value = 0.0
# while p_value < 0.99:
#     p.append(round(p_value, 2))
#     p_value += step

simulation_results = []
exit_probabilities = []

for p_value in p:
    print(p_value)
    result = simulate(L, x, N, p_value)
    simulation_results.append((p_value, result))
    exit_probabilities.append(result)
    
data = np.column_stack((p, exit_probabilities))
np.savetxt('exit_probabilities.txt', data, delimiter='\t', header='p\texit_probability')
    
plt.plot(p, exit_probabilities)
plt.xlabel('Convincing Ability of Yes-Agents (p)')
plt.ylabel('Exit Probability (E)')
plt.title('Exit Probability E(p)')
plt.grid(True)
plt.show()
