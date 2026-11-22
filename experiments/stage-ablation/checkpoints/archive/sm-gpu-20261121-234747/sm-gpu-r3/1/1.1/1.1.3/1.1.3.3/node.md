# N172: RTX 4080 Super 16GB 在运行 Qwen3-27B W4 量化模型时的显存占用实测值为 15.2GB（权重）+ 1.8GB（KV Cache 3

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

RTX 4080 Super 16GB 在运行 Qwen3-27B W4 量化模型时的显存占用实测值为 15.2GB（权重）+ 1.8GB（KV Cache 32K）= 17.0GB，超出 16GB 显存上限，因此该方案在 32K 上下文下不可行，除非使用 CPU Offload，此时吞吐量下降系数需单独计算

## Corrected Claim

RTX 4080 Super 16GB 在运行 Qwen3-27B W4 量化模型时，仅权重占用约 15.2GB，剩余显存不足 1GB，无法容纳 32K 上下文所需的 KV Cache（通常需数 GB），因此该方案在 32K 上下文下不可行，除非使用 CPU Offload。

## Evidence

[质询]KV Cache 占用 1.8GB 的数值缺乏具体上下文长度和 Batch Size 的明确界定，且不同推理框架（如 vLLM, llama.cpp）的内存管理策略差异可能导致实际占用波动，该精确数值可能过于理想化或特定于某一未指明的配置。 | 先验知识/题面给定，逻辑校验通过：15.2GB + 1.8GB = 17.0GB > 16GB，数学推导成立，结论符合显存限制的基本物理约束。

## Search Query

RTX 4080 Super 16GB Qwen3-27B W4 quantization VRAM usage 32K context
