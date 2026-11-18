# N279: 2x RTX 4090 在 FP8 量化下的 KV Cache 显存占用计算：KV_Cache = 2 * 32K * 32 * 128 * 2 bytes =

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N109

## Claim

2x RTX 4090 在 FP8 量化下的 KV Cache 显存占用计算：KV_Cache = 2 * 32K * 32 * 128 * 2 bytes = 512MB/层 * 64 层 = 32GB，但实际因注意力头压缩和量化优化，KV Cache 占用约为 16GB-20GB，需从 48GB 总显存中扣除

## Corrected Claim

KV Cache 占用计算需修正：若每层 KV Cache 为 512MB，64 层总计 32GB，但这通常不适用于标准 LLM 推理；若总占用为 16-20GB，则每层占用应约为 256-320MB，或层数/头数/维度参数有误。建议重新核对模型架构参数（如 num_heads, head_dim, num_layers）及量化精度对 KV Cache 的具体影响。

## Evidence

[质询]数值计算存在内部矛盾：公式中 2*32K*32*128*2 的计算结果约为 512MB，但陈述称其为 512MB/层，随后乘以 64 层得到 32GB，这与公式本身的量级（512MB）不符，且 32GB 的总 KV Cache 占用对于 2x RTX 4090 (48GB) 在 FP8 下显得过高，通常 LLM 的 KV Cache 占用远低于此，除非上下文极长或模型极大。 | 先验知识/题面给定，逻辑校验未通过：公式计算结果与文字描述的量级不一致（512MB vs 512MB/层），且 32GB 的 KV Cache 占用在常规 LLM 推理场景中不合理，存在明显的数值或单位错误。

## Search Query

Qwen3-27B FP8 KV cache size 32k context
