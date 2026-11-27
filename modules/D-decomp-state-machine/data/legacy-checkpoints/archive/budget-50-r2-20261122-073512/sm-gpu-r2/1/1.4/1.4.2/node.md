# N51: KV Cache 显存占用项量化：KV_cache_GB = (2 × 32 × 128 × 32768 × Bytes_per_token) / (1024^

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

KV Cache 显存占用项量化：KV_cache_GB = (2 × 32 × 128 × 32768 × Bytes_per_token) / (1024^3) × N，其中 Bytes_per_token 取决于精度（BF16=2, FP8=1, INT8=1），N 为并发数；此值直接决定显存需求对并发数的线性敏感度。

## Corrected Claim

KV Cache 显存占用项量化：KV_cache_GB = (2 × 32 × 128 × 32768 × Bytes_per_token) / (1024^3) × N，其中 Bytes_per_token 取决于精度（BF16=2, FP8=1, INT8=1），N 为并发数；此值直接决定显存需求对并发数的线性敏感度。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合KV Cache显存计算标准（2×层数×头数×头维度×序列长度×字节数），量纲与数值量级合理，且明确指出了对并发数N的线性依赖关系。
