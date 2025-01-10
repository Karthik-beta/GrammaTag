import spacy

def pos_tagging(text: str):
    """Perform Part-of-Speech tagging on the input text."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [(token.text, token.pos_, token.tag_) for token in doc]

if __name__ == "__main__":
    sample_text = "Barack Obama was the 44th President of the United States."
    pos_tags = pos_tagging(sample_text)
    for token, pos, tag in pos_tags:
        print(f"{token:12} {pos:10} {tag}")
