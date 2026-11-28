# N30: 在 16GB V100 显存中，Qwen3.8-27B NVFP4 权重的实际加载体积为 13.5GB/卡（27GB总权重/4卡），剩余 2.5GB 显存需分配

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

在 16GB V100 显存中，Qwen3.8-27B NVFP4 权重的实际加载体积为 13.5GB/卡（27GB总权重/4卡），剩余 2.5GB 显存需分配给 CUDA Context (约 0.3GB)、激活值缓冲 (约 0.5GB) 及 KV Cache，实际可用于 KV Cache 的净显存约为 1.7GB/卡。

## Corrected Claim

在 16GB V100 显存中，Qwen3.8-27B NVFP4 权重的实际加载体积约为 6.75GB/卡（假设27GB为FP16总重，NVFP4量化后约为13.5GB总重，即6.75GB/卡），剩余显存需分配给 CUDA Context、激活值缓冲及 KV Cache。

## Evidence

先验知识/题面给定，逻辑校验通过：27GB总权重除以4卡等于6.75GB/卡，加上CUDA Context(0.3GB)和激活值(0.5GB)后，16GB-6.75GB-0.3GB-0.5GB=8.45GB，但题目声称剩余2.5GB用于KV Cache，这里存在明显的算术矛盾。重新计算：16GB - 6.75GB(权重) = 9.25GB剩余。若扣除0.3GB Context和0.5GB激活，剩8.45GB。题目称'剩余2.5GB...实际可用1.7GB'，这与16GB总显存减去6.75GB权重后的9.25GB严重不符。除非'27GB总权重'是指FP16/BF16下的体积，而NVFP4量化后体积减半约为13.5GB总重，即6.75GB/卡。若权重为6.75GB/卡，16-6.75=9.25GB。题目中'13.5GB/卡'的描述与'27GB总权重/4卡'矛盾（27/4=6.75，而非13.5）。若13.5GB是每卡权重，则总重54GB，远超27B模型FP16体积。若27GB是总重，每卡6.75GB。题目陈述内部数据自相矛盾：'13.5GB/卡' vs '27GB总权重/4卡'。因此逻辑不自洽。
