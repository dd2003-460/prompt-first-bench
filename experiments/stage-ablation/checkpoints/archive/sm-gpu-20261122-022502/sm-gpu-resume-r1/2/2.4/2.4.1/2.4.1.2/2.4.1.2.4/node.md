# N641: vLLM 或 TensorRT-LLM 中 TP=2 的权重分片策略：若采用 Column Parallel (QKV/Output) 和 Row Parall

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N197

## Claim

vLLM 或 TensorRT-LLM 中 TP=2 的权重分片策略：若采用 Column Parallel (QKV/Output) 和 Row Parallel (FFN)，每卡显存占用 = 27GB/2 + KV Cache 共享部分；实测每卡实际读取带宽受 HBM 控制器调度影响，有效带宽通常达理论值 85-90%，即 1008 * 0.85 ≈ 857 GB/s 至 1008 * 0.90 ≈ 907 GB/s

## Corrected Claim

在vLLM或TensorRT-LLM中，若采用Column Parallel和Row Parallel策略，每卡权重显存占用约为总权重的一半（忽略KV Cache差异）。实测每卡有效读取带宽受HBM控制器调度影响，通常可达理论峰值带宽的85-90%（具体数值取决于GPU型号，例如H100 SXM理论带宽约3.35TB/s，此处1008GB/s可能指代特定单卡或特定配置下的有效/理论值，需结合具体硬件确认）。

## Evidence

[质询]该陈述包含具体的硬件性能参数（HBM理论带宽1008 GB/s）和实测效率范围（85-90%），属于经验事实。虽然TP分片策略描述符合主流框架（vLLM/TensorRT-LLM）的常规实现，但具体的带宽数值和效率比例缺乏通用性，高度依赖于具体的GPU型号（如H100 SXM vs PCIe）和系统配置，且未提供特定硬件上下文，存在以偏概全或参数错配的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体带宽/效率数值无法从第一性原理严格推出，需依赖特定硬件实测数据）

## Search Query

vLLM tensor parallelism weight sharding memory bandwidth efficiency RTX 4090
