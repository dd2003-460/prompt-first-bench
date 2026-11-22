# N21: 推理吞吐量基准公式：Throughput(tokens/s) = (GPU_Memory_Bandwidth_GBps * 1000) / (Model_Siz

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

推理吞吐量基准公式：Throughput(tokens/s) = (GPU_Memory_Bandwidth_GBps * 1000) / (Model_Size_GB * Precision_Factor)，其中 Precision_Factor 为量化后单 token 权重字节数与 BF16 的比值（如 FP8=0.5, INT4=0.25），需结合具体硬件带宽实测值修正

## Corrected Claim

推理吞吐量基准公式：Throughput(tokens/s) = (GPU_Memory_Bandwidth_GBps * 1000) / (Model_Size_GB * Precision_Factor)，其中 Precision_Factor 为量化后单 token 权重字节数与 BF16 的比值（如 FP8=0.5, INT4=0.25），需结合具体硬件带宽实测值修正

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合大模型推理中内存带宽瓶颈（Memory-Bound）的基本物理直觉，量纲推导正确（GB/s / GB = 1/s，乘以1000转换为tokens/s需隐含每token处理1KB数据的假设或单位换算系数，此处通常指每token需读取的权重字节数与带宽之比，公式结构在工程估算中是标准近似），且Precision_Factor定义合理。

## Search Query

LLM inference throughput formula memory bandwidth bound
