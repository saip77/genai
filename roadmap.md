# Roadmap for Gen AI and AI Agents

## 📌 Day 0: Preliminaries
- Overview of Python & AI Ecosystem (for vocabulary, APIs, no coding)

---

## 🧭 Part 1: LLM Foundations & Prompt Engineering (Days 1–25)

### 🔍 LLM Core Concepts
1. What is a Large Language Model (LLM)?
2. Transformer Architecture (Conceptual Overview)
3. Attention Mechanism (Self-Attention Concept)
4. Pretraining vs. Fine-Tuning
5. Decoder-Only vs Encoder-Decoder Models
6. Tokenization: BPE, WordPiece (Theory)
7. Open vs Closed-Weight Models
8. Model Families: GPT, Claude, Gemini, Mistral, LLaMA
9. Context Windows & Limitations
10. Token Limits & Truncation
11. Token-Based Pricing Models
12. Streamed vs Unstreamed Generation

### 🔧 Generation Controls
13. Temperature
14. Top-p Sampling (Nucleus Sampling)
15. Frequency Penalty
16. Presence Penalty
17. Stopping Criteria

### 🧠 Prompt Engineering
18. What is Prompt Engineering?
19. Role-based Prompts & Context Inclusion
20. Format, Output Control & Examples
21. Iterative Prompt Refinement
22. Chain-of-Thought Prompting (CoT)
23. Function Calling (Concept Only)
24. Prompt Engineering vs. Fine-Tuning
25. Reasoning vs. Standard LLM Behavior

---

## 🧩 Part 2: RAG, Embeddings & Vector DBs (Days 26–35)

26. What are Embeddings? (Semantic Vectors)
27. Vector Search vs Keyword Search
28. Cosine Similarity (Conceptual)
29. Vector DBs: FAISS, Chroma, Weaviate, Redis
30. Chunking Strategies & Metadata
31. What is RAG (Retrieval-Augmented Generation)?
32. RAG Architecture (Query → Retrieve → Generate)
33. Hybrid & Multimodal RAG
34. Summarization & Memory Compression
35. Forgetting / Aging / User Profiles in RAG

---

## 🤖 Part 3: AI Agents (Days 36–65)

### 🔁 Agent Loop & Planning
36. What Are AI Agents?
37. The Agent Loop (Perceive → Plan → Act → Reflect)
38. Tool Use in Agents: Definition & Purpose
39. Tool Schema: Input/Output, Description, Error Handling
40. Examples of Tools: APIs, Code, DBs, File Access, Web Search

### 🧠 Agent Memory
41. Short-Term vs. Long-Term Memory
42. Episodic vs Semantic Memory
43. Vector-Based Memory Concepts
44. Memory in Prompts vs External Vector DBs
45. State Management Across Sessions

### 🧠 Agent Reasoning & Architecture
46. Perception & Input Parsing
47. Reasoning and Planning in Agents
48. Acting: Tool Execution
49. Observation & Reflection Mechanisms
50. Prompt Chains vs Agentic Planning

### 🧠 Agent Architectures
51. ReAct (Reason + Act)
52. Tree of Thought (ToT)
53. Planner–Executor Architecture
54. DAG Agents (Directed Acyclic Graphs)
55. MCP (Model Context Protocol) Overview
56. **LangGraph**: DAG-based Orchestration for Agents

### 🔨 Building & Using Agents
57. Manual Agent Construction (Conceptual Only)
58. OpenAI Function Calling (Concept Overview)
59. OpenAI Assistant API (Planning, Threads, Tools)
60. **LangChain**: Chains, Agents, and Tools (Theory)
61. **LlamaIndex**: Document Indexing & Connectors
62. CrewAI / AutoGen / Smol-AI: Multi-Agent Systems

### 📊 Evaluation, Monitoring & Ethics
63. Agent Evaluation Metrics (Accuracy, Latency, Relevance)
64. **LangSmith**: Tracing, Logging, Evaluation
65. Security & Ethics: Prompt Injection, Red Teaming, Guardrails

---

## 🧪 Optional Advanced Add-ons (Days 66–70)

66. Multimodal GenAI: GPT-4o, LLaVA, BLIP
67. Mixture of Experts (MoE) Architectures
68. LoRA & QLoRA (Fine-Tuning Techniques)
69. Quantization: 8-bit, 4-bit, AWQ Concepts
70. Enterprise Data Connectors (RDBMS, APIs, ETL Pipelines)

---
