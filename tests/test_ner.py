import unittest
from src.ner import named_entity_recognition

class TestNER(unittest.TestCase):
    def test_ner(self):
        text = "Barack Obama was born in Hawaii."
        entities = named_entity_recognition(text)
        self.assertIsInstance(entities, list)
        self.assertTrue(all(isinstance(entity, tuple) for entity in entities))

if __name__ == "__main__":
    unittest.main()