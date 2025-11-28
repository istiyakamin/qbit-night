# PennyLane Setup Guide

[PennyLane](https://pennylane.ai/) is a cross-platform Python library for differentiable programming of quantum computers. It's particularly powerful for quantum machine learning applications and is hardware-agnostic.

## Prerequisites

- Python 3.9 or later
- pip package manager
- A virtual environment (recommended)

## Installation

### Step 1: Create a Virtual Environment

```bash
python -m venv pennylane-env
source pennylane-env/bin/activate  # On Windows: pennylane-env\Scripts\activate
```

### Step 2: Install PennyLane

```bash
pip install pennylane
```

### Step 3: Install Plugin for Your Hardware (Optional)

For IBM Quantum:
```bash
pip install pennylane-qiskit
```

For Google Cirq:
```bash
pip install pennylane-cirq
```

For Amazon Braket:
```bash
pip install amazon-braket-pennylane-plugin
```

For Lightning (high-performance simulator):
```bash
pip install pennylane-lightning
```

## Verify Installation

Run this Python script to verify your installation:

```python
import pennylane as qml
print(f"PennyLane version: {qml.__version__}")

# Create a device
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.probs(wires=[0, 1])

result = circuit()
print("Circuit executed successfully!")
print(f"Probabilities: {result}")
```

Expected output:
```
PennyLane version: 0.x.x
Circuit executed successfully!
Probabilities: [0.5 0.  0.  0.5]
```

## Your First Quantum Program

```python
import pennylane as qml
from pennylane import numpy as np

# Create a quantum device (simulator)
dev = qml.device("default.qubit", wires=2)

# Define a quantum circuit as a QNode
@qml.qnode(dev)
def bell_state():
    qml.Hadamard(wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.probs(wires=[0, 1])

# Execute the circuit
probs = bell_state()
print("Bell State Probabilities:")
print(f"|00⟩: {probs[0]:.4f}")
print(f"|01⟩: {probs[1]:.4f}")
print(f"|10⟩: {probs[2]:.4f}")
print(f"|11⟩: {probs[3]:.4f}")

# Draw the circuit
print("\nCircuit Diagram:")
print(qml.draw(bell_state)())
```

## Key Concepts in PennyLane

### Devices

```python
# Default qubit simulator
dev = qml.device("default.qubit", wires=4)

# Lightning (fast C++ simulator)
dev = qml.device("lightning.qubit", wires=4)

# Mixed state simulator (for noise)
dev = qml.device("default.mixed", wires=4)

# Specific hardware (requires plugin)
dev = qml.device("qiskit.ibmq", wires=4, backend='ibmq_qasm_simulator')
```

### QNodes (Quantum Nodes)

```python
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def my_circuit(params):
    qml.RX(params[0], wires=0)
    qml.RY(params[1], wires=1)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0))

# Execute with parameters
result = my_circuit([0.5, 0.3])
```

### Gates and Operations

```python
# Single-qubit gates
qml.PauliX(wires=0)        # Pauli X
qml.PauliY(wires=0)        # Pauli Y
qml.PauliZ(wires=0)        # Pauli Z
qml.Hadamard(wires=0)      # Hadamard
qml.T(wires=0)             # T gate
qml.S(wires=0)             # S gate

# Rotation gates
qml.RX(theta, wires=0)     # X rotation
qml.RY(theta, wires=0)     # Y rotation
qml.RZ(theta, wires=0)     # Z rotation

# Two-qubit gates
qml.CNOT(wires=[0, 1])     # Controlled-NOT
qml.CZ(wires=[0, 1])       # Controlled-Z
qml.SWAP(wires=[0, 1])     # SWAP
```

### Measurements

```python
qml.expval(qml.PauliZ(0))      # Expectation value
qml.var(qml.PauliZ(0))         # Variance
qml.probs(wires=[0, 1])        # Probabilities
qml.sample(qml.PauliZ(0))      # Samples
qml.state()                     # Full state vector
```

## Quantum Machine Learning Example

```python
import pennylane as qml
from pennylane import numpy as np

# Create device
dev = qml.device("default.qubit", wires=2)

# Parameterized quantum circuit (variational)
@qml.qnode(dev)
def variational_circuit(params):
    qml.RX(params[0], wires=0)
    qml.RY(params[1], wires=0)
    qml.RX(params[2], wires=1)
    qml.RY(params[3], wires=1)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0))

# Cost function
def cost(params):
    return (variational_circuit(params) - 0.5) ** 2

# Initialize parameters
params = np.array([0.1, 0.2, 0.3, 0.4], requires_grad=True)

# Optimize
opt = qml.GradientDescentOptimizer(stepsize=0.4)

for i in range(100):
    params = opt.step(cost, params)
    if (i + 1) % 20 == 0:
        print(f"Step {i+1}: cost = {cost(params):.6f}")

print(f"Optimized result: {variational_circuit(params):.4f}")
```

## Common Issues and Solutions

### Issue: NumPy compatibility
**Solution:** Use PennyLane's NumPy: `from pennylane import numpy as np`

### Issue: Gradient computation errors
**Solution:** Ensure parameters have `requires_grad=True`

### Issue: Device not found
**Solution:** Install the appropriate plugin: `pip install pennylane-qiskit`

## Resources

- [PennyLane Documentation](https://pennylane.ai/qml/)
- [PennyLane Demos](https://pennylane.ai/qml/demos)
- [PennyLane GitHub](https://github.com/PennyLaneAI/pennylane)
- [Quantum Machine Learning Tutorials](https://pennylane.ai/qml/demonstrations)
