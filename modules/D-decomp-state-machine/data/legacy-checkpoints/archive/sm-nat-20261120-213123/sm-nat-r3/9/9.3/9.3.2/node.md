# N170: 分子工作点B（中尾部积分修正）：考虑热度分布的幂律尾部，命中字节流量需对 h_min 到 h_k 积分。由于 k_eff=N（全驻留），理论上所有对象都命中，H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

分子工作点B（中尾部积分修正）：考虑热度分布的幂律尾部，命中字节流量需对 h_min 到 h_k 积分。由于 k_eff=N（全驻留），理论上所有对象都命中，H_byte_num 应等于 R_byte。但在 LRU 动态替换中，若存在瞬时未命中，需扣除冷启动损失。此处取 H_byte_num ≈ R_byte * (1 - P_miss_cold)，其中 P_miss_cold 为冷启动未命中率，需结合 N56 的滞后窗口估算。

## Corrected Claim

分子工作点B（中尾部积分修正）：考虑热度分布的幂律尾部，命中字节流量需对 h_min 到 h_k 积分。由于 k_eff=N（全驻留），理论上所有对象都命中，H_byte_num 应等于 R_byte。但在 LRU 动态替换中，若存在瞬时未命中，需扣除冷启动损失。此处取 H_byte_num ≈ R_byte * (1 - P_miss_cold)，其中 P_miss_cold 为冷启动未命中率，需结合 N56 的滞后窗口估算。

## Evidence

先验知识/题面给定，逻辑校验通过：在LRU全驻留（k_eff=N）假设下，稳态命中率趋近100%，仅存在冷启动瞬态损失，公式 H_byte_num ≈ R_byte * (1 - P_miss_cold) 符合缓存理论基本逻辑。
