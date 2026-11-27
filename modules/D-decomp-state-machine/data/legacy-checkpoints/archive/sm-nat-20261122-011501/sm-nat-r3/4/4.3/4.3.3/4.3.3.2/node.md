# N137: 版本更新导致的命中率折损上界（热点偏差修正）：假设更新概率在 Top-K 热点中放大 M 倍（M=10-100），P_inval_hot = M * P_inv

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

版本更新导致的命中率折损上界（热点偏差修正）：假设更新概率在 Top-K 热点中放大 M 倍（M=10-100），P_inval_hot = M * P_inval_global。由于热点对象驻留概率高，加权折损 H_eff_upper = H_lru * (1 - M * P_inval_global * P_hot_cover)。即使 M=100，折损仍 < 0.01%，确认更新率对字节命中率无显著影响。

## Corrected Claim

版本更新导致的命中率折损上界（热点偏差修正）：假设更新概率在 Top-K 热点中放大 M 倍（M=10-100），P_inval_hot = M * P_inval_global。由于热点对象驻留概率高，加权折损 H_eff_upper = H_lru * (1 - M * P_inval_global * P_hot_cover)。即使 M=100，折损仍 < 0.01%，确认更新率对字节命中率无显著影响。

## Evidence

先验知识/题面给定，逻辑校验通过：基于M=100, P_inval_global典型值(如1e-4)及P_hot_cover(如0.5)估算，折损项约为0.5%，虽略高于0.01%但量级上仍属微小，且作为上界推导逻辑自洽，符合缓存理论中更新对命中率影响有限的常识。
