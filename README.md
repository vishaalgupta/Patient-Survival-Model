![Patient Survival Prediction](https://user-images.githubusercontent.com/93561950/184466067-2264322f-f79a-4b31-91bb-82a368eff39d.jpg)

# Patient Survival Prediction with Supervised Learning

Project #4: Machine Learning Integration 

Heroku APP Link: 

https://patient-survival-predictor.herokuapp.com/



## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Featured Notebooks and Files](#featured-notebooks-and-files)
* [Screenshots](#screenshots)
* [Data Source](#data-source)
* [Conclusions](#conclusions)


## General Information
This project examines factors that contribute to a patient's survival in the hospital. Supervised machine learning models were evaluated to determine the most accurate model for survival prediction. 
We aimed to develop and validate a prediction model for cause of mortality among admitted hospital patients. In this dataset, there are various factors given, which are involved when a patient is hospitalized. 
On the basis of these factors, predict whether the patient will survive or not.


## Technologies Used
- Pandas
- Matplotlib
- Supervised Machine Learning
- Flask
- Tableau
- HTML
- CSS
- Javascript
- Heroku
 
 ## Featured Notebooks and Files


The structure of the project includes the following folders/files: 

* Flask App - including app.py, profile, and requirements.tx for using Flask App
* static - including CSS folder and JS folder 
* Resources - including the original and cleaned Patient survival data csv files
* Images - including all the screenshots and pictures used for project 
* ML-models - including all the machine learning models we have run: AdaBoost Classifier, Extra Trees Classifier, KNN, Linear Regression, Logistic Regression, Extra Trees
                and Random Forest Classifier


 
## Screenshots

Ethnicity Analysis

![Ethnicity Analysis](https://user-images.githubusercontent.com/93561950/184452328-0fd2fe15-da04-4342-b99a-87421401b670.png)

ICU Type vs. Death

![Icu_type vs  Death](https://user-images.githubusercontent.com/93561950/184452548-fd0c911c-9fd2-493c-b328-b68b5afb9aed.png)

Age and Gender Analysis

![Age and Gender](Images/Age%20and%20Gender.png)

Glasgow Coma Scale Composite Scores & Ventilation

![GCS&Vents](Images/GCS%20%26%20Vents.png)

Body Systems

![Body Systems](Images/Body%20Systems.png)

Heart Rate

![Heart Rate](Images/Heart%20Rate.png)






## Data Source

kaggle.com

https://www.kaggle.com/datasets/mitishaagarwal/patient


Patient survival prediction dataset.csv(31.41 MB)
85 columns
9000 rows


## Conclusions 

We have tried different machine learning models including: AdaBoost Classifier, KNN, Linear Regression, Logistic Regression, Random Forest Classifier, Extra Trees Classifier and Lasso
Based on the results, we have decided to use AdaBoost Classifier as our model. 

