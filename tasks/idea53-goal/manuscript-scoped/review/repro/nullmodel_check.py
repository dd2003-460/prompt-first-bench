"""Check the chance-level calibration claim used in the review.
Null model: S is uniform random in {0..3}, independent of D (a 'useless surface node').
Question: what are the chance rates of the branch-flip and within-flip cells?
"""
import random
random.seed(0)
N=400000; BR=[0,0,1,1]
both=co=branchonly=within=0
for _ in range(N):
    S=random.randrange(4); D=random.randrange(4)
    bS=BR[S]; bD=BR[D]
    if bS!=bD: branchonly+=1
    elif S!=D: within+=1
    else: both+=1
print(f"null model (useless surface node):")
print(f"  P(branch flip) = {(branchonly+0)/N:.4f}   [note: cells]")
# recompute properly: branch flip = co-flip + branch-only in paper's convention
# paper's within-flip cell == branch-only in long version? verify mapping here.
print(f"  both={both/N:.4f} branch_flip_total={branchonly/N:.4f} within_if_branch_same={within/N:.4f}")
print(f"  P(leaf flip) = {(branchonly+within)/N:.4f}")
print(f"  => chance(branch flip)=0.5 ; chance(within | branch same)=0.25 ; chance(leaf flip)=0.75")
print()
# Now apply to real data
real={'T5000':(0.184,0.290),'A100':(0.486,0.114),'5090':(0.399,0.194),'4090':(0.493,0.112)}
print(f"{'plat':7s} {'branch':>8s} {'within':>8s} {'br/0.5':>8s} {'wi/0.25':>8s} {'dom_raw':>8s} {'dom_norm':>9s}")
for k,(b,w) in real.items():
    print(f"{k:7s} {b:8.3f} {w:8.3f} {b/0.5:8.3f} {w/0.25:8.3f} "
          f"{('branch' if b>w else 'within'):>8s} {('branch' if b/0.5>w/0.25 else 'within'):>9s}")
