import yaml
import logging
import os
import warnings
import spacy
import torch

def load_config():
    """Load configuration from config.yaml."""
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config

def setup_logging():
    """Set up logging based on the configuration."""
    config = load_config()
    logging_level = config['logging']['level']
    logging_file = config['logging']['file']
    
    os.makedirs(os.path.dirname(logging_file), exist_ok=True)
    
    logging.basicConfig(
        level=logging_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(logging_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def load_spacy_model(model_name: str):
    """Load a SpaCy model with PyTorch weights."""
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning, message=".*weights_only=False.*")
        nlp = spacy.load(model_name)
    return nlp

logger = setup_logging()