# N317: NVIDIA A100 80GB SXM 与 PCIe 版本在 Qwen3-27B BF16 32K 上下文下的 TPS 差异百分比 = (TPS_sxm - 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N103

## Claim

NVIDIA A100 80GB SXM 与 PCIe 版本在 Qwen3-27B BF16 32K 上下文下的 TPS 差异百分比 = (TPS_sxm - TPS_pcie) / TPS_pcie；基于带宽差 (2039/1935 ≈ 1.054) 和效率差 (η_sxm/η_pcie ≈ 1.05)，预期 TPS_sxm 比 TPS_pcie 高约 5-10% [待核验]。

## Corrected Claim

NVIDIA A100 80GB SXM 与 PCIe 版本在 Qwen3-27B BF16 32K 上下文下的 TPS 差异受带宽、互联拓扑及效率共同影响，SXM 版本通常略优于 PCIe 版本，具体差异需实测确定，粗略估算可能在 5-10% 范围内。

## Evidence

[质询]该陈述将复杂的推理性能差异简化为带宽和效率的线性乘积，忽略了SXM与PCIe在互联拓扑（NVLink vs PCIe）对多卡通信开销、内存控制器延迟以及实际有效带宽利用率上的非线性影响，且'效率差1.05'缺乏具体基准测试支持，属于过度简化的经验估算。 | 先验知识/题面给定，逻辑校验通过；但作为经验事实，缺乏直接来源支持，且简化模型存在不确定性，故降级。

## Search Query

A100 SXM vs PCIe LLM inference performance difference percentage Qwen3-27B
