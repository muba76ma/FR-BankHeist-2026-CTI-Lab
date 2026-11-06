# FR-BankHeist-2026-CTI-Lab

Cyber Threat Intelligence / Incident Response simulation lab
Modeling the 2026 French banking incidents:

1. FICOBA data leak (Feb 2026) - 1.2M IBAN/identity records exfiltrated using stolen civil-servant credentials.
2. Credit Mutuel Arkea heist (Nov 2026) - ~100M EUR moved from bank accounts to crypto exchanges via compromised third-party vendor.

DISCLAIMER: All data is synthetic. For defensive research only.

## Quick start
pip install pandas networkx
python scripts/gen_ficoba.py
python scripts/gen_arkea_flow.py
python scripts/analyze_ficoba.py
python scripts/analyze_arkea.py
