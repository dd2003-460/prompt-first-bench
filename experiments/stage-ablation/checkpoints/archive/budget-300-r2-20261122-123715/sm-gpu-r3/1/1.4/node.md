# N8: 32K 上下文推理的最小显存需求 = 模型权重显存 + KV Cache 显存 + 激活值显存 + 框架开销；对于 Qwen3-27B 模型，需计算不同精度下的

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

32K 上下文推理的最小显存需求 = 模型权重显存 + KV Cache 显存 + 激活值显存 + 框架开销；对于 Qwen3-27B 模型，需计算不同精度下的权重大小（BF16: ~54GB, FP8: ~27GB, INT8: ~27GB, W4: ~13.5GB）以确定最低硬件显存要求。

## Corrected Claim

32K 上下文推理的最小显存需求 = 模型权重显存 + KV Cache 显存 + 激活值显存 + 框架开销；对于 Qwen3-27B 模型，需计算不同精度下的权重大小（BF16: ~54GB, FP8: ~27GB, INT8: ~27GB, W4: ~13.5GB）以确定最低硬件显存要求。

## Evidence

先验知识/题面给定，逻辑校验通过：显存构成公式正确，Qwen3-27B参数量约27B，各精度下权重大小计算（27B*2B=54GB, 27B*1B=27GB, 27B*0.5B=13.5GB）符合数学逻辑。
