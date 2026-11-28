# N333: LLM-as-a-Judge (GPT-4o) 对科研结论的评分与人类同行评审的 Pearson 相关系数 r 在 0.75-0.85 区间内波动，但当研究结论

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N104, N105, N106

## Claim

LLM-as-a-Judge (GPT-4o) 对科研结论的评分与人类同行评审的 Pearson 相关系数 r 在 0.75-0.85 区间内波动，但当研究结论涉及新颖方法学（Novel Methodology）时，r 降至 0.50-0.60，因为 Judge 缺乏领域内的隐性知识（Tacit Knowledge），此时需强制触发人类复核。

## Corrected Claim

LLM-as-a-Judge (GPT-4o) 在评估常规科研结论时与人类评审具有较高一致性，但在涉及新颖方法学等需要领域隐性知识的场景下，其评估准确性显著下降，建议引入人类复核机制。

## Evidence

[质询]具体数值区间（0.75-0.85 和 0.50-0.60）及特定场景下的相关性下降幅度属于经验事实，缺乏通用共识或标准基准，且参考来源未提供针对‘科研结论’这一特定领域的精确 Pearson 相关系数数据。 | 逻辑上 LLM 在缺乏隐性知识的新颖方法学评估中表现较差符合直觉，但参考来源 [1][2] 主要关注通用 LLM 评估或对齐任务，未直接提供科研结论评估的具体 r 值区间，属于经验事实缺来源支持。

## Search Query

LLM as a judge peer review correlation novel methodology bias

## Retrieval Sources

- {'url': 'https://arxiv.org/html/2403.02839v4&rut=3dd7cf294daedca0a9e62c7b0f069a000edef028359831fb1054a5e143980cce', 'type': 'ddg', 'title': 'An Empirical Study of LLM-as-a-Judge for LLM Evaluation: Fine-tuned ...'}
- {'url': 'https://arxiv.org/html/2408.13006v1&rut=ba8b3a7b06fb2d4554e7ce5c5145bb81296f353220e1b0e967df588b7013a81b', 'type': 'ddg', 'title': 'Systematic Evaluation of LLM-as-a-Judge in LLM Alignment Tasks:'}
