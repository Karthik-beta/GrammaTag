from .utils import load_spacy_model, logger, load_config

def extract_phrases_and_relationships(text: str):
    """Extract meaningful phrases and relationships from the input text.
    
    Args:
        text (str): Input text to analyze.
    
    Returns:
        list: List of tuples containing the phrase, its dependency, and the head word.
    """
    try:
        config = load_config()
        nlp = load_spacy_model(config['nlp']['model'])
        doc = nlp(text)
        relationships = []
        for token in doc:
            if token.dep_ in ("nsubj", "dobj", "pobj"):
                relationships.append((token.text, token.dep_, token.head.text))
        logger.info(f"Text extraction completed successfully for text: {text}")
        return relationships
    except Exception as e:
        logger.error(f"Error in text extraction: {e}")
        raise

if __name__ == "__main__":
    sample_text = "Barack Obama was the President of the United States."
    phrases = extract_phrases_and_relationships(sample_text)
    for phrase in phrases:
        print(f"{phrase[0]:12} {phrase[1]:10} {phrase[2]}")