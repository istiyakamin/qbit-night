# Quantum Q Bit Night 🌙⚛️

> *Demystifying the quantum realm, one qubit at a time*

**Quantum Q Bit Night** is a dedicated student initiative where we demystify the quantum realm. It's more than a club—it's a collaborative workspace where students from all disciplines come together to learn quantum computing concepts, experiment with quantum circuits, and prepare for the future of information technology.

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

---

## 🎯 Our Mission

We aim to:
- **Democratize** quantum computing education for students of all backgrounds
- **Build** a supportive community of learners and practitioners
- **Create** hands-on learning resources and projects
- **Prepare** the next generation of quantum computing professionals
- **Bridge** the gap between theoretical concepts and practical applications

---

## 📁 Repository Structure

```
qbit-night/
├── docs/                    # Documentation and guides
│   ├── getting-started.md   # Quick start guide
│   ├── glossary.md          # Quantum computing terminology
│   └── setup-guides/        # Framework installation guides
│       ├── qiskit-setup.md
│       ├── cirq-setup.md
│       └── pennylane-setup.md
├── notebooks/               # Interactive Jupyter notebooks
│   ├── 01_quantum_basics.ipynb
│   ├── 02_single_qubit_gates.ipynb
│   └── 03_multi_qubit_gates.ipynb
├── examples/                # Example quantum programs
│   ├── hello_quantum.py
│   ├── bell_state.py
│   └── quantum_random.py
├── projects/                # Community projects
├── resources/               # Curated learning resources
├── roadmaps/                # Structured learning paths
│   ├── beginner.md
│   ├── intermediate.md
│   └── advanced.md
└── collaboration/           # Community collaboration space
    ├── challenges/          # Weekly learning challenges
    └── templates/           # Project and meeting templates
```

---

## 🚀 Quick Start

### 1. Choose Your Framework

We support three major quantum computing frameworks:

| Framework | Best For | Documentation |
|-----------|----------|---------------|
| [Qiskit](docs/setup-guides/qiskit-setup.md) | IBM Quantum access, comprehensive tools | [Official Docs](https://docs.quantum.ibm.com/) |
| [Cirq](docs/setup-guides/cirq-setup.md) | Google Quantum access, research focus | [Official Docs](https://quantumai.google/cirq) |
| [PennyLane](docs/setup-guides/pennylane-setup.md) | Quantum ML, hardware agnostic | [Official Docs](https://pennylane.ai/) |

### 2. Set Up Your Environment

```bash
# Create a virtual environment
python -m venv quantum-env
source quantum-env/bin/activate  # On Windows: quantum-env\Scripts\activate

# Install your chosen framework
pip install qiskit  # or cirq, pennylane
```

### 3. Run Your First Quantum Program

```python
from qiskit import QuantumCircuit
from qiskit.primitives import Sampler

# Create a quantum circuit
qc = QuantumCircuit(1, 1)
qc.h(0)          # Put qubit in superposition
qc.measure(0, 0) # Measure the qubit

# Run the circuit
sampler = Sampler()
result = sampler.run(qc, shots=1000).result()
print(result)
```

For more details, see our [Getting Started Guide](docs/getting-started.md).

---

## 📚 Learning Roadmap

Choose your path based on your experience level:

### 🌱 [Beginner](roadmaps/beginner.md) (12 weeks)
- Quantum computing fundamentals
- Qubits and superposition
- Single and multi-qubit gates
- First quantum algorithms

### 🌿 [Intermediate](roadmaps/intermediate.md) (12 weeks)
- Grover's and Shor's algorithms
- Quantum protocols (teleportation, QKD)
- Noise and error mitigation
- Variational algorithms (VQE, QAOA)

### 🌳 [Advanced](roadmaps/advanced.md) (12 weeks)
- Quantum error correction
- Quantum simulation
- Quantum machine learning
- Research frontiers

---

## 📓 Notebooks and Examples

### Interactive Notebooks
1. [Quantum Basics](notebooks/01_quantum_basics.ipynb) - Your first quantum concepts
2. [Single-Qubit Gates](notebooks/02_single_qubit_gates.ipynb) - Pauli, Hadamard, and rotation gates
3. [Multi-Qubit Gates](notebooks/03_multi_qubit_gates.ipynb) - CNOT, entanglement, Bell states

### Example Programs
- [hello_quantum.py](examples/hello_quantum.py) - Your first quantum program
- [bell_state.py](examples/bell_state.py) - Creating quantum entanglement
- [quantum_random.py](examples/quantum_random.py) - True random number generation

---

## 📖 Glossary

New to quantum computing? Check out our [comprehensive glossary](docs/glossary.md) covering:
- Qubits and superposition
- Quantum gates and circuits
- Entanglement and measurement
- Quantum algorithms
- And much more!

---

## 🤝 Contributing

We welcome contributions from everyone! Here's how you can help:

### Ways to Contribute
- 📝 **Documentation**: Improve guides, fix typos, add examples
- 💻 **Code**: Add notebooks, examples, or projects
- 🎯 **Challenges**: Create weekly learning challenges
- 🐛 **Issues**: Report bugs or suggest improvements
- 💬 **Community**: Answer questions, review PRs

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature`
3. **Make** your changes with clear commit messages
4. **Test** your changes thoroughly
5. **Submit** a pull request

### Code Style
- Follow PEP 8 for Python code
- Include docstrings and comments
- Test code before submitting
- Keep notebooks clean and well-documented

### First Time Contributors
Look for issues labeled `good first issue` or `help wanted` to get started!

---

## 📅 Weekly Challenges

Join our weekly learning challenges in the [collaboration/challenges](collaboration/challenges/) folder!

**Current Challenge**: [Bell State Explorer](collaboration/challenges/week-001-bell-state-explorer.md)

Each week features:
- A new quantum computing problem
- Multiple difficulty levels
- Community discussion
- Solution walkthroughs

---

## 🔗 Resources

Find curated learning resources in our [resources folder](resources/):
- Official documentation links
- Recommended textbooks
- Video courses and tutorials
- Research papers
- Community forums

---

## 📜 License

This project is released under the [CC0 1.0 Universal](LICENSE) license. You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

---

## 🌟 Acknowledgments

- IBM Quantum and the Qiskit community
- Google Quantum AI and the Cirq team
- Xanadu and the PennyLane team
- All our amazing contributors and learners

---

## 📞 Connect With Us

- **GitHub Issues**: For questions and discussions
- **Pull Requests**: For contributions
- **Community**: Join our collaboration space

---

<p align="center">
  <b>Start your quantum journey today!</b><br>
  <i>The future of computing is quantum. Be part of it.</i>
</p>
