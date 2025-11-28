# Intermediate Roadmap

A 12-week journey to deepen your quantum computing knowledge!

## Prerequisites

- Completed the [Beginner Roadmap](beginner.md) or equivalent
- Comfortable with basic quantum circuits
- Familiar with Python and NumPy

## Week 1-2: Advanced Gates and Circuits

### Topics
- [ ] Controlled gates (CZ, CCX, etc.)
- [ ] Universal gate sets
- [ ] Circuit optimization
- [ ] Parametrized circuits

### Resources
- [Qiskit Circuit Library](https://docs.quantum.ibm.com/api/qiskit/circuit_library)
- [Nielsen & Chuang - Chapter 4](https://www.cambridge.org/highereducation/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE)

### Practice
- Implement universal gate decompositions
- Optimize circuits for depth
- Build parametrized quantum circuits

---

## Week 3-4: Quantum Algorithms I

### Topics
- [ ] Grover's search algorithm
- [ ] Amplitude amplification
- [ ] Oracle construction techniques
- [ ] Complexity analysis

### Resources
- [IBM Quantum Learning - Grover's Algorithm](https://learning.quantum.ibm.com/)
- [Qiskit Textbook - Grover's Algorithm](https://github.com/Qiskit/textbook)

### Practice
- Implement Grover's algorithm for N=4, 8
- Create custom oracles
- Analyze the quadratic speedup

---

## Week 5-6: Quantum Algorithms II

### Topics
- [ ] Quantum Fourier Transform (QFT)
- [ ] Quantum Phase Estimation
- [ ] Introduction to Shor's algorithm
- [ ] Modular arithmetic for quantum

### Resources
- [Qiskit Textbook - QFT](https://github.com/Qiskit/textbook)
- [IBM Quantum Learning](https://learning.quantum.ibm.com/)

### Practice
- Implement QFT for various sizes
- Build phase estimation circuits
- Understand the period-finding subroutine

---

## Week 7-8: Quantum Protocols

### Topics
- [ ] Quantum teleportation
- [ ] Superdense coding
- [ ] Quantum key distribution (BB84)
- [ ] No-cloning theorem applications

### Resources
- [Qiskit Textbook - Protocols](https://github.com/Qiskit/textbook)
- Research papers on quantum protocols

### Practice
- Implement teleportation protocol
- Implement superdense coding
- Simulate BB84 key exchange

---

## Week 9-10: Noise and Error Mitigation

### Topics
- [ ] Types of quantum noise
- [ ] Noise models in simulators
- [ ] Error mitigation techniques
- [ ] Introduction to quantum error correction

### Resources
- [Qiskit Aer Noise Module](https://docs.quantum.ibm.com/api/qiskit/aer)
- [IBM Quantum Learning - Error Mitigation](https://learning.quantum.ibm.com/)

### Practice
- Simulate noisy circuits
- Apply error mitigation techniques
- Compare ideal vs noisy results

---

## Week 11-12: Variational Algorithms

### Topics
- [ ] Variational Quantum Eigensolver (VQE)
- [ ] QAOA (Quantum Approximate Optimization)
- [ ] Ansatz design
- [ ] Classical optimizers

### Resources
- [Qiskit Algorithms Module](https://qiskit-community.github.io/qiskit-algorithms/)
- [PennyLane VQE Tutorials](https://pennylane.ai/qml/demos/tutorial_vqe)

### Practice
- Implement VQE for small molecules
- Apply QAOA to optimization problems
- Experiment with different ansatz designs

---

## Milestones Checklist

- [ ] Implement Grover's algorithm
- [ ] Build QFT and phase estimation circuits
- [ ] Complete quantum teleportation
- [ ] Run circuits with noise models
- [ ] Implement a variational algorithm
- [ ] Contribute to an open-source quantum project

## Projects to Attempt

1. **Quantum Game**: Build a quantum version of a classic game
2. **Chemistry Simulation**: Use VQE to find molecular ground states
3. **Optimization**: Solve a real optimization problem with QAOA
4. **Cryptography**: Implement a quantum key distribution protocol

## Next Steps

After completing this roadmap:
1. Move to the [Advanced Roadmap](advanced.md)
2. Start a major project
3. Consider contributing to Qiskit or other frameworks
4. Explore quantum hardware specifics
