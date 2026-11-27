# N377: 条件性推荐边界条件3（基础设施兼容性）：推荐 RTX 5090 的前提是用户具备支持 PCIe 5.0 x16 插槽且供电能力 ≥ 1200W 的主机平台。若用

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

条件性推荐边界条件3（基础设施兼容性）：推荐 RTX 5090 的前提是用户具备支持 PCIe 5.0 x16 插槽且供电能力 ≥ 1200W 的主机平台。若用户现有基础设施为 PCIe 4.0 平台，RTX 5090 带宽利用率将下降至 50%（理论 1792 GB/s -> 实际有效 ~896 GB/s），此时性价比排序反转，RTX 4090 (PCIe 4.0 原生) 或 A100 PCIe 4.0 成为更优选择，需重新评估 TCO 拐点。

## Corrected Claim

条件性推荐边界条件3（基础设施兼容性）：推荐 RTX 5090 的前提是用户具备支持 PCIe 5.0 x16 插槽且供电能力 ≥ 1200W 的主机平台。若用户现有基础设施为 PCIe 4.0 平台，RTX 5090 带宽利用率将下降至 50%（理论 1792 GB/s -> 实际有效 ~896 GB/s），此时性价比排序反转，RTX 4090 (PCIe 4.0 原生) 或 A100 PCIe 4.0 成为更优选择，需重新评估 TCO 拐点。

## Evidence

检索失败: no sources from any channel (all 5 failed)
