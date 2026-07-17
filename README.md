# Network Security Phishing Detection System

## Overview

The Network Security Phishing Detection System is an end-to-end Machine Learning project designed to identify phishing websites based on various URL and network-related features. The project includes data ingestion, validation, transformation, model training, prediction APIs, Docker support, CI/CD automation, and cloud deployment capabilities.

The system automates the complete ML lifecycle, from collecting data to serving predictions through a FastAPI application.

---

## Features

* End-to-End Machine Learning Pipeline
* Automated Data Ingestion from MongoDB
* Data Validation and Drift Detection
* Data Transformation and Preprocessing
* Model Training and Evaluation
* FastAPI-based Prediction Service
* Docker Containerization
* AWS Deployment Support
* CI/CD Integration using GitHub Actions
* Model and Preprocessor Serialization
* Logging and Exception Handling

---

## Project Architecture

```text
NetworkSecurity/
│
├── Artifacts/
├── data_schema/
├── final_model/
├── logs/
├── Network_Data/
├── networksecurity/
│   ├── cloud/
│   ├── components/
│   ├── constant/
│   ├── entity/
│   ├── exception/
│   ├── logging/
│   ├── pipeline/
│   └── utils/
│
├── templates/
├── app.py
├── main.py
├── push_data.py
├── requirements.txt
├── setup.py
├── Dockerfile
└── README.md
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Machine Learning

* Scikit-Learn
* NumPy
* Pandas

### Database

* MongoDB Atlas
* PyMongo

### MLOps & Deployment

* Docker
* GitHub Actions
* AWS EC2
* AWS ECR

### Experiment Tracking

* MLflow
* DagsHub

---

## Dataset

The project uses a phishing website dataset containing various URL and network-related attributes.

Target Variable:

* `1` → Legitimate Website
* `-1` → Phishing Website

Dataset Location:

```text
Network_Data/phisingData.csv
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/network-security-phishing-detection.git
cd network-security-phishing-detection
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory.

```env
MONGODB_URL_KEY=your_mongodb_connection_string
```

Example:

```env
MONGODB_URL_KEY=mongodb+srv://username:password@cluster.mongodb.net/
```

---

## Running Training Pipeline

Execute the complete training pipeline:

```bash
python main.py
```

Pipeline Stages:

1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Model Saving

Artifacts are generated automatically inside the `Artifacts/` directory.

---

## Running FastAPI Application

Start the API server:

```bash
python app.py
```

or

```bash
uvicorn app:app --reload
```

API URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

## API Endpoints

### Home

```http
GET /
```

Redirects to Swagger documentation.

---

### Train Model

```http
GET /train
```

Triggers the complete ML training pipeline.

Response:

```text
Training is successful
```

---

### Predict

```http
POST /predict
```

Upload a CSV file containing feature values.

Returns:

* Predictions
* HTML table view of results
* CSV output file

Example Request:

```bash
curl -X POST \
-F "file=@test.csv" \
http://localhost:8000/predict
```

---

## Docker Support

### Build Docker Image

```bash
docker build -t networksecurity .
```

### Run Container

```bash
docker run -p 8000:8000 networksecurity
```

---

## AWS Deployment

### Required GitHub Secrets

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
AWS_ECR_LOGIN_URI
ECR_REPOSITORY_NAME
```

Example:

```text
AWS_REGION=us-east-1
ECR_REPOSITORY_NAME=networkssecurity
```

---

## CI/CD Pipeline

The project includes GitHub Actions workflows for:

* Automated Build
* Docker Image Creation
* AWS ECR Push
* Deployment Automation

Workflow Location:

```text
.github/workflows/
```

---

## Model Artifacts

Trained models are stored in:

```text
final_model/
```

Files:

```text
model.pkl
preprocessor.pkl
```

---

## Logging

Application logs are automatically generated in:

```text
logs/
```

These logs help monitor:

* Pipeline Execution
* Model Training
* Data Validation
* Prediction Requests
* Exceptions

---

## Future Enhancements

* Real-Time URL Classification
* Explainable AI (XAI)
* Monitoring Dashboard
* Kubernetes Deployment
* Automated Retraining
* Model Performance Monitoring

---

## Author

Developed as a Network Security and Machine Learning project demonstrating:

* MLOps Practices
* Data Engineering Pipelines
* Model Deployment
* Cloud Integration
* Production-Ready ML Systems

---

## License

This project is intended for educational and research purposes.
