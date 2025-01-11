import unittest
from src.pos_tagging import pos_tagging

class TestPOSTagging(unittest.TestCase):
    def test_pos_tagging(self):
        text = "Barack Obama was the 44th President of the United States."
        tags = pos_tagging(text)
        self.assertIsInstance(tags, list)
        self.assertTrue(all(isinstance(tag, tuple) for tag in tags))

if __name__ == "__main__":
    unittest.main()