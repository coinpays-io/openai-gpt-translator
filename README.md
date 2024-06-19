![enter image description here](https://coinpays.ams3.cdn.digitaloceanspaces.com/marketing/openai-gpt-translator.png)


# Welcome to OpenAI GPT Translator From CoinPays!

A translation assistant developed using OpenAI's ChatGPT-3.5-Turbo.

## Overview

This project provides a simple translation assistant that leverages OpenAI's ChatGPT-3.5-Turbo model to translate text. It can be used to translate individual lines of text or entire files into specified languages.

## Features

- **Direct Translations**: Provides direct translations without additional information or formatting.
- **File Processing**: Translates the content of a file line by line and saves the translations to a new file.
- **Multi-language Support**: Easily extendable to support multiple target languages.

## Installation

### Prerequisites

- Python 3.6 or higher
- OpenAI API Key

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/coinpays-io/openai-gpt-translator.git
```

### Install Dependencies

Navigate to the repository directory and install the required dependencies:

```bash
cd openai-gpt-translator
pip install openai
```

## Usage

### Setting Up Your OpenAI API Key

Replace the placeholder `'[open_ai_api_key]'` in the `gpt_translator.py` file with your actual OpenAI API key. You can obtain an API key by signing up at [OpenAI](https://beta.openai.com/signup/).

### Translating Text

To translate text using the script, you can use the `translate_text` function. This function takes two parameters:

- `text`: The text to be translated.
- `prompt_language`: The target language for translation.

### Translating a File

To translate the contents of a file, use the `process_file` function. This function reads a file line by line, translates each line, and writes the translations to a new file.

#### Example Usage

1. Prepare your `word_list.txt` file with the text you want to translate.
2. Specify the target languages in the `languages` list (e.g., `["Turkish"]`).
3. Run the script:

```bash
python gpt_translator.py
```

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or feature requests, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or support, please open an issue on this repository or contact the project maintainers.

---

Thank you for using the OpenAI GPT Translator!
