import spacy

def extract_phrases_and_relationships(text: str):
    """Extract meaningful phrases and relationships from the input text."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    relationships = []
    for token in doc:
        if token.dep_ in ("nsubj", "dobj", "pobj"):
            relationships.append((token.text, token.dep_, token.head.text))
    return relationships

if __name__ == "__main__":
    sample_text = "Barack Obama was the President of the United States."
    phrases = extract_phrases_and_relationships(sample_text)
    for phrase in phrases:
        print(f"{phrase[0]:12} {phrase[1]:10} {phrase[2]}")
