# N61: 工作点 B（冷门对象）：对于热度 90%-100% 的对象，假设其访问频率极低，T_LRU 可能接近缓存替换周期，若 T_LRU ≈ 1 天，则 R_inv_B

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

工作点 B（冷门对象）：对于热度 90%-100% 的对象，假设其访问频率极低，T_LRU 可能接近缓存替换周期，若 T_LRU ≈ 1 天，则 R_inv_B ≈ 0.01 * 1 = 1%，折损为 1%；此类对象的有效命中率 H_eff ≈ H_LRU * 0.99。

## Corrected Claim

工作点 B（冷门对象）：对于热度 90%-100% 的对象，假设其访问频率极低，T_LRU 可能接近缓存替换周期，若 T_LRU ≈ 1 天，则 R_inv_B ≈ 0.01 * 1 = 1%，折损为 1%；此类对象的有效命中率 H_eff ≈ H_LRU * 0.99。

## Evidence

先验知识/题面给定，逻辑校验通过：基于题面设定的假设（T_LRU≈1天，频率极低），数值计算 0.01*1=1% 及 H_eff 推导在逻辑上自洽且量纲合理。
