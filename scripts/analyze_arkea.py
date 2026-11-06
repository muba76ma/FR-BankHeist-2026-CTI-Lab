import json, os, sys
try:
    import networkx as nx
except ImportError:
    sys.exit("pip install networkx")
P = os.path.join(os.path.dirname(__file__), "..", "data", "arkea_heist_flow.json")
d = json.load(open(P, encoding="utf-8"))
G = nx.DiGraph()
for e in d["edges"]:
    G.add_edge(e["src"], e["dst"], amount=e["amount_eur"], ts=e["ts"])
print(f"[+] Nodes: {G.number_of_nodes()}  Edges: {G.number_of_edges()}")
print("\n[+] Flow to crypto/mixer:")
for u,v,data in G.edges(data=True):
    if "CRYPTO" in v or "MIXER" in v:
        print(f"  {u:20s} -> {v:20s} EUR {data['amount']:,}  @ {data['ts']}")
print("\n[+] Laundering paths:")
for p in nx.all_simple_paths(G, "ARK_INTERNAL_OP", "CRYPTO_MIXER"):
    print("  " + " -> ".join(p))
