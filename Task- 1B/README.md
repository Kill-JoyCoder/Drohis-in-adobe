# Quick Start

This project can be run either with **Docker** (recommended for portability and consistency) or with a **local Python virtual environment**.  
The system works fully offline using only **CPU**.

---

## 1. Running with Docker (Recommended)

### a. Build the Docker Image

Open your terminal (Command Prompt or PowerShell on Windows) and run:

```bash
docker build -t docintelligence:latest .
```
b. Prepare Folders for Input/Output
Place your input PDF files in the pdfs/ directory at your project root.

Ensure there is an outputs/ directory for results.

c. Run in Interactive Mode (Prompts for Persona & Job)
```
docker run --rm -it -v %cd%\pdfs:/app/pdfs -v %cd%\outputs:/app/outputs docintelligence:latest
```

On prompt, enter:

Persona (e.g., PhD researcher in computational biology)

Job to be done (e.g., Prepare a comprehensive literature review...)

PDF file paths, comma-separated (e.g., pdfs/file1.pdf, pdfs/file2.pdf)

d. Run in CLI Argument Mode (All Info as Arguments)
```
docker run --rm -it -v %cd%\pdfs:/app/pdfs -v %cd%\outputs:/app/outputs docintelligence:latest ^
  "Persona here" "Job to be done here" pdfs/file1.pdf pdfs/file2.pdf
```
⚠️ For multi-line in PowerShell, use ^; for Bash (Linux/Mac), use \.

e. Retrieve Output
Find JSON results in the outputs/ folder.
Files will be named as:


extracted_persona_job_timestamp.json
Example:

outputs/extracted_phd_researcher_literature_review_20250728-223014.json


2. Running Without Docker (Python Virtual Environment)
a. Set Up Environment
```
python -m venv venv
venv\Scripts\activate     # On Windows
#
```
or:
```
source venv/bin/activate  # On Linux/Mac
```
b. Install Dependencies


```
pip install -r requirements.txt
```
c. Run the Application
With Prompts:
```
python app/main.py
```
You will be prompted for persona, job, and PDF file paths.

With All Arguments:
```
python app/main.py "Persona here" "Job to be done here" pdfs/file1.pdf pdfs/file2.pdf
```

3. Notes
All processing is offline (no network required).

JSON output structure matches the official hackathon template.

Works for any persona, any task, and supports 3–10 PDFs at once.

The system auto-filters non-informative document sections to maximize relevance.

If you experience "file not found" errors, ensure your PDF paths and folder structure match expectations.

4. Troubleshooting
File Not Found: Make sure the PDFs exist in pdfs/ and supply correct names.

Dependencies Not Installing: Ensure Python 3.10+, Docker, and pip are installed.

Output Missing: Check the outputs/ directory; filenames include persona/job/timestamp.

For any issues, consult README.md troubleshooting section or contact the project owner.

---

### ✅ Instructions

1. Copy the entire Markdown content above.
2. Open your GitHub repository.
3. Open or create the file `README.md`.
4. Paste the content.
5. Commit the changes.

Let me know if you'd like to embed images, add badges, or include example screenshots.
