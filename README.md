# SignatureMMD-TwoSampleTests

This repository demonstrates how to perform **two-sample hypothesis tests** for time series (or more general stochastic process) data using the **robust signature MMD** approach from the paper:

> *Signature Moments to Characterize Laws of Stochastic Processes*  
> Ilya Chevyrev and Harald Oberhauser (2022).

In addition, it compares Type I error and power against other classical two-sample tests (e.g., Hotelling's T^2, standard MMD on raw data, etc.).

## Repository Structure

- **`.gitignore`**: Excludes Python caches, Jupyter checkpoints, and the virtual environment folder.
- **`data/`**: 
  - `toy_data_example.csv`: A toy dataset (e.g. artificially generated time series). 
  - `real_data_example.csv`: Placeholder for a real-world dataset (see below for sources).
- **`notebooks/signature_mmd_experiments.ipynb`**: A single notebook demonstrating:
  1. Generation or loading of toy time series data.
  2. Loading a small real-world time series dataset.
  3. Implementing robust signature MMD, standard MMD, and other tests.
  4. Estimating Type I error (when the two samples are from the same distribution).
  5. Estimating power (when the two samples are from different distributions).
- **`venv/`**: (Optional) Local Python virtual environment for reproducibility. By default, it is in `.gitignore`.

No license is provided.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/iHugoMMM/SignatureMMD-TwoSampleTests.git
   cd SignatureMMD-TwoSampleTests

## Installing Dependencies
```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
