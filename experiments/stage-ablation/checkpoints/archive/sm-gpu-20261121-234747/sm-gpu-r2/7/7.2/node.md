# N145: RTX 3090 24GB在运行Qwen3-27B INT8量化模型时，在32K上下文长度下的实测吞吐量（tokens/s）具体数值，需注明是否因显存带宽瓶颈（

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

RTX 3090 24GB在运行Qwen3-27B INT8量化模型时，在32K上下文长度下的实测吞吐量（tokens/s）具体数值，需注明是否因显存带宽瓶颈（936 GB/s vs 1008 GB/s）导致与4090的比例差异，并标注具体量化方法（如AWQ/GPTQ）

## Corrected Claim

RTX 3090 24GB在运行Qwen3-27B INT8量化模型时，在32K上下文长度下的实测吞吐量具体数值需通过实际基准测试获取，其性能受显存带宽（936 GB/s）限制，与RTX 4090（1008 GB/s）的比例差异需结合具体量化方法（如AWQ/GPTQ）及软件优化程度进行实测对比。

## Evidence

[质询]该陈述要求提供具体的实测吞吐量数值及特定量化方法下的性能对比，属于高度依赖具体硬件环境、软件栈版本及量化实现的经验事实，且参考来源缺失，无法验证具体数值及带宽瓶颈的具体影响比例。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 3090 Qwen3-27B INT8 32k context tokens/s benchmark memory bandwidth bottleneck
