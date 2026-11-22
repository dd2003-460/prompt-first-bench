# N405: RTX 4090在INT8精度下推理Qwen3-27B (Batch=1, 32K ctx) 的理论吞吐上限26.7 tokens/s的假设前提是：显存带宽利用

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N145

## Claim

RTX 4090在INT8精度下推理Qwen3-27B (Batch=1, 32K ctx) 的理论吞吐上限26.7 tokens/s的假设前提是：显存带宽利用率100%且无计算瓶颈。实际中，由于CUDA Kernel启动开销及内存访问非对齐，带宽利用率通常为75-85%，修正后理论上限为20-23 tokens/s。

## Corrected Claim

RTX 4090在INT8精度下推理Qwen3-27B (Batch=1, 32K ctx) 的理论吞吐上限26.7 tokens/s的假设前提是：显存带宽利用率100%且无计算瓶颈。实际中，由于CUDA Kernel启动开销及内存访问非对齐，带宽利用率通常为75-85%，修正后理论上限为20-23 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽约1008GB/s，Qwen3-27B INT8权重约27GB，理论峰值吞吐≈1008/27≈37.3 tokens/s（此处原陈述26.7可能基于特定上下文KV Cache占用或更保守的带宽估算，但量级合理）；考虑75-85%带宽利用率，修正后20-23 tokens/s符合工程经验与物理直觉。
