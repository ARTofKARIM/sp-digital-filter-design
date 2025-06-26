# Digital Filter Design Tool

A signal processing toolkit for designing, analyzing, and applying digital filters (IIR and FIR) with comprehensive frequency response visualization.

## Architecture
```
sp-digital-filter-design/
├── src/
│   ├── filter_design.py      # Butterworth, Chebyshev, Elliptic, FIR design
│   ├── signal_generator.py   # Test signal generation (sine, chirp, noise)
│   ├── filter_processor.py   # Filter application with SNR computation
│   └── visualization.py      # Frequency response, signal comparison plots
├── config/config.yaml
├── tests/test_filters.py
└── main.py
```

## Filter Types
| Filter | IIR/FIR | Description |
|--------|---------|-------------|
| Butterworth | IIR | Maximally flat passband |
| Chebyshev I | IIR | Equiripple passband |
| Chebyshev II | IIR | Equiripple stopband |
| Elliptic | IIR | Sharpest transition |
| FIR | FIR | Linear phase, windowed |
| Notch | IIR | Narrow band rejection |

## Installation
```bash
git clone https://github.com/mouachiqab/sp-digital-filter-design.git
cd sp-digital-filter-design
pip install -r requirements.txt
```

## Usage
```bash
python main.py --demo --filter all
```

## Technologies
- Python 3.9+, NumPy, SciPy, Matplotlib










