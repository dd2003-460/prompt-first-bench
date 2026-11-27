"""Is 'dominant dimension' a property of hardware, or of the branch split?
Compare 2v2 (paper) with 1v3 and 3v1 splits. Also report chance baseline.
"""
import math, random
COMPS=['fp4','fp16','scalar','bw']
SPECS={'5090':{'fp4':1677.,'fp16':419.,'scalar':21760.,'bw':1792.},
'T5000':{'fp4':1035.,'fp16':258.,'scalar':2560.,'bw':273.},
'4090':{'fp4':57.,'fp16':114.,'scalar':16384.,'bw':1008.},
'A100':{'fp4':156.,'fp16':312.,'scalar':6912.,'bw':2039.}}
def cells(name,br,n=200000,seed=42):
    rng=random.Random(seed); r=[SPECS[name][c] for c in COMPS]
    both=cof=bo=wi=0
    for _ in range(n):
        g=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); f=[x/s for x in g]
        t=[f[i]/r[i] for i in range(4)]
        S=max(range(4),key=lambda i:f[i]); D=max(range(4),key=lambda i:t[i])
        nb=len(set(br)); fs=[0.]*nb; ts=[0.]*nb
        for i in range(4): fs[br[i]]+=f[i]; ts[br[i]]+=t[i]
        bS=max(range(nb),key=lambda b:fs[b]); bD=max(range(nb),key=lambda b:ts[b])
        bf=bS!=bD; lf=S!=D
        if not lf and not bf: both+=1
        elif lf and bf: cof+=1
        elif bf: bo+=1
        else: wi+=1
    return dict(both=both/n,co_flip=cof/n,branch_only=bo/n,within=wi/n,
                P_branch_flip=(cof+bo)/n, P_leaf_flip=(cof+wi)/n)
splits={"2v2 {fp4,fp16}|{scalar,bw}":[0,0,1,1],
        "1v3 {fp4}|{fp16,scalar,bw}":[0,1,1,1],
        "3v1 {fp4,fp16,scalar}|{bw}":[0,0,0,1],
        "2v2 {fp4,bw}|{fp16,scalar}":[0,1,1,0]}
for sn,br in splits.items():
    print(f"\n--- split {sn} ---")
    print(f"{'plat':7s} {'P(leaf flip)':>12s} {'P(branch flip)':>14s} {'within':>8s} {'dominant':>9s}")
    for nm in ['T5000','A100','5090','4090']:
        d=cells(nm,br)
        dom='branch' if d['P_branch_flip']>d['within'] else 'within'
        print(f"{nm:7s} {d['P_leaf_flip']:>12.3f} {d['P_branch_flip']:>14.3f} {d['within']:>8.3f} {dom:>9s}")
print("\nChance baselines: P(leaf flip | random S)=3/4=0.750; P(branch flip | random)=1/2=0.500")
