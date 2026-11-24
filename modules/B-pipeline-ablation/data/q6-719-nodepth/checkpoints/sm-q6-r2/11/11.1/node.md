# N130: s_avg 扰动对 C_bw 的影响机制：C_bw ∝ R_daily * s_avg * (1-H)，当 s_avg 增加 20%，若 H 不变，带宽成本线性

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

s_avg 扰动对 C_bw 的影响机制：C_bw ∝ R_daily * s_avg * (1-H)，当 s_avg 增加 20%，若 H 不变，带宽成本线性增加 20%；但若大文件更多导致缓存命中率 H 下降（长尾效应），则 C_bw 增加幅度 > 20%，弹性系数 E_bw > 1。

## Corrected Claim

s_avg 扰动对 C_bw 的影响机制：C_bw ∝ R_daily * s_avg * (1-H)，当 s_avg 增加 20%，若 H 不变，带宽成本线性增加 20%；但若大文件更多导致缓存命中率 H 下降（长尾效应），则 C_bw 增加幅度 > 20%，弹性系数 E_bw > 1。

## Evidence

先验知识/题面给定，逻辑校验通过：基于公式 C_bw ∝ R_daily * s_avg * (1-H)，若 H 不变，s_avg 增加 20% 确实导致 C_bw 线性增加 20%；若 H 下降，(1-H) 增大，则总增幅超过 20%，弹性系数大于 1，推导符合数学逻辑。

## Search Query

cache hit rate sensitivity to object size distribution long tail
