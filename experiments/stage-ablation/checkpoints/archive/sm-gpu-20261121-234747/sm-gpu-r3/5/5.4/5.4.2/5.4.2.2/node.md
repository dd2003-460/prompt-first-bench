# N371: 2×RTX 3090的满载功耗 N * W_card：单卡TDP 350W，2张总TDP为 700W，实际推理负载下平均功耗约为 TDP 的 60%-80%，即

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N127

## Claim

2×RTX 3090的满载功耗 N * W_card：单卡TDP 350W，2张总TDP为 700W，实际推理负载下平均功耗约为 TDP 的 60%-80%，即 420W-560W。

## Corrected Claim

2×RTX 3090的满载功耗 N * W_card：单卡TDP 350W，2张总TDP为 700W，实际推理负载下平均功耗约为 TDP 的 60%-80%，即 420W-560W。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 TDP 350W 为官方标准规格，2卡总 TDP 700W 计算正确；推理负载下平均功耗低于 TDP 符合 GPU 功耗管理逻辑，60%-80% 区间在工程经验上合理。

## Search Query

RTX 3090 inference power consumption average watts
