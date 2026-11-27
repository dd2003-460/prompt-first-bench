# N298: Qwen3-27B 在 NVFP4 量化下，WikiText2 Perplexity 绝对值通常升至 6.2-6.5，相比 BF16 基准 (5.6) 增加约 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

Qwen3-27B 在 NVFP4 量化下，WikiText2 Perplexity 绝对值通常升至 6.2-6.5，相比 BF16 基准 (5.6) 增加约 10.7-16.1%，严重超出 N98 定义的 5% 阈值，表明 4-bit 精度在通用文本生成上存在显著质量损失。

## Corrected Claim

Qwen3-27B 在 4-bit 量化（如 NVFP4）下，WikiText2 Perplexity 通常会出现显著上升（例如从 BF16 基准的 ~5.6 升至 6.0 以上），增幅往往超过 5%，表明 4-bit 精度在通用文本生成上存在可感知的质量损失。

## Evidence

[质询]具体数值（6.2-6.5, 5.6）及百分比增幅属于特定实验条件下的经验数据，不同量化实现（如GPTQ, AWQ, SmoothQuant）或校准数据集可能导致结果差异，且NVFP4并非业界最通用的4-bit标准（常见为INT4/FP4），缺乏通用性保证。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体量化精度损失数值无法从第一性原理严格推导，属于需实证验证的经验参数）

## Search Query

Qwen3-27B NVFP4 quantization WikiText2 perplexity absolute value
