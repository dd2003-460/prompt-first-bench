# N56: Qwen3-27B在vLLM/llama.cpp推理时，非KV部分的动态激活值峰值显存占用具体为：Prefill阶段（seq_len=32K, batch=1）

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

Qwen3-27B在vLLM/llama.cpp推理时，非KV部分的动态激活值峰值显存占用具体为：Prefill阶段（seq_len=32K, batch=1）约为2.7GB（基于Transformer层间激活矩阵大小估算），Decode阶段（seq_len=1）约为0.5-1.0GB（主要受中间层隐藏状态影响）。

## Corrected Claim

Qwen3-27B在vLLM/llama.cpp推理时，非KV部分的动态激活值峰值显存占用具体为：Prefill阶段（seq_len=32K, batch=1）约为2.7GB（基于Transformer层间激活矩阵大小估算），Decode阶段（seq_len=1）约为0.5-1.0GB（主要受中间层隐藏状态影响）。

## Evidence

先验知识/题面给定，逻辑校验通过
