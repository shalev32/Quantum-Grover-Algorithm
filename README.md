# Quantum Computing HW4 🌌

> **Implementing Quantum Algorithms on Real IBM Quantum Hardware**

[![Qiskit](https://img.shields.io/badge/Qiskit-2.0+-6929C4?style=flat&logo=qiskit)](https://qiskit.org/)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat&logo=jupyter)](https://jupyter.org/)
[![IBM Quantum](https://img.shields.io/badge/IBM-Quantum-1F70C1?style=flat)](https://quantum.ibm.com/)

Comprehensive implementation and analysis of quantum algorithms using IBM Qiskit, featuring both ideal simulator results and **real quantum hardware execution** on IBM's 156-qubit quantum processors.

## 🎯 Overview

This repository contains two major quantum computing assignments:

| **Task** | **Algorithm** | **Qubits** | **Highlights** |
|----------|--------------|------------|----------------|
| **Task 1** | GHZ State | 15 qubits | Quantum entanglement demonstration |
| **Task 2** | Grover's Algorithm | 3-6 qubits | **Custom operator from scratch** + NISQ analysis |

### 🌟 Key Achievements

✅ **Custom Grover's Algorithm** - Built from elementary gates (H, X, MCX) without black boxes  
✅ **Real QPU Execution** - Tested on IBM's 156-qubit quantum hardware  
✅ **NISQ Cliff Analysis** - Demonstrated exponential error growth in real quantum computers  
✅ **Comprehensive Scaling** - Tested from 3 to 20 qubits (simulator) and 3-6 qubits (QPU)  
✅ **Publication-Quality Results** - Detailed analysis with visualizations

---

## 📊 Results Highlights

### Task 1: GHZ State (15 Qubits)
**Ideal Result**: 50% `000...000` and 50% `111...111`

| Platform | `000...000` | `111...111` | Other States |
|----------|-------------|-------------|--------------|
| **Simulator** | 49.5% | 50.5% | 0% ✅ |
| **IBM QPU** | 21.3% | 18.4% | 60.3% (noise) ⚠️ |

> **Key Insight**: Real quantum hardware shows significant decoherence, demonstrating NISQ-era limitations.

---

### Task 2: Grover's Algorithm Performance

#### Simulator Results (Perfect)
- **3 qubits**: 94% success finding "011" 
- **4 qubits**: 96% success finding "0011"
- **Scales to 20+ qubits** with >94% accuracy

#### Real QPU Results (The "NISQ Cliff")

| Qubits | Success Rate | vs Random | Circuit Depth | Status |
|--------|--------------|-----------|---------------|---------|
| **3** | **~79%** | 25x better | 144 gates | ✅ Excellent |
| **4** | **15-65%*** | 2-10x better | 441 gates | ✅ Variable |
| **5** | **~7%** | 2x better | 1433 gates | ⚠️ Poor |
| **6** | **~2%** | ~Random | 5142 gates | ❌ Failed |

**Note**: The 4-qubit result shows 15-65% range across runs, demonstrating **temporal quantum noise** - a key characteristic of current quantum hardware.

> **The NISQ Cliff**: Performance drops exponentially after 4 qubits due to gate errors (~1% per gate) accumulating across hundreds of operations.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- IBM Quantum account (free tier available)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/QC-HW4.git
cd QC-HW4

# Install dependencies
pip install -r requirements.txt

# Set up IBM Quantum credentials
python setup_ibm.py
```

### Run the Notebooks

```bash
jupyter notebook
```

Then open and run:
1. `hw4_task1_ghz.ipynb` - GHZ State Implementation
2. `hw4_task2_grover.ipynb` - Grover's Algorithm (Custom + Built-in)

See [QUICKSTART.md](QUICKSTART.md) for detailed instructions.

---

## 📁 Project Structure

```
HW4/
├── hw4_task1_ghz.ipynb         # Task 1: GHZ state (15 qubits)
├── hw4_task2_grover.ipynb      # Task 2: Grover's algorithm
├── requirements.txt             # Python dependencies
├── setup_ibm.py                # IBM Quantum setup helper
├── README.md                   # This file
└── QUICKSTART.md               # Fast setup guide
```

---

## 🔬 Technical Deep Dive

### Task 1: GHZ State

**GHZ (Greenberger-Horne-Zeilinger) states** are maximally entangled quantum states:

```
|GHZ⟩ = (|000...0⟩ + |111...1⟩) / √2
```

**Implementation**:
1. Apply Hadamard to qubit 0
2. Apply CNOT cascade (0→1, 1→2, ..., 14→15)
3. Measure all qubits

**Result**: Only two outcomes possible in ideal case!

---

### Task 2: Grover's Algorithm

**Grover's Algorithm** provides quadratic speedup for unstructured search:
- **Classical**: O(N) time to search N items
- **Quantum**: O(√N) time

#### Custom Implementation Highlights

We built the **complete Grover operator from scratch**:

```python
def custom_grover_operator(oracle):
    # 1. Apply Oracle (marks target state)
    qc.compose(oracle)
    
    # 2. Diffusion Operator (amplifies marked state)
    qc.h(range(n))          # Hadamard all qubits
    qc.x(range(n))          # X all qubits
    # Multi-controlled Z using H-MCX-H sandwich
    qc.h(n-1)
    qc.mcx(range(n-1), n-1)
    qc.h(n-1)
    qc.x(range(n))          # X all qubits
    qc.h(range(n))          # Hadamard all qubits
```

**Optimal Iterations**: π/4 × √(2^n) ≈ 2 (for 3 qubits), 3 (for 4 qubits)

---

## 📈 Scaling Analysis

### Simulator Limits
- **Memory bound**: ~20-25 qubits on typical hardware
- **Success rate**: Maintains >94% across all tested sizes
- **Time complexity**: Exponential growth (2^n states)

### QPU Limits (The NISQ Reality)
- **Noise bound**: Viable up to 3-4 qubits for Grover's algorithm
- **Error accumulation**: With 99% gate fidelity:
  - 100 gates → 37% final accuracy
  - 400 gates → 2% final accuracy
- **Future**: Requires quantum error correction for practical advantage

---

## 🎓 Key Learnings

### ✅ What Worked
- **Algorithms are correct**: Both implementations match theory perfectly
- **Quantum quadratic speedup**: Clearly observable in simulator
- **Custom operator**: Successfully validated against Qiskit's built-in

### ⚠️ Current Limitations
- **Gate errors**: ~1% error rate per gate on current hardware
- **Decoherence**: Qubits lose information over time
- **Circuit depth**: Deeper circuits → more errors exponentially
- **Temporal noise**: Results vary significantly between runs

### 🔮 Future Directions
Current quantum computers are in the **NISQ** (Noisy Intermediate-Scale Quantum) era. For practical quantum advantage:
- **Quantum Error Correction** is essential
- **Better qubit coherence times** needed
- **Lower gate error rates** (<0.1%) required

---

## 📚 References

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [IBM Quantum Experience](https://quantum.ibm.com/)
- [Grover's Algorithm](https://en.wikipedia.org/wiki/Grover%27s_algorithm)
- [GHZ State](https://en.wikipedia.org/wiki/Greenberger%E2%80%93Horne%E2%80%93Zeilinger_state)

---

## 👤 Author

**Shalev Ohayon**
- GitHub: [@Shalev Ohayon](https://github.com/shalev32)
- Course: Quantum Computing
- Assignment: HW4 - Quantum Programming with IBM Qiskit

---

<div align="center">

**Made with ⚛️ using IBM Qiskit**

[⬆ back to top](#quantum-computing-hw4-)

</div>
