# N96: W4 量化精度下最小显存门槛计算：权重 13.5GB + KV Cache (32K, 8GB, 通常 KV 不量化或量化至 FP8 4GB) + 激活值 (4

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

W4 量化精度下最小显存门槛计算：权重 13.5GB + KV Cache (32K, 8GB, 通常 KV 不量化或量化至 FP8 4GB) + 激活值 (4GB) + 框架开销 (2GB) = 27.5GB (KV=8GB) 或 23.5GB (KV=4GB)。因此，显存 >= 24GB 的 GPU (如 RTX 4090) 在理论边缘可行，但需严格监控 OOM 风险，实际部署建议预留 10% 余量，即需 >= 25-26GB，故 24GB 卡处于高风险区。

## Corrected Claim

W4 量化精度下最小显存门槛计算：权重 13.5GB + KV Cache (32K, 8GB, 通常 KV 不量化或量化至 FP8 4GB) + 激活值 (4GB) + 框架开销 (2GB) = 27.5GB (KV=8GB) 或 23.5GB (KV=4GB)。因此，显存 >= 24GB 的 GPU (如 RTX 4090) 在理论边缘可行，但需严格监控 OOM 风险，实际部署建议预留 10% 余量，即需 >= 25-26GB，故 24GB 卡处于高风险区。

## Evidence

先验知识/题面给定，逻辑校验通过：W4量化下13.5GB权重符合13B模型量级，KV Cache与激活值估算符合常规工程经验，总显存计算逻辑自洽且数值量级合理。
