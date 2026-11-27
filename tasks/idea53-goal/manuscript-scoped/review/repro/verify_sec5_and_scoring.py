"""Two independent checks:
(A) §5 four-cell table: reconstruct with AGGREGATE branch times (compute={fp4,fp16}, memory={scalar,bw})
(B) Does H(D|S) actually score 'contribution'? Test the anti-bottleneck control:
    a deep node that ALWAYS outputs the wrong component (argmin instead of argmax).
    If H(D|S) is a contribution score, an always-wrong node must score ~0.
"""
import math, random
COMPS=['fp4','fp16','scalar','bw']
SPECS={'5090':{'fp4':1677.,'fp16':419.,'scalar':21760.,'bw':1792.},
'T5000':{'fp4':1035.,'fp16':258.,'scalar':2560.,'bw':273.},
'4090':{'fp4':57.,'fp16':114.,'scalar':16384.,'bw':1008.},
'A100':{'fp4':156.,'fp16':312.,'scalar':6912.,'bw':2039.}}
BR={0:0,1:0,2:1,3:1}

def H(c,n): return -sum((x/n)*math.log2(x/n) for x in c if x)

def sec5(name,n=200000,seed=42):
    rng=random.Random(seed); r=[SPECS[name][c] for c in COMPS]
    both=cof=branchonly=within=0
    for _ in range(n):
        g=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); f=[x/s for x in g]
        t=[f[i]/r[i] for i in range(4)]
        S=max(range(4),key=lambda i:f[i]); D=max(range(4),key=lambda i:t[i])
        # aggregate branch judgments
        fs=[f[0]+f[1], f[2]+f[3]]; ts=[t[0]+t[1], t[2]+t[3]]
        bS=max(range(2),key=lambda b:fs[b]); bD=max(range(2),key=lambda b:ts[b])
        bflip = bS!=bD; lflip = S!=D
        if not lflip and not bflip: both+=1
        elif lflip and bflip: cof+=1
        elif bflip and not lflip: branchonly+=1
        else: within+=1
    return dict(both_correct=both/n, co_flip=cof/n, branch_only=branchonly/n, within_branch=within/n)

print("=== (A) §5 four cells, aggregate-branch definition ===")
print(f"{'platform':8s} {'both_correct':>12s} {'co_flip':>8s} {'branch_only':>11s} {'within_branch':>13s} {'branch_flip':>11s}")
for nm in ['T5000','A100','5090','4090']:
    d=sec5(nm); bf=d['co_flip']+d['branch_only']
    print(f"{nm:8s} {d['both_correct']:>12.3f} {d['co_flip']:>8.3f} {d['branch_only']:>11.3f} {d['within_branch']:>13.3f} {bf:>11.3f}")
print("\nLong paper.tex rows: T5000 0.530/0.145/0.036/0.290 (bf .181); A100 0.399/0.442/0.045/0.114 (bf .487)")
print("TMLR short tex rows:  T5000 co-flip .530 / within-flip .145 / co-correct .036 / within-correct .290")
print("                      (header order = co-flip, within-flip, co-correct, within-correct)")

print("\n=== (B) anti-bottleneck control: deep node that is ALWAYS WRONG ===")
def hds(name,n=400000,seed=7,mode='correct'):
    rng=random.Random(seed); r=[SPECS[name][c] for c in COMPS]
    j=[0]*16; Sc=[0]*4; Dc=[0]*4
    for _ in range(n):
        g=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); f=[x/s for x in g]
        t=[f[i]/r[i] for i in range(4)]
        Si=max(range(4),key=lambda i:f[i])
        Di=max(range(4),key=lambda i:t[i]) if mode=='correct' else min(range(4),key=lambda i:t[i])
        j[Si*4+Di]+=1; Sc[Si]+=1; Dc[Di]+=1
    HS=H(Sc,n);HD=H(Dc,n);HSD=H(j,n)
    return dict(H_D=HD,H_S=HS,I=HS+HD-HSD,H_DS=HSD-HS)
print(f"{'platform':8s} {'H(D|S) correct':>15s} {'H(D|S) ANTI (always-wrong)':>28s}")
for nm in SPECS:
    a=hds(nm,mode='correct'); b=hds(nm,mode='anti')
    print(f"{nm:8s} {a['H_DS']:>15.3f} {b['H_DS']:>28.3f}")
