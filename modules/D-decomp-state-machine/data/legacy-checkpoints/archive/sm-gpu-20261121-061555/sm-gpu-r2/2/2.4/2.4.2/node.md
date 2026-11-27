# N66: FP8/INT8精度下的总显存需求计算：Memory_Weights=27GB, Memory_KV≈0.43GB (FP8 KV Cache减半), Over

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

FP8/INT8精度下的总显存需求计算：Memory_Weights=27GB, Memory_KV≈0.43GB (FP8 KV Cache减半), Overhead≈3.5GB, 总需求=27+0.43+3.5=30.93GB；加上15%安全余量后，Minimum_VRAM=30.93*1.15≈35.6GB。

## Corrected Claim

FP8/INT8精度下的总显存需求计算：Memory_Weights=27GB, Memory_KV≈0.43GB (FP8 KV Cache减半), Overhead≈3.5GB, 总需求=27+0.43+3.5=30.93GB；加上15%安全余量后，Minimum_VRAM=30.93*1.15≈35.6GB。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 27+0.43+3.5=30.93 及 30.93*1.15=35.5695≈35.6 均正确，量级符合大模型推理显存估算常识。
