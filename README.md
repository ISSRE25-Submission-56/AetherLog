# AetherLog

AetherLog is a synergistic framework for log-based root cause analysis (RCA), combining the semantic reasoning power of large language models (LLMs) with the structure and domain specificity of knowledge graphs (KGs). Designed for modern large-scale distributed systems, it provides an accurate, explainable, and efficient way to identify system faults.

## 🔍 Key Features

- **LLM + KG Integration**: Combine context-aware log understanding with structured fault knowledge.
- **Semantic Entity Aggregation**: Normalize redundant or similar fault indicators via embedding-based clustering.
- **Context-Aware Retrieval**: Dynamically recall relevant fault entities from the KG based on summarized logs.
- **Prompt-Driven RCA**: Construct powerful prompts to guide LLMs in accurate fault reasoning.
- **Modular & Extensible**: Fully script-based pipeline with CLI tools for preprocessing, KG construction, RCA, and evaluation.

## 📦 Installation

```bash
pip install .
```

## 🚀 Quick Start

1. **Preprocess Logs**
```bash
aetherlog-preprocess --input data/raw_logs.json --output data/summary.json
```

2. **Build Knowledge Graph**
```bash
aetherlog-buildkg
```

3. **Recall Entities**
```bash
aetherlog-recall --log data/summary.json --entity data/kg.json --output data/recalled.json
```

4. **Construct RCA Prompt**
```bash
aetherlog-prompt --summary data/summary.json --entity data/recalled.json --output data/prompt.json
```

5. **Run RCA Analysis**
```bash
aetherlog-rca --log data/summary.json --kg data/kg.json --out data/result.json
```

6. **Evaluate Performance**
```bash
aetherlog-eval --pred data/result.json --gold data/groundtruth.json
```

## 📁 Project Structure
```
AetherLog/
├── scripts/            # Main RCA pipeline scripts
├── src/                # Core modules (LLM interface, KG, model)
├── data/               # Input logs, KG and results
├── configs/            # YAML configuration files
├── setup.py            # Install and entry points
└── README.md           # Project description
```

## 📄 Citation
If you find AetherLog useful for your research, please cite the paper:

```bibtex
@article{aetherlog2025,
  title={AetherLog: Log-based Root Cause Analysis by Integrating Large Language Models with Knowledge Graphs},
  author={...},
  journal={International Symposium on Software Reliability Engineering.},
  year={2025}
}
```

## 🔗 Links
- [Code](https://github.com/ISSRE25-Submission-56/AetherLog)
