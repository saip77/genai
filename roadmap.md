# 🚀 GenAI & AI Agent Learning Roadmap

This roadmap is designed to guide you through the essential concepts and practical skills needed to work with Generative AI and AI Agents, from foundational knowledge to advanced topics and production readiness.

---

## 🗓️ Month 1: Python, Tooling & ML/DL Foundations
🎯 **Goal:** Master Python, set up the ecosystem, and gain foundational ML/DL knowledge essential for working with GenAI.

### 🔧 Environment & Tooling
*   `Conda` vs `Miniconda` vs `Miniforge`
*   `venv` vs `pipenv` vs `poetry`
*   Python installation & `PATH` setup
*   Working with environments (conda, venv)
*   Jupyter Notebooks vs JupyterLab
*   IDEs: VSCode, PyCharm (quick intro)
*   Installing key packages (`pip`, `conda`, `requirements.txt`)
*   Git + GitHub basics (cloning, pushing code, version control)

### 🐍 Python Refresher (Essentials Only)
*   Lists, Tuples, Sets (in one day)
*   Dictionaries & Comprehensions
*   Loops, Conditions, Functions
*   Modules & Packages
*   Exception Handling
*   File I/O basics
*   Object-Oriented Python (Classes, `__init__`, inheritance)

### 📚 ML & DL Core Concepts (Essentials for GenAI)
*   What is Machine Learning? (Supervised, Unsupervised, Reinforcement)
*   Linear Regression, Logistic Regression (Core Intuition)
*   Loss functions: MSE, Cross-Entropy
*   Training vs Testing vs Validation
*   Introduction to Neural Networks
*   Perceptrons, activation functions (ReLU, Sigmoid, Softmax)
*   Forward and backward propagation
*   Epochs, batch size, learning rate
*   Overfitting & regularization (dropout, early stopping)
*   Deep Learning with PyTorch or TensorFlow (basic overview)
*   Introduction to GPU usage and CUDA (optional but recommended)

---

## 🗓️ Month 2: LLM Foundations & Prompt Engineering
🎯 **Goal:** Understand how LLMs work, and how to interact with them effectively.

### 🔍 LLM Core Concepts
*   What is a Large Language Model (LLM)?
*   Transformer Architecture (Conceptual)
*   Self-Attention & Multi-Head Attention (MHA)
*   Decoder-only vs Encoder–Decoder models
*   Pretraining vs Fine-tuning
*   Tokenization: BPE, WordPiece
*   Token Limits, Truncation & Context Windows
*   Token-Based Pricing & API Costs
*   Streamed vs Non-Streamed Generation
*   Open vs Closed-weight Models
*   Model Families: GPT, Claude, Gemini, Mistral, LLaMA, BART

### 🔧 Generation Controls
*   Temperature
*   Top-p Sampling (Nucleus Sampling)
*   Frequency & Presence Penalties
*   Stopping Criteria

### ✍️ Prompt Engineering
*   What is Prompt Engineering?
*   Role-based prompting & context control
*   Output formatting with examples
*   Chain-of-Thought (CoT) prompting
*   Iterative prompt refinement
*   Function calling (conceptual only)
*   Prompt Engineering vs Fine-Tuning
*   Reasoning vs Standard LLM Behavior

---

## 🗓️ Month 3: RAG, Embeddings & Vector DBs
🎯 **Goal:** Build Retrieval-Augmented Generation systems and master semantic search.

### 🔠 Embeddings & Semantic Search
*   What are Embeddings?
*   Word2Vec vs Transformer Embeddings
*   Cosine Similarity & Distance Metrics
*   Vector Search vs Keyword Search

### 🧱 Vector Databases
*   FAISS, Chroma, Weaviate, Redis (overview)
*   Chunking Strategies & Text Splitting
*   Metadata & Filtering
*   Indexing and Query Flow
*   Memory Compression, Aging & User Profiles

### 🔄 RAG Architectures
*   What is RAG?
*   RAG Flow: Query → Retrieve → Generate
*   Hybrid RAG (Keyword + Embedding)
*   Multimodal RAG (images, PDFs, tables)
*   Evaluation of RAG outputs (Precision, Recall, Relevance)

---

## 🗓️ Month 4: AI Agents
🎯 **Goal:** Understand how agents think, plan, use tools, and maintain memory.

### 🧠 Agent Fundamentals
*   What Are AI Agents?
*   The Agent Loop (Perceive → Plan → Act → Reflect)
*   Tools: APIs, Code Execution, Web, DBs, Files
*   Tool Schema: I/O, Description, Error Handling

### 🧠 Memory in Agents
*   Short-Term vs Long-Term Memory
*   Episodic vs Semantic Memory
*   In-Prompt vs External Vector DB Memory
*   State Persistence Between Sessions

### 🔍 Reasoning, Planning & Acting
*   Perception / Input Parsing
*   Action Execution
*   Reflection / Self-Feedback
*   Prompt Chains vs Agentic Planning

### 🏗 Agent Architectures
*   ReAct (Reason + Act)
*   Tree of Thought (ToT)
*   Planner–Executor Architecture
*   DAG Agents
*   MCP (Model Context Protocol)
*   LangGraph: DAG-based orchestration for Agents

### 🛠 Building Agents
*   Manual Agent Building (Conceptual)
*   OpenAI Function Calling (Theory)
*   Assistant API: Threads, Tools, Planning
*   LangChain: Chains, Agents, Tools
*   LlamaIndex: Indexing & RAG pipelines
*   CrewAI / AutoGen / Smol-AI (Multi-Agent Systems)

---

## 🗓️ Month 5: Advanced Topics (GenAI & Agents in Production)
🎯 **Goal:** Explore cutting-edge GenAI research and production readiness.

### 🧠 Advanced GenAI Concepts
*   Multimodal Models: GPT-4o, LLaVA, Gemini, BLIP
*   Mixture of Experts (MoE)
*   FlashAttention / Multi-Query Attention (MQA)

### 🧠 Advanced Agent Concepts
*   Agent Evaluation: Accuracy, Latency, Relevance
*   LangSmith: Tracing, Logging, Evaluation
*   Security, Prompt Injection, Red Teaming
*   Guardrails & Hardening LLM Systems

---

## 🗓️ Month 6: Optional / Expert-Level Topics
🎯 **Goal:** For learners aiming to deploy models, fine-tune them, or run them locally.

*   LoRA & QLoRA: Low-rank fine-tuning
*   Quantization: 8-bit, 4-bit, AWQ
*   Distillation: Knowledge Distillation (e.g., DistilBERT, TinyLLaMA)
*   RLHF: Reinforcement Learning with Human Feedback
*   Supervised Fine-Tuning (SFT)
*   Preference Modeling (BPR)
*   DPO (Direct Preference Optimization)
*   Connecting to Enterprise Systems (RDBMS, APIs, ETL Pipelines)
*   Running LLMs Locally (LLama.cpp, Ollama, etc.)
