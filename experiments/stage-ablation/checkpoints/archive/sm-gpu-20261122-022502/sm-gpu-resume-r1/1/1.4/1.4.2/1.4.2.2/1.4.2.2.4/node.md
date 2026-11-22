# N510: RTX 5090 在 Decode 阶段的实际有效带宽利用率通常仅为 60-75%（受限于 Kernel 启动开销、内存访问模式及 PCIe/NVLink 瓶颈

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N156

## Claim

RTX 5090 在 Decode 阶段的实际有效带宽利用率通常仅为 60-75%（受限于 Kernel 启动开销、内存访问模式及 PCIe/NVLink 瓶颈），因此实际可观测的 Decode 吞吐约为 39.8-49.8 tokens/s (66.37 * 0.6-0.75)。

## Corrected Claim

RTX 5090 在 Decode 阶段的有效带宽利用率受 Kernel 开销及内存访问模式限制，通常低于理论峰值（具体数值依负载而定），导致实际吞吐低于理论上限。

## Evidence

[质询]60-75%的带宽利用率是一个高度依赖具体模型架构、Batch Size、序列长度及硬件配置的经验性估计值，并非固定物理常数；且RTX 5090作为消费级显卡，其PCIe带宽瓶颈在Decode阶段（小Batch）通常比NVLink更显著，笼统归因于'PCIe/NVLink瓶颈'且给出精确的39.8-49.8 tokens/s范围缺乏普适性依据。 | 先验知识/题面给定，逻辑校验通过（数学计算 66.37 * 0.6 ≈ 39.8, 66.37 * 0.75 ≈ 49.8 正确），但具体利用率区间属于经验事实，缺乏通用性，故降级。

## Search Query

LLM inference memory bandwidth utilization efficiency typical range 60-75%
