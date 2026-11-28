# N47: W4/NVFP4 精度下模型权重显存占用约为 13.5-14 GB，加上 32K Context 的 KV Cache (若 KV 保持 BF16 约 12-1

- **status**: degraded
- **level**: L3
- **source**: calculation
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13, N14, N15

## Claim

W4/NVFP4 精度下模型权重显存占用约为 13.5-14 GB，加上 32K Context 的 KV Cache (若 KV 保持 BF16 约 12-18 GB，若 KV 也量化则更低)，总显存需求约为 25-32 GB，因此单张 24GB 显卡在 KV 量化配合下勉强可行，48GB 显卡则绰绰有余

## Corrected Claim

W4/NVFP4 精度下模型权重显存占用约为 13.5-14 GB。KV Cache 显存占用取决于模型架构（层数、注意力头配置等），对于典型中等规模模型，32K Context 的 BF16 KV Cache 可能在 10-20 GB 范围。总显存需求通常在 25-35 GB 之间，因此单张 24GB 显卡需配合激进 KV 量化才勉强可行，48GB 显卡则较为充裕。

## Evidence

[质询]KV Cache 的显存占用估算（12-18 GB for 32K context in BF16）缺乏具体的模型架构参数（如层数、头数、head_dim）支持，不同模型（如 Llama-3-8B vs 70B）差异巨大，此处数值可能基于特定未指明的模型假设，存在以偏概全的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且 KV Cache 具体数值依赖模型结构，无法从第一性原理唯一确定）
