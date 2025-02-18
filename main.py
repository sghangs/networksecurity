from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.components.model_trainer import ModelTrainer
import sys

if __name__=="__main__":
    try:
        ## Data Ingestion

        trainingpipelinecofig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelinecofig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data initiation completed")
        print(dataingestionartifact)

        ## Data Validation

        data_validation_config=DataValidationConfig(trainingpipelinecofig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("INitiate data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data validation completed")

        ## Data Transformation

        data_transformation_config=DataTransformationConfig(trainingpipelinecofig)
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        logging.info("INitiate data Transformation")
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("data transformation completed")

        ## Model Training and Evaluation

        logging.info("Model training started...")
        model_trainer_config=ModelTrainerConfig(trainingpipelinecofig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info("Model Training completed")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)

        
