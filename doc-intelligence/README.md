Quick Summary
This project requires Python 3.10 or Docker (recommended for reproducibility), runs solely on CPU, and takes PDFs along with user-specified persona and job as input. Output is a structured JSON file per run.

1. Running with Docker (Recommended)
a. Build the Docker Image
Open your terminal (Command Prompt/PowerShell on Windows) in your project root:

shell
docker build -t docintelligence:latest .
b. Prepare Input/Output Folders
Place your PDF files to be analyzed in the pdfs/ directory.

Ensure there is an (empty or existing) outputs/ folder at project root.

c. Run in Interactive Mode (Prompts for Persona/Job)
shell
docker run --rm -it -v %cd%\pdfs:/app/pdfs -v %cd%\outputs:/app/outputs docintelligence:latest
When prompted, enter:

Persona (e.g., PhD researcher in computational biology)

Job to be done (e.g., Prepare a comprehensive literature review...)

PDF file paths, comma-separated (e.g., pdfs/file1.pdf, pdfs/file2.pdf)

d. Run in CLI Arguments Mode
For non-interactive runs, provide persona, job, and PDF paths as arguments:

shell
docker run --rm -it -v %cd%\pdfs:/app/pdfs -v %cd%\outputs:/app/outputs docintelligence:latest ^
  "Persona here" "Job to be done here" pdfs/file1.pdf pdfs/file2.pdf
Note: use ^ to break lines in PowerShell; on Linux/macOS, use \.

e. Retrieve Output
The output JSON file will appear in outputs/.

Filename includes persona/job for easy ID, e.g.:

text
outputs/extracted_phd_researcher_prepare_a_comp_20250728-223014.json
2. Running Without Docker (Python Virtualenv)
a. Create and Activate Virtual Environment
shell
python -m venv venv
venv\Scripts\activate         # On Windows
# or source venv/bin/activate # On Linux/Mac
b. Install Dependencies
shell
pip install -r requirements.txt
c. Run Application
Interactive prompts:

shell
python app/main.py
Direct CLI arguments:

shell
python app/main.py "Persona here" "Job to be done here" pdfs/file1.pdf pdfs/file2.pdf
3. Input and Output
Input PDFs: Place in the pdfs/ folder (use full path inside Docker or local shell).

Output: Will appear in outputs/ with detailed metadata, section rankings, and summaries.

JSON output structure matches hackathon specification.

4. Important Notes
No internet is required at runtime; all models/dependencies are included.

System auto-filters uninformative sections and produces rich sub-section output.

Works for any persona, job, or PDF collection (3–10 files recommended).

For reproducibility, use the included requirements.txt and, if needed, the Dockerfile.

For any issues, please consult the README troubleshooting section or contact the project owner.
