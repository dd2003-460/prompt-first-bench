# N122: s_min 从 1KB 增至 10KB 时，截断 Pareto(α=1.1) 的期望值 E[s] 并非线性增加 10 倍，因为分布尾部主导均值；需通过数值积分 

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39, N40, N41

## Claim

s_min 从 1KB 增至 10KB 时，截断 Pareto(α=1.1) 的期望值 E[s] 并非线性增加 10 倍，因为分布尾部主导均值；需通过数值积分 ∫_{10KB}^{s_max} s * f(s) ds 重新计算 E[s]，预计 E[s] 增加幅度小于 10 倍，导致 C_norm 下降幅度小于 10 倍。

## Corrected Claim

s_min 从 1KB 增至 10KB 时，截断 Pareto(α=1.1) 的期望值 E[s] 并非线性增加 10 倍，因为分布尾部主导均值；需通过数值积分 ∫_{10KB}^{s_max} s * f(s) ds 重新计算 E[s]，预计 E[s] 增加幅度小于 10 倍，导致 C_norm 下降幅度小于 10 倍。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Pareto alpha 1.1 expected value lower bound 1KB 10KB
