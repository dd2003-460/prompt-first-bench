# N192: MTPx4 接受率 α 的实测基线：在 V100 上运行 Qwen3.8-27B 自回归任务，记录 1000 次生成的平均接受率，预期 α = 0.75 ± 0

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

MTPx4 接受率 α 的实测基线：在 V100 上运行 Qwen3.8-27B 自回归任务，记录 1000 次生成的平均接受率，预期 α = 0.75 ± 0.05，若 α < 0.7 则关闭 MTP 以节省算力。

## Corrected Claim

在 V100 上运行 Qwen3.8-27B 自回归任务时，MTPx4 的接受率 α 通常较高（预期约 0.75），若实测 α 低于 0.7 则建议关闭 MTP 以优化算力效率。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑依赖而非正交：子节点1（理论衰减模型）推导出的 α 值是子节点2（净收益计算）的核心输入变量，两者构成‘原因’与‘结果’或‘参数估计’与‘决策依据’的关系，而非完全独立的研究维度。此外，父节点核心要求是‘实测基线’及‘基于实测的开关策略’，但子节点1主要提供的是理论/经验公式推导，未明确包含‘如何执行1000次生成以获取实测α’的具体实验步骤，导致对父节点‘实测’要求的覆盖存在缺口。）

## Search Query

Qwen3.8-27B MTP speculative decoding acceptance rate V100

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072074634476909289&rut=d97b6d9efd23719ef153d2ef7ccd044b4627c803640d57d09052962666bf48ca', 'type': 'ddg', 'title': 'Qwen3.8-27B 实测：V100 上的部署要点与 Q4/Q8 全量基准'}
- {'url': 'https://github.com/jackinthebox52/qwen38-v100-serve&rut=882b2b646742d318a98a9b60b3dfdb027086e524bfc62bb80022c564c3f7bbc3', 'type': 'ddg', 'title': 'Qwen3.8-27B Serving on NVIDIA Tesla V100-32GB - GitHub'}
