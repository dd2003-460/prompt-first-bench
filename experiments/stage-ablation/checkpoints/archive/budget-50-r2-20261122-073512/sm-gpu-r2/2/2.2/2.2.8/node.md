# N88: NVIDIA H100 80GB 单卡运行 Qwen3-27B (BF16) 的 CAPEX 构成：P_gpu ≈ $30000 [时效待核] + P_chas

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N14

## Claim

NVIDIA H100 80GB 单卡运行 Qwen3-27B (BF16) 的 CAPEX 构成：P_gpu ≈ $30000 [时效待核] + P_chassis (服务器) ≈ $2000 + P_psu (2000W+) ≈ $500 + P_network (NVLink/PCIe) ≈ $500 + P_cooling (液冷/风冷) ≈ $500，总计 ≈ $33500。

## Corrected Claim

NVIDIA H100 80GB 单卡运行 Qwen3-27B (BF16) 的 CAPEX 估算：GPU 成本约 $30,000（随市场波动），配套硬件（机箱、电源、网络、冷却）合计约 $3,000，总计约 $33,000。

## Evidence

[质询]H100 80GB 单卡的市场价格波动较大，$30,000 仅为特定时期或特定渠道的估算值，并非固定常数；此外，服务器机箱、电源、网络及冷却系统的成本因具体配置（如风冷 vs 液冷、PCIe vs NVLink 拓扑）差异显著，$2000/$500 等数值为粗略估算，缺乏统一标准。 | source=knowledge，逻辑自洽（各组件成本量级符合行业常识，总和计算正确），但具体价格属于经验事实且随市场波动，无固定标准，故降级为定性/估算表述。
