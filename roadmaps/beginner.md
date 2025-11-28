# Beginner Roadmap

A 12-week journey from zero to quantum-comfortable!

## Prerequisites

- Basic Python programming
- High school mathematics
- Curiosity and enthusiasm!

## Week 1-2: Foundations

### Topics
- [ ] What is quantum computing?
- [ ] Classical vs quantum computing
- [ ] Bits vs qubits
- [ ] Introduction to linear algebra basics

### Resources
- [IBM Quantum Learning - Basics of Quantum Information](https://learning.quantum.ibm.com/course/basics-of-quantum-information)
- [3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

### Practice
- Set up your Python environment
- Install Qiskit: `pip install qiskit`
- Run the `hello_quantum.py` example

---

## Week 3-4: Qubits and States

### Topics
- [ ] Qubit states (|0⟩, |1⟩)
- [ ] Superposition
- [ ] Dirac notation basics
- [ ] The Bloch sphere

### Resources
- [Our notebook: 01_quantum_basics.ipynb](../notebooks/01_quantum_basics.ipynb)
- [Qiskit Textbook - Single Qubit States](https://github.com/Qiskit/textbook)

### Practice
- Visualize qubit states on the Bloch sphere
- Create superposition states
- Experiment with measurement

---

## Week 5-6: Single-Qubit Gates

### Topics
- [ ] Pauli gates (X, Y, Z)
- [ ] Hadamard gate
- [ ] Phase gates (S, T)
- [ ] Rotation gates (Rx, Ry, Rz)

### Resources
- [Our notebook: 02_single_qubit_gates.ipynb](../notebooks/02_single_qubit_gates.ipynb)
- [Qiskit Textbook - Single Qubit Gates](https://github.com/Qiskit/textbook)

### Practice
- Implement all single-qubit gates
- Understand gate matrices
- Verify gate identities (e.g., HXH = Z)

---

## Week 7-8: Multi-Qubit Systems

### Topics
- [ ] Tensor products
- [ ] Multi-qubit states
- [ ] CNOT gate
- [ ] Quantum entanglement

### Resources
- [Our notebook: 03_multi_qubit_gates.ipynb](../notebooks/03_multi_qubit_gates.ipynb)
- [Our example: bell_state.py](../examples/bell_state.py)

### Practice
- Create Bell states
- Verify entanglement through measurement
- Implement SWAP using CNOTs

---

## Week 9-10: Quantum Circuits

### Topics
- [ ] Building quantum circuits
- [ ] Circuit depth and width
- [ ] Measurement and classical bits
- [ ] Running on simulators

### Resources
- [Qiskit Circuits Documentation](https://docs.quantum.ibm.com/api/qiskit/circuit)
- Practice with all example scripts

### Practice
- Build circuits of increasing complexity
- Analyze circuit properties
- Compare simulator results

---

## Week 11-12: First Algorithms

### Topics
- [ ] Deutsch-Jozsa algorithm
- [ ] Bernstein-Vazirani algorithm
- [ ] Introduction to oracles
- [ ] Quantum parallelism

### Resources
- [Qiskit Textbook - Quantum Algorithms](https://github.com/Qiskit/textbook)
- [IBM Quantum Learning](https://learning.quantum.ibm.com/)

### Practice
- Implement Deutsch-Jozsa
- Understand oracle construction
- Compare quantum vs classical solutions

---

## Milestones Checklist

- [ ] Set up development environment
- [ ] Create and visualize qubit states
- [ ] Master single-qubit gates
- [ ] Create entangled states
- [ ] Build multi-qubit circuits
- [ ] Implement a simple quantum algorithm
- [ ] Run a circuit on a real quantum computer (IBM Quantum)

## Next Steps

After completing this roadmap:
1. Move to the [Intermediate Roadmap](intermediate.md)
2. Join our weekly learning challenges in [Collaboration](../collaboration/)
3. Start a project in the [Projects](../projects/) section

## Tips for Success

1. **Be patient**: Quantum concepts take time to internalize
2. **Practice daily**: Even 30 minutes of practice helps
3. **Ask questions**: Use our collaboration channels
4. **Don't memorize**: Focus on understanding concepts
5. **Have fun**: Quantum computing is fascinating!
