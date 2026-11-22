# N118: 有效驻留对象数 k_eff 在‘大小-热度正相关’假设下的对比数值：若 ρ=+0.3，Top-k 对象平均大小 E[S|Top-k] ≈ 15KB，则 k_ef

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

有效驻留对象数 k_eff 在‘大小-热度正相关’假设下的对比数值：若 ρ=+0.3，Top-k 对象平均大小 E[S|Top-k] ≈ 15KB，则 k_eff = 1.28e11 / 15360 ≈ 8.3e6，仍远大于 N=1e5，表明在给定容量下，无论相关性强弱，容量都不是限制 k_eff 的主要因素，而是热度分布的截断点。

## Corrected Claim

有效驻留对象数 k_eff 在‘大小-热度正相关’假设下的对比数值：若 ρ=+0.3，Top-k 对象平均大小 E[S|Top-k] ≈ 15KB，则 k_eff = 1.28e11 / 15360 ≈ 8.3e6，仍远大于 N=1e5，表明在给定容量下，无论相关性强弱，容量都不是限制 k_eff 的主要因素，而是热度分布的截断点。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 1.28e11 / 15360 ≈ 8.33e6 正确，且 8.33e6 > 1e5 的结论符合逻辑，推论自洽。
