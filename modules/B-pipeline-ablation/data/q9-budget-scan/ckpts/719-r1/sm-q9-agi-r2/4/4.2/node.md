# N17: 建立幻觉检测的定量基线：在Qwen3.8-27B本地部署环境下，对50个已知事实性陈述进行零样本评估，计算幻觉率（False Claim Rate），目标阈值<

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

建立幻觉检测的定量基线：在Qwen3.8-27B本地部署环境下，对50个已知事实性陈述进行零样本评估，计算幻觉率（False Claim Rate），目标阈值<5% [待核验]

## Corrected Claim

在Qwen3.8-27B本地部署环境下，建议建立幻觉检测基线，例如对若干已知事实性陈述进行零样本评估以计算幻觉率，具体样本量与阈值需根据实际业务需求确定。

## Evidence

[质询]该陈述包含具体的实验设计参数（50个样本、零样本评估、<5%阈值），属于经验性操作规范或特定项目设定，无法从第一性原理推导，且参考来源中未提及此具体测试方案及结果。 | 逻辑自洽（幻觉率定义及阈值设定符合常规评估逻辑），但参考来源[1][2]主要关注部署性能与Agent适配，未提供关于‘50个陈述零样本评估’的具体数据或支持，属经验事实缺来源支持。

## Search Query

Qwen 27B hallucination rate benchmark evaluation factual accuracy zero-shot

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2072074634476909289&rut=d97b6d9efd23719ef153d2ef7ccd044b4627c803640d57d09052962666bf48ca', 'type': 'ddg', 'title': 'Qwen3.8-27B 实测：V100 上的部署要点与 Q4/Q8 全量基准'}
- {'url': 'https://zhuanlan.zhihu.com/p/2076326126692185570&rut=2b419bbb28df927b509f204811130819b3a4ee03714f8e39cec41f5e43384a9a', 'type': 'ddg', 'title': '阿里开源 Qwen3.8-27B 本地实测：性能很强，但 Agent 适配仍待补课'}
