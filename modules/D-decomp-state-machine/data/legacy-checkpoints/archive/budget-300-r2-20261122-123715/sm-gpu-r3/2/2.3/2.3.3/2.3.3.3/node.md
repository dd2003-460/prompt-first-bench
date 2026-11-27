# N223: H100 PCIe 版本 (700W) 与 SXM 版本 (700W) 在 FP8 推理吞吐量上存在差异，PCIe 版本因 NVLink 缺失或带宽较低 (40

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N62

## Claim

H100 PCIe 版本 (700W) 与 SXM 版本 (700W) 在 FP8 推理吞吐量上存在差异，PCIe 版本因 NVLink 缺失或带宽较低 (400GB/s vs 900GB/s)，在多卡并行时效率下降，但单卡推理时差异较小，需根据具体部署方式 (单卡 vs 多卡) 选择版本。

## Corrected Claim

H100 PCIe 版本与 SXM 版本在 FP8 推理吞吐量上存在差异，SXM 版本因具备 NVLink 高速互联（900GB/s）及更高带宽的 HBM3 显存，在多卡并行时效率显著高于 PCIe 版本（无 NVLink，依赖 PCIe 互联），单卡推理时差异主要源于显存带宽差异（HBM3 vs GDDR6），需根据具体部署方式选择版本。

## Evidence

[质询]数值量级与规格混淆：H100 PCIe 版本通常配备 80GB GDDR6 显存，带宽约为 2TB/s，而 SXM 版本配备 80GB HBM3 显存，带宽约为 3.35TB/s。陈述中提到的 '400GB/s vs 900GB/s' 既不符合 H100 的显存带宽规格，也不符合 NVLink 带宽规格（H100 NVLink 为 900GB/s，但 PCIe 版本无 NVLink 或仅通过 PCIe 连接，PCIe 5.0 x16 带宽约为 64GB/s）。该数值可能混淆了其他代际产品或特定接口带宽，导致技术细节错误。 | 逻辑上多卡并行依赖高速互联（NVLink）是合理的，但具体数值（400GB/s vs 900GB/s）与 H100 公开规格不符（H100 SXM NVLink 为 900GB/s，PCIe 无 NVLink；显存带宽分别为 ~2TB/s 和 ~3.35TB/s）。参考来源 [1] 仅列出 H100 存在 PCIe 和 SXM 版本，未提供具体带宽对比数据，无法直接支持该具体数值，且该数值属于经验事实，缺乏可靠来源支持，故降级。

## Search Query

H100 PCIe vs SXM FP8 inference performance difference single card

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units', 'type': 'wikipedia', 'title': 'List of Nvidia graphics processing units'}
