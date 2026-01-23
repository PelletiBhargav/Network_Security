from networksecurity.compontents.data_ingestion import DataIngestion
from networksecurity.compontents.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig
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
        
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)