# N317: 2×RTX 4090 (FP8) 在 Batch Size=1, 32K输入/1K输出下的实测吞吐量下限：基于vLLM/TensorRT-LLM在RTX 409

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88

## Claim

2×RTX 4090 (FP8) 在 Batch Size=1, 32K输入/1K输出下的实测吞吐量下限：基于vLLM/TensorRT-LLM在RTX 4090双卡PCIe拓扑下的公开基准测试，FP8精度下Qwen3-27B的实测吞吐量通常在 5-12 tokens/s 区间 [search: 需检索具体benchmark]，显著低于父节点预估的20-30 tokens/s，主要受限于PCIe 4.0 x16带宽瓶颈和FP8 kernel在Ada架构上的优化程度。

## Corrected Claim

2×RTX 4090 (FP8) 在 Batch Size=1, 32K输入/1K输出下的实测吞吐量具体数值需进一步验证，但通常受限于显存带宽及FP8 kernel优化程度，可能低于单卡理想预估。

## Evidence

[质询]数值量级存疑：2x RTX 4090 拥有约 96GB 显存，足以容纳 Qwen3-27B (FP8 约 27GB) 且无需频繁 PCIe 交换权重；在 Batch=1 下，推理瓶颈通常为显存带宽而非 PCIe 带宽，5-12 tokens/s 的下限可能过低，且缺乏具体公开基准测试的直接引用。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据验证具体吞吐量数值）

## Search Query

vLLM RTX 4090 dual GPU Qwen3-27B FP8 throughput benchmark 32k context
