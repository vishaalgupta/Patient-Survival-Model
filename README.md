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

* Flask App - app.py, profile, and requirements.tx for using Flask App
* static - CSS folder and JS folder 
* Resources - the original and cleaned patient survival data csv files
* Images - screenshots and pictures used for project 
* ML-models - machine learning models: AdaBoost Classifier, Extra Trees Classifier, KNN, Linear Regression, Logistic Regression, Extra Trees
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
91,700 rows


## Conclusions 

We have imbalanced data-set, to compensate the situation, the data-set was first oversampled and then scaled to fit all models.

### Test Accuracy: 

 1. Linear Regression : 38.9% 
 2. Logistic Regression: 78.2%
 3. K Nearest Neighbors: 95.1%
 4. Random Forest Classifier: 98.7%
 5. AdaBoost Classifier: 80.7%
 6. Extra Trees Classifier: 99.5%


Based on the testing accuracy we have decided to use Extra Trees Classifier as our model. 

Patient Form

![Patient Form](https://user-images.githubusercontent.com/100645924/185009028-c792827a-e103-4c7c-92a0-2941f1d2e337.png)
