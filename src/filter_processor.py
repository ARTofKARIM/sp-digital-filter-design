"""Apply filters to signals."""
import numpy as np
from scipy import signal as sig

class FilterProcessor:
    def __init__(self, sample_rate=44100):
        self.fs = sample_rate

    def apply_filter(self, signal_data, b, a, method="filtfilt"):
        if method == "filtfilt":
            return sig.filtfilt(b, a, signal_data)
        elif method == "lfilter":
            return sig.lfilter(b, a, signal_data)
        else:
            raise ValueError(f"Unknown method: {method}")

    def apply_sos_filter(self, signal_data, sos):
        return sig.sosfilt(sos, signal_data)

    def compute_snr(self, original, filtered):
        noise = original - filtered
        signal_power = np.mean(original ** 2)
        noise_power = np.mean(noise ** 2) + 1e-10
        return 10 * np.log10(signal_power / noise_power)
