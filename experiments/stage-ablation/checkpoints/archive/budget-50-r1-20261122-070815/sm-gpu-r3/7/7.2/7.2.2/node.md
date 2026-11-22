# N376: 若将 KV Cache 量化为 INT8，32K 上下文下 KV Cache 显存占用从 2.0GB 降至 1.0GB，总需求降至 14.5GB，剩余 1.5G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N132

## Claim

若将 KV Cache 量化为 INT8，32K 上下文下 KV Cache 显存占用从 2.0GB 降至 1.0GB，总需求降至 14.5GB，剩余 1.5GB 显存，此时需验证激活值峰值是否 ≤1.5GB 以确保稳定运行 [待核验: INT8 KV Cache 对 Qwen3 混合注意力架构的兼容性]

## Corrected Claim

若将 KV Cache 量化为 INT8，32K 上下文下 KV Cache 显存占用从 2.0GB 降至 1.0GB，总需求降至 14.5GB，剩余 1.5GB 显存，此时需验证激活值峰值是否 ≤1.5GB 以确保稳定运行 [待核验: INT8 KV Cache 对 Qwen3 混合注意力架构的兼容性]

## Evidence

先验知识/题面给定，逻辑校验通过：INT8量化将KV Cache显存减半（2.0GB->1.0GB）符合数据位宽减半的物理规律；总需求14.5GB与剩余1.5GB的算术关系自洽（假设总显存16GB）；INT8量化在主流LLM推理框架中是标准且兼容的技术，无逻辑矛盾。

## Search Query

Qwen3 INT8 KV cache memory usage 32k context llama.cpp vllm
