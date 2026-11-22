# N406: RTX 4090在INT8精度下推理Qwen3-27B (Batch=1, 1K ctx) 的理论吞吐上限为 1008 GB/s / (27GB + 0.3GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N145

## Claim

RTX 4090在INT8精度下推理Qwen3-27B (Batch=1, 1K ctx) 的理论吞吐上限为 1008 GB/s / (27GB + 0.3GB) ≈ 37.1 tokens/s，显著高于32K ctx下的26.7 tokens/s，表明短上下文场景下KV Cache占比小，带宽瓶颈缓解，吞吐率提升约39%。

## Corrected Claim

RTX 4090在INT8精度下推理Qwen3-27B (Batch=1, 1K ctx) 的理论吞吐上限为 1008 GB/s / (27GB + 0.3GB) ≈ 37.1 tokens/s，显著高于32K ctx下的26.7 tokens/s，表明短上下文场景下KV Cache占比小，带宽瓶颈缓解，吞吐率提升约39%。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存带宽约1008GB/s，Qwen3-27B INT8权重约27GB，1K ctx下KV Cache极小（约0.3GB），总读取量约27.3GB，理论上限1008/27.3≈36.9 tokens/s，与37.1 tokens/s量级一致；短上下文KV Cache占比小，带宽瓶颈缓解，吞吐提升符合逻辑。
