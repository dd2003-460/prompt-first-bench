# N11: BF16 精度下 Qwen3-27B 推理质量基准：作为无损参考，困惑度（Perplexity）和下游任务准确率（如 MMLU、GSM8K）应作为基线值 [待核

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

BF16 精度下 Qwen3-27B 推理质量基准：作为无损参考，困惑度（Perplexity）和下游任务准确率（如 MMLU、GSM8K）应作为基线值 [待核验：具体数值需查 Qwen3 官方评测报告]

## Corrected Claim

BF16 精度下 Qwen3-27B 推理质量基准：作为无损参考，困惑度（Perplexity）和下游任务准确率（如 MMLU、GSM8K）应作为基线值。具体数值需查阅 Qwen3 官方技术报告或评测文档，现有参考来源未提供确切数值。

## Evidence

[质询]参考来源[1]讨论的是 'Qwen3.8-27B' 和 'Qwen3.6 MoE'，而待核验事实针对的是 'Qwen3-27B'。版本号不匹配（3.8 vs 3），且来源摘要仅提及部署与性能测试（BF16 vs FP8, MTP, 单卡速度），未明确提供困惑度（Perplexity）或下游任务（MMLU, GSM8K）的具体基准数值，无法直接支持该事实节点中的具体数值需求。 | 来源[1]主题相关（Qwen3系列27B模型、BF16精度）但版本不一致（Qwen3.8 vs Qwen3），且未提供具体的Perplexity或MMLU/GSM8K数值，属于间接相关但缺乏直接数据支持，符合经验事实缺来源支持的降级条件。

## Search Query

Qwen3-27B BF16 perplexity MMLU GSM8K benchmark

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072597504793880030&rut=939cafd07a4e15ae1245f5a339b74e22b7f3b2377110377f185cd50347b447f0', 'type': 'ddg', 'title': 'Qwen3.8-27B 的 BF16、FP8、MTP、单卡表现，以及与 Qwen3.6 MoE 的差距'}
