# 🪜 Phase 0: Python & AI Ecosystem Setup
**Goal:** Set up the environment and master core Python needed for AI work.

## 🔧 Environment & Tooling
* Conda vs Miniconda vs Miniforge
* venv vs pipenv vs poetry
* Python installation & PATH setup
* Working with environments (conda, venv)
* Jupyter Notebooks vs JupyterLab
* IDEs: VSCode, PyCharm (quick intro)
* Installing key packages (pip, conda, requirements.txt)
* Git + GitHub basics (cloning, pushing code, version control)

## 🐍 Python Refresher (Essentials Only)
* Lists, Tuples, Sets (in one day)
* Dictionaries & Comprehensions
* Loops, Conditions, Functions
* Modules & Packages
* Exception Handling
* File I/O basics
* Object-Oriented Python (Classes, `__init__`, inheritance)

# 📘 Phase 1: LLM Foundations & Prompt Engineering
**Goal:** Understand how LLMs work, and how to control and interact with them.

## 🔍 LLM Core Concepts
* What is a Large Language Model (LLM)?
* Transformer Architecture (Conceptual)
* Self-Attention & Multi-Head Attention (MHA)
* Decoder-only vs Encoder–Decoder models
* Pretraining vs Fine-tuning
* Tokenization: BPE, WordPiece
* Token Limits, Truncation & Context Windows
* Token-Based Pricing & API Costs
* Streamed vs Non-Streamed Generation
* Open vs Closed-weight Models
* Model Families: GPT, Claude, Gemini, Mistral, LLaMA, BART

## 🔧 Generation Controls
* Temperature
* Top-p Sampling (Nucleus Sampling)
* Frequency & Presence Penalties
* Stopping Criteria

## ✍️ Prompt Engineering
* What is Prompt Engineering?
* Role-based prompting & context control
* Output formatting with examples
* Chain-of-Thought (CoT) prompting
* Iterative prompt refinement
* Function calling (conceptual only)
* Prompt Engineering vs Fine-Tuning
* Reasoning vs Standard LLM Behavior

# 🧩 Phase 2: RAG, Embeddings & Vector DBs
**Goal:** Deep dive into Retrieval-Augmented Generation (RAG) systems.

## 🔠 Embeddings & Semantic Search
* What are Embeddings?
* Word2Vec vs Transformer Embeddings
* Cosine Similarity & Distance Metrics
* Vector Search vs Keyword Search

## 🧱 Vector Databases
* FAISS, Chroma, Weaviate, Redis (overview)
* Chunking Strategies & Text Splitting
* Metadata & Filtering
* Indexing and Query Flow
* Memory Compression, Aging & User Profiles

## 🔄 RAG Architectures
* What is RAG?
* RAG Flow: Query → Retrieve → Generate
* Hybrid RAG (Keyword + Embedding)
* Multimodal RAG (images, PDFs, tables)
* Evaluation of RAG outputs (Precision, Recall, Relevance)

# 🤖 Phase 3: AI Agents
**Goal:** Understand how agents think, plan, use tools, and maintain memory.

## 🧠 Agent Fundamentals
* What Are AI Agents?
* The Agent Loop (Perceive → Plan → Act → Reflect)
* Tools: APIs, Code Execution, Web, DBs, Files
* Tool Schema: I/O, Description, Error Handling

## 🧠 Memory in Agents
* Short-Term vs Long-Term Memory
* Episodic vs Semantic Memory
* In-Prompt vs External Vector DB Memory
* State Persistence Between Sessions

## 🔍 Reasoning, Planning & Acting
* Perception / Input Parsing
* Action Execution
* Reflection / Self-Feedback
* Prompt Chains vs Agentic Planning

## 🏗 Agent Architectures
* ReAct (Reason + Act)
* Tree of Thought (ToT)
* Planner–Executor Architecture
* DAG Agents
* MCP (Model Context Protocol)
* LangGraph: DAG-based orchestration for Agents

## 🛠 Building Agents
* Manual Agent Building (Conceptual)
* OpenAI Function Calling (Theory)
* Assistant API: Threads, Tools, Planning
* LangChain: Chains, Agents, Tools
* LlamaIndex: Indexing & RAG pipelines
* CrewAI / AutoGen / Smol-AI (Multi-Agent Systems)

# 🚀 Phase 4: Advanced Topics (GenAI & Agents)
**Goal:** Explore cutting-edge research and production-level architecture.

## 🧠 Advanced GenAI Concepts
* Multimodal Models: GPT-4o, LLaVA, Gemini, BLIP
* Mixture of Experts (MoE)
* FlashAttention / Multi-Query Attention (MQA)

## 🧠 Advanced Agent Concepts
* Agent Evaluation: Accuracy, Latency, Relevance
* LangSmith: Tracing, Logging, Evaluation
* Security, Prompt Injection, Red Teaming
* Guardrails & Hardening LLM Systems

# 🔧 Phase 5: Optional / Expert Topics
**Goal:** For learners aiming at finetuning, deployment, or model building.

* LoRA & QLoRA: Low-rank fine-tuning
* Quantization: 8-bit, 4-bit, AWQ
* Distillation: Knowledge Distillation (e.g., DistilBERT, TinyLLaMA)
* RLHF: Reinforcement Learning with Human Feedback
* Supervised Fine-Tuning (SFT)
* Preference Modeling (BPR)
* DPO (Direct Preference Optimization)
* Connecting to Enterprise Systems (RDBMS, APIs, ETL Pipelines)
* Running LLMs Locally (LLama.cpp, Ollama, etc.)