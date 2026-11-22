# N193: 阈值不等式右项 C_wait * T_wait 的基准数值估算：复用 N101 公式，假设 T_wait=24小时(1天)，C_opportunity≈0.08

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

阈值不等式右项 C_wait * T_wait 的基准数值估算：复用 N101 公式，假设 T_wait=24小时(1天)，C_opportunity≈0.08元/天，C_attention=10*1=10元/天，则 C_wait * T_wait ≈ 10.08元。对比左项6元 < 10.08元，表明在标准参数下买家不应等待，需校准参数以匹配观察到的等待行为。

## Corrected Claim

阈值不等式右项 C_wait * T_wait 的基准数值估算：复用 N101 公式，假设 T_wait=24小时(1天)，C_opportunity≈0.08元/天，C_attention=10*1=10元/天，则 C_wait * T_wait ≈ 10.08元。对比左项6元 < 10.08元，表明在标准参数下买家不应等待，需校准参数以匹配观察到的等待行为。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 10 + 0.08 = 10.08 正确，且 6 < 10.08 的比较逻辑自洽，符合成本效益分析的基本原理。

## Search Query

waiting cost calculation 24 hours consumer decision
