# N77: N22 中 ΔH ≤ 0.05 的上界假设 LFU 能完美识别最高频率对象，但在 Pareto(β=0.9) 分布下，第 K 名与第 K+1 名对象的频率差异极

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

N22 中 ΔH ≤ 0.05 的上界假设 LFU 能完美识别最高频率对象，但在 Pareto(β=0.9) 分布下，第 K 名与第 K+1 名对象的频率差异极小，LFU 的增益主要来自对尾部对象的过滤，实际增益上限约为 (R_K - R_{K+1})/R_total，需通过具体 K 值计算。

## Corrected Claim

N22 中 ΔH ≤ 0.05 的上界假设 LFU 能完美识别最高频率对象，但在 Pareto(β=0.9) 分布下，第 K 名与第 K+1 名对象的频率差异极小，LFU 的增益主要来自对尾部对象的过滤，实际增益上限约为 (R_K - R_{K+1})/R_total，需通过具体 K 值计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU vs LRU performance gap Pareto distribution
