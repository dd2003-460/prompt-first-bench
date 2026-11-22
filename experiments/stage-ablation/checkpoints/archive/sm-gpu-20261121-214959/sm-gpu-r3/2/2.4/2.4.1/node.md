# N66: 单卡 vs 多卡延迟分解：单卡延迟 T_single = T_compute + T_memory; 多卡延迟 T_multi = T_compute + T_

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

单卡 vs 多卡延迟分解：单卡延迟 T_single = T_compute + T_memory; 多卡延迟 T_multi = T_compute + T_memory + T_comm + T_sync。T_comm = Data_Size / Interconnect_Bandwidth。对于 2x RTX 4090 (PCIe 4.0 x16, 64 GB/s)，若 KV Cache 分片存储，每次生成需跨卡传输 KV 数据 (假设 12.58GB / 2 = 6.29GB)，T_comm = 6.29GB / 64 GB/s ≈ 0.098s。T_compute (FP8 权重, 27GB) = 27GB / (1008 GB/s * 2) ≈ 0.013s。总延迟 ≈ 0.111s/token，吞吐 ≈ 9.0 tokens/s，比单卡 H100 (37.76 tokens/s) 低 76%。

## Corrected Claim

在特定假设下（每次生成需跨卡传输 6.29GB KV Cache 且计算耗时仅由权重读取决定），2x RTX 4090 的延迟约为 0.111s/token，吞吐约为 9.0 tokens/s，显著低于单卡 H100。但该假设（全量 KV 传输）非标准推理场景，实际多卡推理延迟取决于并行策略（如 Tensor Parallelism 或 Pipeline Parallelism）及 KV Cache 管理方式，不能直接推广为通用结论。

## Evidence

[质询]数值量级与物理直觉严重不符：1. T_compute 计算错误：27GB 数据在 2016 GB/s 带宽下耗时应为 ~13ms (0.013s)，但单 token 生成通常受限于内存带宽读取权重，若按此计算，单卡 H100 的 37.76 tokens/s (约 26ms/token) 意味着其有效带宽利用率极低或模型远小于 27GB，此处存在口径混淆（将总权重加载时间误作单 token 计算时间，或忽略了 Attention 计算开销）。2. T_comm 计算错误：6.29GB 数据在 64 GB/s 带宽下耗时应为 ~98ms (0.098s)，这与陈述一致，但 0.098s 的通信开销对于 PCIe 4.0 传输 6GB 数据是合理的，然而总延迟 0.111s 导致吞吐 9 tokens/s，这与 H100 的 37.76 tokens/s 相比确实低 76%，但前提假设（KV Cache 每次生成需跨卡传输 6.29GB）在常规 LLM 推理中极不寻常（通常 KV Cache 是增量更新，而非每次全量传输 6GB），该假设缺乏典型场景支持，属于特定极端假设下的推导，而非通用事实。 | 先验知识/题面给定，逻辑校验发现 T_compute 与 T_comm 的量级及假设场景（每次传输 6.29GB KV）在常规 LLM 推理中不具代表性，且 T_compute 的计算逻辑（27GB/2016GB/s）混淆了权重加载与单 token 计算耗时，导致结论缺乏普适性，降级为特定假设下的定性描述。
