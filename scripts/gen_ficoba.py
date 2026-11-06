import random, csv, os
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "ficoba_leak_sim.csv")
N = 1_200_000
first = ["Jean","Marie","Pierre","Sophie","Lucas","Emma","Hugo","Lea","Paul","Chloe"]
last  = ["Martin","Bernard","Dubois","Thomas","Robert","Richard","Petit","Durand","Leroy","Moreau"]
cities= ["Paris","Lyon","Marseille","Toulouse","Nice","Nantes","Strasbourg","Bordeaux"]
def iban():
    return "FR76" + "".join(str(random.randint(0,9)) for _ in range(23))
def tax_id():
    return str(random.randint(1,2)) + f"{random.randint(0,99):02d}" + f"{random.randint(0,12):02d}" + f"{random.randint(0,999):03d}"
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["tax_id","full_name","address","iban","bank_code","leak_date","source"])
    for _ in range(N):
        name = f"{random.choice(first)} {random.choice(last)}"
        addr = f"{random.randint(1,200)} rue {random.choice(last)}, {random.choice(cities)}"
        w.writerow([tax_id(), name, addr, iban(), f"{random.randint(10000,99999)}", "2026-02-14", "FICOBA"])
print(f"[+] wrote {N} rows -> {OUT}")
