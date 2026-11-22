# N321: NVIDIA H100 PCIe 80GB 的官方 TDP 为 350W（非 SXM 版的 700W），该功耗限制导致其在持续高负载推理下的实际 FP8 算力利

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N109, N110, N111

## Claim

NVIDIA H100 PCIe 80GB 的官方 TDP 为 350W（非 SXM 版的 700W），该功耗限制导致其在持续高负载推理下的实际 FP8 算力利用率约为 SXM 版的 50-60%，需以 350W 而非 700W 重新计算其能效比。

## Corrected Claim

NVIDIA H100 PCIe 80GB 的官方 TDP 通常低于 SXM 版（如 350W 对比 700W），这可能导致其在持续高负载下的实际算力利用率低于 SXM 版，具体比例需参考实测数据。

## Evidence

[质询]该陈述包含具体的经验性数据（TDP数值及算力利用率比例），属于硬件规格与性能表现的经验事实，无法仅通过第一性原理推导得出，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

NVIDIA H100 PCIe 80GB TDP 350W specifications
