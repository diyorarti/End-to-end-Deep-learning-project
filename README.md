# Xray Classification Project

## Project Overview
This project focuses on classifying X-ray images to detect normal and pneumonia cases. It employs deep learning techniques using PyTorch and is integrated with BentoML for model serving and deployment. The project is modular, with components handling data ingestion, transformation, model training, evaluation, and deployment.

## Key Components

### Data Ingestion
**Purpose**: Downloads and extracts the X-ray dataset from Google Drive.  
**Files**:
- `data_ingestion.py`: Handles downloading and extracting files from Google Drive.  
**Output**: Data is stored in the `artifacts/data_ingestion/` folder.

### Data Transformation
**Purpose**: Applies transformations to the data and prepares it for model training.  
**Files**:
- `data_transformation.py`: Handles data augmentation (e.g., resizing, cropping, normalization) for both training and testing sets.  
**Output**: Transformed data is stored in `artifacts/data_transformation/`.

### Model Training
**Purpose**: Trains a CNN model for X-ray image classification using PyTorch.  
**Files**:
- `model_training.py`: Handles model training, optimizer setup, and loss function.  
**Output**: The trained model is saved as `model.pt` in `artifacts/trained_model/`.

### Model Evaluation
**Purpose**: Evaluates the trained model using test data and calculates accuracy.  
**Files**:
- `model_evaluation.py`: Loads the model and computes evaluation metrics such as accuracy and loss.  
**Output**: Evaluation results are logged.

### Model Deployment with BentoML
**Purpose**: Deploys the trained model using BentoML for serving predictions.  
**Files**:
- `model_pusher.py`: Builds and pushes the model to BentoML, containerizes the model, and pushes it to AWS ECR.  
**Output**: The BentoML model is deployed as a service.

### API Deployment
**Purpose**: Deploys the model as an API using BentoML.  
**Files**:
- `model_service.py`: Contains the BentoML service and defines an API to predict pneumonia from X-ray images.  

### Research
This folder contains Jupyter notebooks for experimentation and trials:
- `trials.ipynb`

## Docker Setup

The project uses BentoML and Docker to package and deploy the model for real-time inference.

- **bentofile.yaml**: Defines the BentoML service, Python dependencies, and packages used in the project.
  
### Building and Running Docker Container
```bash
# Build the BentoML service
bentoml build

# Containerize the service using BentoML
bentoml containerize xray_service:latest -t <ECR_REPOSITORY_URI>:latest

# Push the image to AWS ECR
docker push <ECR_REPOSITORY_URI>:latest

# Programming Language & Frameworks:
- Python: Core programming language for the project.
## Libraries/Packages:
- Torch (PyTorch): For building and training the deep learning models (CNN architecture).
- Torchvision: For handling image-related tasks like transformations.
- Joblib: For saving and loading models.
- Pillow: For handling image input and processing.
- NumPy: For numerical operations and data manipulation.
## Cloud Services:
- Google Drive (gdown): For downloading the dataset from Google Drive.