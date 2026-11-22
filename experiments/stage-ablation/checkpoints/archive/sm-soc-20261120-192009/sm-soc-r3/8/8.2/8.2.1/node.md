# N322: 同类商品匹配度阈值：定义'同类'的条件为 Category ID 相同、Brand 相同、Condition 等级差 ≤ 1（如 95新 与 9成新 视为同类）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

同类商品匹配度阈值：定义'同类'的条件为 Category ID 相同、Brand 相同、Condition 等级差 ≤ 1（如 95新 与 9成新 视为同类），若条件差 > 1 则剔除；需验证该阈值下样本量 N_sample ≥ 30 才能计算有效 P25/P75。

## Corrected Claim

同类商品匹配度阈值：定义'同类'的条件为 Category ID 相同、Brand 相同、Condition 等级差 ≤ 1（如 95新 与 9成新 视为同类），若条件差 > 1 则剔除；需验证该阈值下样本量 N_sample ≥ 30 才能计算有效 P25/P75。

## Evidence

先验知识/题面给定，逻辑校验通过：统计上样本量N≥30是应用中心极限定理计算有效分位数（P25/P75）的通用经验法则，逻辑自洽。
