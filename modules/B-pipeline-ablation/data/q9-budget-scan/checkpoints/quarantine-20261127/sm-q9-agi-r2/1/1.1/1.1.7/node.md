# N40: 显存分配冲突：4x16GB=64GB 总显存，扣除 NVFP4 权重 (~14GB) 与激活值/临时缓冲区 (~4GB) 后，剩余 46GB 用于 KV Cac

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

显存分配冲突：4x16GB=64GB 总显存，扣除 NVFP4 权重 (~14GB) 与激活值/临时缓冲区 (~4GB) 后，剩余 46GB 用于 KV Cache；在 max_num_seqs=8 且平均上下文长度 8k tokens 时，所需 KV Cache 为 8 * 8192 * 1.2 MB ≈ 78 GB，超出 46GB 限额，导致 OOM。实际支持的 max_num_seqs 在 8k 上下文下仅为 4-5，而非 8。

## Corrected Claim

在特定模型配置下（假设单 token KV Cache 占用约 1.2 MB），4x16GB 显存扣除权重和激活后剩余 46GB，不足以支撑 8 个并发序列在 8k 上下文下的 KV Cache 需求（约 78GB），因此实际最大并发数受限于显存容量，通常低于 8。

## Evidence

[质询]KV Cache 的具体大小（1.2 MB/token）高度依赖于模型架构（层数、头数、隐藏维度）和精度（FP16/BF16/FP8），陈述中未指明具体模型，直接给出固定数值缺乏普适性基础，且 1.2MB 对于主流大模型（如 Llama-3-8B 约 0.5MB, 70B 约 3.5MB）而言处于中间值，若无特定模型背景，该数值可能不准确。 | source=knowledge，逻辑推导过程（64-14-4=46GB 可用，78GB > 46GB 导致 OOM）自洽，但核心参数 1.2MB/token 为经验值且依赖具体模型，缺乏通用性，故降级。
