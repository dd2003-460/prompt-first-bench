# N542: H100 SXM 单卡在 FP8 精度下的性价比工作点：权重+KV Cache 显存占用约 35GB，适配 80GB 显存；Decode 速度理论值 60.9 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N224

## Claim

H100 SXM 单卡在 FP8 精度下的性价比工作点：权重+KV Cache 显存占用约 35GB，适配 80GB 显存；Decode 速度理论值 60.9 tokens/s（带宽瓶颈未变），质量损失系数 0.98，有效吞吐 59.7 tokens/s，单位成本吞吐 = 59.7 / 15000 = 0.00398 tok/s/$。

## Corrected Claim

H100 SXM 单卡在 FP8 精度下的性价比工作点：权重+KV Cache 显存占用约 35GB，适配 80GB 显存；Decode 速度理论值 60.9 tokens/s（带宽瓶颈未变），质量损失系数 0.98，有效吞吐 59.7 tokens/s，单位成本吞吐 = 59.7 / 15000 = 0.00398 tok/s/$。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8权重+KV Cache占用35GB在80GB显存内合理；Decode速度60.9 tokens/s符合H100 SXM带宽瓶颈下的理论估算；质量损失系数0.98及有效吞吐59.7 tokens/s计算自洽；单位成本吞吐0.00398 tok/s/$数值量级合理。
