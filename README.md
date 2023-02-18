# Tesco Telco Prediction

AutoML Tesco Telco Prediction using AutoGluon Framework

## Introduction

This will be using `AutoGluon` framework.

## Business objective

## Environment Setup

Create an environment
```
conda create --name insuranceenv python=3.9 -y
```

Activate the environment
```
conda activate insuranceenv

Install packages in the environment
NB: This is for Windows

```
pip install torch==1.12.1+cpu torchvision==0.13.1+cpu torchtext==0.13.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
pip install autogluon chardet
conda install streamlit jupyter
```

### Test your instructions as follows:

```bash
(insuranceenv) C:\Users\User\Documents\workspace_datahackermen\insurance_premium_prediction>python
Python 3.9.16 (main, Jan 11 2023, 16:16:36) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from autogluon.tabular import TabularDataset, TabularPredictor
```

If that works, then you have good installation for `autogluon`.

And then for `Streamlit`,

```bash
(insuranceenv) C:\Users\User\Documents\workspace_datahackermen\insurance_premium_prediction>streamlit hello
  Welcome to Streamlit. Check out our demo in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.43.234:8501

  Ready to create your own Python apps super quickly?
  Head over to https://docs.streamlit.io

  May you create awesome apps!
  ```

  This will automatically pop up on your default browser on this address - `http://localhost:8501/`


## Project Structure

```

Insurance Premium
|--README.md
|--images
|--data
|--main.py
|--main.ipynb
|--experimentation.ipynb
|--app.py
```

## Data Ingestion

## Exploratory Data Analysis (EDA)

## Features Engineering and processing

## Model Building

## Model Evaluation

## Model Deployment

Deployment will be done on `Streamlit`.
