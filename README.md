What This Project Is
This tool acts as a “document analyst”: it extracts and ranks the most relevant PDF sections based on:

Your persona (e.g., student, analyst, researcher, manager)

Your job-to-be-done (e.g., find exam concepts, summarize trends, review literature)

Works for:

Business, academic, technical, or any PDF domain

Any persona, any need—no hardcoding!

1A vs 1B Support
1A — Prebuilt use-cases:

Can be integrated into larger workflows, optionally accepts persona/job via config files or scheduled runs.

Follows standardized folder mounts for input/output and model location.

1B — User-driven tasks:

Accepts persona, job, and PDFs at runtime (interactive or CLI arguments)

Outputs hackathon-compliant JSON files, including rich summaries for each result

Features
Multi-document analysis: Handles 3–10 PDFs per run

Semantic relevance: State-of-the-art embeddings match user context to document content

Generic parsing: No persona-specific rules—runs for ANY role/task

Fast and efficient: <1GB model, CPU-only, <60s for 3–5 PDFs

Simple to run: Interactive mode and full CLI support, runs inside Docker or plain Python
