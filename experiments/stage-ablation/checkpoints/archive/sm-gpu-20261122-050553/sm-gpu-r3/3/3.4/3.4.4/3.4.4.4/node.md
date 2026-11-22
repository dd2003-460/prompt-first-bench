# N234: Qwen3-27B BF16 在通用对话基准（如 MT-Bench 或 AlpacaEval）上的相对得分基线 (Score_base_chat) 为 [待核验

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N74

## Claim

Qwen3-27B BF16 在通用对话基准（如 MT-Bench 或 AlpacaEval）上的相对得分基线 (Score_base_chat) 为 [待核验]，需引用官方或第三方评测中 Qwen3-27B 的对话质量分数（如 MT-Bench 2.0 的 Win Rate 或 Likert 评分），作为对话任务 PPL 阈值判定的替代量化指标（因 PPL 非直接对话指标）。

## Corrected Claim

Qwen3-27B BF16 在通用对话基准（如 MT-Bench 或 AlpacaEval）上的相对得分基线 (Score_base_chat) 需引用官方或第三方评测中的具体对话质量分数（如 MT-Bench 2.0 的 Win Rate 或 Likert 评分），作为对话任务 PPL 阈值判定的替代量化指标；具体数值需查阅最新评测报告确认。

## Evidence

[质询]该陈述声称存在一个具体的数值基线（Score_base_chat），但Qwen3-27B的具体对话基准得分（如MT-Bench或AlpacaEval分数）属于经验事实，且不同评测版本（如MT-Bench 1.0 vs 2.0）和评测协议会导致数值差异，无法从第一性原理推导，且当前无来源支持具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体模型评测分数属于需外部验证的经验数据，不适用第一性原理推导条款）

## Search Query

Qwen3-27B MT-Bench AlpacaEval baseline score
