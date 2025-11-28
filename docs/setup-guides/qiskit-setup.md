# Qiskit Setup Guide

[Qiskit](https://qiskit.org/) is IBM's open-source SDK for working with quantum computers. It provides tools for creating and manipulating quantum programs and running them on prototype quantum devices on IBM Quantum or on simulators.

## Prerequisites

- Python 3.9 or later
- pip package manager
- A virtual environment (recommended)

## Installation

### Step 1: Create a Virtual Environment

```bash
python -m venv qiskit-env
source qiskit-env/bin/activate  # On Windows: qiskit-env\Scripts\activate
```

### Step 2: Install Qiskit

```bash
pip install qiskit
```

### Step 3: Install Visualization Tools (Optional but Recommended)

```bash
pip install qiskit[visualization]
```

### Step 4: Install Additional Components

For working with real quantum hardware:
```bash
pip install qiskit-ibm-runtime
```

For machine learning applications:
```bash
pip install qiskit-machine-learning
```

For nature/chemistry simulations:
```bash
pip install qiskit-nature
```

## Verify Installation

Run this Python script to verify your installation:

```python
import qiskit
print(f"Qiskit version: {qiskit.__version__}")

from qiskit import QuantumCircuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
print("Circuit created successfully!")
print(qc.draw())
```

Expected output:
```
Qiskit version: 1.x.x
Circuit created successfully!
     ┌───┐     
q_0: ┤ H ├──■──
     └───┘┌─┴─┐
q_1: ─────┤ X ├
          └───┘
```

## Setting Up IBM Quantum Account

1. Create a free account at [IBM Quantum](https://quantum.ibm.com/)
2. Get your API token from the IBM Quantum dashboard
3. Save your credentials:

```python
from qiskit_ibm_runtime import QiskitRuntimeService

# Save account (only need to do this once)
QiskitRuntimeService.save_account(
    channel="ibm_quantum",
    token="YOUR_API_TOKEN",
    overwrite=True
)
```

## Your First Quantum Program

```python
from qiskit import QuantumCircuit
from qiskit.primitives import Sampler
from qiskit.visualization import plot_histogram

# Create a Bell state circuit
qc = QuantumCircuit(2)
qc.h(0)          # Hadamard on qubit 0
qc.cx(0, 1)      # CNOT with control=0, target=1
qc.measure_all() # Measure all qubits

# Visualize the circuit
print(qc.draw())

# Run the circuit on a simulator
sampler = Sampler()
result = sampler.run(qc, shots=1000).result()

# Display results
print(result)
```

## Common Issues and Solutions

### Issue: ImportError for visualization
**Solution:** Install matplotlib: `pip install matplotlib`

### Issue: Jupyter notebook not showing circuits
**Solution:** Install ipywidgets: `pip install ipywidgets`

### Issue: API token not found
**Solution:** Ensure you've saved your credentials and restart Python

## Resources

- [Qiskit Documentation](https://docs.quantum.ibm.com/)
- [Qiskit Textbook](https://github.com/Qiskit/textbook)
- [IBM Quantum Learning](https://learning.quantum.ibm.com/)
- [Qiskit Community Tutorials](https://github.com/qiskit-community/qiskit-community-tutorials)
