# N374: Qwen3-27B 在 W4A16 (4-bit 权重, 16-bit 激活) 量化下，WikiText2 Perplexity 相比 BF16 基准的相对增加

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N131

## Claim

Qwen3-27B 在 W4A16 (4-bit 权重, 16-bit 激活) 量化下，WikiText2 Perplexity 相比 BF16 基准的相对增加幅度通常控制在 < 2% (绝对值 < 0.15)，具体需参考 HuggingFace 社区发布的 Qwen3-27B-W4A16 评测报告 [待核验]

## Corrected Claim

Qwen3-27B 在 W4A16 量化下，WikiText2 Perplexity 相比 BF16 基准通常会有轻微增加，具体幅度需参考 HuggingFace 社区发布的 Qwen3-27B-W4A16 评测报告。

## Evidence

[质询]该陈述包含具体的经验性数值指标（Perplexity 增加幅度 < 2% 且绝对值 < 0.15），属于特定模型在特定量化方案下的性能表现，无法从第一性原理推导，且参考来源缺失，无法验证该具体数值是否准确或是否存在特定评测条件（如数据集版本、评测代码版本）导致的偏差。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值指标）

## Search Query

Qwen3-27B W4A16 WikiText2 perplexity benchmark
