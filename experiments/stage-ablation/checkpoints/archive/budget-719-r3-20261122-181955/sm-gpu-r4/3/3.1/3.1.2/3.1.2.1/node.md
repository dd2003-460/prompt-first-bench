# N274: RTX 4090 在 BF16 精度下的有效内存带宽利用率系数 η_mem 约为 0.65-0.75，该系数反映了实际带宽受 PCIe 传输、内存控制器排队及非

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N91

## Claim

RTX 4090 在 BF16 精度下的有效内存带宽利用率系数 η_mem 约为 0.65-0.75，该系数反映了实际带宽受 PCIe 传输、内存控制器排队及非连续内存访问的影响，需通过 vLLM 或 TensorRT-LLM 基准测试获取具体数值。

## Corrected Claim

RTX 4090 在 BF16 精度下的有效内存带宽利用率系数 η_mem 受 PCIe 传输、内存控制器排队及访问模式影响，具体数值需通过 vLLM 或 TensorRT-LLM 等基准测试在特定负载下获取，典型值通常在 0.6-0.8 之间波动。

## Evidence

[质询]该陈述包含具体的经验数值范围（0.65-0.75），属于经验事实，无法从第一性原理严格推导；且不同模型架构、序列长度及硬件配置下，内存带宽利用率波动较大，固定区间可能缺乏普适性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

RTX 4090 BF16 memory bandwidth utilization efficiency LLM inference vLLM benchmark
