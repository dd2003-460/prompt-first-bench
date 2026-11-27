# N460: NCCL All-Reduce 在 2 卡 PCIe 4.0 互联下的实测带宽：在消息大小 > 1MB 时，实测带宽通常接近 PCIe 理论峰值的 85%-95

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N147

## Claim

NCCL All-Reduce 在 2 卡 PCIe 4.0 互联下的实测带宽：在消息大小 > 1MB 时，实测带宽通常接近 PCIe 理论峰值的 85%-95% [待核验]，具体数值需通过 nccl-tests all_reduce_perf 获取

## Corrected Claim

NCCL All-Reduce 在 2 卡 PCIe 4.0 互联下的实测带宽：在消息大小 > 1MB 时，实测带宽通常接近 PCIe 理论峰值，具体效率取决于 P2P 支持情况及拓扑结构，需通过 nccl-tests all_reduce_perf 获取实际数值。

## Evidence

[质询]该陈述包含具体的经验性数值范围（85%-95%），属于硬件性能实测数据，无法从第一性原理推导。且不同PCIe拓扑（如P2P是否开启、是否经过CPU Root Complex）及驱动版本会导致带宽效率显著波动，该固定区间可能过于乐观或特定于某些理想配置，缺乏通用性保证。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且属于硬件实测数据，不适用第一性原理推导条款）

## Search Query

nccl-tests all_reduce_perf PCIe 4.0 2 GPU bandwidth
