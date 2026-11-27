import math, random
COMPS=['fp4','fp16','scalar','bw']; BR=[0,0,1,1]
SPECS={'5090':{'fp4':1677.,'fp16':419.,'scalar':21760.,'bw':1792.},
'T5000':{'fp4':1035.,'fp16':258.,'scalar':2560.,'bw':273.},
'4090':{'fp4':57.,'fp16':114.,'scalar':16384.,'bw':1008.},
'A100':{'fp4':156.,'fp16':312.,'scalar':6912.,'bw':2039.}}
def H(c,n): return -sum((x/n)*math.log2(x/n) for x in c if x)
print("### 1. shift 定义污染检查 (shift 在 S!=D 时跨分量比较)")
print(f"{'plat':7s} {'paper shift(all)':>17s} {'shift|S==D only':>16s} {'shift|S!=D only':>16s} {'alt granularity':>16s}")
for nm in SPECS:
    rng=random.Random(42); r=[SPECS[nm][c] for c in COMPS]
    a=0.;b=0.;c_=0.;na=0;nb=0;nc_=0;alt=0.
    for _ in range(40000):
        g=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); f=[x/s for x in g]
        t=[f[i]/r[i] for i in range(4)]; T=sum(t)
        S=max(range(4),key=lambda i:f[i]); D=max(range(4),key=lambda i:t[i])
        d=abs(t[D]/T - f[S])
        if S==D: b+=d; nb+=1
        else: c_+=d; nc_+=1
        a+=d
        alt+=abs(t[D]/T-f[D])   # same-component granularity
    print(f"{nm:7s} {a/40000:17.3f} {b/nb:16.3f} {c_/nc_:16.3f} {alt/40000:16.3f}")
print("\n### 2. H(D|S) vs flip 的秩相关")
d={'5090':(0.527,0.7667),'T5000':(0.434,0.7639),'4090':(0.563,0.7128),'A100':(0.556,0.7464)}
def rank(vals):
    s=sorted(range(len(vals)),key=lambda i:vals[i]); r=[0]*len(vals)
    for k,i in enumerate(s): r[i]=k+1
    return r
ks=list(d); fl=rank([d[k][0] for k in ks]); hd=rank([d[k][1] for k in ks])
n=len(ks); s2=sum((fl[i]-hd[i])**2 for i in range(n))
print(f"  flip ranks: {dict(zip(ks,fl))}")
print(f"  H(D|S) ranks: {dict(zip(ks,hd))}")
print(f"  Spearman rho = {1-6*s2/(n*(n*n-1)):.2f}  (n=4, 最小可达 -1.0)")
print("  => H(D|S) 与 flip 反向：flip 最高的 4090 的 H(D|S) 最低")
print("\n### 3. H(D|S) 对'纯噪声深层节点'的取值")
for nm in ['T5000','4090']:
    rng=random.Random(42); r=[SPECS[nm][c] for c in COMPS]
    n=200000; j=[0]*16; Sc=[0]*4
    for _ in range(n):
        g=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); f=[x/s for x in g]
        S=max(range(4),key=lambda i:f[i]); D=rng.randrange(4)
        j[S*4+D]+=1; Sc[S]+=1
    print(f"  {nm}: 噪声节点 H(D|S) = {H(j,n)-H(Sc,n):.3f} bits  (真实深层节点 = {d[nm][1]:.3f})")
print("  上限 log2(4) = 2.000 bits")
