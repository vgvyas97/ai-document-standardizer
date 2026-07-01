# 📝 AI Documentation Standardizer & Replicator

An automated technical writing tool designed to eliminate structural documentation drift, reduce friction in engineering team offboardings/onboardings, and implement a rigid "Documentation-as-Code" standard. This web application transforms chaotic, unformatted engineer logs and rough notes into production-grade, compliance-ready Markdown documents (SOPs, Runbooks, and Knowledge Bases) using deterministic AI layout replication.

## 🚀 The Operational Problem Solved
In scaling enterprise environments, internal documentation (Confluence, wikis, repositories) becomes highly fragmented. Engineers write documentation using varying structures, lengths, and levels of technical depth, resulting in stale runbooks that increase MTTR during critical incident responses. 

**This solution automates the standardization phase**, allowing raw technical brain-dumps to be instantaneously mapped into the organization's mandatory templates.

---

## 🛠️ Architecture & Tech Stack

* **Frontend Framework:** Streamlit (Python-native layout engine)
* **AI Engine Framework:** OpenAI SDK API wrapper
* **Upstream Cloud Provider:** Google AI Studio (Gemini 3.5 Flash engine)
* **Design Pattern:** Dynamic Target-Template Mapping

---

## ⚙️ Core Features
* **Dual-Column Contextual Architecture:** Implements a side-by-side workspace allowing real-time mapping of unstructured source text against variable structural layouts.
* **Deterministic Layout Ingestion:** Uses zero-temperature parameter controls to force the cloud language model to mirror structural headers precisely, preventing layout hallucinations.
* **Intelligent Auto-Generation:** If critical context is missing from the engineering notes, the system relies on predefined systems administration rules to insert contextually safe placeholder guidelines.

---

## 💻 Local Setup & Execution

### Prerequisites
* Python 3.9 or higher installed
* A valid Google AI Studio (Gemini) API Key

### Installation & Initialization
1. Clone the repository to your desktop machine:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/ai-document-standardizer.git](https://github.com/YOUR_GITHUB_USERNAME/ai-document-standardizer.git)
   cd ai-document-standardizer
