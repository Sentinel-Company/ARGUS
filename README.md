# ARGUS: AI Relationship Graph & Underground Sentinel

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🎯 Mission

ARGUS is a decentralized, autonomous investigative platform designed to analyze massive data leaks (Epstein Files, Pandora Papers, etc.) and expose hidden networks of corruption, financial crimes, and abuse.

## 🏗️ Architecture

- **De-Redaction Engine**: Computer vision + NLP to recover redacted names
- **Neural Graph Mapping**: GNN-based relationship inference
- **Decentralized Storage**: IPFS + P2P mesh network
- **Zero-Knowledge Proofs**: Whistleblower protection
- **Auto-Generated Legal Briefs**: AI-powered report generation

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/argus-project/argus.git
cd argus

# Start infrastructure
docker-compose up -d

# Initialize database
python scripts/init_graph_schema.py

# Ingest data
python ingest/pandora_papers.py --source ./data/raw/

# Launch web UI
cd frontend && npm start
```

## 📚 Documentation

- [Technical Architecture](docs/ARCHITECTURE.md)
- [API Documentation](docs/API.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Security Model](docs/SECURITY.md)

## 🛠️ Tech Stack

**Backend:**
- Rust (P2P networking)
- Python (ML/NLP pipelines)
- Neo4j (Graph database)
- IPFS (Decentralized storage)

**Frontend:**
- React + TypeScript
- D3.js (Graph visualization)
- Mapbox GL (Geographic mapping)

**ML/AI:**
- PyTorch (GNN training)
- Transformers (NER, de-redaction)
- spaCy (Entity extraction)

## 🔒 Security

- End-to-end encryption (Age/GPG)
- Tor/I2P hidden services
- Multi-signature governance
- Regular security audits

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📄 License

MIT License - See [LICENSE](LICENSE)

## ⚖️ Ethical Guidelines

1. Public interest journalism only
2. Victim protection (auto-redaction)
3. 3+ source verification requirement
4. Right to reply for flagged entities

---

*"The truth is paywalled, but the lies are free." — ARGUS reverses this.*
