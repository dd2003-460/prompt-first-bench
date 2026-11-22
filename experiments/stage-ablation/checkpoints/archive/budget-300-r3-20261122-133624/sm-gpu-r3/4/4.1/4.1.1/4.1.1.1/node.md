# N303: PCIe 5.0 x16在TP=2场景下的有效带宽Bw_eff修正值：理论峰值64 GB/s，但受协议开销、双向传输竞争及驱动延迟影响，实际有效带宽约为理论值的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98

## Claim

PCIe 5.0 x16在TP=2场景下的有效带宽Bw_eff修正值：理论峰值64 GB/s，但受协议开销、双向传输竞争及驱动延迟影响，实际有效带宽约为理论值的70-80%，即Bw_eff ≈ 45-51 GB/s。此修正值直接决定T_comm的最终计算结果。

## Corrected Claim

PCIe 5.0 x16在TP=2场景下的理论峰值带宽为64 GB/s。实际有效带宽受协议开销、双向传输竞争及驱动延迟影响，通常低于理论值，具体数值需依据实测数据或特定硬件文档确定，一般经验估计约为理论值的70-80%（即45-51 GB/s），但此范围未经来源验证。

## Evidence

[质询]该陈述包含具体的经验性数值范围（70-80%效率，45-51 GB/s），属于经验事实而非第一性原理可推导的数学或物理定律。在缺乏外部来源支持的情况下，无法确认该特定效率区间是否准确反映了TP=2场景下的实际协议开销和驱动延迟影响，存在数值偏差的可能性。 | 经验事实，逻辑自洽但缺来源支持。理论峰值64 GB/s计算正确（32 GT/s * 16 lanes / 8 bits * 2 directions），但70-80%的实际效率比属于经验参数，无来源直接支持，故降级。

## Search Query

PCIe 5.0 x16 effective bandwidth tensor parallel LLM inference overhead
