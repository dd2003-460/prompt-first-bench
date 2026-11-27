# N627: 本地工作站 CPU 推理方案（如 64 核 EPYC/Threadripper）的硬件一次性成本：基于 Qwen3-27B INT4 量化权重 (~13.5GB

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N221

## Claim

本地工作站 CPU 推理方案（如 64 核 EPYC/Threadripper）的硬件一次性成本：基于 Qwen3-27B INT4 量化权重 (~13.5GB) 加载至 128GB DDR5 内存，CPU 主机 (含 CPU+主板+128GB RAM) 市场价约为 $2,500-$4,000，显著高于单张 RTX 4090 的 $1,650，但远低于 A100 80GB 的 $15,000。

## Corrected Claim

本地工作站 CPU 推理方案（如 64 核 EPYC/Threadripper）的硬件一次性成本：基于 Qwen3-27B INT4 量化权重 (~13.5GB) 加载至 128GB DDR5 内存，CPU 主机 (含 CPU+主板+128GB RAM) 市场价通常在数千美元量级，显著高于单张 RTX 4090，但远低于 A100 80GB。

## Evidence

[质询]具体硬件组合（64核EPYC/Threadripper + 128GB DDR5）的市场价格区间 $2,500-$4,000 属于经验事实，且受市场波动影响大，缺乏实时来源支持，无法排除价格偏差或配置不匹配的可能性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

64 core CPU 128GB RAM workstation price 2024 Q4 USD
