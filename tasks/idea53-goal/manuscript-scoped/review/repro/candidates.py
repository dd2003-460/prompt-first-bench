import math, random
N=40000
COMPS=["fp4","fp16","scalar","bw"]
SPECS={"5090":{"fp4":1677.,"fp16":419.,"scalar":21760.,"bw":1792.},
"T5000":{"fp4":1035.,"fp16":258.,"scalar":2560.,"bw":273.},
"4090":{"fp4":57.,"fp16":114.,"scalar":16384.,"bw":1008.},
"A100":{"fp4":156.,"fp16":312.,"scalar":6912.,"bw":2039.}}
def run(name,seed=12345,n=N):
    rng=random.Random(seed); r=[SPECS[name][c] for c in COMPS]
    acc={k:0.0 for k in ["bn_S","bn_D","all","l1_over_2","max"]}
    flips=0
    # 2x2 branch structure: branch0={fp4,fp16}, branch1={scalar,bw}
    cell={"coflip":0,"coflip_leafsame":0,"withinsame_leafflip":0,"withinboth":0}
    brflip=0; leafflip=0
    for _ in range(n):
        g=[-math.log(rng.random()) for _ in range(4)]; s=sum(g); f=[x/s for x in g]
        t=[f[i]/r[i] for i in range(4)]; zt=sum(t); sh=[x/zt for x in t]
        S=max(range(4),key=lambda i:f[i]); D=max(range(4),key=lambda i:t[i])
        d=[abs(sh[i]-f[i]) for i in range(4)]
        acc["bn_S"]+=d[S]; acc["bn_D"]+=d[D]; acc["all"]+=sum(d)/4
        acc["l1_over_2"]+=sum(d)/2; acc["max"]+=max(d)
        flips+= (S!=D); leafflip += (S!=D)
        bS = 0 if S in (0,1) else 1; bD = 0 if D in (0,1) else 1
        brflip += (bS!=bD)
        if bS!=bD:
            cell["coflip"] += 1
            if S==D: cell["coflip_leafsame"] += 1
        else:
            if S!=D: cell["withinsame_leafflip"] += 1
            else: cell["withinboth"] += 1
    return {k:v/n for k,v in acc.items()} | {"flip":flips/n,"branch_flip":brflip/n,
        **{k:v/n for k,v in cell.items()}}
for name in ["5090","T5000","4090","A100"]:
    r=run(name)
    print(name, {k:round(v,4) for k,v in r.items()})
print("\npaper paper shift column: 5090 0.200  T5000 0.166  4090 0.231  A100 0.218")
