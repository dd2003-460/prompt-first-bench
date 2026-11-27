"""Does an EXACT closed form for P(D=i) exist that the paper failed to derive?

Dirichlet(1,1,1,1) = g/||g||_1 with g_i ~ Exp(1) iid.
Then t_i = f_i/r_i ∝ g_i/r_i, and g_i/r_i ~ Exp(rate=r_i).
D = argmax_i t_i  <=>  the component whose Exp(r_i) variable is the LARGEST.

P(Exp(λ_i) is max) = ∫_0^∞ λ_i e^{-λ_i t} Π_{j≠i}(1 - e^{-λ_j t}) dt
                   = Σ_{S ⊆ others} (-1)^{|S|} λ_i / (λ_i + Σ_{j∈S} λ_j)

This is an exact rational function of the rates: no Monte Carlo needed.
"""
from fractions import Fraction
import itertools, math, random
COMPS=['fp4','fp16','scalar','bw']
SPECS={'5090':{'fp4':1677.,'fp16':419.,'scalar':21760.,'bw':1792.},
'T5000':{'fp4':1035.,'fp16':258.,'scalar':2560.,'bw':273.},
'4090':{'fp4':57.,'fp16':114.,'scalar':16384.,'bw':1008.},
'A100':{'fp4':156.,'fp16':312.,'scalar':6912.,'bw':2039.}}

def exact_P(lam):
    n=len(lam); P=[]
    for i in range(n):
        others=[j for j in range(n) if j!=i]; s=0.0
        for k in range(len(others)+1):
            for S in itertools.combinations(others,k):
                s += (-1)**k * lam[i]/(lam[i]+sum(lam[j] for j in S))
        P.append(s)
    return P

def mc_P(lam,n=400000,seed=3):
    rng=random.Random(seed); c=[0]*len(lam)
    for _ in range(n):
        g=[rng.expovariate(1.0) for _ in range(4)]
        u=[g[i]/lam[i] for i in range(4)]
        c[max(range(4),key=lambda i:u[i])]+=1
    return [x/n for x in c]

print(f"{'platform':8s} {'exact P(D)':>46s}  {'sum':>7s}  {'max|exact-MC|':>14s}")
for nm in SPECS:
    lam=[SPECS[nm][c] for c in COMPS]
    e=exact_P(lam); m=mc_P(lam)
    print(f"{nm:8s} [{', '.join(f'{x:.6f}' for x in e)}]  {sum(e):>7.6f}  {max(abs(a-b) for a,b in zip(e,m)):>14.6f}")

def H(p): return -sum(x*math.log2(x) for x in p if x>0)
print("\nH(D) from EXACT P(D) (replaces MC estimate):")
for nm in SPECS:
    lam=[SPECS[nm][c] for c in COMPS]
    print(f"  {nm:6s} H(D)_exact = {H(exact_P(lam)):.6f} bits")
print("\nPaper reports H(D|S) as 0.71-0.77 bits, not H(D). But H(D) itself is exact.")
print("Exact 2-component sanity check: P(Exp(a)>Exp(b)) should equal b/(a+b).")
a,b=3.0,7.0
print(f"  formula={exact_P([a,b])[0]:.10f}  b/(a+b)={b/(a+b):.10f}")
