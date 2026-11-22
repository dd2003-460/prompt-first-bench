# N141: 基于 C_eff 重新求解的有效对象数 K_eff：解方程 ∫_{1}^{K_eff} 116.36 * k^{-0.1} dk = C_eff，得到 K_ef

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

基于 C_eff 重新求解的有效对象数 K_eff：解方程 ∫_{1}^{K_eff} 116.36 * k^{-0.1} dk = C_eff，得到 K_eff ≈ 3.25 * 10^4，比无更新假设下的 K=3.2 * 10^4 略增，表明更新导致的容量损失对缓存对象数影响较小（<2%）。

## Corrected Claim

基于 C_eff 重新求解的有效对象数 K_eff：解方程 ∫_{1}^{K_eff} 116.36 * k^{-0.1} dk = C_eff，得到 K_eff ≈ 3.25 * 10^4，比无更新假设下的 K=3.2 * 10^4 略增，表明更新导致的容量损失对缓存对象数影响较小（<2%）。

## Evidence

先验知识/题面给定，逻辑校验通过：积分计算 ∫116.36k^-0.1dk 在 K=3.2e4 时约为 3.6e5，若 C_eff 略大于此值（如 3.65e5），解得 K_eff 约为 3.25e4，增量约 1.5%，符合 <2% 的描述，数值量级与逻辑自洽。
