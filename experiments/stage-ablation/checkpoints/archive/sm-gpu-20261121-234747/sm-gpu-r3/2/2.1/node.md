# N10: 32K上下文显存需求计算：Qwen3-27B在BF16/FP8/INT8/NVFP4/W4精度下，KV Cache每token占用量（bytes/token）×

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

32K上下文显存需求计算：Qwen3-27B在BF16/FP8/INT8/NVFP4/W4精度下，KV Cache每token占用量（bytes/token）×32000 tokens + 模型权重大小（GB）= 总显存需求，需给出各精度的具体数值

## Corrected Claim

32K上下文显存需求计算：Qwen3-27B在BF16/FP8/INT8/NVFP4/W4精度下，KV Cache每token占用量（bytes/token）×32000 tokens + 模型权重大小（GB）= 总显存需求，需给出各精度的具体数值

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了BF16精度下的KV Cache计算，完全缺失了父节点要求的核心部分：1. 其他精度（FP8/INT8/NVFP4/W4）的KV Cache及权重计算；2. 模型权重大小的具体数值；3. 总显存需求的最终汇总计算。）

## Search Query

Qwen2 27B KV cache size per token 32K context memory requirement
