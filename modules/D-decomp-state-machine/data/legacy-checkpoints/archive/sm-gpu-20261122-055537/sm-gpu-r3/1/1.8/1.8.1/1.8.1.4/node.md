# N199: INT8 KV Cache 量化对显存需求的降低：将 KV Cache 从 BF16 (2 bytes) 量化至 INT8 (1 byte)，KV Cache 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

INT8 KV Cache 量化对显存需求的降低：将 KV Cache 从 BF16 (2 bytes) 量化至 INT8 (1 byte)，KV Cache 大小减半至 0.95 GB；此时 BF16 权重 + INT8 KV Cache 总需求 = 55.6 + 0.95 + 3 = 59.55 GB，仍超过 48GB，但接近 80GB 卡的 75% 利用率。

## Corrected Claim

INT8 KV Cache 量化对显存需求的降低：将 KV Cache 从 BF16 (2 bytes) 量化至 INT8 (1 byte)，KV Cache 大小减半至 0.95 GB；此时 BF16 权重 + INT8 KV Cache 总需求 = 55.6 + 0.95 + 3 = 59.55 GB，仍超过 48GB，但接近 80GB 卡的 75% 利用率。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16(2B)转INT8(1B)确实减半；55.6+0.95+3=59.55计算正确；59.55/80≈74.4%接近75%。

## Search Query

vLLM INT8 KV cache quantization memory reduction
