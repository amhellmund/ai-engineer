# AI Engineering Fundamentals

A 120-day, hands-on curriculum that builds solid knowledge of AI / ML / LLM / GenAI
— from base components (PyTorch, embeddings, transformers, training loops) through
fine-tuning, alignment, evaluation, and up to retrieval, agents, and LLMOps.

- **Format:** one tutorial per day, ~30 minutes each
- **Structure:** 24 sections × 5 tutorials = 120 tutorials
- **Arc:** Foundations → Transformers & internals → Using LLMs → Fine-tuning track →
  Applications (RAG, agents) → Production & capstone

---

## Sections Overview

| # | Section | Theme |
|---|---------|-------|
| 1 | AI Engineering Foundations & Setup | Tooling, Python, workflow |
| 2 | Math & Data Essentials for ML | The minimum viable math |
| 3 | PyTorch Fundamentals | Tensors, autograd, training loop |
| 4 | Neural Networks & Deep-Network Training | Perceptron → MLP → backprop, optimizers |
| 5 | Embeddings & NLP Foundations | Dense vectors, classical NLP, RNNs |
| 6 | The Transformer Architecture | Self-attention from scratch |
| 7 | Modern Transformer Internals | RoPE, GQA/MQA, RMSNorm, SwiGLU |
| 8 | KV Caching & Efficient Inference | KV cache, PagedAttention, speculative decoding |
| 9 | Tokenization, Losses & Optimization | BPE, cross-entropy, AdamW |
| 10 | Encoders, Decoders & Pretraining Objectives | BERT / GPT / T5, transfer learning |
| 11 | Building & Training a Small LLM | nanoGPT-style hands-on |
| 12 | Working with Pretrained LLMs & APIs | HF ecosystem, Claude API, local models |
| 13 | Prompt Engineering & In-Context Learning | Prompting, CoT, structured output |
| 14 | PEFT: LoRA & QLoRA | Low-rank adapters |
| 15 | Fine-Tuning Pipelines: Axolotl & Unsloth | Modern FT stack, hands-on |
| 16 | Data Engineering for Fine-Tuning | Curation, synthetic data |
| 17 | Alignment & Preference Optimization | SFT, RM, DPO/ORPO/SimPO |
| 18 | LLM Evaluation & Observability | lm-eval-harness, LLM-as-judge |
| 19 | Quantization, Serving & Model Merging | GPTQ/AWQ/GGUF, vLLM, mergekit |
| 20 | Retrieval-Augmented Generation (RAG) | Chunking → pipeline → eval |
| 21 | Vector Databases & Search Infrastructure | ANN, FAISS, production DBs |
| 22 | AI Agents | ReAct, tools, multi-agent |
| 23 | Production LLMOps: Serving, Monitoring & Security | Deploy, observe, guardrails |
| 24 | Capstone & Responsible AI | End-to-end build, ethics, portfolio |

---

## Tutorials by Section

### Section 1 — AI Engineering Foundations & Setup
1. What is AI Engineering? The landscape & your roadmap
2. Environment setup (Python, `uv`/conda, Jupyter, VS Code)
3. Python essentials for ML (NumPy arrays & vectorization)
4. Data manipulation crash course with Pandas
5. Reproducibility basics: Git, seeds & experiment tracking (W&B)

### Section 2 — Math & Data Essentials for ML
6. Linear algebra for ML (vectors, matrices, dot products)
7. Calculus & gradients (derivatives, chain rule, partials)
8. Probability & statistics essentials (distributions, Bayes)
9. Gradient descent intuition (cost surfaces, learning rate)
10. Data preprocessing (scaling, normalization, train/val/test splits)

### Section 3 — PyTorch Fundamentals
11. Tensors: creation, indexing, broadcasting, ops
12. Autograd: automatic differentiation explained
13. Building models with `nn.Module`
14. `Dataset` & `DataLoader`
15. Your first training loop (linear regression end-to-end)

### Section 4 — Neural Networks & Deep-Network Training
16. Perceptron, neurons & activation functions (ReLU, sigmoid, tanh, GELU)
17. Multilayer perceptrons & the forward pass
18. Backpropagation explained *and* implemented
19. Build an MLP classifier on MNIST
20. Training essentials: loss functions, optimizers, regularization, normalization

### Section 5 — Embeddings & NLP Foundations
21. What are embeddings? One-hot → dense vectors
22. Word2Vec, GloVe & training your own embeddings
23. Similarity & distance metrics; visualizing embeddings (PCA, t-SNE, UMAP)
24. Classical NLP (tokenizing, BoW, TF-IDF) & sequence models (RNN/LSTM/GRU)
25. Sequence-to-sequence models & the attention mechanism (intuition & origins)

### Section 6 — The Transformer Architecture
26. Transformer overview: *Attention Is All You Need*
27. Scaled dot-product self-attention
28. Multi-head attention
29. Positional encodings (sinusoidal & learned)
30. Build a full Transformer block from scratch

### Section 7 — Modern Transformer Internals
31. Rotary Positional Embeddings (RoPE) — theory & from-scratch impl
32. Grouped-Query & Multi-Query Attention (GQA/MQA)
33. RMSNorm, SwiGLU & pre-norm: the modern block recipe
34. Building a Llama/Qwen-style decoder block end-to-end
35. Long-context techniques (RoPE/NTK scaling, ALiBi, sliding-window)

### Section 8 — KV Caching & Efficient Inference
36. The KV cache: why autoregressive decoding caches keys & values
37. Implementing a KV cache in a mini-decoder (prefill vs. decode)
38. Memory math: KV-cache size, GQA savings & KV-cache quantization
39. PagedAttention & continuous batching (the vLLM idea)
40. Speculative & assisted decoding for faster generation

### Section 9 — Tokenization, Losses & Optimization
41. Tokenization fundamentals (word / char / subword)
42. BPE & WordPiece; building with Hugging Face `tokenizers`
43. LM loss functions: cross-entropy, label smoothing, perplexity
44. Optimization deep dive: SGD → Adam → AdamW (decoupled weight decay)
45. Warmup, LR schedules, gradient clipping & mixed precision

### Section 10 — Encoders, Decoders & Pretraining Objectives
46. Encoder-only models (BERT) & masked language modeling
47. Decoder-only models (GPT) & causal language modeling
48. Encoder-decoder models (T5, BART)
49. Pretraining objectives compared
50. Transfer learning & the pretrain → finetune paradigm

### Section 11 — Building & Training a Small LLM
51. Anatomy of a GPT-style model
52. Implement a mini-GPT (nanoGPT style)
53. Train your mini-GPT on a small corpus
54. Decoding strategies (greedy, beam, top-k, top-p, temperature)
55. Scaling laws & compute considerations

### Section 12 — Working with Pretrained LLMs & APIs
56. The Hugging Face ecosystem (transformers, hub, pipelines)
57. Running open models locally (Llama, Mistral, Qwen)
58. The Claude API: Messages, system prompts & parameters
59. Streaming, tool use & structured outputs with Claude
60. Quantization & efficient inference (intro: bitsandbytes, vLLM)

### Section 13 — Prompt Engineering & In-Context Learning
61. Anatomy of a good prompt
62. Few-shot & in-context learning
63. Chain-of-thought & reasoning techniques
64. Structured output & function/tool calling
65. Prompt patterns, templates & prompt management

### Section 14 — PEFT: LoRA & QLoRA
66. When to fine-tune vs. prompt vs. RAG; full FT vs. PEFT trade-offs
67. LoRA explained (low-rank adapters, rank/alpha, target modules)
68. QLoRA (4-bit NF4, double quant, paged optimizers)
69. Hands-on LoRA with the PEFT library on Qwen2.5-1.5B
70. Merging adapters, multi-adapter serving & when full FT pays off

### Section 15 — Fine-Tuning Pipelines: Axolotl & Unsloth
71. The fine-tuning stack: Axolotl, Unsloth, TRL, PEFT — how they fit
72. Unsloth deep dive: 2× faster, low-VRAM QLoRA run
73. Axolotl deep dive: YAML-config-driven training & multi-GPU
74. End-to-end SFT run on Phi-3-mini / Qwen2.5-1.5B with chat templates
75. Reproducibility: configs, checkpointing, resuming & W&B logging

### Section 16 — Data Engineering for Fine-Tuning
76. Dataset curation & formats (ShareGPT / ChatML / Alpaca)
77. Synthetic data generation I: Self-Instruct
78. Synthetic data generation II: Evol-Instruct & distillation from a teacher
79. Quality filtering, dedup, decontamination & difficulty balancing
80. Domain-specific datasets, sample packing & formatting

### Section 17 — Alignment & Preference Optimization
81. Post-training overview: SFT → preference optimization; chat formatting
82. RLHF classic: reward modeling & PPO (concepts)
83. DPO — direct preference optimization explained
84. ORPO & SimPO — reference-free / no-reward-model modern methods
85. Hands-on DPO run with TRL on your SFT checkpoint

### Section 18 — LLM Evaluation & Observability
86. Why eval is hard; perplexity, metrics & contamination
87. Benchmarking with lm-evaluation-harness (MMLU, GSM8K, …)
88. LLM-as-a-judge (pairwise, rubric, bias mitigation)
89. Building task-specific eval sets & failure analysis
90. Experiment tracking & observability (W&B, Langfuse)

### Section 19 — Quantization, Serving & Model Merging
91. Post-training quantization: GPTQ vs. AWQ
92. GGUF & llama.cpp; running quantized models locally
93. High-throughput serving with vLLM & TGI
94. Local/edge serving with Ollama; API design & guardrails
95. Model merging with mergekit (SLERP, TIES, DARE, task arithmetic)

### Section 20 — Retrieval-Augmented Generation (RAG)
96. RAG fundamentals & architecture (why/when retrieval beats fine-tuning)
97. Document loading, chunking strategies & embedding
98. Build a basic RAG pipeline end-to-end
99. Advanced RAG (reranking, hybrid search, query rewriting, HyDE)
100. Evaluating RAG (faithfulness, context precision/recall, RAGAS)

### Section 21 — Vector Databases & Search Infrastructure
101. Vector search & ANN algorithms (HNSW, IVF, PQ)
102. FAISS hands-on
103. Production vector DBs (pgvector, Qdrant, Weaviate, Pinecone, Chroma)
104. Hybrid search, metadata filtering & BM25 fusion
105. Scaling, indexing trade-offs & retrieval-latency optimization

### Section 22 — AI Agents
106. What is an agent? The ReAct loop & agent anatomy
107. Tools & function calling; structured tool orchestration
108. Build an agent with the Claude Agent SDK / LangGraph
109. Memory, planning & multi-step reasoning
110. Multi-agent systems & orchestration patterns

### Section 23 — Production LLMOps: Serving, Monitoring & Security
111. Deployment patterns: containerization (Docker), cloud & serverless GPUs
112. Production inference (batching, autoscaling, response caching)
113. Observability: logging, tracing, cost & latency monitoring
114. Guardrails & safety (prompt injection, PII, content filtering, jailbreaks)
115. CI/CD for LLM apps: versioning, A/B testing & rollback

### Section 24 — Capstone & Responsible AI
116. Responsible & ethical AI (bias, transparency, governance, licensing)
117. System design: combining fine-tuning + RAG + agents
118. Capstone I — scope, curate data & fine-tune a domain model
119. Capstone II — evaluate, quantize & serve with guardrails
120. Capstone III — ship, monitor & write up (portfolio & next steps)
