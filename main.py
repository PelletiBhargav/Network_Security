from networksecurity.compontents.data_ingestion import DataIngestion
from networksecurity.compontents.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig

from networksecurity.compontents.data_transformation import DataTransformation

from networksecurity.compontents.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import ModelTrainerConfig
if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info('data initiation completed')
        print(dataingestionartifact)
        
        data_validaton_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validaton_config)
        logging.info('initiate the data validation')
        data_validation_Artidfact=data_validation.initiate_data_validation()
        logging.info('data validation completed')
        print(data_validation_Artidfact)
        
        data_transformaton_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info('initiate the data transformation')
        data_transformation=DataTransformation(data_validation_Artidfact,data_transformaton_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info('data transformation completed')
        print(data_transformation_artifact)
        
        
        
        
        logging.info("Model Training sstared")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")
    except Exception as e:
        raise NetworkSecurityException(e,sys)