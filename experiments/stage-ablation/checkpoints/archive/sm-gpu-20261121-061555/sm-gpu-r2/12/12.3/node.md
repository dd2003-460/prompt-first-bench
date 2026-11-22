# N136: 2x RTX 4090 双卡系统在 FP8 推理下的 PCIe Gen4 x16 互联带宽瓶颈影响：All-Reduce 通信延迟具体数值（us/token），

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

2x RTX 4090 双卡系统在 FP8 推理下的 PCIe Gen4 x16 互联带宽瓶颈影响：All-Reduce 通信延迟具体数值（us/token），以及由此导致的吞吐量下降百分比（相比理论线性加速比），用于评估多卡方案的实际有效性能损失是否抵消了部分 TCO 优势。

## Corrected Claim

2x RTX 4090 双卡系统在 FP8 推理下，若仅通过 PCIe Gen4 x16 互联（无 NVLink），All-Reduce 通信将成为显著瓶颈，导致实际吞吐量低于理论线性加速比，具体性能损失取决于模型规模与通信频率，需实测评估其是否抵消 TCO 优势。

## Evidence

[质询]该陈述要求提供具体的经验性数值（All-Reduce 延迟 us/token 及吞吐量下降百分比），但缺乏具体的硬件拓扑（NVLink 或纯 PCIe）、软件栈版本（NCCL 版本）及模型架构细节，导致无法从第一性原理推导出唯一确定的数值，且检索无可用来源支持。 | 经验事实，逻辑自洽但缺来源支持；PCIe Gen4 x16 带宽瓶颈确实会限制双卡通信效率，但具体延迟和吞吐损失需实测数据，无法仅凭逻辑推导得出精确数值。

## Search Query

2x RTX 4090 PCIe Gen4 tensor parallelism all-reduce latency overhead LLM inference
