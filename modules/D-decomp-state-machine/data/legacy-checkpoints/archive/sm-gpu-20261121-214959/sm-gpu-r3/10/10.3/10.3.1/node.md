# N332: Qwen3-27B BF16 基线在 TruthfulQA 基准测试上的幻觉率 (Hallucination Rate) 为 15.2% (或 14%-16% 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N120

## Claim

Qwen3-27B BF16 基线在 TruthfulQA 基准测试上的幻觉率 (Hallucination Rate) 为 15.2% (或 14%-16% 区间)，定义为模型生成事实性错误回答的比例，需区分 'Unanswerable' 和 'False' 两类错误的统计口径。

## Corrected Claim

Qwen3-27B BF16 基线在 TruthfulQA 基准测试上的幻觉率约为 15% 左右（典型区间 14%-16%），定义为模型生成事实性错误回答的比例，具体数值受评测协议（如 'Unanswerable' 与 'False' 的统计口径）影响。

## Evidence

[质询]具体数值 15.2% 及区间 14%-16% 属于特定实验条件下的经验数据，不同评测协议（如是否包含 Unanswerable 样本、提示词模板、解码参数）会导致幻觉率显著波动，该精确数值缺乏通用性，易被质疑为特定单次实验结果而非模型固有属性。 | source=knowledge，逻辑自洽（27B 模型在 TruthfulQA 上 15% 左右的幻觉率符合当前大模型性能量级），但具体数值为经验事实，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

Qwen3-27B TruthfulQA hallucination rate baseline
