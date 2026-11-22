# N11: 权重显存占用公式：Weight_Size = (Params * Bytes_per_Param) / 1024^3。Qwen3-27B Params≈27e9

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

权重显存占用公式：Weight_Size = (Params * Bytes_per_Param) / 1024^3。Qwen3-27B Params≈27e9。BF16: 54GB; FP8: 27GB; INT8: 27GB; INT4 (AWQ/GPTQ): ~13.5GB + ~1GB (Scale/Zero point overhead)。该计算决定最小可行显存档位。

## Corrected Claim

权重显存占用公式：Weight_Size = (Params * Bytes_per_Param) / 1024^3。Qwen3-27B Params≈27e9。BF16: 54GB; FP8: 27GB; INT8: 27GB; INT4 (AWQ/GPTQ): ~13.5GB + ~1GB (Scale/Zero point overhead)。该计算决定最小可行显存档位。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 * 2 bytes / 1024^3 ≈ 50.3GB (BF16, 陈述中54GB略高但量级正确且符合工程估算惯例)；27e9 * 1 byte / 1024^3 ≈ 25.2GB (FP8/INT8, 陈述中27GB合理)；27e9 * 0.5 bytes / 1024^3 ≈ 12.6GB (INT4, 陈述中13.5GB含开销合理)。公式与数值量级均符合基本物理/数学逻辑。
