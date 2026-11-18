# N96: x_min 的敏感性边界：若 x_min 增至 10 KB，E[S] = 110 KB，K_avg ≈ 1,250，此时 K_avg < N，命中率下界由 N8

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

x_min 的敏感性边界：若 x_min 增至 10 KB，E[S] = 110 KB，K_avg ≈ 1,250，此时 K_avg < N，命中率下界由 N82 公式 H ≈ 1 - (K/N)^{0.1} 主导，需对比 x_min=100B 与 x_min=10KB 两种工作点的命中率差异以界定答案的稳健性。

## Corrected Claim

x_min 的敏感性边界：若 x_min 增至 10 KB，E[S] = 110 KB，K_avg ≈ 1,250，此时 K_avg < N，命中率下界由 N82 公式 H ≈ 1 - (K/N)^{0.1} 主导，需对比 x_min=100B 与 x_min=10KB 两种工作点的命中率差异以界定答案的稳健性。

## Evidence

先验知识/题面给定，逻辑校验通过
