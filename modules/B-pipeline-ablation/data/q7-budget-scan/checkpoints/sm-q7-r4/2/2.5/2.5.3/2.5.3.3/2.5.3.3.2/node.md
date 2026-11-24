# N649: 在访问率 10% 的基准工作点，C_retrieval_S3 = 40,960 GB × $0.01/GB × 7.2 ≈ ¥2,949/年，取回成本较低，S3

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N235

## Claim

在访问率 10% 的基准工作点，C_retrieval_S3 = 40,960 GB × $0.01/GB × 7.2 ≈ ¥2,949/年，取回成本较低，S3 IA 方案在此访问频率下具有成本优势。

## Corrected Claim

在访问率 10% 的基准工作点，C_retrieval_S3 = 40,960 GB × $0.01/GB × 7.2 ≈ ¥2,949/年，取回成本较低，S3 IA 方案在此访问频率下具有成本优势。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 40960 * 0.01 * 7.2 = 2949.12，数值准确；S3 IA 在低访问率下通常比标准存储更便宜符合一般云存储定价逻辑。
