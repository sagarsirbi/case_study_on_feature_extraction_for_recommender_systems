# CASE STUDY ON FEATURE EXTRACTION FOR RECOMMENDER SYSTEMS

![FRNVGggUYAEg5MA](https://user-images.githubusercontent.com/89741376/218879722-22e4d3b6-c86c-4e44-a0c6-571eb9a7019a.jpg)
*Reference: https://www.updatepedia.com/top-05-upcoming-movies-in-2021/*
# INTRODUCTION
With the explosive growth of online information, users are generally provided without endless movies, products and services. As a result, recommender systems have come to rescue and posses effective strategy to overcome such information load. The influence of deep learning has been revolutionizing over the decade in the area of recommender systems and brings in a number of opportunities to improve the performance of the recommender. Moreover, the influence of feature extraction techniques in recommender systems is not very well documented. Hence, this project focus on the survey of state-of-the-art feature extraction techniques currently implemented in recommender systems. More concretely, we implement feature extraction techniques using an autoencoder for a deep neural network predictive model and a hybrid approach for feature extraction using a machine learning predictive model. We evaluate these models against the baseline model, derived from traditional structured dataset, being fed into the model. Furthermore, we demonstrate our models performance of two different datasets of varying sparsity, namely Movielens100k and Movielens1M. Lastly, we evaluate our models performance using Root metrics Mean Squared Error and Mean Absolute Error.

## INSTALL AND RUN THE PROJECT
Install all dependencies from ```requirements.txt``` file and use anaconda environment.
To create the same environment from the requirements file, you can use the following command:

```
$ conda create --name new_env --file requirements.txt
```
This will create a new conda environment called ```my_env``` and install all the packages from the requirements.text file

## DATASETS
The datasets used in this project is ```MovieLens-100K``` and ```MovieLens-1M``` obtained from https://grouplens.org/datasets/movielens/

  - [MovieLens-100K](https://files.grouplens.org/datasets/movielens/ml-100k.zip): Dataset used in Machine Learning proposed model
  - [MovieLens-1M](https://files.grouplens.org/datasets/movielens/ml-1m.zip): Dataset used in Deep Learning Neural Network model 

## DATA PREPARATION 
Proposed Deep Learning Model utilizes users and items data. The corresponding data prepared pickle file for downloads can be found here:
  - [UsersData](https://drive.google.com/file/d/1zdAGWRK4LY1f0FpladJBjWHbozmYbd-8/view?usp=share_link) Data preparation pickle file for user autoenocder
  - [MoviesData](https://drive.google.com/file/d/1B2uOP7YZYpPkP7pJOTRtGR5pdlB5kJlG/view?usp=share_link) Data preparation pickle file for item autoencoder
  
## PROJECT FILE DESCRIPTION
  - [Hybrid Approach for Feature Extraction in Recommender systems](https://github.com/ISG-Siegen/SA_Sagar_Sirbi/tree/main/CASE%20STUDY%20ON%20FEATURE%20EXTRACTION%20FOR%20RECOMMENDER%20SYSTEMS/1.%20FEATURE%20EXTRACTION%20WITH%20DATA%20CLUSTERING) for machine learning model approach.
  - [Deep Autoencoders for Feature Extraction with Embeddings in Recommender Systems](https://github.com/ISG-Siegen/SA_Sagar_Sirbi/tree/main/CASE%20STUDY%20ON%20FEATURE%20EXTRACTION%20FOR%20RECOMMENDER%20SYSTEMS/2.%20DEEP%20AUTOENCODERS%20FOR%20FEATURE%20EXTRACTION) for deep learning model approach.

## AUTHOR
This project was created by
  - Sagar K Sirbi (sagar.sirbi@student.uni-siegen.de)

If you have any questions or feedback about the project, please feel free to contact me via e-mail.

## ACKNOWLEDGEMENT
I would like to thank the following individuals and organizations for their contibutions in this project:
  - Mr. Lukas Wegmeth, for providing valuable feedback and suggestions throughout the development process.
  - Prof. Dr-ing. Joeran Beel for creating opportunites for studienarbeit at the University.
  - Kirana Rama, Pradeep Kumar, Bharat Bhasker and Andreea Salinca for their valuable research contributions and providing a strong foundation for my research.
  - University of Siegen, for providing support and resources for this research project.

I am grateful for the support and assistance that I have received, and I would not have been able to complete this project without the help of these individuals and organizations.
