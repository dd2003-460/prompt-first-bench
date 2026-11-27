# N242: W4A8 量化下 Qwen3-27B 在 WikiText-2 数据集上的 Perplexity (PPL) 具体数值，需对比 W4A16 的 PPL 以量化 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

W4A8 量化下 Qwen3-27B 在 WikiText-2 数据集上的 Perplexity (PPL) 具体数值，需对比 W4A16 的 PPL 以量化 1-3 个百分点的损失幅度，来源需包含校准集大小和量化算法（如 SmoothQuant/GPTQ）细节。

## Corrected Claim

W4A8 量化下 Qwen3-27B 在 WikiText-2 数据集上的 Perplexity (PPL) 通常较 W4A16 有所上升，具体数值取决于量化算法（如 SmoothQuant/GPTQ）及校准集配置，一般损失幅度在 1-3 个百分点范围内，需查阅特定实验报告获取精确值。

## Evidence

[质询]该陈述要求提供具体的PPL数值及量化损失幅度，属于高度依赖具体实验配置（校准集大小、量化算法、硬件环境）的经验事实。不同实现（如SmoothQuant vs GPTQ）和校准数据会导致PPL数值显著波动，不存在唯一的‘具体数值’，且‘1-3个百分点’的损失幅度并非固定常数，而是随模型版本和量化策略变化的统计结果。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该事实无法从第一性原理严格推出，属于具体实验数据）。

## Search Query

Qwen3-27B W4A8 quantization perplexity WikiText-2 vs W4A16 benchmark
