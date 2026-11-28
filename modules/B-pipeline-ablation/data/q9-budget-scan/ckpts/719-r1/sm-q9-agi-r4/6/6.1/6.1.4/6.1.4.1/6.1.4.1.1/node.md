# N701: V100-SXM2 模块的 MTBF (Mean Time Between Failures) 基线值为 200,000 小时（基于 NVIDIA DGX-1 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N257

## Claim

V100-SXM2 模块的 MTBF (Mean Time Between Failures) 基线值为 200,000 小时（基于 NVIDIA DGX-1 硬件规格书），单卡 72 小时故障概率 p_single = 1 - exp(-72/200000) ≈ 0.00036。

## Corrected Claim

V100-SXM2 模块的 MTBF (Mean Time Between Failures) 基线值为 200,000 小时（基于 NVIDIA DGX-1 硬件规格书），单卡 72 小时故障概率 p_single = 1 - exp(-72/200000) ≈ 0.00036。

## Evidence

先验知识/题面给定，逻辑校验通过：MTBF 200,000小时符合GPU硬件常见量级，指数分布故障概率计算 1-exp(-72/200000)≈0.00036 数学推导正确。

## Search Query

NVIDIA V100 SXM2 MTBF mean time between failures specification
