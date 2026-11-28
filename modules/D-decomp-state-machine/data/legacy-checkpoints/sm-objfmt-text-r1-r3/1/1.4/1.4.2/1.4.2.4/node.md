# N114: BF16 精度下单请求最小显存需求修正值：Weight (54.36 GB) + KV Cache (8.59 GB) + Activation (4.29 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33, N34, N35

## Claim

BF16 精度下单请求最小显存需求修正值：Weight (54.36 GB) + KV Cache (8.59 GB) + Activation (4.29 GB) + Runtime Overhead (估算 0.5-1 GB for CUDA context/workspace) ≈ 67.7 - 68.2 GB。N34 的 64.6-66.6 GB 低估了激活值和运行时开销，实际需至少 68 GB 显存才能安全运行。

## Corrected Claim

BF16 精度下单请求最小显存需求修正值：Weight (54.36 GB) + KV Cache (8.59 GB) + Activation (4.29 GB) + Runtime Overhead (估算 0.5-1 GB for CUDA context/workspace) ≈ 67.7 - 68.2 GB。N34 的 64.6-66.6 GB 低估了激活值和运行时开销，实际需至少 68 GB 显存才能安全运行。

## Evidence

先验知识/题面给定，逻辑校验通过：各项显存占用（权重、KV Cache、激活值、运行时开销）相加符合算术逻辑，且BF16下各组件量级符合大模型推理显存估算的工程常识。
