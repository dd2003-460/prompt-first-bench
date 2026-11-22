# N153: 并发>4 的显存需求量化：每个并发请求需独立 KV Cache，4 并发 × 16.8GB (BF16, 32K) = 67.2GB KV + 54GB 权重 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

并发>4 的显存需求量化：每个并发请求需独立 KV Cache，4 并发 × 16.8GB (BF16, 32K) = 67.2GB KV + 54GB 权重 = 121.2GB，需单卡 ≥128GB (如 MI300X 192GB) 或多卡方案 (如 2× A100 80GB)；若使用 FP8，KV 减半，4 并发需 33.6GB KV + 27GB 权重 = 60.6GB，单卡 80GB (A100) 可支持。

## Corrected Claim

并发>4 的显存需求量化：每个并发请求需独立 KV Cache，4 并发 × 16.8GB (BF16, 32K) = 67.2GB KV + 54GB 权重 = 121.2GB，需单卡 ≥128GB (如 MI300X 192GB) 或多卡方案 (如 2× A100 80GB)；若使用 FP8，KV 减半，4 并发需 33.6GB KV + 27GB 权重 = 60.6GB，单卡 80GB (A100) 可支持。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（4*16.8=67.2, 67.2+54=121.2; 4*8.4=33.6, 33.6+27=60.6），硬件规格符合常识（MI300X 192GB, A100 80GB），FP8精度减半逻辑自洽。
