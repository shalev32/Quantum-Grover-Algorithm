# Quick Start Guide - HW4 Quantum Computing

## TL;DR - Fast Setup

### 1. Install Dependencies (2 minutes)
```bash
cd c:\CS\year_D\QC\HW4
pip install -r requirements.txt
```

### 2. Set Up IBM Quantum Token (1 minute)
```bash
python setup_ibm.py
```
Enter your IBM Quantum API token when prompted.

### 3. Run Notebooks (30-60 minutes total)
```bash
jupyter notebook
```

Then:
1. Open and run **hw4_task1_ghz.ipynb** (run all cells)
2. Open and run **hw4_task2_grover.ipynb** (run all cells)

Wait for QPU jobs to complete (they'll be queued on IBM's quantum computers).

### 4. Submit
Once both notebooks show output, create a ZIP with:
- `hw4_task1_ghz.ipynb`
- `hw4_task2_grover.ipynb`

Done! 🎉

---

## What You're Submitting

### Task 1: GHZ State (hw4_task1_ghz.ipynb)
- 15-qubit GHZ circuit
- Simulator results
- Real QPU results
- Comparison and analysis

### Task 2: Grover's Algorithm (hw4_task2_grover.ipynb)
- Built-in Grover (3 & 4 qubits)
- **Custom Grover operator** using elementary gates ⭐
- QPU execution
- Scaling experiments (finding max qubits)
- Detailed analysis

---

## Important Notes

**⏱️ Timing**: QPU jobs can take 5-15 minutes each due to queue. Plan accordingly!

**💡 Simulator Only**: If you prefer not to use your quantum time, you can run everything on the simulator. Just skip the QPU cells in the notebooks.

**🔑 Token Storage**: The `setup_ibm.py` script only needs to be run once. Your token is saved locally.

**📊 Expected Success Rates**:
- Simulator: 80-95% (high)
- Real QPU: 30-60% (lower due to noise)

This is normal and demonstrates NISQ limitations!

---

## Troubleshooting

**"ModuleNotFoundError"** → Run `pip install -r requirements.txt`

**"No IBM Quantum token"** → Run `python setup_ibm.py`

**QPU job taking forever** → Wait up to 15 min, or check IBM Quantum dashboard

**Notebook won't open** → Run `jupyter notebook` from the HW4 directory

---

## What Makes Your Implementation Stand Out

✅ Custom Grover operator implementation from scratch

✅ Uses only H, X, and multi-controlled gates (no black boxes)

✅ Comprehensive scaling experiments

✅ Real quantum hardware execution

✅ Professional analysis comparing simulator vs. QPU

✅ Clean, well-documented code

---

For detailed information, see [README.md](README.md) or [walkthrough.md](file:///C:/Users/User/.gemini/antigravity/brain/494aa568-877d-456c-a935-5eb23acb5619/walkthrough.md).

**Good luck! 🚀**
