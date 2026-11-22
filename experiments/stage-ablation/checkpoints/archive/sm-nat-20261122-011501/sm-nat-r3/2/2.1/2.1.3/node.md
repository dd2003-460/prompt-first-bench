# N36: 大小-热度负相关ρ=-0.3对LRU驻留集合的修正系数：由于热门对象偏小，LRU实际保留对象的平均大小比独立假设下降低约15%-20%，导致N_resident

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N9

## Claim

大小-热度负相关ρ=-0.3对LRU驻留集合的修正系数：由于热门对象偏小，LRU实际保留对象的平均大小比独立假设下降低约15%-20%，导致N_resident增加，命中率下界需乘以修正因子(1 + 0.3 * (1 - ρ))。

## Corrected Claim

大小-热度负相关（ρ≈-0.3）导致LRU驻留对象平均尺寸减小，从而增加驻留对象数量N_resident。命中率下界需引入修正因子以反映此效应，具体系数需根据实际负载分布拟合，而非固定公式(1 + 0.3 * (1 - ρ))。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 834)
