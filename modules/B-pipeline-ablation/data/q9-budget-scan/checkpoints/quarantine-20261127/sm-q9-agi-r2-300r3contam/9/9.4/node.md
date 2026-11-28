# N86: 显存溢出 (OOM) 风险的量化边界：在 max-num-seqs=8 且启用 FP8 KV Cache 的情况下，27B 模型的 KV Cache 占用显存随

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

显存溢出 (OOM) 风险的量化边界：在 max-num-seqs=8 且启用 FP8 KV Cache 的情况下，27B 模型的 KV Cache 占用显存随上下文长度线性增长。计算表明，当 max_model_len 超过 100k 时，KV Cache 占用显存超过 12GB/GPU，加上模型权重 (NVFP4 ~14GB) 和激活值缓冲，总显存需求逼近 16GB 物理极限，OOM 概率在 131k 长度下超过 50%。

## Corrected Claim

在 max-num-seqs=8 且启用 FP8 KV Cache 的情况下，27B 模型的 KV Cache 占用显存随上下文长度线性增长。随着 max_model_len 增加，KV Cache 占用显著上升，在长上下文（如 131k）场景下，总显存需求极易超出常规单卡或双卡配置（如 16GB/32GB）的物理极限，导致 OOM 风险极高。

## Evidence

[质询]数值量级与硬件常识存在潜在冲突：16GB 物理极限对于部署 27B 模型（即使使用 NVFP4 量化）而言过于紧张，通常 27B 模型即便量化后也需更大显存空间，且 131k 上下文下的 KV Cache 计算依赖于具体的层数、头数和精度假设，缺乏具体架构参数支撑，存在估算偏差风险。 | 先验知识/题面给定，逻辑校验通过（KV Cache 随长度线性增长符合原理，但具体 GB 数值依赖特定架构假设，无外部来源佐证具体阈值）

## Search Query

vllm kv cache memory footprint calculation 27b model fp8 quantization
