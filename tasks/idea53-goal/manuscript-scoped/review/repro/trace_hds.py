"""Trace where 0.76/0.71/0.77/0.74 could come from."""
import math, random
from collections import Counter, defaultdict
COMPS=['fp4','fp16','scalar','bw']
SPECS={'5090':{'fp4':1677.,'fp16':419.,'scalar':21760.,'bw':1792.},
'T5000':{'fp4':1035.,'fp16':258.,'scalar':2560.,'bw':273.},
'4090':{'fp4':57.,'fp16':114.,'scalar':16384.,'bw':1008.},
'A100':{'fp4':156.,'fp16':312.,'scalar':6912.,'bw':2039.}}

# ---- (A) paper's shift definition per idea53-theory-flip.py: abs(deep_share - surface_share of surface winner)
def shift_paper(name,n=40000,seed=42):
    rng=random.Random(seed); r=[SPECS[name][c] for c in COMPS]; acc=0.0
    for _ in range(n):
        g=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); f=[x/s for x in g]
        t=[f[i]/r[i] for i in range(4)]; T=sum(t)
        sc=max(range(4),key=lambda i:f[i]); dc=max(range(4),key=lambda i:t[i])
        acc+=abs(t[dc]/T - f[sc])
    return acc/n
for nm in SPECS: print(f"shift(py-def) {nm:6s} = {shift_paper(nm):.4f}")

# ---- (B) idea53-theory.py residual entropy per hardware
def node_vals(spec,f):
    dom=max(COMPS,key=lambda c:f[c]); pc=f['fp4']+f['fp16']
    mix=0 if pc<1e-9 else min(4,int((f['fp16']/pc)*5))
    scal=min(4,int(f['scalar']*5)); bw=min(4,int(f['bw']*5))
    return (dom,mix,scal,bw)
def b_label(spec,f):
    t={c:f[c]/spec[c] for c in COMPS}; T=sum(t.values())
    c=max(t,key=t.get); return (c,min(9,int(t[c]/T*10)))
def cond_H(data,idx):
    d=defaultdict(Counter)
    for nv,bl in data: d[tuple(nv[i] for i in idx)][bl]+=1
    h=0.0; n=len(data)
    for cnt in d.values():
        m=sum(cnt.values())
        for v in cnt.values(): p=v/m; h-=(m/n)*p*math.log2(p)
    return h
def gains(data,order):
    h=cond_H(data,[]); out=[]
    for i in range(len(order)):
        hn=cond_H(data,order[:i+1]); out.append(h-hn); h=hn
    return out,h
print()
for nm,sp in SPECS.items():
    rng=random.Random(42); data=[]
    for _ in range(20000):
        gv=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(gv); f={c:v/s for c,v in zip(COMPS,gv)}
        data.append((node_vals(sp,f),b_label(sp,f)))
    g_,rem=gains(data,[0,1,2,3])
    print(f"theory.py {nm:6s} per_node={[round(x,4) for x in g_]} residual_H={rem:.4f}  sum={sum(g_):.4f}")

# ---- (C) all-plausible definitions of H(D|S)
def H(c,n): return -sum((x/n)*math.log2(x/n) for x in c if x)
def hds_all(name,n=400000,seed=7):
    rng=random.Random(seed); r=[SPECS[name][c] for c in COMPS]
    j=[0]*16; Sc=[0]*4; Dc=[0]*4
    for _ in range(n):
        g=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); f=[x/s for x in g]
        t=[f[i]/r[i] for i in range(4)]
        Si=max(range(4),key=lambda i:f[i]); Di=max(range(4),key=lambda i:t[i])
        j[Si*4+Di]+=1; Sc[Si]+=1; Dc[Di]+=1
    HS=H(Sc,n); HD=H(Dc,n); HSD=H(j,n); I=HS+HD-HSD
    return dict(HD=HD,HS=HS,I=I,HDS=HD-I,HSD_HS=HSD-HS,HSD=HSD)
print()
for nm in SPECS:
    d=hds_all(nm); print(f"H(D|S) {nm:6s} " + "  ".join(f"{k}={v:.4f}" for k,v in d.items()))
print("\nPAPER: 5090 0.76 | T5000 0.71 | 4090 0.77 | A100 0.74")
