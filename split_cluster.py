# split_cluster.py
from flitsr.advanced.cluster import Cluster
from flitsr.spectrumBuilder import SpectrumBuilder
from flitsr.spectrum import Outcome

class SplitByFailingCluster(Cluster):
    """
    Cluster that splits a Spectrum into sub-spectra.
    Each sub-spectrum contains all passing tests + exactly one failing test.
    """

    def cluster(self, spectrum, **kwargs):
        results = []
        passes = [t for t in spectrum.tests() if t.outcome == Outcome.PASS]
        fails = spectrum.failing()
        elems = spectrum.elements()

        for f in fails:
            sb = SpectrumBuilder()

            # Map tests: add all passing tests + the current failing test
            test_map = {}
            for t in passes + [f]:
                test_map[t] = sb.addTest(t.name, t.outcome)

            # Map elements
            elem_map = {}
            for e in elems:
                elem_map[e] = sb.addElement((str(e),), e.faults)

            # Copy executions
            for t in passes + [f]:
                for e in spectrum.get_executed_elements(t):
                    sb.addExecution(test_map[t], elem_map[e])

            # Save the sub-spectrum
            results.append(sb.get_spectrum())

        return results
