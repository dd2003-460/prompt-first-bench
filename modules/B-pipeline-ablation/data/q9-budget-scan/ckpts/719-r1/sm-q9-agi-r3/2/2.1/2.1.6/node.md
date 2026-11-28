# N45: ReAct 框架中，当单步工具调用延迟从 1s 增加到 10s 时，任务成功率（Task Success Rate）的衰减斜率（即每增加 1s 延迟导致的成功率

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N10, N11, N12

## Claim

ReAct 框架中，当单步工具调用延迟从 1s 增加到 10s 时，任务成功率（Task Success Rate）的衰减斜率（即每增加 1s 延迟导致的成功率下降百分点），需通过 A/B 测试测定

## Corrected Claim

ReAct 框架中，当单步工具调用延迟从 1s 增加到 10s 时，任务成功率（Task Success Rate）会随延迟增加而下降，其具体衰减曲线（非线性或分段线性）及在不同任务/模型下的变化幅度，需通过 A/B 测试或受控实验测定。

## Evidence

[质询]该陈述将‘衰减斜率’描述为一个需要测定的固定数值或线性关系，但实际中成功率随延迟的变化通常是非线性的（例如存在阈值效应或饱和效应），且不同任务类型、模型能力下斜率差异巨大，不存在通用的‘每增加1s下降X个百分点’的恒定斜率，因此‘测定斜率’这一表述隐含了线性假设，可能与实际非线性衰减不符。 | 经验事实，逻辑自洽但缺来源支持；且‘斜率’一词隐含线性假设，与实际可能的非线性衰减存在潜在冲突，故降级为定性表述。

## Search Query

Agent tool call latency impact task success rate curve ReAct framework
