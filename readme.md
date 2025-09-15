# Localization of Multiple Faults using Spectral Clustering

**Student:** Ashleys Jane  

---

## Objective

Split a spectrum into sub-spectra, each containing:

- All passing tests  
- Exactly one failing test  

Using FLITSR (`SpectrumBuilder` and `Spectrum`).

---

## Steps Completed

1. Built a demo spectrum with passing and failing tests.  
2. Implemented `split_spectrum_by_failing(S)` to create sub-spectra.  
3. Verified outputs: sub-spectra include all passing tests + one failing test.

---

## How to Test

1. Install Python 3 and FLITSR.  
2. Run the demo script:

```bash
python split_spectrum_simple.py
