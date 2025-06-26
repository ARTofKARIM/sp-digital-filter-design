"""Main entry point for digital filter design tool."""
import argparse
import yaml
from src.filter_design import FilterDesigner
from src.signal_generator import SignalGenerator
from src.filter_processor import FilterProcessor
from src.visualization import FilterVisualizer

def main():
    parser = argparse.ArgumentParser(description="Digital Filter Design Tool")
    parser.add_argument("--config", default="config/config.yaml")
    parser.add_argument("--filter", choices=["lowpass", "highpass", "bandpass", "notch", "all"], default="all")
    parser.add_argument("--demo", action="store_true", help="Run demo with test signals")
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    fs = config["signal"]["sample_rate"]
    designer = FilterDesigner(fs)
    viz = FilterVisualizer()

    if args.demo:
        gen = SignalGenerator(fs)
        proc = FilterProcessor(fs)
        t, noisy = gen.multi_tone([200, 1000, 5000], 0.1, [1.0, 0.5, 0.3])
        t, noise = gen.white_noise(0.1, 0.2)
        noisy = noisy + noise[:len(noisy)]
        b, a = designer.butterworth(config["filters"]["lowpass"]["cutoff"],
                                     config["filters"]["lowpass"]["order"])
        filtered = proc.apply_filter(noisy, b, a)
        viz.plot_signal_comparison(t, noisy, filtered, "Lowpass Demo")
        w, mag, phase = designer.frequency_response(b, a)
        viz.plot_frequency_response(w, mag, phase, "Butterworth Lowpass")
    print("Done.")

if __name__ == "__main__":
    main()
