# N104: NVLink 4.0 (H100) 的双向带宽为 900 GB/s，NVLink 3.0 (A100) 的双向带宽为 600 GB/s。相比 PCIe，NVLi

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

NVLink 4.0 (H100) 的双向带宽为 900 GB/s，NVLink 3.0 (A100) 的双向带宽为 600 GB/s。相比 PCIe，NVLink 将 AllReduce 延迟降低至 PCIe 方案的 1/10 至 1/15，使得多卡推理的通信开销占比从 20%-40% 降至 5%-10% [待核验]。

## Corrected Claim

NVLink 4.0 (H100) 的双向带宽为 900 GB/s，NVLink 3.0 (A100) 的双向带宽为 600 GB/s。相比 PCIe，NVLink 显著降低了 AllReduce 延迟（通常可达一个数量级），在多卡推理中可将通信开销占比从较高的水平（如 20%-40%）大幅降低（如降至 5%-10%），具体数值取决于模型架构与并行策略。

## Evidence

[质询]NVLink 4.0 (H100) 的官方标称双向带宽通常为 900 GB/s，但部分文档或特定配置下可能指单向或不同链路数量下的数值，需确认是否为总带宽；此外，AllReduce 延迟降低至 1/10-1/15 及通信开销占比的具体数值属于经验性性能数据，受具体模型规模、网络拓扑和软件栈影响极大，缺乏通用性保证。 | 先验知识/题面给定，逻辑校验通过。NVLink 4.0 带宽 900GB/s 和 NVLink 3.0 带宽 600GB/s 符合 NVIDIA 官方公开规格（H100 SXM 为 900GB/s，A100 SXM 为 600GB/s）。虽然具体延迟比率和开销占比是经验数据，但在多卡推理场景下，NVLink 的高带宽低延迟特性确实能显著降低通信瓶颈，量级合理。由于 source 为 knowledge，且核心硬件参数准确，逻辑自洽，但经验性比例数据缺乏绝对普适性，故保留但降级以强调其情境依赖性。

## Search Query

NVLink 4.0 vs 3.0 bandwidth AllReduce latency comparison
