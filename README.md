# Student Copilot AI

Student Copilot AI is a powerful and versatile educational assistance tool designed to help students with various aspects of their academic journey. It uses OpenAI's GPT-3 model to generate summaries, translations, brainstorm ideas, find quotes, generate outlines, and create study guides dynamically.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Adding API Key](#adding-api-key)
- [Usage](#usage)
- [Licence](#licence)

## Features

- **Summarizer**: Generate concise summaries of text files or user input.
- **Translator**: Translate text to different languages using GPT-3.
- **Brainstormer**: Generate thesis statements, arguments, and ideas for essay topics from user input or text files.
- **Quote Finder**: Discover relevant quotes from a given text or text file to support a specific topic or argument.
- **Outline**: Create an outline for an essay, including thesis statements, arguments, counterarguments, and direct quotes with user-defined specifications.
- **StudyGuide**: Generate study guides for exams and tests using bullet points, paragraphs, key definitions, and practice questions.

## Getting Started

To use the Student Copilot AI, you will need to clone the repository and install the necessary Python libraries.

1. Clone the repository:

   ```
   git clone https://github.com/patrickmaub/student-copilot.git
   ```

2. Install the necessary libraries:

   ```
   pip install openai
   ```

## Adding API Key

Before using the program, be sure to set your OpenAI API key as the environment variable `OPENAI_API_KEY`:

1. Locate your OpenAI API key from the OpenAI website. It should start with `sk-`.

2. Add an environment variable:

   - For Windows:
     ```
     setx OPENAI_API_KEY "your_api_key_here"
     ```

   - For macOS and Linux:
     ```
     export OPENAI_API_KEY="your_api_key_here"
     ```

## Usage

### Running the program
Simply run `main.py`:
```
python main.py
```

The program will present you with a list of available capabilities. Make a selection by entering its corresponding number, and follow the prompts.

### Example Usage

1. Selecting '1' for Summarizer:

   ```
   Welcome to the AI text summarizer. Would you like to input the text or pick a file?
   1. Input text
   2. Pick a file
   ```

   Choose whether to input the text directly or select a file, and follow the prompts for customizing the summary output.
