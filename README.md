# Shopfloor AI

A free, 90-day course in AI for PLM and digital manufacturing, with a focus on **generative AI, agentic AI and the Model Context Protocol (MCP)**.

**Open the course:** https://aditykulkarni.github.io/shopfloor-ai/

## The plan

- **13 weeks, 26 units, 104 sessions**, starting Monday 12 October 2026 and finishing the week of 4 January 2027.
- About **12 hours a week**: two units a week, each with lessons, a hands-on lab, a manufacturing case and a quiz.
- **Six parts**, each ending in a shipped project:

| Part | Units | Weeks | Topic | Project |
|---|---|---|---|---|
| 1 | 1–4 | 1–2 | Python and product data | BOM health checker |
| 2 | 5–8 | 3–4 | Machine learning, vision and how generative models work | Predictive maintenance with an honest ROI |
| 3 | 9–13 | 5–7 | Prompting, RAG and evaluation | PLM document copilot |
| 4 | 14–17 | 7–9 | Tool calling, workflows and agents | Change impact agent with approval |
| 5 | 18–21 | 9–11 | MCP servers, hosts and security | PLM MCP servers |
| 6 | 22–26 | 11–13 | Value cases, LLMOps and deployment | Deployed engineering assistant |

A mid-course exam follows Unit 12 and a final exam follows Unit 26. The site also has formula sheets, flashcards, a project page and a presales AI kit.

## What you need

- Python 3.11 or later, VS Code and Git.
- [Ollama](https://ollama.com) with `qwen2.5:3b` and `nomic-embed-text` for local labs.
- Free accounts only: Kaggle, GitHub, Streamlit Community Cloud, and a free API key from Groq or Google AI Studio for the deployed capstone.

All data is public or synthetic. The `data/` folder holds the synthetic Sahyadri Motors E3 electric scooter dataset (parts, EBOM, MBOM, changes and 16 engineering documents) used across the labs.

## Saving your progress

Progress, quiz scores and notes are kept in your browser. To sync across devices, create a **private** repository named `shopfloor-ai-progress` and sign in on the site with a fine-grained token that can only read and write that repository.

## Structure

```
index.html            the course player
content/syllabus.json parts, resources and file list
content/m1a..m6b.html sessions for each part
content/revision.json formulas and flashcards
content/library.html  projects and presales kit
data/                 synthetic dataset and its generator
```
