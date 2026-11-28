# N192: MTPx4 接受率 α 的实测基线：在 V100 上运行 Qwen3.8-27B 自回归任务，记录 1000 次生成的平均接受率，预期 α = 0.75 ± 0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55

## Claim

MTPx4 接受率 α 的实测基线：在 V100 上运行 Qwen3.8-27B 自回归任务，记录 1000 次生成的平均接受率，预期 α = 0.75 ± 0.05，若 α < 0.7 则关闭 MTP 以节省算力。

## Corrected Claim

在 V100 上运行 Qwen3.8-27B 自回归任务时，MTPx4 的接受率 α 通常较高（预期约 0.75），若实测 α 低于 0.7 则建议关闭 MTP 以优化算力效率。

## Evidence

[质询]该陈述包含具体的经验性数值基线（α = 0.75 ± 0.05）和特定的决策阈值（α < 0.7），这属于经验事实而非第一性原理可推导内容。参考来源虽然涉及相同的硬件（V100）和模型（Qwen3.8-27B）以及MTP技术，但摘要中并未提供具体的接受率数值或验证该特定基线的数据，因此缺乏直接的外部证据支持该具体数值。 | 逻辑自洽（MTP接受率通常在0.7-0.9之间，阈值设定合理），但作为经验事实，参考来源[1][2]仅确认了测试环境和技术栈的存在，未提供具体的α数值支持，故降级。

## Search Query

Qwen3.8-27B MTP speculative decoding acceptance rate V100

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072074634476909289&rut=d97b6d9efd23719ef153d2ef7ccd044b4627c803640d57d09052962666bf48ca', 'type': 'ddg', 'title': 'Qwen3.8-27B 实测：V100 上的部署要点与 Q4/Q8 全量基准'}
- {'url': 'https://github.com/jackinthebox52/qwen38-v100-serve&rut=882b2b646742d318a98a9b60b3dfdb027086e524bfc62bb80022c564c3f7bbc3', 'type': 'ddg', 'title': 'Qwen3.8-27B Serving on NVIDIA Tesla V100-32GB - GitHub'}
