"""Visualization for filter analysis."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

class FilterVisualizer:
    def __init__(self, output_dir="output/"):
        self.output_dir = output_dir

    def plot_frequency_response(self, freqs, magnitude_db, phase, title="", save=True):
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        ax1.plot(freqs, magnitude_db, color="steelblue", linewidth=1.5)
        ax1.set_ylabel("Magnitude (dB)")
        ax1.set_title(f"Frequency Response - {title}")
        ax1.grid(True, alpha=0.3)
        ax1.set_xlim(0, freqs[-1])
        ax2.plot(freqs, np.degrees(phase), color="coral", linewidth=1.5)
        ax2.set_xlabel("Frequency (Hz)")
        ax2.set_ylabel("Phase (degrees)")
        ax2.grid(True, alpha=0.3)
        if save:
            fig.savefig(f"{self.output_dir}freq_response_{title.lower().replace(' ', '_')}.png", dpi=150, bbox_inches="tight")
        plt.close(fig)

    def plot_signal_comparison(self, t, original, filtered, title="", save=True):
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
        ax1.plot(t, original, linewidth=0.5, alpha=0.8, label="Original")
        ax1.set_title("Original Signal")
        ax1.legend()
        ax2.plot(t, filtered, linewidth=0.5, color="coral", alpha=0.8, label="Filtered")
        ax2.set_xlabel("Time (s)")
        ax2.set_title("Filtered Signal")
        ax2.legend()
        if save:
            fig.savefig(f"{self.output_dir}comparison_{title.lower().replace(' ', '_')}.png", dpi=150, bbox_inches="tight")
        plt.close(fig)

    def plot_filter_comparison(self, filters_data, save=True):
        fig, ax = plt.subplots(figsize=(12, 6))
        for name, (freqs, mag) in filters_data.items():
            ax.plot(freqs, mag, linewidth=1.5, label=name)
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("Magnitude (dB)")
        ax.set_title("Filter Comparison")
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_ylim(-80, 5)
        if save:
            fig.savefig(f"{self.output_dir}filter_comparison.png", dpi=150, bbox_inches="tight")
        plt.close(fig)
