# N298: 工作点C（效率因子修正项）：Attention_Efficiency_Factor 在 W4 量化下并非恒定 0.6，而是随 KV Cache 量化精度变化：若

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N98

## Claim

工作点C（效率因子修正项）：Attention_Efficiency_Factor 在 W4 量化下并非恒定 0.6，而是随 KV Cache 量化精度变化：若 KV 为 INT8，访存数据减半，有效带宽利用率提升，因子可升至 0.75；若 KV 为 BF16 且开启 FlashAttention-2，因子维持在 0.6-0.65；该因子是吞吐预测的关键可变参数。

## Corrected Claim

工作点C（效率因子修正项）：Attention_Efficiency_Factor 在 W4 量化下并非恒定，而是随 KV Cache 量化精度变化：若 KV 为 INT8，访存数据减半，有效带宽利用率提升，因子通常高于 BF16 情况；若 KV 为 BF16 且开启 FlashAttention-2，因子处于较低区间；该因子是吞吐预测的关键可变参数。

## Evidence

[质询]具体数值（0.75, 0.6-0.65）缺乏通用理论支撑，属于特定模型或实验条件下的经验拟合值，不同硬件架构或实现细节下可能显著不同，存在将特定实验结果泛化为通用规律的风险。 | 先验知识/题面给定，逻辑校验通过（量化降低数据量从而提升带宽利用率符合物理直觉），但具体数值为经验事实且无外部来源支持，故降级。
