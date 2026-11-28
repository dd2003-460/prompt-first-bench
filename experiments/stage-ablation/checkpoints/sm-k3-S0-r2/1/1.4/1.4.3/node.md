# N42: 长上下文衰减的主要机制是 Attention Score 稀疏化导致的 Key-Value 信息丢失，量化表现为有效注意力熵 H_eff 随长度 L 增加而下降

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10

## Claim

长上下文衰减的主要机制是 Attention Score 稀疏化导致的 Key-Value 信息丢失，量化表现为有效注意力熵 H_eff 随长度 L 增加而下降；当 L > 32,768 时，H_eff 下降斜率显著变陡，成为 Perplexity 上升的主导因素（贡献度 >70%）。

## Corrected Claim

长上下文衰减的主要机制通常归因于 Attention Score 稀疏化导致的 Key-Value 信息丢失，表现为有效注意力熵 H_eff 随长度 L 增加而下降；在超长上下文场景下（如超过 32k tokens），这种熵的下降往往成为 Perplexity 上升的重要驱动因素之一。

## Evidence

[质询]该陈述包含具体的经验性阈值（L > 32,768）和精确的贡献度比例（>70%），这些并非从第一性原理或数学公理中严格推导出的必然结论，而是依赖于特定模型架构、训练数据分布及评估方法的经验观测值。不同模型（如 RoPE vs ALiBi）或不同任务下，衰减机制的主导因素和临界点可能存在差异，因此将其表述为普适性的‘主要机制’和‘主导因素’缺乏绝对的理论必然性。 | 先验知识/题面给定，逻辑校验通过。虽然逻辑自洽且符合当前大模型长上下文研究的普遍共识（Attention Sink/Sparsity导致信息稀释），但具体的数值阈值（32k）和贡献度（70%）属于经验事实，在无外部来源直接佐证具体数值的情况下，依据经验事实排除条款，降级为定性表述。

## Search Query

LLM long context attention entropy decay mechanism key value information loss
