# N111: 热度-大小负相关（ρ=-0.3）对 LFU 分子项 B_top1pct 的修正因子：由于热门对象（rank≤1000）倾向于较小，其平均大小 E[S|rank≤

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

热度-大小负相关（ρ=-0.3）对 LFU 分子项 B_top1pct 的修正因子：由于热门对象（rank≤1000）倾向于较小，其平均大小 E[S|rank≤1000] 低于全局均值 E[S]。量化修正：B_top1pct_corrected = B_top1pct_independent * (1 - ρ * σ_lnS * z_top1000)，其中 z_top1000 为前 1% 排名对象的标准化热度 Z-score，σ_lnS 为大小对数标准差。此修正使得 LFU 实际可缓存的字节数低于独立假设预测，从而降低理论上限。

## Corrected Claim

热度-大小负相关（ρ=-0.3）对 LFU 分子项 B_top1pct 的修正因子：由于热门对象（rank≤1000）倾向于较小，其平均大小 E[S|rank≤1000] 低于全局均值 E[S]。量化修正：B_top1pct_corrected = B_top1pct_independent * (1 - ρ * σ_lnS * z_top1000)，其中 z_top1000 为前 1% 排名对象的标准化热度 Z-score，σ_lnS 为大小对数标准差。此修正使得 LFU 实际可缓存的字节数低于独立假设预测，从而降低理论上限。

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态分布假设，条件期望 E[S|Rank] 与相关性 ρ 的线性修正公式在数学上自洽，且负相关导致热门对象平均大小小于全局均值的结论符合直觉。
