# Experiment 1: Check Python and required libraries
import sys

print("Python version:", sys.version)
for name in ["numpy", "pandas", "sklearn", "matplotlib", "seaborn"]:
    try:
        module = __import__(name)
        print(name, "is installed")
    except ImportError:
        print(name, "is NOT installed")
        print("Install with: pip install numpy pandas scikit-learn matplotlib seaborn")
