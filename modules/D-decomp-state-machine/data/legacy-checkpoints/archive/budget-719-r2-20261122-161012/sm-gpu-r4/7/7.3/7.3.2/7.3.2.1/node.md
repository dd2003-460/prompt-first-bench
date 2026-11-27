# N656: H100 SXM 在 FP8 精度下运行 Qwen3-27B 的 KV Cache 显存占用为 0.5GB 的假设存在误差：32K 上下文下 KV Cache 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N271

## Claim

H100 SXM 在 FP8 精度下运行 Qwen3-27B 的 KV Cache 显存占用为 0.5GB 的假设存在误差：32K 上下文下 KV Cache 实际占用取决于层数、头数和精度，若 KV 保持 BF16 则占用约为 1.0-1.5GB，总显存需求修正为 28.5-28.5GB，但仍远低于 80GB 上限，结论不变但数值需修正

## Corrected Claim

H100 SXM 在 FP8 精度下运行 Qwen3-27B 的 KV Cache 显存占用假设存在误差：32K 上下文下，若 KV 保持 BF16，KV Cache 实际占用约为 2-4GB（取决于具体架构），模型权重（FP8）约 13.5-14GB，总显存需求修正为约 15.5-18GB（若权重为BF16则约为56-58GB），但仍远低于 80GB 上限，结论不变但数值需修正。

## Evidence

[质询]数值量级与内部逻辑存在矛盾：1. 若KV Cache为1.0-1.5GB，模型权重（27B参数，BF16约54GB）加上KV Cache，总显存需求应约为55-55.5GB，而非陈述中声称的'28.5-28.5GB'（该数值仅接近FP8权重大小，未包含KV Cache或计算错误）；2. 27B模型在32K上下文下，若KV为BF16，占用1.0-1.5GB的量级偏小（通常27B模型32K KV Cache在BF16下约为2-4GB，取决于具体架构如GQA/MQA），导致总显存估算偏低。 | 先验知识/题面给定，逻辑校验未通过：总显存需求数值（28.5GB）与分项之和（权重+KV）不符，存在内部矛盾；KV Cache量级估算可能偏低。

## Search Query

Qwen3-27B KV cache size 32k context BF16 calculation
