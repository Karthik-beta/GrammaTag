import warnings
from src.pos_tagging import pos_tagging
from src.ner import named_entity_recognition
from src.text_extraction import extract_phrases_and_relationships
from src.utils import logger

# Suppress the PyTorch warning globally
warnings.filterwarnings("ignore", category=UserWarning, message=".*weights_only=False.*")

def main():
    """Main function to run the GrammaTag project."""
    try:
        text = input("Enter text to analyze: ")

        print("\nPOS Tagging:")
        pos_tags = pos_tagging(text)
        for token, pos, tag in pos_tags:
            print(f"{token:12} {pos:10} {tag}")

        print("\nNamed Entity Recognition:")
        entities = named_entity_recognition(text)
        for entity, label in entities:
            print(f"{entity:20} {label}")

        print("\nText Extraction and Relationships:")
        relationships = extract_phrases_and_relationships(text)
        for phrase in relationships:
            print(f"{phrase[0]:12} {phrase[1]:10} {phrase[2]}")

    except Exception as e:
        logger.error(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()