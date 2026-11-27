import math, random, itertools
COMPS=["fp4","fp16","scalar","bw"]
SPECS={"5090":{"fp4":1677.,"fp16":419.,"scalar":21760.,"bw":1792.},
"T5000":{"fp4":1035.,"fp16":258.,"scalar":2560.,"bw":273.},
"4090":{"fp4":57.,"fp16":114.,"scalar":16384.,"bw":1008.},
"A100":{"fp4":156.,"fp16":312.,"scalar":6912.,"bw":2039.}}
def H(counts,n):
    return -sum((c/n)*math.log2(c/n) for c in counts if c)
def joint_H(counts,n):
    return -sum((c/n)*math.log2(c/n) for c in counts if c)
def run(name,n=200000,seed=1,bin_=None):
    rng=random.Random(seed); r=[SPECS[name][c] for c in COMPS]
    cod=lambda i,j: i*4+j
    jc=[0]*(16); Sc=[0]*4; Dc=[0]*4
    if bin_ is not None:
        Bc=[0]*(4*bin_)
    for _ in range(n):
        g=[-math.log(rng.random()) for _ in range(4)]; s=sum(g); f=[x/s for x in g]
        t=[f[i]/r[i] for i in range(4)]; z=sum(t)
        Si=max(range(4),key=lambda i:f[i]); Di=max(range(4),key=lambda i:t[i])
        jc[cod(Si,Di)]+=1; Sc[Si]+=1; Dc[Di]+=1
        if bin_ is not None:
            b=min(bin_-1,int(t[Di]/z*bin_)); Bc[Di*bin_+b]+=1
    HS=H(Sc,n); HD=H(Dc,n); HSD=joint_H(jc,n); I=HS+HD-HSD
    out={"H(S)":HS,"H(D)":HD,"I(S;D)":I,"H(D|S)=HD-I":HD-I,"H(D|S)=H(SD)-H(S)":HSD-HS}
    if bin_ is not None:
        HB=H(Bc,n); out["H(B)"]=HB; out["H(B|D)"]=HB-HD; out["H(B|S)"]=HB-(HS+HD-HSD)
    return out
for n in [40000,200000]:
    print(f"--- N={n} ---")
    for name in ["5090","T5000","4090","A100"]:
        r=run(name,n=n)
        print(f"{name:6s} "+"  ".join(f"{k}={v:.4f}" for k,v in r.items()))
print("\n--- B=(type,10-bin share) ---")
for name in ["5090","T5000","4090","A100"]:
    r=run(name,n=100000,bin_=10)
    print(f"{name:6s} "+"  ".join(f"{k}={v:.4f}" for k,v in r.items()))
print("\nPAPER:  5090 H(D|S)=0.76 | T5000 0.71 | 4090 0.77 | A100 0.74")
