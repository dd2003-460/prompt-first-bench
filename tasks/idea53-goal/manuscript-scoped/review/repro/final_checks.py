import math, random, itertools
COMPS=['fp4','fp16','scalar','bw']
SPECS={'5090':{'fp4':1677.,'fp16':419.,'scalar':21760.,'bw':1792.},
'T5000':{'fp4':1035.,'fp16':258.,'scalar':2560.,'bw':273.},
'4090':{'fp4':57.,'fp16':114.,'scalar':16384.,'bw':1008.},
'A100':{'fp4':156.,'fp16':312.,'scalar':6912.,'bw':2039.}}

# ---- 1. permutation invariance with COMMON RANDOM NUMBERS (same workloads for all 24 perms)
def perm_crn(name,n=40000,seed=42):
    rng=random.Random(seed); W=[]
    for _ in range(n):
        g=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); W.append([x/s for x in g])
    r0=[SPECS[name][c] for c in COMPS]
    out=[]
    for p in itertools.permutations(range(4)):
        r=[r0[p[i]] for i in range(4)]; f_=0
        for f in W:
            t=[f[i]/r[i] for i in range(4)]
            if max(range(4),key=lambda i:f[i])!=max(range(4),key=lambda i:t[i]): f_+=1
        out.append(f_/n)
    return out
print("=== 1. permutation invariance, COMMON RANDOM NUMBERS (exact test, no MC noise) ===")
for nm in SPECS:
    o=perm_crn(nm)
    print(f"  {nm:6s} flip over 24 perms: min={min(o):.6f} max={max(o):.6f} distinct_values={len(set(round(x,9) for x in o))}")
print("  (paper: 5090 in 0.5251--0.5304, attributed to a 'narrow Monte-Carlo band')")

# ---- 2. MC error of H(D|S) across seeds at N=40000
def H(c,n): return -sum((x/n)*math.log2(x/n) for x in c if x)
def hds(name,n=40000,seed=1):
    rng=random.Random(seed); r=[SPECS[name][c] for c in COMPS]
    j=[0]*16; Sc=[0]*4; Dc=[0]*4
    for _ in range(n):
        g=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); f=[x/s for x in g]
        t=[f[i]/r[i] for i in range(4)]
        Si=max(range(4),key=lambda i:f[i]); Di=max(range(4),key=lambda i:t[i])
        j[Si*4+Di]+=1; Sc[Si]+=1; Dc[Di]+=1
    HS=H(Sc,n);HD=H(Dc,n);HSD=H(j,n); return HSD-HS
print("\n=== 2. H(D|S) MC spread across 20 seeds at N=40000 ===")
for nm in SPECS:
    v=[hds(nm,seed=s) for s in range(20)]
    print(f"  {nm:6s} mean={sum(v)/len(v):.4f} min={min(v):.4f} max={max(v):.4f} sd={ (sum((x-sum(v)/len(v))**2 for x in v)/len(v))**0.5:.4f}")
print("  paper values: 5090 0.76 | T5000 0.71 | 4090 0.77 | A100 0.74")

# ---- 3. is H(D|S) maximized by a WRONG deep node?
print("\n=== 3. H(D|S) of an always-WRONG deep node (reports argmin time = anti-bottleneck) ===")
for nm in SPECS:
    v=[hds(nm,seed=s) for s in range(4)]
    rng=random.Random(5); r=[SPECS[nm][c] for c in COMPS]
    j=[0]*16; Sc=[0]*4; Dc=[0]*4; n=200000
    for _ in range(n):
        g=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); f=[x/s for x in g]
        t=[f[i]/r[i] for i in range(4)]
        Si=max(range(4),key=lambda i:f[i]); Di=min(range(4),key=lambda i:t[i])
        j[Si*4+Di]+=1; Sc[Si]+=1; Dc[Di]+=1
    HS=H(Sc,n);HD=H(Dc,n);HSD=H(j,n)
    print(f"  {nm:6s} correct D: H(D|S)={sum(v)/len(v):.4f}   ANTI D: H(D|S)={HSD-HS:.4f}"
          f"   {'<-- WRONG node scores HIGHER' if HSD-HS > sum(v)/len(v) else ''}")
