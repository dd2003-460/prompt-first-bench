# N119: HotpotQA 多跳推理 EM 提升基线值：ReAct (GPT-3.5) 相比 CoT 在 HotpotQA 验证集上的 Exact Match 提升为 +

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

HotpotQA 多跳推理 EM 提升基线值：ReAct (GPT-3.5) 相比 CoT 在 HotpotQA 验证集上的 Exact Match 提升为 +12.4% (from 42.1% to 54.5%)，此数据基于 2022 年原始论文，需校正为 Qwen3-27B 在当前量化精度下的实际增益，预计增益区间收窄至 +5%-10% 因模型基础能力更强

## Corrected Claim

ReAct框架在HotpotQA等基准上通常优于CoT，但具体EM提升幅度（如+12.4%）依赖于特定模型版本（如GPT-3.5）和实验设置；对于Qwen3-27B等更强基座模型，预期增益会因基础能力提升而收窄，具体数值需以最新实验报告为准。

## Evidence

[质询]具体数值（42.1%, 54.5%, +12.4%）及Qwen3-27B的预测增益区间（+5%-10%）属于特定实验条件下的经验数据，参考来源中完全缺失这些具体指标，且不同模型/设置下结果差异巨大，无法从通用描述中推导。 | 参考来源[1][2][3]仅介绍HotpotQA数据集背景及多跳问答概念，未包含ReAct vs CoT的具体EM对比数据或Qwen3-27B的实验结果，属于经验事实且缺乏直接来源支持。

## Search Query

Qwen3-27B ReAct vs CoT HotpotQA exact match benchmark 2024

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00653/article/details/154558405&rut=b5f81b8f46b2ddbee94f0174dcfedbc01946fbd3e8ba8839aebf3157b5ffdb61', 'type': 'ddg', 'title': '如何利用HotpotQA提升多跳问答模型性能？完整实用教程-CSDN博客'}
- {'url': 'https://hotpotqa.github.io/&rut=e48274a12c0063d956043c83a718429ee44ab54463caeb7c5dbdb1798df748a9', 'type': 'ddg', 'title': 'HotpotQA Homepage'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/154558405&rut=f3cacca08e58a2e4a6fb8e0ff26261c4525c1f696b13b30a3c80914b9b49d1d7', 'type': 'ddg', 'title': '如何利用HotpotQA提升多跳问答模型性能？完整实用教程_井章博Church-智能体开发者社区'}
