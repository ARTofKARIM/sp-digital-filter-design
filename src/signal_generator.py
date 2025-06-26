"""Test signal generation for filter testing."""
import numpy as np

class SignalGenerator:
    def __init__(self, sample_rate=44100):
        self.fs = sample_rate

    def sine(self, freq, duration, amplitude=1.0):
        t = np.arange(0, duration, 1/self.fs)
        return t, amplitude * np.sin(2 * np.pi * freq * t)

    def multi_tone(self, freqs, duration, amplitudes=None):
        t = np.arange(0, duration, 1/self.fs)
        if amplitudes is None:
            amplitudes = [1.0] * len(freqs)
        signal = sum(a * np.sin(2 * np.pi * f * t) for f, a in zip(freqs, amplitudes))
        return t, signal

    def chirp(self, f0, f1, duration):
        t = np.arange(0, duration, 1/self.fs)
        return t, np.sin(2 * np.pi * (f0 * t + (f1 - f0) * t**2 / (2 * duration)))

    def white_noise(self, duration, amplitude=1.0):
        n_samples = int(duration * self.fs)
        t = np.arange(n_samples) / self.fs
        return t, amplitude * np.random.randn(n_samples)

    def noisy_signal(self, freq, duration, snr_db=20):
        t, clean = self.sine(freq, duration)
        noise_power = 10 ** (-snr_db / 10)
        noise = np.sqrt(noise_power) * np.random.randn(len(t))
        return t, clean + noise
