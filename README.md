# Feature Extraction in Recommender Systems

A professional, research-driven repository for state-of-the-art feature extraction techniques in recommender systems, featuring both machine learning (clustering-based) and deep learning (autoencoder-based) approaches. This project is designed for researchers, practitioners, and students interested in advanced recommender system methodologies and reproducible experiments.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Datasets](#datasets)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Citation](#citation)
- [Contact](#contact)

---

## Project Overview
This repository provides a comprehensive case study and implementation of feature extraction techniques for recommender systems. It includes:
- **Hybrid Machine Learning Models:** Clustering-based feature extraction using collaborative and content-based filtering.
- **Deep Learning Models:** Autoencoder-based feature extraction for user/item embeddings and collaborative filtering.
- **Reproducible Experiments:** Scripts and notebooks for data preparation, model training, and evaluation.
- **Detailed Report:** Analysis and comparison of all approaches using standard metrics (RMSE, MAE) on MovieLens datasets.

## Repository Structure
```
feature_extraction_in_recommender_systems/
├── clustering_feature_extraction/
│   ├── collaborative_filtering/
│   ├── content_based_filtering/
├── deep_autoencoders_feature_extraction/
│   ├── data_preparation/
│   ├── user_autoencoder/
│   ├── item_autoencoder/
│   ├── collaborative_filtering/
│   ├── autoencoder_collaborative_filtering/
│   └── module/
├── FINAL_REPORT.pdf
├── requirements.txt
├── README.md
```
- All scripts, notebooks, and modules use lowercase and underscores for clarity and consistency.

## Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd feature_extraction_in_recommender_systems
   ```
2. Install dependencies using Anaconda:
   ```bash
   conda create --name recsys_env --file requirements.txt
   conda activate recsys_env
   ```

## Datasets
- [MovieLens-100K](https://files.grouplens.org/datasets/movielens/ml-100k.zip)
- [MovieLens-1M](https://files.grouplens.org/datasets/movielens/ml-1m.zip)

Download and extract datasets as required by the scripts in each module.

### Data Preparation for Deep Learning
- [UsersData (pickle)](https://drive.google.com/file/d/1zdAGWRK4LY1f0FpladJBjWHbozmYbd-8/view?usp=share_link)
- [MoviesData (pickle)](https://drive.google.com/file/d/1B2uOP7YZYpPkP7pJOTRtGR5pdlB5kJlG/view?usp=share_link)

## Usage
- For clustering-based feature extraction, see `clustering_feature_extraction/` subfolders for collaborative and content-based filtering experiments.
- For deep autoencoder-based feature extraction, see `deep_autoencoders_feature_extraction/` subfolders for data preparation, user/item autoencoders, and collaborative filtering.
- Each module contains its own README.md with detailed instructions.

Typical workflow:
1. Prepare datasets and required pickle files.
2. Run data preparation scripts.
3. Train and evaluate models as described in the respective module directories.

## Results
- Models are evaluated using RMSE and MAE.
- Experiments are conducted on MovieLens-100K and 1M datasets.
- See `final_report.pdf` for a detailed analysis and comparison.

## Contributing
Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request.

