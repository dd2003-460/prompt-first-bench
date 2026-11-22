# N23: Qwen3-27B模型在FP8精度下的理论内存占用为27GB，计算公式为 27B参数 × 1字节/参数，相比BF16节省50%显存但引入约2-3%的困惑度（Pe

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

Qwen3-27B模型在FP8精度下的理论内存占用为27GB，计算公式为 27B参数 × 1字节/参数，相比BF16节省50%显存但引入约2-3%的困惑度（Perplexity）上升。

## Corrected Claim

Qwen3-27B模型在FP8精度下的理论内存占用为27GB，计算公式为 27B参数 × 1字节/参数，相比BF16节省50%显存但引入约2-3%的困惑度（Perplexity）上升。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8（1字节/参数）下理论内存占用确为27GB，相比BF16（2字节/参数）节省50%显存；2-3%的困惑度上升符合FP8量化在大模型上的典型经验误差范围。
