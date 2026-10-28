# Automatic Resume Sorter

A Python-based project for automatically extracting, structuring, and preparing resume information for intelligent candidate screening. The project uses local Large Language Models (LLMs) through [Ollama](https://ollama.com/) to convert resume text into structured JSON data validated with Pydantic.

The long-term goal is to build a system that can evaluate resumes against a job description and rank candidates according to their relevance.

## Current Features

### 1. Resume Text Extraction

Extracts text from resumes in the following formats:

- PDF (`.pdf`)
- Microsoft Word (`.docx`)
- Plain text (`.txt`)

The PDF extraction pipeline uses PyMuPDF4LLM to produce Markdown-formatted text, with additional handling for two-column layouts. Word documents are processed using their paragraphs and tables.

### 2. LLM-Based Information Extraction

Uses a locally running Ollama model to extract relevant information from resume text.

The extraction process is divided into two stages:

**Core profile extraction**

- Personal information and contact details
- Professional summary and profile
- Education, including GPA when available
- Work experience
- Projects, including descriptions when provided

**Additional qualifications extraction**

- Technical and programming skills
- Published journal articles and conference papers
- Academic courses
- Certifications
- Languages and language proficiency tests
- Exam scores
- Honors and awards

The second extraction stage also receives the previously extracted core profile to help maintain consistency and reduce classification errors.

### 3. Structured JSON Output

Uses Pydantic models to define the expected data structure and validate the extracted information.

- Requests structured output using JSON Schema.
- Uses a temperature of `0` to encourage consistent extraction.
- Represents missing information using appropriate empty lists or `null` values, according to the schema.
- Applies post-processing rules, including adding English to the language list when an IELTS or TOEFL result is identified.

### 4. Local LLM Inference

Uses Ollama to run language models locally rather than relying on a cloud-based LLM API.

The current parser configuration uses `gemma3:4b`. Other compatible Ollama models can be tested by changing the configured model name.

## Project Structure

```text
Automatic_resume_sorter/
├── input_resumes/
│   └── ...                 # Input resumes
├── extracted_text/
│   └── ...                 # Extracted resume text
├── main.py                 # Main application workflow
├── resume_reader.py        # Resume text extraction
├── resume_parser.py        # LLM-based information extraction
├── resume_schema.py        # Pydantic data models
├── README.md
└── .gitignore
```

The exact directory contents may evolve as the project develops.

## Requirements

- Python 3.10 or later
- [Ollama](https://ollama.com/download) installed and running
- An Ollama-compatible language model
- Python packages:
  - `ollama`
  - `pydantic`
  - `pymupdf4llm`
  - `python-docx`

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sahandi78/Automatic_resume_sorter.git
cd Automatic_resume_sorter
```

### 2. Install Python dependencies

```bash
python -m pip install ollama pydantic pymupdf4llm python-docx
```

### 3. Install and prepare Ollama

Install Ollama from its official website, then download the configured model:

```bash
ollama pull gemma3:4b
```

Verify that the model is available:

```bash
ollama list
```

Ensure the Ollama service is running before executing the Python application.

### 4. Prepare the input directory

Place the resumes you want to process in the `input_resumes/` directory, using one of the supported file formats.

## Usage

Run the main application from the project directory:

```bash
python main.py
```

The application workflow is designed to extract text from the input resumes, pass that text to the local LLM for information extraction, validate the structured results, and prepare JSON data for downstream processing.

The exact output location and processing behavior depend on the current implementation in `main.py`.

## Data Extraction Principles

The parser is designed to prioritize accuracy and avoid inventing information.

- Extract information only when supported by the resume text.
- Distinguish academic degrees from individual courses.
- Include only explicitly published journal articles and conference papers in the publications field.
- Preserve project descriptions when they are available.
- Inspect relevant subsections when extracting technical skills.
- Leave missing information empty instead of generating unsupported values.

Because LLM extraction is not perfectly reliable, generated JSON should be reviewed before being used for consequential recruitment decisions.

## Roadmap

Planned development includes:

- [ ] Improve extraction accuracy across different resume formats and layouts.
- [ ] Refine JSON schemas and validation rules.
- [ ] Optimize inference time when processing multiple resumes.
- [ ] Build a job-description-based candidate evaluation system.
- [ ] Rank resumes according to their relevance to a given job description.
- [ ] Evaluate extraction quality and ranking performance on representative test cases.

## Technologies

- **Python** — application logic and data processing
- **Ollama** — local LLM inference
- **Gemma 3** — current configured language model
- **Pydantic** — schema definition and data validation
- **PyMuPDF4LLM** — PDF text extraction and Markdown conversion
- **python-docx** — Microsoft Word document processing

## Disclaimer

This project is under active development. Extraction results may vary depending on resume formatting, model capabilities, and the information provided. The current focus is structured resume information extraction; automated candidate ranking against job descriptions is a future development goal.
