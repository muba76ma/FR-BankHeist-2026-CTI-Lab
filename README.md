# FR-BankHeist-2026-CTI-Lab

**Cyber Threat Intelligence / Incident Response simulation lab**
Modeling the 2026 French banking incidents:

1. **FICOBA data leak (Feb 2026)** – 1.2M IBAN/identity records exfiltrated using stolen civil-servant credentials.
2. **Crédit Mutuel Arkéa heist (Nov 2026)** – ~€100M moved from the bank's own accounts to crypto exchanges via a compromised third-party vendor.

> ⚠️ **Disclaimer**
> All data in this repo is **synthetic**. This project is for **defensive research, detection engineering and tabletop exercises only**. Do not use for illegal activity.

## Structure

## Quick start
```bash
pip install pandas networkx matplotlib pyyaml
python scripts/gen_ficoba.py
python scripts/gen_arkea_flow.py
python scripts/analyze_ficoba.py
python scripts/analyze_arkea.py
---

## 2. `.gitignore`

```bash
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.ipynb_checkpoints/
*.png
*.html
.env
venv/
