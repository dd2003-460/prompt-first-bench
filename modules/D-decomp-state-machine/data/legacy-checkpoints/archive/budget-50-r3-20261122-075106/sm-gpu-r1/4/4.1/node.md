# N27: 在BF16精度下，NVIDIA RTX 4090 (24GB) 运行 Qwen3-27B 的稳态生成吞吐率（Token/s）约为 15-25，首Token延迟（

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

在BF16精度下，NVIDIA RTX 4090 (24GB) 运行 Qwen3-27B 的稳态生成吞吐率（Token/s）约为 15-25，首Token延迟（TTFT）约为 2-5s，每Token生成时间（TPOT）约为 40-65ms

## Corrected Claim

在BF16精度下，Qwen3-27B模型参数占用约54GB显存，无法直接装入NVIDIA RTX 4090 (24GB)显存中运行；若使用量化（如INT8/INT4）或CPU offload，性能指标需另行评估。

## Evidence

[质询]来源仅讨论了显存占用（27B * 2 bytes ≈ 54GB，远超24GB，暗示BF16无法直接装入24GB显存，需量化），未提供具体的吞吐率、TTFT或TPOT数值，且BF16下27B模型在24GB显存上通常无法运行（除非使用offload或极低精度，但题目指定BF16），存在前提可行性矛盾。 | 来源[1]指出BF16下27B模型参数占用约54GB显存，超出RTX 4090的24GB显存限制，因此该陈述的前提（BF16下在24GB显存上运行）在逻辑上存疑，且来源未提供性能数据支持。

## Search Query

NVIDIA RTX 4090 Qwen3-27B BF16 inference throughput tokens per second TTFT TPOT

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2078119870546309718&rut=267744f036c0de570b3a5a196b6d0bf88002cc9ce0f95ce7243a1d95e0df04b8', 'type': 'ddg', 'title': 'RTX 4090 24GB 能跑 Qwen3.8-27B 吗？该选什么量化和云GPU？'}
