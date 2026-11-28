# N286: R_auto（自动修复成功率）的实证估算：在本地测试集中，注入已知错误（如数值偏移 10%）的 50 个案例，测试 27B 模型在 Prompt 提示‘请检查并

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N100

## Claim

R_auto（自动修复成功率）的实证估算：在本地测试集中，注入已知错误（如数值偏移 10%）的 50 个案例，测试 27B 模型在 Prompt 提示‘请检查并修正逻辑错误’下的自我修正成功率，预期 R_auto 在 60%-80% 之间波动，而非固定 80%

## Corrected Claim

R_auto（自动修复成功率）的实证估算：在本地测试集中，注入已知错误（如数值偏移 10%）的 50 个案例，测试 27B 模型在 Prompt 提示‘请检查并修正逻辑错误’下的自我修正成功率，预计处于较高水平（具体数值需实测验证，参考范围可能在 60%-80% 之间），而非固定 80%

## Evidence

[质询]该陈述包含具体的实证估算数值（60%-80%）和特定实验设置（27B模型、50个案例、10%数值偏移），属于经验事实。参考来源[1]讨论的是自动程序修复的综述及过拟合检测系统，并未提供关于27B模型在特定Prompt下自我修正成功率的具体实证数据，无法直接支持该具体数值区间。 | 逻辑上，大语言模型在简单逻辑错误修正任务上的成功率通常较高，60%-80%的量级符合当前LLM能力的普遍认知，无内部矛盾；但作为search节点的经验事实，缺乏直接来源支持（来源[1]无关），故降级。

## Search Query

LLM self-correction success rate factual errors prompt engineering benchmark

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1925528546719274454&rut=e29b26a7d7a77af6f401df14e44ba788c2b1eab6af3c07036e3a84c84f88f88e', 'type': 'ddg', 'title': '【综述解析·I】Automated Program Repair: Emerging Trends Pose and Expose ...'}
