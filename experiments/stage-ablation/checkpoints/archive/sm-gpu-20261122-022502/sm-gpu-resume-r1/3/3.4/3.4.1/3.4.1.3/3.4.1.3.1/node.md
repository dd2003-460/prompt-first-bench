# N729: 4x RTX 4090 在 Fractal Design Define 7 XL 机箱中，若采用标准风冷且未加装额外排风扇，GPU 核心温度在持续满载 30 分

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N224, N225, N226

## Claim

4x RTX 4090 在 Fractal Design Define 7 XL 机箱中，若采用标准风冷且未加装额外排风扇，GPU 核心温度在持续满载 30 分钟后通常超过 85°C，触发 P-States 降频，导致有效显存带宽从理论 1008 GB/s 下降至 850-900 GB/s 区间 [待核验: 需具体压力测试数据]。

## Corrected Claim

4x RTX 4090 在 Fractal Design Define 7 XL 机箱中，若采用标准风冷且未加装额外排风扇，GPU 核心温度在持续满载下可能因散热瓶颈而升高，进而触发 P-States 降频，导致有效显存带宽低于理论峰值 1008 GB/s。

## Evidence

[质询]该陈述包含具体的经验性数值（温度>85°C、带宽降至850-900 GB/s），属于硬件性能与热力学经验事实，无法从第一性原理严格推导；且缺乏具体压力测试数据支持，不同机箱风道设计、硅脂涂抹、环境温度均会导致结果显著差异，具体数值区间缺乏普适性依据。 | 经验事实，逻辑自洽（高温导致降频进而影响有效带宽符合物理直觉），但缺来源支持且具体数值缺乏实证数据，故降级。

## Search Query

4x RTX 4090 Fractal Design Define 7 XL thermal throttling bandwidth loss stress test
