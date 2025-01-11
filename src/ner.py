from .utils import load_spacy_model, logger, load_config

def named_entity_recognition(text: str):
    """Perform Named Entity Recognition on the input text.
    
    Args:
        text (str): Input text to analyze.
    
    Returns:
        list: List of tuples containing the entity text and its label.
    """
    try:
        config = load_config()
        nlp = load_spacy_model(config['nlp']['model'])
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        logger.info(f"NER completed successfully for text: {text}")
        return entities
    except Exception as e:
        logger.error(f"Error in NER: {e}")
        raise

if __name__ == "__main__":
    sample_text = "Barack Obama was born in Hawaii and became the US President."
    entities = named_entity_recognition(sample_text)
    for entity, label in entities:
        print(f"{entity:20} {label}")