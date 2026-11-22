# N111: 条件分支1（预算<$3,000, W4量化）的延迟量化：2× RTX 3090 PCIe 互联在 W4 量化下的理论 Decode 吞吐量上限 = (Memor

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

条件分支1（预算<$3,000, W4量化）的延迟量化：2× RTX 3090 PCIe 互联在 W4 量化下的理论 Decode 吞吐量上限 = (Memory_Bandwidth_GBps / Bytes_per_token) * 1000，其中 RTX 3090 带宽 936GB/s，W4 下 Bytes_per_token ≈ 13.55GB/1024 (假设有效参数密度)，需计算具体 tokens/s 并对比单卡 4090 的 1008GB/s 带宽优势，评估 PCIe 通信开销（N24）导致的实际性能衰减比例。

## Corrected Claim

条件分支1（预算<$3,000, W4量化）的延迟量化：2× RTX 3090 PCIe 互联在 W4 量化下的理论 Decode 吞吐量上限需基于具体模型规模（如参数量、KV Cache 大小）计算 Bytes_per_token，公式为 (Memory_Bandwidth_GBps / Bytes_per_token) * 1000，其中 RTX 3090 带宽 936GB/s，需明确模型参数后计算具体 tokens/s 并对比单卡 4090 的 1008GB/s 带宽优势，评估 PCIe 通信开销（N24）导致的实际性能衰减比例。

## Evidence

[质询]公式中 Bytes_per_token 的定义存在量纲和逻辑混淆：'13.55GB/1024' 并非标准的每 token 字节数计算方式，且 W4 量化下每 token 的内存占用取决于模型架构（如 KV Cache 大小、权重分布），不能简单用总带宽除以一个模糊的'有效参数密度'得出理论上限，该计算缺乏明确的模型规模假设。 | 先验知识/题面给定，逻辑校验未通过：Bytes_per_token 的计算逻辑不清晰，且未明确模型规模，导致吞吐量公式无法直接应用。
