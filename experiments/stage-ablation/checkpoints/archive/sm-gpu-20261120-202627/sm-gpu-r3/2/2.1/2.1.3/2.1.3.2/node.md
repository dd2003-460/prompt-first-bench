# N210: GSM8K 评测的提示工程依赖度分析：量化 Few-shot（如 5-shot）与 Zero-shot 下 Qwen3-27B 准确率的差值，以验证 N51 中

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

GSM8K 评测的提示工程依赖度分析：量化 Few-shot（如 5-shot）与 Zero-shot 下 Qwen3-27B 准确率的差值，以验证 N51 中 90%-95% 估算是否依赖于特定的少样本提示，从而确定 Quality_Factor 计算时的基准条件一致性

## Corrected Claim

GSM8K 评测的提示工程依赖度分析：需量化 Few-shot（如 5-shot）与 Zero-shot 下 Qwen3-27B 准确率的差值，以验证 N51 中 90%-95% 估算是否依赖于特定的少样本提示，从而确定 Quality_Factor 计算时的基准条件一致性（当前缺乏具体量化数据支持）。

## Evidence

[质询]该陈述声称量化了特定模型（Qwen3-27B）在 GSM8K 上 Few-shot 与 Zero-shot 的准确率差值，但参考来源显示检索失败，无可用外部证据支持这一具体数值或结论；且 Qwen3-27B 的具体评测数据属于经验事实，无法仅凭逻辑推导得出。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B GSM8K few-shot vs zero-shot accuracy gap
