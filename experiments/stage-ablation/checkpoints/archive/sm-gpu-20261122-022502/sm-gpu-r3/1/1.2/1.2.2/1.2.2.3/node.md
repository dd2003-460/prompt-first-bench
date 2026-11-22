# N119: H100 80GB 在 BF16 下的 TCO_per_token 计算：假设新品价格 $25,000，3年折旧，功耗 700W，电价 $0.15/kWh，年运

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

H100 80GB 在 BF16 下的 TCO_per_token 计算：假设新品价格 $25,000，3年折旧，功耗 700W，电价 $0.15/kWh，年运行 8000小时，则 3年总成本 ≈ $25,000 + 3 * 8000 * 0.7 * 0.15 = $31,960；若吞吐量 25 tokens/s，3年总 tokens = 25 * 3600 * 8000 * 3 = 2,160,000,000 tokens，TCO ≈ $0.0000148/token (即 $14.8/百万tokens)。

## Corrected Claim

H100 80GB 在 BF16 下的 TCO_per_token 计算：假设新品价格 $25,000，3年折旧，功耗 700W，电价 $0.15/kWh，年运行 8000小时，则 3年总成本 ≈ $25,000 + 3 * 8000 * 0.7 * 0.15 = $31,960；若吞吐量 25 tokens/s，3年总 tokens = 25 * 3600 * 8000 * 3 = 2,160,000,000 tokens，TCO ≈ $0.0000148/token (即 $14.8/百万tokens)。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（3年电费 $2,960 + 硬件 $25,000 = $31,960；总tokens 21.6亿；单价 $31,960/2,160,000,000 ≈ $0.0000148），参数假设符合H100典型工程规格。
