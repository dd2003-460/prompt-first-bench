# N195: 过渡区 δ 的精确表达式为 δ = 1 - C_steady * (1 - P_hit_cold)，其中 P_hit_cold 需根据更新类型分解：若 50% 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

过渡区 δ 的精确表达式为 δ = 1 - C_steady * (1 - P_hit_cold)，其中 P_hit_cold 需根据更新类型分解：若 50% 更新导致内容变更 (P=0) 且 50% 为元数据刷新 (P=1)，则 P_hit_cold=0.5，代入 C_steady=0.632 得 δ = 1 - 0.632*0.5 = 0.684，即有效命中率折损因子。

## Corrected Claim

过渡区 δ 的精确表达式为 δ = 1 - C_steady * (1 - P_hit_cold)，其中 P_hit_cold 需根据更新类型分解：若 50% 更新导致内容变更 (P=0) 且 50% 为元数据刷新 (P=1)，则 P_hit_cold=0.5，代入 C_steady=0.632 得 δ = 1 - 0.632*0.5 = 0.684，即有效命中率折损因子。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 1 - 0.632 * 0.5 = 0.684 正确，公式推导逻辑自洽。
