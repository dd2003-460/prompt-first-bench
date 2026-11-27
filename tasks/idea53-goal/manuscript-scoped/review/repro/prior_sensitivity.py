"""The paper claims 'the flat-control zeroing and structural observation are
prior-robust by construction'.  Test the STRUCTURAL (§5) claim under a different
workload prior: real LLM inference is fp16-dominant, not Dirichlet(1,1,1,1)."""
import math, random
COMPS=['fp4','fp16','scalar','bw']; BR=[0,0,1,1]
SPECS={'5090':{'fp4':1677.,'fp16':419.,'scalar':21760.,'bw':1792.},
'T5000':{'fp4':1035.,'fp16':258.,'scalar':2560.,'bw':273.},
'4090':{'fp4':57.,'fp16':114.,'scalar':16384.,'bw':1008.},
'A100':{'fp4':156.,'fp16':312.,'scalar':6912.,'bw':2039.}}
def cells(name,alpha,n=100000,seed=42):
    rng=random.Random(seed); r=[SPECS[name][c] for c in COMPS]; bf=0; wi=0; lf=0
    for _ in range(n):
        g=[rng.gammavariate(a,1.) for a in alpha]; s=sum(g); f=[x/s for x in g]
        t=[f[i]/r[i] for i in range(4)]
        S=max(range(4),key=lambda i:f[i]); D=max(range(4),key=lambda i:t[i])
        fs=[f[0]+f[1],f[2]+f[3]]; ts=[t[0]+t[1],t[2]+t[3]]
        bS=max(range(2),key=lambda b:fs[b]); bD=max(range(2),key=lambda b:ts[b])
        if bS!=bD: bf+=1
        elif S!=D: wi+=1
        if S!=D: lf+=1
    return bf/n, wi/n, lf/n
for label,alpha in [("uniform Dir(1,1,1,1) [paper]",[1,1,1,1]),
                    ("fp16-heavy Dir(1,6,1,1)",[1,6,1,1]),
                    ("fp16+fp4 heavy Dir(2,6,1,1)",[2,6,1,1]),
                    ("bandwidth-heavy Dir(1,1,1,4)",[1,1,1,4])]:
    print(f"\n--- prior: {label} ---")
    print(f"{'plat':7s} {'flip':>7s} {'branch':>7s} {'within':>7s} {'dominant':>9s}")
    for nm in ['T5000','A100','5090','4090']:
        bf,wi,lf=cells(nm,alpha)
        print(f"{nm:7s} {lf:7.3f} {bf:7.3f} {wi:7.3f} {('branch' if bf>wi else 'within'):>9s}")
