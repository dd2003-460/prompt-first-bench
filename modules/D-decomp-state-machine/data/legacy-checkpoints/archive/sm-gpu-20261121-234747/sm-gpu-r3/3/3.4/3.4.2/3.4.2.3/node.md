# N275: 4×A100在PCIe互联下的实测吞吐量下降比例并非固定30-50%，而是与batch size和序列长度正相关；在32K长上下文下，由于KV Cache传输量

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98

## Claim

4×A100在PCIe互联下的实测吞吐量下降比例并非固定30-50%，而是与batch size和序列长度正相关；在32K长上下文下，由于KV Cache传输量巨大，PCIe瓶颈导致吞吐量可能下降50-70%，需基于具体硬件拓扑（如是否支持P2P）和软件栈版本进行实测验证

## Corrected Claim

4×A100在PCIe互联下的实测吞吐量下降比例与batch size和序列长度正相关；在32K长上下文下，由于KV Cache传输量巨大，PCIe瓶颈可能导致显著的性能下降（具体幅度需基于硬件拓扑和软件栈实测验证）。

## Evidence

[质询]具体数值区间（50-70%）缺乏通用基准支持，属于高度依赖特定硬件拓扑（如是否启用P2P、PCIe版本）和软件栈优化的经验性估计，存在将特定场景数据泛化为普遍规律的风险。 | 经验事实，逻辑自洽（KV Cache随序列长度线性增长导致PCIe带宽瓶颈加剧符合物理直觉），但检索无可用来源，且具体百分比数值无法从第一性原理严格推导，故降级。

## Search Query

A100 PCIe tensor parallel throughput degradation long context 32K
