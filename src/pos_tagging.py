from .utils import load_spacy_model, logger, load_config

def pos_tagging(text: str):
    """Perform Part-of-Speech tagging on the input text.
    
    Args:
        text (str): Input text to analyze.
    
    Returns:
        list: List of tuples containing the token, its POS tag, and its detailed tag.
    """
    try:
        config = load_config()
        nlp = load_spacy_model(config['nlp']['model'])
        doc = nlp(text)
        pos_tags = [(token.text, token.pos_, token.tag_) for token in doc]
        logger.info(f"POS tagging completed successfully for text: {text}")
        return pos_tags
    except Exception as e:
        logger.error(f"Error in POS tagging: {e}")
        raise

if __name__ == "__main__":
    sample_text = "Barack Obama was the 44th President of the United States."
    pos_tags = pos_tagging(sample_text)
    for token, pos, tag in pos_tags:
        print(f"{token:12} {pos:10} {tag}")