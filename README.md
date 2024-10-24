# Agent-Based Simulation for Decision Making

This repository contains a project to simulate the decision-making process in a company using an **Agent-Based Model (ABM)** with **Monte Carlo simulation**.

## Problem Description

The company operates with an employee-friendly policy where a decision is only made if **all employees agree** (i.e., reach a consensus). Employees can initially have mixed opinions—some agree (*yes*), and others disagree (*no*). 

- After a decision proposal, employees discuss their stance with their two immediate neighbors in a 1D vector and may change their opinion based on interactions.
- A "yes-agent" can convince a neighboring "no-agent" with a certain probability, `p`. The aim is to understand how this probability affects the likelihood of reaching a **positive consensus** (where all employees agree to the decision).

### Simulation Setup

1. **Initial Setup**: 
   - A 1D vector of length 50 represents the company's employees.
   - Initially, 50% of the employees agree with the decision (i.e., `x = 0.5`).

2. **Periodic Boundary Condition**: The interaction is performed in a 1D circular structure, where the first and last employees are neighbors.

3. **Monte Carlo Simulation**: Run the simulation over 100,000 configurations to estimate the probability of reaching a positive consensus under different values of the convincing probability `p`.

## Tasks

### (a) Exit Probability `E` vs. Convincing Ability `p`

- **Objective**: Plot the **exit probability** `E`, which is the fraction of configurations where a positive consensus is reached, as a function of the convincing ability `p`.
- **Goal**: Determine the minimum convincing ability `p` for which a positive consensus is always reached.

### (b) Positive Consensus with 50% Probability

- **Objective**: Identify the value of `p` that results in a **50% chance** of reaching a positive consensus.
- **Goal**: Understand the critical threshold of convincing ability for half of the simulations to reach consensus.

### (c) Effect of `p` on Consensus Probability

- **Objective**: Analyze how the value of `p` influences the overall probability of reaching a positive consensus.
- **Goal**: Comment on how the strength of the yes-agents' influence affects consensus formation.

### (d) Bonus Task: Varying Vector Length

- **Objective**: Repeat the simulation for vectors of length 100 and 500 to assess how the size of the employee group affects the results.
- **Goal**: Observe the scalability of the model and comment on the findings.

## Results and Discussion

The results will explore how the probability `p` impacts the likelihood of reaching a positive consensus and identify the critical thresholds where consensus formation becomes highly probable or less likely.

## How to Run the Simulation

To reproduce the results, implement the agent-based model in Python using periodic boundary conditions and Monte Carlo simulation. Ensure that the length of the employee vector and convincing probability `p` are configurable for further experimentation.

## Conclusion

This project demonstrates how agent-based modeling can provide insights into decision-making processes, where interactions and influences among individuals play a critical role in reaching a group consensus.
