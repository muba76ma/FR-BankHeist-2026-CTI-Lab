import json, os
P = os.path.join(os.path.dirname(__file__), "..", "data", "arkea_heist_flow.json")
d = json.load(open(P, encoding="utf-8"))
total = sum(e["amount_eur"] for e in d["edges"] if e["src"]=="ARK_INTERNAL_OP")
print(f"[+] case={d['case']}  edges={len(d['edges'])}  out_from_internal=EUR {total:,}")
