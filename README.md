# GrammaTag

GrammaTag is an advanced Natural Language Processing (NLP) project designed to perform sophisticated text analysis tasks, including text extraction, Named Entity Recognition (NER), and Part-of-Speech (POS) tagging. Built with modern Python tools and libraries, GrammaTag is optimized for efficiency and scalability.

## Features

- **Text Extraction and Relationship Mapping**: Extract meaningful phrases and relationships between words in a text.
- **Named Entity Recognition (NER)**: Identify and classify entities such as names, locations, organizations, and more.
- **Part-of-Speech (POS) Tagging**: Annotate text with linguistic tags for detailed grammatical analysis.
- **Advanced NLP Models**: Utilizes spaCy's transformer-based models (`en_core_web_trf`) for higher accuracy.
- **Logging and Configuration**: Robust logging and configuration management for better debugging and customization.
- **Unit Testing**: Includes comprehensive unit tests to ensure reliability.

## Requirements

- **Python**: 3.12 or higher
- **Package Manager**: `uv` (lightning-fast Python package installer)
- **Libraries**:
  - `spacy`: For NLP tasks.
  - `nltk`: For additional linguistic processing (optional).
  - `transformers`: For advanced NLP models (optional).
  - `pyyaml`: For configuration management.
  - `pytest`: For running unit tests.

## Installation

### Clone the Repository
```bash
git clone https://github.com/Karthik-beta/grammatag.git
cd grammatag
```

### Install Dependencies
Use the `uv` package manager to install dependencies:
```bash
uv install
```

### Download the SpaCy Model
Download the transformer-based model for enhanced accuracy:
```bash
uv run python -m spacy download en_core_web_trf
```

## Usage

### Run the Main Script
Execute the `main.py` script to analyze text:
```bash
uv run python main.py
```

### Input Text
Follow the prompts to input the text you want to analyze.

### View Results
The results will be displayed in the terminal and saved in the `results/` folder.

## Project Structure

```plaintext
grammatag/
├── data/             # Folder for storing datasets
├── src/              # Core Python modules
│   ├── __init__.py
│   ├── text_extraction.py
│   ├── ner.py
│   ├── pos_tagging.py
│   ├── utils.py      # Utility functions (logging, config loading)
├── tests/            # Unit tests
│   ├── test_ner.py
│   ├── test_pos_tagging.py
│   ├── test_text_extraction.py
├── results/          # Output files (e.g., analysis results)
├── notebooks/        # Jupyter notebooks for experimentation
├── config.yaml       # Configuration file (logging, NLP model settings)
├── main.py           # Entry point for the application
├── requirements.txt  # List of dependencies
└── README.md         # Project documentation
```

## Configuration

The `config.yaml` file allows you to customize the project settings:

- **Logging**: Adjust logging levels and output file.
- **NLP Model**: Switch between different SpaCy models (e.g., `en_core_web_sm`, `en_core_web_trf`).

### Example `config.yaml`:
```yaml
logging:
  level: INFO
  file: logs/grammatag.log

nlp:
  model: en_core_web_trf
```

## Running Tests

To ensure the functionality of the project, run the included unit tests:
```bash
uv run pytest tests/
```

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions, feedback, or support, feel free to reach out:

- **GitHub**: [Karthik-beta](https://github.com/Karthik-beta)
<!-- - **Email**: [Your Email Address] -->

## Acknowledgments

- **SpaCy**: For providing state-of-the-art NLP models.
- **UV**: For making dependency management fast and efficient.
- **Python Community**: For continuous support and innovation.

