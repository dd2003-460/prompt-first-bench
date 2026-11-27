# N194: 2×RTX 4090 方案的稳定性风险：PCIe 互联无 ECC 保护 (部分主板支持但 GPU 显存本身无 ECC 或仅支持有限 ECC)，导致长时间运行 (

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N66

## Claim

2×RTX 4090 方案的稳定性风险：PCIe 互联无 ECC 保护 (部分主板支持但 GPU 显存本身无 ECC 或仅支持有限 ECC)，导致长时间运行 (24/7) 下出现位翻转 (Bit Flip) 的概率高于 HBM 方案，预计 MTBF (平均无故障时间) 比 A100/H100 低 20-30%，需计入维护成本和潜在数据损坏风险，建议每 6 个月进行一次显存健康检查。

## Corrected Claim

2×RTX 4090 方案因显存无 ECC 保护，在 24/7 长时间运行下出现静默数据损坏（Bit Flip）的风险高于 HBM 方案（如 A100/H100），需计入维护成本和潜在数据损坏风险，建议定期（如每 6 个月）进行显存健康检查。

## Evidence

[质询]MTBF 降低 20-30% 的具体数值缺乏公开基准数据支持，属于经验性估算而非可推导事实；此外，RTX 4090 显存（GDDR6X）确实无 ECC，但 PCIe 互联本身通常有 CRC 校验，将‘PCIe 无 ECC’直接归因为位翻转主因在技术细节上略显粗糙，主要风险确实来自显存无 ECC。 | 先验知识/题面给定，逻辑校验通过：RTX 4090 显存无 ECC 是事实，长期运行稳定性低于带 ECC 的 HBM 方案符合工程直觉，但具体 MTBF 降幅为经验估计，故降级。
