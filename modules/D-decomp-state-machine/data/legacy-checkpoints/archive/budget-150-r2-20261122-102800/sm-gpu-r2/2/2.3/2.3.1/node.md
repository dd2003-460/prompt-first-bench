# N81: 修正后的总显存需求 (32K ctx, batch=1)：BF16 = 54 (权重) + 2.15 (KV) + 2 (激活) + 1 (CUDA) ≈ 59

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

修正后的总显存需求 (32K ctx, batch=1)：BF16 = 54 (权重) + 2.15 (KV) + 2 (激活) + 1 (CUDA) ≈ 59.15 GB；INT8/FP8 = 27 + 1.07 + 2 + 1 ≈ 31.07 GB；W4/NVFP4 = 13.5 + 0.54 + 2 + 1 ≈ 17.04 GB。

## Corrected Claim

修正后的总显存需求 (32K ctx, batch=1)：BF16 = 54 (权重) + 2.15 (KV) + 2 (激活) + 1 (CUDA) ≈ 59.15 GB；INT8/FP8 = 27 + 1.07 + 2 + 1 ≈ 31.07 GB；W4/NVFP4 = 13.5 + 0.54 + 2 + 1 ≈ 17.04 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：各项显存组成（权重、KV Cache、激活、CUDA开销）量级符合大模型推理显存估算常识，数值加和逻辑自洽。
