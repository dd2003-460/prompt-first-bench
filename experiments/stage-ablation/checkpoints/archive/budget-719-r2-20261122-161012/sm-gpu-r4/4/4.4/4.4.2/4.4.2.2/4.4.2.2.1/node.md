# N541: H100 SXM 单卡在 BF16 精度下的性价比工作点：权重+KV Cache 显存占用约 60GB，适配 80GB 显存；Decode 速度理论值 60.9

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N224

## Claim

H100 SXM 单卡在 BF16 精度下的性价比工作点：权重+KV Cache 显存占用约 60GB，适配 80GB 显存；Decode 速度理论值 60.9 tokens/s，质量损失系数 1.0，单位成本吞吐 = 60.9 / 15000 = 0.00406 tok/s/$。

## Corrected Claim

H100 SXM 单卡在 BF16 精度下的性价比工作点：权重+KV Cache 显存占用约 60GB，适配 80GB 显存；Decode 速度理论值 60.9 tokens/s，质量损失系数 1.0，单位成本吞吐 = 60.9 / 15000 = 0.00406 tok/s/$。

## Evidence

先验知识/题面给定，逻辑校验通过：60GB < 80GB 显存适配合理；60.9 / 15000 = 0.00406 计算准确；BF16 质量损失系数 1.0 符合基准定义。
