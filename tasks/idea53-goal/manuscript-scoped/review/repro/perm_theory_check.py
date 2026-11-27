"""CRITICAL SELF-CHECK.

Claim to test: is flip EXACTLY permutation-invariant in the POPULATION?

Argument for YES: f ~ Dirichlet(1,1,1,1) is EXCHANGEABLE. Substituting f_i = g_{pi(i)}
with g ~ same law, argmax_i f_i = pi(argmax g) and argmax_i f_i/r_{pi(i)} = pi(argmax g_j/r_j).
So flip(pi r) = P(pi(argmax g) != pi(argmax g/r)) = flip(r).  EXACTLY equal, for ALL pi.

If that is right, then the 24-permutation test CANNOT fail -> it is a tautology, not a
control.  The tiny spread 0.5251-0.5304 seen with common random numbers is finite-sample
relabeling noise of ONE fixed draw, which must shrink as N grows.

Test: raise N and see whether the 24 values collapse onto one number.
"""
import math, random, itertools, statistics
COMPS=['fp4','fp16','scalar','bw']
R=[1677.,419.,21760.,1792.]   # 5090
def flip_for(rates,W):
    f_=0
    for f in W:
        t=[f[i]/rates[i] for i in range(4)]
        if max(range(4),key=lambda i:f[i])!=max(range(4),key=lambda i:t[i]): f_+=1
    return f_/len(W)
print(f"{'N':>9s} {'#distinct(24)':>14s} {'min':>9s} {'max':>9s} {'range':>9s}  (5090)")
for N in [40000, 200000, 1000000, 4000000]:
    rng=random.Random(42); W=[]
    for _ in range(N):
        g=[rng.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); W.append([x/s for x in g])
    vals=[flip_for([R[p[i]] for i in range(4)],W) for p in itertools.permutations(range(4))]
    print(f"{N:>9d} {len(set(round(v,10) for v in vals)):>14d} {min(vals):9.6f} {max(vals):9.6f} {max(vals)-min(vals):9.6f}")
print()
print("If the range shrinks like 1/sqrt(N), the population value is a single number")
print("=> the 24-permutation test cannot fail => it is a tautology, not a falsifiable control.")
print()
print("Independent-seed check (fresh N=2e6 draws per permutation): should agree within MC error")
rng=random.Random(999)
vals=[]
for k,p in enumerate(itertools.permutations(range(4))):
    r=random.Random(1000+k); W=[]
    for _ in range(2000000):
        g=[r.gammavariate(1.,1.) for _ in range(4)]; s=sum(g); W.append([x/s for x in g])
    vals.append(flip_for([R[p[i]] for i in range(4)],W))
print(f"  24 independent runs: mean={statistics.mean(vals):.6f} sd={statistics.pstdev(vals):.6f} "
      f"min={min(vals):.6f} max={max(vals):.6f}")
print(f"  expected MC sd at N=2e6: {math.sqrt(0.5276*0.4724/2000000):.6f}")
