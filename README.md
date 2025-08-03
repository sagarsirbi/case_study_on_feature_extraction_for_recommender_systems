# Feature Extraction in Recommender Systems

![Recommender Systems](https://user-images.githubusercontent.com/89741376/218879722-22e4d3b6-c86c-4e44-a0c6-571eb9a7019a.jpg)
*Reference: https://www.updatepedia.com/top-05-upcoming-movies-in-2021/*

## Overview
This repository presents a comprehensive case study on state-of-the-art feature extraction techniques for recommender systems. It implements and compares both machine learning (hybrid clustering) and deep learning (autoencoder-based) approaches for feature extraction, using the MovieLens-100K and MovieLens-1M datasets. The project includes code, data preparation scripts, and a detailed report evaluating model performance using standard metrics.

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Datasets](#datasets)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [Author](#author)
- [Acknowledgements](#acknowledgements)

## Project Structure
```
CASE STUDY ON FEATURE EXTRACTION FOR RECOMMENDER SYSTEMS/
├── 1. FEATURE EXTRACTION WITH DATA CLUSTERING/
│   ├── COLLABORATIVE FILTERING/
│   └── CONTENT BASED FILTERING/
├── 2. DEEP AUTOENCODERS FOR FEATURE EXTRACTION/
│   ├── 1. DATA PREPARATION/
│   ├── 2. USER AUTOENCODER/
│   ├── 3. ITEM AUTOENCODER/
│   ├── 4. COLLABORATIVE FILTERING/
│   ├── 5. AUTOENCODER COLLABORATIVE FILTERING/
│   └── MODULE/
│   └── README.md
└── FINAL REPORT.pdf
```
- **1. FEATURE EXTRACTION WITH DATA CLUSTERING/**: Implements hybrid machine learning approaches (clustering, collaborative filtering, content-based filtering).
- **2. DEEP AUTOENCODERS FOR FEATURE EXTRACTION/**: Implements deep learning approaches using autoencoders for user/item embeddings and collaborative filtering.
- **FINAL REPORT.pdf**: Contains the detailed case study and results.

## Installation
1. Clone this repository:
   ```
   git clone <repo-url>
   cd feature_extraction_in_recommender_systems
   ```
2. Install dependencies using Anaconda:
   ```
   conda create --name recsys_env --file requirements.txt
   conda activate recsys_env
   ```

## Datasets
The project uses the following datasets from [GroupLens](https://grouplens.org/datasets/movielens/):
- [MovieLens-100K](https://files.grouplens.org/datasets/movielens/ml-100k.zip): Used in machine learning models
- [MovieLens-1M](https://files.grouplens.org/datasets/movielens/ml-1m.zip): Used in deep learning models

Download and extract the datasets as required by the scripts in each module.

### Data Preparation
For deep learning models, preprocessed pickle files are required:
- [UsersData](https://drive.google.com/file/d/1zdAGWRK4LY1f0FpladJBjWHbozmYbd-8/view?usp=share_link): For user autoencoder
- [MoviesData](https://drive.google.com/file/d/1B2uOP7YZYpPkP7pJOTRtGR5pdlB5kJlG/view?usp=share_link): For item autoencoder

## Usage
- **Hybrid Machine Learning Approach:**
  - See `CASE STUDY ON FEATURE EXTRACTION FOR RECOMMENDER SYSTEMS/1. FEATURE EXTRACTION WITH DATA CLUSTERING/` for scripts and instructions on running clustering, collaborative, and content-based filtering models.
- **Deep Learning Autoencoder Approach:**
  - See `CASE STUDY ON FEATURE EXTRACTION FOR RECOMMENDER SYSTEMS/2. DEEP AUTOENCODERS FOR FEATURE EXTRACTION/README.md` for detailed instructions on running autoencoder-based models for user/item embeddings and collaborative filtering.

Typical steps:
1. Prepare the datasets and required pickle files.
2. Run the data preparation scripts.
3. Train and evaluate the models as described in the respective module directories.

## Results
- The project evaluates models using Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE).
- Experiments are conducted on datasets of varying sparsity (MovieLens-100K and 1M).
- See `FINAL REPORT.pdf` for a detailed analysis and comparison of all approaches.

## Contributing
Contributions, issues, and feature requests are welcome! Please open an issue or submit a pull request.

## Author
Created by Sagar K Sirbi (sagar.sirbi@student.uni-siegen.de)

## Acknowledgements
- Mr. Lukas Wegmeth, for valuable feedback and suggestions.
- Prof. Dr-ing. Joeran Beel, for research opportunities at University of Siegen.
- Kirana Rama, Pradeep Kumar, Bharat Bhasker, and Andreea Salinca for foundational research.
- University of Siegen, for support and resources.
