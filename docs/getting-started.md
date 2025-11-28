# Getting Started with Quantum Computing

Welcome to your quantum computing journey! This guide will help you get started with the basics.

## Prerequisites

Before diving into quantum computing, you should have:

- **Basic Python knowledge** - Familiarity with Python programming
- **Linear algebra fundamentals** - Understanding of vectors, matrices, and basic operations
- **Basic probability concepts** - Understanding of probability distributions

## Setting Up Your Environment

### 1. Install Python

We recommend Python 3.9 or later. You can download it from [python.org](https://www.python.org/downloads/).

### 2. Create a Virtual Environment

```bash
python -m venv quantum-env
source quantum-env/bin/activate  # On Windows: quantum-env\Scripts\activate
```

### 3. Choose Your Quantum Framework

We support three major quantum computing frameworks:

| Framework | Best For | Installation |
|-----------|----------|--------------|
| [Qiskit](setup-guides/qiskit-setup.md) | IBM Quantum access, comprehensive tools | `pip install qiskit` |
| [Cirq](setup-guides/cirq-setup.md) | Google Quantum access, research focus | `pip install cirq` |
| [PennyLane](setup-guides/pennylane-setup.md) | Quantum ML, hardware agnostic | `pip install pennylane` |

## Your First Quantum Circuit

Here's a simple example using Qiskit to create a quantum circuit:

```python
from qiskit import QuantumCircuit
from qiskit.primitives import Sampler

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Apply Hadamard gate to first qubit
qc.h(0)

# Apply CNOT gate
qc.cx(0, 1)

# Add measurements
qc.measure_all()

# Run the circuit
sampler = Sampler()
result = sampler.run(qc, shots=1000).result()
print(result)
```

This creates a Bell state, demonstrating quantum entanglement!

## Next Steps

1. **Explore the [Notebooks](../notebooks/)** - Hands-on learning materials
2. **Read the [Glossary](glossary.md)** - Understand quantum terminology
3. **Check the [Roadmaps](../roadmaps/)** - Follow structured learning paths
4. **Join [Collaboration](../collaboration/)** - Connect with fellow learners

## Resources

- [IBM Quantum Learning](https://learning.quantum.ibm.com/)
- [Qiskit Textbook](https://github.com/Qiskit/textbook)
- [Google Cirq Tutorials](https://quantumai.google/cirq/start)
- [PennyLane Demos](https://pennylane.ai/qml/demos)
