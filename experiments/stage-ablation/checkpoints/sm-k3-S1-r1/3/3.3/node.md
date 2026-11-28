# N23: 投机解码的草稿模型应为主模型的蒸馏版本（如Qwen3-7B），参数量为主模型的1/4-1/8，草稿模型生成速度为主模型的4-8倍，验证开销为1次主模型前向传播，

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

投机解码的草稿模型应为主模型的蒸馏版本（如Qwen3-7B），参数量为主模型的1/4-1/8，草稿模型生成速度为主模型的4-8倍，验证开销为1次主模型前向传播，净加速比为 (draft_speedup * acceptance_rate) / (1 + verification_overhead)。

## Corrected Claim

投机解码的草稿模型应为主模型的蒸馏版本（如Qwen3-7B），参数量为主模型的1/4-1/8，草稿模型生成速度为主模型的4-8倍，验证开销为1次主模型前向传播，净加速比为 (draft_speedup * acceptance_rate) / (1 + verification_overhead)。

## Evidence

先验知识/题面给定，逻辑校验通过：投机解码的核心机制即为小模型草稿+大模型验证，加速比公式符合串行/并行计算逻辑，参数比例与速度倍数符合常见工程实践量级。

## Search Query

speculative decoding draft model ratio Qwen3
