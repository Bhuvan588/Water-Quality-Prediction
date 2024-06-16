
# Water Quality Prediction

In this project with the help of Machine Learning, I have classified a water sample as safe or not safe based on concentration of 20 elements in the sample.



## Demo
![image](![WhatsApp Image 2024-06-17 at 12 35 23 AM](https://github.com/Bhuvan588/Water-Quality-Prediction/assets/68458621/65a7eb00-3c20-4167-ac53-d0b90d9b1349)
![image2]![WhatsApp Image 2024-06-17 at 12 35 52 AM](https://github.com/Bhuvan588/Water-Quality-Prediction/assets/68458621/47a64b26-ff7c-42fe-ae2c-1f6cf5a8c9bf)





## About

First the dataset has been taken from Kaggle (link will be provided below). Then after using preprocessing techniques and performing data analysis, different classification models have been fitted into the dataset and a good accuracy has been achieved.

Then the model has been partially deployed using Anvil - an online tool which helps you to directly connect your notebook with an interface.

Taking one step further , I have downlaoded the model using joblib and then containerized it using Docker.
## Project Structure
- app - contains server.py (used for creating endpoints using FastAPI) and model.joblib (downloaded model)

- Dockerfile - for creating container
- client.py - Just a test file for sending data
- requirements.txt- contains all requirements used when building container
- water-quality-notebook.ipynb - Google colab file containing the preprocessing, data analysis and model fitting.
- water-quality-pca.ipynb - Bonus notebook where I have applied PCA to check and retain the variance with less number of features
## Dataset Link

https://www.kaggle.com/datasets/mssmartypants/water-quality

## Sample data you can pass at the FastAPI endpoint

{"features":[0.940, 14.470,0.030,2.880,0.003,0.800,0.430,1.380,0.110,0.670,0.670,0.135,9.750,1.890,0.006,27.170,5.420,0.080,0.190,0.020]}

Output: 1
## Libraries and Tools Used

- Python - Programming language for ML
- Numpy, Pandas - Used for loading and working on dataset
- Anvil - Used for building interface
- Docker - Used for containerization
