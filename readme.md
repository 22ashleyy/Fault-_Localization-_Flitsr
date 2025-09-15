# Localization of Multiple Faults using Spectral Clustering

**Student:** Ashleys Jane  
---

## Objective

Implement a method to split a spectrum into sub-spectra, where each sub-spectrum contains:

- All passing tests  
- Exactly one failing test  

Using the FLITSR framework (`SpectrumBuilder` and `Spectrum`).

---

## Steps Completed

### 1. Built a demo spectrum

```python
from flitsr.spectrum import Outcome
from flitsr.spectrumBuilder import SpectrumBuilder

sb = SpectrumBuilder()

# Add tests
t1 = sb.addTest("t1", Outcome.PASS)
t2 = sb.addTest("t2", Outcome.FAIL)
t3 = sb.addTest("t3", Outcome.FAIL)

# Add elements
e1 = sb.addElement(("functionA",), faults=[])
e2 = sb.addElement(("functionB",), faults=[])

# Record executions
sb.addExecution(t1, e1)
sb.addExecution(t2, e1)
sb.addExecution(t2, e2)
sb.addExecution(t3, e2)

S = sb.get_spectrum()
