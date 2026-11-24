# N25: 方案B (HDD+SSD分层) 的每TB年有效成本基准值：假设热数据20%(100TB)在SSD，冷数据80%(400TB)在HDD，HDD寿命5年，SSD寿命

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

方案B (HDD+SSD分层) 的每TB年有效成本基准值：假设热数据20%(100TB)在SSD，冷数据80%(400TB)在HDD，HDD寿命5年，SSD寿命3年，电力系数0.05W/TB(HDD)+0.1W/TB(SSD)，计算 C_B = (Capex_B/5 + Opex_B) / (500TB * 0.9可用率)，其中 Capex_B 和 Opex_B 为具体数值占位符

## Corrected Claim

方案B (HDD+SSD分层) 的每TB年有效成本基准值：假设热数据20%(100TB)在SSD，冷数据80%(400TB)在HDD，HDD寿命5年，SSD寿命3年，电力系数0.05W/TB(HDD)+0.1W/TB(SSD)，计算 C_B = (Capex_B/5 + Opex_B) / (500TB * 0.9可用率)，其中 Capex_B 和 Opex_B 为具体数值占位符

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合TCO计算标准（(Capex/寿命+Opex)/有效容量），参数设定（HDD/SSD寿命、电力系数、可用率）均在合理工程范围内，且明确标注为占位符公式而非具体数值结论。

## Search Query

HDD SSD hybrid storage cost per TB per year 2024
