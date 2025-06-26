"""Digital filter design using scipy."""
import numpy as np
from scipy import signal as sig

class FilterDesigner:
    def __init__(self, sample_rate=44100):
        self.fs = sample_rate
        self.nyquist = sample_rate / 2

    def butterworth(self, cutoff, order=5, btype="low"):
        wn = np.array(cutoff) / self.nyquist
        b, a = sig.butter(order, wn, btype=btype)
        return b, a

    def chebyshev1(self, cutoff, order=4, ripple=1, btype="low"):
        wn = np.array(cutoff) / self.nyquist
        b, a = sig.cheby1(order, ripple, wn, btype=btype)
        return b, a

    def chebyshev2(self, cutoff, order=4, attenuation=40, btype="low"):
        wn = np.array(cutoff) / self.nyquist
        b, a = sig.cheby2(order, attenuation, wn, btype=btype)
        return b, a

    def elliptic(self, cutoff, order=4, ripple=1, attenuation=40, btype="low"):
        wn = np.array(cutoff) / self.nyquist
        b, a = sig.ellip(order, ripple, attenuation, wn, btype=btype)
        return b, a

    def notch(self, freq, quality=30):
        wn = freq / self.nyquist
        b, a = sig.iirnotch(wn, quality)
        return b, a

    def fir_filter(self, cutoff, num_taps=101, window="hamming", btype="lowpass"):
        if btype in ["bandpass", "bandstop"]:
            wn = [c / self.nyquist for c in cutoff]
        else:
            wn = cutoff / self.nyquist
        coeffs = sig.firwin(num_taps, wn, window=window, pass_zero=(btype in ["lowpass", "bandstop"]))
        return coeffs, [1.0]

    def frequency_response(self, b, a, n_points=1024):
        w, h = sig.freqz(b, a, worN=n_points, fs=self.fs)
        magnitude_db = 20 * np.log10(np.abs(h) + 1e-10)
        phase_rad = np.angle(h)
        return w, magnitude_db, phase_rad

    def group_delay(self, b, a, n_points=1024):
        w, gd = sig.group_delay((b, a), w=n_points, fs=self.fs)
        return w, gd
