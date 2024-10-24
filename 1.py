import numpy as np
import matplotlib.pyplot as plt

def simulate(L, x, N, p):
    t_max = 3000
    exit_count = 0
    config = 0
    idx = np.arange(0, L)
    new_agents = []
    
    for i in range(0, N):
        t = 0
        grid = np.zeros(L)
        for i in range(L):
            if np.random.random() < x:
                grid[i] = 1
            else:
                grid[i] = -1
                
        config += 1
        
        while t < t_max and (np.sum(grid) != L) and (np.sum(grid) != -L):
            t += 1
            
            for i in range(L):
                current_agent = np.random.choice(idx)
                left_neighbor = grid[current_agent - 1]
                right_neighbor = grid[(current_agent + 1) % L]
                
                if current_agent == 1:  # yes-agent
                    if left_neighbor == -1 and right_neighbor == -1:
                        current_agent = -1
                    elif (left_neighbor == -1 and right_neighbor == 1) or (right_neighbor == -1 and left_neighbor == 1):
                         if p > 0.5:
                             current_agent = 1
                         else:
                            current_agent = -1
                    else:
                        current_agent = 1
                
                elif current_agent == -1:  # no-agent
                    if left_neighbor == 1 and right_neighbor == 1:
                        current_agent = 1
                    elif (left_neighbor == -1 and right_neighbor == 1) or (right_neighbor == -1 and left_neighbor == 1):
                         if p > 0.5:
                             current_agent = 1
                         else:
                            current_agent = -1
                    else:
                        current_agent = -1
                
                new_agents.append(current_agent)
            
            agents = new_agents
            
            if new_agents.count(1) == L or new_agents.count(-1) == L:
                if new_agents.count(1) == L:
                    exit_count += 1 
                break
    
        exit_probability = exit_count / N
        
    return exit_probability

L = 10
x = 0.5
N = 10 ** 3 #configurations #5
step = 0.1 #0.01
p = np.arange(0, 1 + step, step)

print(p)

simulation_results = []
exit_probabilities = []

for p_value in enumerate(p):
    results = simulate(L, x, N, p_value)
    simulation_results.append((p_value, results))
    exit_probabilities.append(results)
    
plt.plot(p, exit_probabilities)
plt.xlabel('Convincing Ability of Yes-Agents (p)')
plt.ylabel('Exit Probability (E)')
plt.title('Exit Probability vs. Convincing Ability')
plt.grid(True)
plt.show()

# Finding the minimum value of p for which all employees would agree to take the decision (positive consensus)
min_p_for_consensus = p[next(i for i, p in enumerate(exit_probabilities) if p == 1)]
print(f"Minimum p for consensus: {min_p_for_consensus}")

    