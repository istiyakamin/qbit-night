"""
Bell State Creation

This program demonstrates quantum entanglement by creating a Bell state.
A Bell state is a maximally entangled two-qubit state where the qubits
are perfectly correlated.

Usage:
    python bell_state.py

Requirements:
    pip install qiskit
"""

from qiskit import QuantumCircuit
from qiskit.primitives import Sampler
from qiskit.quantum_info import Statevector


def create_bell_state(state_type="phi_plus"):
    """
    Create one of the four Bell states.
    
    Parameters:
        state_type: One of 'phi_plus', 'phi_minus', 'psi_plus', 'psi_minus'
    
    Returns:
        QuantumCircuit: The circuit that creates the Bell state
    """
    qc = QuantumCircuit(2, 2)
    
    # Create the base Bell state |Φ+⟩
    qc.h(0)       # Put first qubit in superposition
    qc.cx(0, 1)   # Entangle with second qubit using CNOT
    
    # Modify based on which Bell state we want
    if state_type == "phi_minus":
        qc.z(0)   # |Φ-⟩ = (|00⟩ - |11⟩) / √2
    elif state_type == "psi_plus":
        qc.x(1)   # |Ψ+⟩ = (|01⟩ + |10⟩) / √2
    elif state_type == "psi_minus":
        qc.x(1)
        qc.z(0)   # |Ψ-⟩ = (|01⟩ - |10⟩) / √2
    # phi_plus is the default: |Φ+⟩ = (|00⟩ + |11⟩) / √2
    
    return qc


def analyze_bell_state():
    """Create a Bell state and analyze its properties."""
    
    print("Creating Bell State |Φ+⟩ = (|00⟩ + |11⟩) / √2")
    print("-" * 50)
    
    # Create the Bell state circuit
    qc = create_bell_state("phi_plus")
    
    # Show the circuit
    print("\nCircuit:")
    print(qc.draw())
    
    # Show the state vector (before measurement)
    state = Statevector.from_instruction(qc)
    print(f"\nState vector: {state}")
    
    # Add measurements and run
    qc.measure([0, 1], [0, 1])
    
    sampler = Sampler()
    job = sampler.run(qc, shots=1000)
    result = job.result()
    
    print("\nMeasurement results (1000 shots):")
    print(result)
    
    print("\n" + "=" * 50)
    print("KEY OBSERVATION:")
    print("=" * 50)
    print("Notice that we ONLY get '00' and '11' outcomes.")
    print("We NEVER see '01' or '10'.")
    print("")
    print("This is the signature of quantum entanglement!")
    print("When you measure one qubit, you instantly know")
    print("the state of the other, regardless of distance.")
    print("=" * 50)


def demonstrate_all_bell_states():
    """Show all four Bell states."""
    
    print("\n" + "=" * 50)
    print("ALL FOUR BELL STATES")
    print("=" * 50)
    
    states = {
        "phi_plus": "|Φ+⟩ = (|00⟩ + |11⟩) / √2",
        "phi_minus": "|Φ-⟩ = (|00⟩ - |11⟩) / √2",
        "psi_plus": "|Ψ+⟩ = (|01⟩ + |10⟩) / √2",
        "psi_minus": "|Ψ-⟩ = (|01⟩ - |10⟩) / √2"
    }
    
    for state_type, description in states.items():
        print(f"\n{description}")
        qc = create_bell_state(state_type)
        state = Statevector.from_instruction(qc)
        print(f"State vector: {state}")


if __name__ == "__main__":
    analyze_bell_state()
    demonstrate_all_bell_states()
