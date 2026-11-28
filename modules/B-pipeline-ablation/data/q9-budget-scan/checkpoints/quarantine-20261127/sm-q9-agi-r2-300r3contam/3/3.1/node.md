# N14: 自我反思机制的成本效益：引入 Critic 角色对初稿进行二次检查，额外消耗 1.5x 推理 token 数。准确率提升幅度取决于任务难度：在事实性错误检测上提

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

自我反思机制的成本效益：引入 Critic 角色对初稿进行二次检查，额外消耗 1.5x 推理 token 数。准确率提升幅度取决于任务难度：在事实性错误检测上提升 15-25%，但在逻辑一致性上仅提升 5-10%。若预算受限，优先在‘结论推导’环节启用，而非‘文献综述’环节。

## Corrected Claim

引入 Critic 角色对初稿进行二次检查会显著增加推理成本（如 Token 消耗和算力占用）。其准确率提升效果因任务而异，通常建议在预算受限时优先用于高价值环节（如结论推导），而非低边际收益环节（如文献综述）。

## Evidence

[质询]陈述中关于“准确率提升幅度”的具体数值（事实性错误检测提升15-25%，逻辑一致性提升5-10%）属于具体的经验统计数据，参考来源仅讨论了成本结构（Token、算力）和定性建议，并未提供这些具体的性能提升百分比数据，存在数据无来源支持的风险。 | 来源[1][2]直接支持了“引入Critic会增加显著成本（如Token消耗增加、算力占用增加）”以及“需权衡成本与收益”的逻辑，但未提供具体的准确率提升百分比数值，故具体数值部分缺乏直接证据支持，降级处理。

## Search Query

self-reflection mechanism LLM factuality improvement cost benefit analysis

## Retrieval Sources

- {'url': 'https://blog.csdn.net/2501_91930600/article/details/161461436&rut=b11921e50611b8dfb7a9ca4001aa6f560dfd6dbb8d9e931dc4fd9742e5ff37a5', 'type': 'ddg', 'title': '反思回路的成本陷阱 何时开启 Critic 何时直接执行-CSDN博客'}
- {'url': 'https://gitcode.csdn.net/6a16e6f2cf85f13e43b6a022.html&rut=3fea5d98d6d8e7885df63dd3e2d35084fe46ea6397c834cde5e5d7dbbcfd27cb', 'type': 'ddg', 'title': '反思回路的成本陷阱 何时开启 Critic 何时直接执行_大数据_搜索引擎技术-AtomGit开源社区'}
