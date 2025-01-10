import spacy

def named_entity_recognition(text: str):
    """Perform Named Entity Recognition on the input text."""
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

if __name__ == "__main__":
    sample_text = "Barack Obama was born in Hawaii and became the US President."
    entities = named_entity_recognition(sample_text)
    for entity, label in entities:
        print(f"{entity:20} {label}")
