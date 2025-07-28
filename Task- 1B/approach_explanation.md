Methodology Overview
This system is a general-purpose persona-driven document intelligence pipeline designed to extract and prioritize the most relevant sections from collections of PDF documents according to any user-defined persona and job-to-be-done. The entire workflow is designed for high efficiency (CPU-only, ≤1GB model) and is robust across any academic, business, or technical domain.

1. Generic PDF Parsing and Section Extraction
Each document is parsed using PyMuPDF. Pages are broken into text lines, and section headings are detected using a combination of font characteristics (boldness, size), short uppercase lines, and a broad list of common heading keywords (e.g., "Method", "Results", "Overview") that are valid across many domains. After a heading is detected, the related body lines are grouped with it to form a logical section, capturing the section title, page number, and the associated text for analysis. The parser intentionally avoids hardcoding around any persona or field—so it generalizes for scientists, analysts, students, and beyond. Filter logic excludes author bios, citation-only lines, and numeric-only titles to ensure sections are informative.

2. Persona and Task-Aware Embedding
The persona description and job-to-be-done are provided entirely by the user as free text on each run—no coding change needed. Both are concatenated into a "user intent" string and embedded using a compact local MiniLM sentence-transformer. Each parsed section's text is also embedded. This design supports semantic similarity regardless of specialty or user background, letting the system generalize the mapping from user request to document content.

3. Relevance Ranking
Section embeddings and the persona+job embedding are compared via cosine similarity to score and rank relevance automatically. This approach ensures that the highest-ranked sections truly match the user's personalized need, regardless of wording differences or document type.

4. Granular Sub-Section Summarization
To maximize informativeness in outputs, the top-ranked sections are summarized by extracting multiple important, keyword-rich sentences and expanding the summary with additional context as needed. The keyword list is broad and domain-neutral, so it does not privilege any field or persona type. The summary dynamically adapts to the section size/content, giving the user a rich snippet, not just a fragment.

5. Output and Generalization
Outputs are written as well-structured JSON including inputs, persona, job, timestamp, ranked sections, and detailed sub-section analyses. All user interaction is via simple prompts or CLI arguments—no code edits or persona-specific settings required. The model and code are kept lightweight and efficient to run offline on any modern CPU.
