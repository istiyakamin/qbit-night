# Challenge #1: Bell State Explorer

**Week of**: November 2024  
**Difficulty**: Beginner  
**Topics**: Entanglement, Bell States, Measurement

## Overview

In this challenge, you'll explore the fascinating world of quantum entanglement by creating and analyzing Bell states. Bell states are the simplest examples of quantum entanglement and form the foundation for many quantum protocols.

## Learning Objectives

By completing this challenge, you will:
- [ ] Create all four Bell states
- [ ] Understand the measurement correlations in entangled states
- [ ] Visualize quantum states
- [ ] Analyze measurement statistics

## Background

The four Bell states are:
- |Φ⁺⟩ = (|00⟩ + |11⟩) / √2
- |Φ⁻⟩ = (|00⟩ - |11⟩) / √2
- |Ψ⁺⟩ = (|01⟩ + |10⟩) / √2
- |Ψ⁻⟩ = (|01⟩ - |10⟩) / √2

These states are "maximally entangled" - measuring one qubit instantly determines the state of the other.

## The Challenge

### Part 1: Create Bell States

Write a function that creates each of the four Bell states. Your function should take a parameter to specify which Bell state to create.

```python
def create_bell_state(state_type):
    """
    Create a Bell state circuit.
    
    Parameters:
        state_type: One of 'phi_plus', 'phi_minus', 'psi_plus', 'psi_minus'
    
    Returns:
        QuantumCircuit: The circuit that creates the specified Bell state
    """
    # Your code here
    pass
```

### Part 2: Measure and Analyze

Run each Bell state circuit 1000 times and collect the measurement results. Answer:
1. What outcomes do you observe for each state?
2. Are there any outcomes you never see? Why?
3. What is the correlation between the two qubits?

### Part 3: Visualization (Bonus)

Create a visualization showing:
1. The circuit for each Bell state
2. A histogram of measurement results
3. The state vector on a Q-sphere or similar visualization

## Expected Output

For Part 1, your circuits should look something like:
```
|Φ⁺⟩:      ┌───┐     
     q_0: ─┤ H ├──■──
           └───┘┌─┴─┐
     q_1: ─────┤ X ├─
                └───┘
```

For Part 2, you should observe:
- |Φ⁺⟩ and |Φ⁻⟩: Only 00 and 11 outcomes
- |Ψ⁺⟩ and |Ψ⁻⟩: Only 01 and 10 outcomes

## Hints

<details>
<summary>Hint 1: Creating |Φ⁺⟩</summary>
Start with both qubits in |0⟩. Apply Hadamard to the first qubit, then CNOT with first as control and second as target.
</details>

<details>
<summary>Hint 2: Creating other states from |Φ⁺⟩</summary>
You can create other Bell states by applying X or Z gates after creating |Φ⁺⟩.
</details>

<details>
<summary>Hint 3: Understanding results</summary>
In entangled states, both qubits always have the same (or opposite) values when measured.
</details>

## Resources

- [Our Bell State Example](../../examples/bell_state.py)
- [Notebook: Multi-Qubit Gates](../../notebooks/03_multi_qubit_gates.ipynb)
- [Qiskit Textbook - Entanglement](https://github.com/Qiskit/textbook)

## Submission Guidelines

1. Complete your solution in a Jupyter notebook or Python script
2. Include comments explaining your code
3. Document your observations and answers to the questions
4. Submit via pull request to the `collaboration/challenges/submissions/week-001/` folder
5. Deadline: End of the week

## Discussion Questions

1. Why can't we describe an entangled qubit independently of its partner?
2. If Alice and Bob share a Bell pair and are separated by a large distance, does measuring one instantly affect the other?
3. How might Bell states be useful in real-world applications?

---

## Solution

*(Will be posted after the submission deadline)*

Good luck and have fun exploring quantum entanglement! 🚀
