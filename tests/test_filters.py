"""Tests for digital filter design."""
import unittest
import numpy as np
from src.filter_design import FilterDesigner
from src.filter_processor import FilterProcessor
from src.signal_generator import SignalGenerator

class TestFilterDesign(unittest.TestCase):
    def setUp(self):
        self.designer = FilterDesigner(44100)

    def test_butterworth_lowpass(self):
        b, a = self.designer.butterworth(1000, order=5, btype="low")
        self.assertEqual(len(b), 6)

    def test_frequency_response(self):
        b, a = self.designer.butterworth(1000)
        w, mag, phase = self.designer.frequency_response(b, a)
        self.assertEqual(len(w), 1024)
        self.assertTrue(mag[0] > -1)  # passband

    def test_notch_filter(self):
        b, a = self.designer.notch(50, quality=30)
        w, mag, _ = self.designer.frequency_response(b, a)
        self.assertTrue(len(b) > 0)

class TestFilterProcessor(unittest.TestCase):
    def test_apply_filter(self):
        gen = SignalGenerator(44100)
        t, signal = gen.noisy_signal(440, 0.1, snr_db=10)
        designer = FilterDesigner(44100)
        b, a = designer.butterworth(1000, order=5)
        proc = FilterProcessor(44100)
        filtered = proc.apply_filter(signal, b, a)
        self.assertEqual(len(filtered), len(signal))

if __name__ == "__main__":
    unittest.main()
