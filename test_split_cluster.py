# test_split_cluster.py
from flitsr.spectrum import Outcome
from flitsr.spectrumBuilder import SpectrumBuilder
from split_cluster import SplitByFailingCluster

# Build a demo spectrum
sb = SpectrumBuilder()
t1 = sb.addTest("t1", Outcome.PASS)
t2 = sb.addTest("t2", Outcome.FAIL)
t3 = sb.addTest("t3", Outcome.FAIL)
e1 = sb.addElement(("functionA",), faults=[])
e2 = sb.addElement(("functionB",), faults=[])
sb.addExecution(t1, e1)
sb.addExecution(t2, e1)
sb.addExecution(t2, e2)
sb.addExecution(t3, e2)
S = sb.get_spectrum()

# Run the cluster
clusterer = SplitByFailingCluster()
split_spectra = clusterer.cluster(S)

print("Original Spectrum tests:", [t.name for t in S.tests()])
for i, sub in enumerate(split_spectra):
    print(f"\n--- Sub-spectrum {i+1} ---")
    print("Tests:", [t.name for t in sub.tests()])
    print("Failing:", [t.name for t in sub.failing()])
    print("Elements:", [str(e) for e in sub.elements()])
    coverage, outcomes = sub.to_matrix()
    print("Coverage:\n", coverage)
    print("Outcomes:", outcomes)
