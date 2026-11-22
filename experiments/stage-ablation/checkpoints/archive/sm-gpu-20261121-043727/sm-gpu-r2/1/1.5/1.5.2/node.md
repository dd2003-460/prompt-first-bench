# N53: AMD MI250X 的精确规格为：128GB HBM2e, 内存带宽 3.2TB/s, TDP 1000W, ROCm 5.x/6.x 支持存在兼容性问题，单

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

AMD MI250X 的精确规格为：128GB HBM2e, 内存带宽 3.2TB/s, TDP 1000W, ROCm 5.x/6.x 支持存在兼容性问题，单卡价格区间 $10,000-$12,000 (2024 Q3 市场价)

## Corrected Claim

AMD MI250X 的规格为：128GB HBM2e, 内存带宽 3.2TB/s。关于 TDP、ROCm 兼容性及 2024 Q3 单卡价格 $10,000-$12,000 的说法缺乏可靠来源支持，且价格可能偏低。

## Evidence

[质询]单卡价格区间 $10,000-$12,000 与 2024 Q3 市场价严重不符，MI250X 作为高端 HPC 加速卡，其市场/渠道价格通常远高于此（往往在 $20,000+ 或需通过特定渠道获取），且参考来源中完全未包含任何价格信息，属于缺乏来源支持的经验事实。 | 来源 [1] 和 [3] 直接支持 128GB HBM2e 和 3.2TB/s 带宽（8192-bit * 3.2 Gbps = 3.2 TB/s），但所有来源均未提及 TDP、ROCm 兼容性细节或具体价格，价格部分缺乏外部证据支持且数值量级存疑。

## Search Query

AMD MI250X specifications price ROCm compatibility 2024

## Retrieval Sources

- {'url': 'https://www.techpowerup.com/gpu-specs/instinct-mi250x.c3837&rut=32f71602f1c8f2838bc7e4b7daead8908212ece2e14cc39550f6b07a5c38bc11', 'type': 'ddg', 'title': 'AMD Instinct MI250X Specs | TechPowerUp GPU Database'}
- {'url': 'https://www.amd.com/en/products/accelerators/instinct/mi200/mi250x.html&rut=638bbc880f97f7959b866729787281912ea696ac8195864056244adda589e611', 'type': 'ddg', 'title': 'AMD Instinct™ MI250X Accelerators'}
- {'url': 'https://www.techpowerup.com/gpu-specs/instinct-mi250.c3847&rut=a6ac921af79bf6e68b5d86fd290bf235d6bfa37cf2978ecc2e09f5b46a77a16f', 'type': 'ddg', 'title': 'AMD Instinct MI250 Specs | TechPowerUp GPU Database'}
