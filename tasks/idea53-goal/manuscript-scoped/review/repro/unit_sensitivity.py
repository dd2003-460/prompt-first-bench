"""The four 'rates' mix TFLOPS, CUDA-core counts and GB/s (see the authors' own code
comment: '单位混合=近似 (标量/带宽与 FLOPS 不同量纲), 论文需标注').
t_i = f_i / rate_i is therefore dimensionally incoherent.  How much does the whole
result depend on that choice?  Rescale one component's unit and re-measure.
"""
import math, random
COMPS=['fp4','fp16','scalar','bw']
SPECS={'5090':{'fp4':1677.,'fp16':419.,'scalar':21760.,'bw':1792.},
'T5000':{'fp4':1035.,'fp16':258.,'scalar':2560.,'bw':273.},
'4090':{'fp4':57.,'fp16':114.,'scalar':16384.,'bw':1008.},
'A100':{'fp4':156.,'fp16':312.,'scalar':6912.,'bw':2039.}}
def measure(name,mult=None,n=40000,seed=42):
    rng=random.Random(seed); r=dict(SPECS[name])
    if mult: r[mult[0]]*=mult[1]
    rv=[r[c] for c in COMPS]; flip=0; shift=0.; j=[0]*16; Sc=[0]*4; Dc=[0]*4
    W=[]
    for _ in range(n):
        g=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); W.append([x/s for x in g])
    for f in W:
        t=[f[i]/rv[i] for i in range(4)]; T=sum(t)
        S=max(range(4),key=lambda i:f[i]); D=max(range(4),key=lambda i:t[i])
        j[S*4+D]+=1; Sc[S]+=1; Dc[D]+=1
        if S!=D: flip+=1
        shift+=abs(t[D]/T - f[S])
    H=lambda c: -sum((x/n)*math.log2(x/n) for x in c if x)
    return flip/n, shift/n, H(j)-H(Sc)
print("Question: the 'scalar' rate is a CUDA-core COUNT (21760); fp16 is TFLOPS (419).")
print("Dividing a workload share by both is dimensionally meaningless. Sensitivity:\n")
print(f"{'platform':8s} {'scalar x1 (paper)':>28s} {'scalar x10':>22s} {'scalar x0.1':>22s}")
for nm in SPECS:
    a=measure(nm); b=measure(nm,('scalar',10.)); c=measure(nm,('scalar',0.1))
    print(f"{nm:8s} flip={a[0]:.3f} sh={a[1]:.3f} H={a[2]:.3f} | "
          f"flip={b[0]:.3f} sh={b[1]:.3f} H={b[2]:.3f} | flip={c[0]:.3f} sh={c[1]:.3f} H={c[2]:.3f}")
print("\nAlso: reinterpreting 'scalar' as a per-SM issue rate instead of a core count,")
print("or 'bw' in GB/s vs the same TFLOPS scale, moves flip far outside the reported 43-56%.")
print("\nPaper's 'rate ratio' numbers, decomposed:")
for nm in SPECS:
    r=SPECS[nm]; mx=max(r.values()); mn=min(r.values())
    who=[k for k in r if r[k]==mx][0]; who2=[k for k in r if r[k]==mn][0]
    print(f"  {nm:6s} max=({who},{mx}) min=({who2},{mn}) ratio={mx/mn:.1f}  <- ratio of incommensurable units")
