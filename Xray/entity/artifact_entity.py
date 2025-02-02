from dataclasses import dataclass
from torch.utils.data.dataloader import DataLoader

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str

@dataclass
class DataTransformationArtifact:
    transformed_train_object: DataLoader
    transformed_test_object: DataLoader
    train_transform_file_path: str
    test_transform_file_path: str

@dataclass
class ModelTrainingArtifact:
    trained_model_path: str

@dataclass
class ModelEvaluationArtifact:
    model_accuracy: float


@dataclass
class ModelPusherArtifact:
    bentoml_model_nae: str
    bentoml_servie_name: str