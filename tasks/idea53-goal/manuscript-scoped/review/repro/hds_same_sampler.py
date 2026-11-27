"""H(D|S) using the AUTHORS' exact sampler (random.Random(42), gammavariate, N=40000),
so the only difference from idea53-theory-flip.py is adding the joint entropy."""
import math, random
COMPS=['fp4','fp16','scalar','bw']
SPECS={'5090':{'fp4':1677.,'fp16':419.,'scalar':21760.,'bw':1792.},
'T5000':{'fp4':1035.,'fp16':258.,'scalar':2560.,'bw':273.},
'4090':{'fp4':57.,'fp16':114.,'scalar':16384.,'bw':1008.},
'A100':{'fp4':156.,'fp16':312.,'scalar':6912.,'bw':2039.}}
def H(c,n): return -sum((x/n)*math.log2(x/n) for x in c if x)
rng=random.Random(42); W=[]
for _ in range(40000):
    gv=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(gv); W.append([v/s for v in gv])
print(f"{'plat':7s} {'flip':>7s} {'shift':>7s} {'H(D)':>7s} {'I(S;D)':>7s} {'H(D|S)':>7s}")
res={}
for nm,sp in SPECS.items():
    r=[sp[c] for c in COMPS]; j=[0]*16; Sc=[0]*4; Dc=[0]*4; flip=0; shift=0.
    for f in W:
        t=[f[i]/r[i] for i in range(4)]; T=sum(t)
        S=max(range(4),key=lambda i:f[i]); D=max(range(4),key=lambda i:t[i])
        j[S*4+D]+=1; Sc[S]+=1; Dc[D]+=1
        if S!=D: flip+=1
        shift+=abs(t[D]/T - f[S])          # authors' definition (idea53-theory-flip.py)
    n=len(W); HS=H(Sc,n); HD=H(Dc,n); HSD=H(j,n)
    res[nm]=dict(flip=flip/n,shift=shift/n,HD=HD,I=HS+HD-HSD,HDS=HSD-HS)
    print(f"{nm:7s} {flip/n:7.4f} {shift/n:7.4f} {HD:7.4f} {HS+HD-HSD:7.4f} {HSD-HS:7.4f}")
print("\npaper tex table:  5090 0.527/0.200/0.76 | T5000 0.434/0.166/0.71 | 4090 0.563/0.231/0.77 | A100 0.556/0.218/0.74")
print("\nIf H(D|S) values are placed in the paper's own row order:")
for nm in ['5090','T5000','4090','A100']:
    print(f"  {nm:6s} recon={res[nm]['HDS']:.3f}")
