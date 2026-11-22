# N190: 专业推理/代码任务中 INT8/FP8 作为底线的量化依据：在此类任务中，INT4 导致的逻辑错误率或幻觉率显著高于 INT8，需引用具体评测（如 GSM8K 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N43

## Claim

专业推理/代码任务中 INT8/FP8 作为底线的量化依据：在此类任务中，INT4 导致的逻辑错误率或幻觉率显著高于 INT8，需引用具体评测（如 GSM8K 或 HumanEval 的 pass@1 对比）证明 INT8 退化 <2% 而 INT4 退化 >5% 的边界条件。

## Corrected Claim

在专业推理/代码任务中，INT8/FP8通常被视为量化底线，因为INT4量化往往会导致逻辑错误率或幻觉率显著上升。具体退化幅度（如INT8退化<2%而INT4退化>5%）依赖于特定模型架构和评测基准（如GSM8K或HumanEval），需引用具体评测数据证明该边界条件，而非作为通用绝对阈值。

## Evidence

[质询]陈述中引用的具体数值阈值（INT8退化<2%而INT4退化>5%）属于特定模型和评测集下的经验数据，并非普适的物理或逻辑定律。不同模型（如Llama vs Qwen）和任务（GSM8K vs HumanEval）下，量化带来的性能损失差异巨大，直接断言存在固定的'2% vs 5%'边界条件缺乏普遍性，且参考来源摘要未提供具体数值支持。 | 来源[1]主题相关（LLM推理量化评估），但摘要仅提及结论与直觉不符及业务场景相似，未提供GSM8K/HumanEval的具体pass@1对比数据或'2%/5%'的具体阈值，属于间接支持且缺乏具体数值佐证，符合经验事实降级条件。

## Search Query

LLM quantization INT8 vs INT4 GSM8K HumanEval accuracy threshold professional tasks

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/18736185169&rut=f30b0e6a98ac90175c937e662c5cc06bef2a64ff425bb9d6f102829df8d2b643', 'type': 'ddg', 'title': 'Llm 推理量化评估：Fp8、Int8 与 Int4 的全面对比 - 知乎'}
