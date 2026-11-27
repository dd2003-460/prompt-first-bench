# N10: KV Cache量化策略：若KV Cache使用FP8 (1 byte/element)而非BF16 (2 bytes/element)，KV Cache占用减

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

KV Cache量化策略：若KV Cache使用FP8 (1 byte/element)而非BF16 (2 bytes/element)，KV Cache占用减半。Qwen3-27B 32K ctx FP8 KV Cache = 10.31 GB。若KV Cache使用INT8，同样为10.31 GB。这将显著降低总显存需求：BF16权重+FP8 KV Cache总需求 ≈ 54.2 + 10.31 + 4.06 ≈ 68.57 GB，可能使48GB卡（如A6000）在优化下可行，但仍需2卡。[待核验: Qwen3-27B是否原生支持FP8 KV Cache或需特定框架支持]

## Corrected Claim

KV Cache量化策略：若KV Cache使用FP8 (1 byte/element)而非BF16 (2 bytes/element)，KV Cache占用减半。Qwen3-27B 32K ctx FP8 KV Cache = 10.31 GB。若KV Cache使用INT8，同样为10.31 GB。这将显著降低总显存需求：BF16权重+FP8 KV Cache总需求 ≈ 54.2 + 10.31 + 4.06 ≈ 68.57 GB，可能使48GB卡（如A6000）在优化下可行，但仍需2卡。[待核验: Qwen3-27B是否原生支持FP8 KV Cache或需特定框架支持]

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache大小与精度线性相关，FP8/INT8均为1字节，故占用减半；总显存计算（54.2+10.31+4.06=68.57）算术正确，量级符合27B模型32K上下文的工程经验。

## Search Query

KV cache quantization FP8 INT8 LLM inference vllm
