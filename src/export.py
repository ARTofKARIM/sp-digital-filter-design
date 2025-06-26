"""Export filter coefficients."""
import json
import numpy as np

class FilterExporter:
    @staticmethod
    def to_json(b, a, filepath, metadata=None):
        data = {"b": b.tolist() if isinstance(b, np.ndarray) else list(b),
                "a": a.tolist() if isinstance(a, np.ndarray) else list(a)}
        if metadata:
            data["metadata"] = metadata
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def to_c_header(b, a, filepath, name="filter"):
        with open(filepath, "w") as f:
            f.write(f"// Auto-generated filter coefficients\n")
            f.write(f"#define {name.upper()}_ORDER {len(b)-1}\n")
            f.write(f"const double {name}_b[] = {{{', '.join(f'{x:.15e}' for x in b)}}};\n")
            f.write(f"const double {name}_a[] = {{{', '.join(f'{x:.15e}' for x in a)}}};\n")
