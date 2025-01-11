import unittest
from src.text_extraction import extract_phrases_and_relationships

class TestTextExtraction(unittest.TestCase):
    def test_text_extraction(self):
        text = "Barack Obama was the President of the United States."
        phrases = extract_phrases_and_relationships(text)
        self.assertIsInstance(phrases, list)
        self.assertTrue(all(isinstance(phrase, tuple) for phrase in phrases))

if __name__ == "__main__":
    unittest.main()