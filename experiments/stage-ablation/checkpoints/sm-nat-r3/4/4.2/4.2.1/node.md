# N61: 工作点 B（冷门对象）：对于热度 90%-100% 的对象，假设其访问频率极低，T_LRU 可能接近缓存替换周期，若 T_LRU ≈ 1 天，则 R_inv_B

- **status**: pending
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

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 5 column 13 (char 79)
