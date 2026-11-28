# N40: 针对 Qwen3.8-27B 模型，在 100 篇 Nature/Science 子刊摘要构成的测试集上，使用 BM25 算法检索 Top-5 文档的 Reca

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10, N11, N12

## Claim

针对 Qwen3.8-27B 模型，在 100 篇 Nature/Science 子刊摘要构成的测试集上，使用 BM25 算法检索 Top-5 文档的 Recall@5 基线值（需实测，预计 0.6-0.8 区间）

## Corrected Claim

针对 Qwen3.8-27B 模型，在 100 篇 Nature/Science 子刊摘要构成的测试集上，使用 BM25 算法检索 Top-5 文档的 Recall@5 基线值待实测，预估区间为 0.6-0.8。

## Evidence

[质询]该陈述声称是一个“基线值”并给出了具体的数值区间（0.6-0.8），这属于经验事实（Empirical Fact）。然而，陈述中明确标注“需实测”，意味着该数据尚未产生，目前的数值仅为预测或估计。将未发生的实验结果作为既定事实陈述，且缺乏任何来源支持该特定模型在特定数据集上的具体表现，存在将“预期”混淆为“事实”的风险。此外，Qwen3.8-27B 是否为真实存在的公开模型版本存疑（通常 Qwen 系列版本命名不同，如 Qwen2.5, Qwen3 等，且 27B 并非标准常见尺寸，可能是虚构或内部代号），若模型不存在，则整个前提失效。 | 经验事实，逻辑自洽但缺来源支持。检索无可用来源，且该数值为预测值而非实测结果，符合 degraded 判定条件。

## Search Query

BM25 Recall at K scientific literature retrieval benchmark Qwen
