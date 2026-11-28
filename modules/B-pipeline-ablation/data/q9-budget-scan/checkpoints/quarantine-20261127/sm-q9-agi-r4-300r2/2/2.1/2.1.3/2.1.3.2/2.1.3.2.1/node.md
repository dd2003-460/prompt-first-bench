# N302: 头部指令保持率 Retention_head ≈ 95% 的量化验证方法：在 32k 上下文下，将关键约束置于 System Prompt (位置 0-1k)，

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N122

## Claim

头部指令保持率 Retention_head ≈ 95% 的量化验证方法：在 32k 上下文下，将关键约束置于 System Prompt (位置 0-1k)，对比置于中间 (位置 15k-16k) 和尾部 (位置 31k-32k) 的 IFEval 通过率差异；预期数据：Head=95%, Middle=60%, Tail=75%，该梯度证实了首因效应和近因效应的存在，中间区域为最差区间。

## Corrected Claim

在长上下文场景下，关键指令置于头部（System Prompt）的遵循率通常显著高于置于中间，中间区域往往是最差区间，体现了首因效应和近因效应；具体数值随模型和任务而异，典型实验中头部保持率可达90%以上，中间区域可能降至60%-70%左右。

## Evidence

[质询]具体数值（95%/60%/75%）缺乏公开基准测试的直接支持，且不同模型、不同评测集下的表现差异巨大，该特定梯度数据可能源自特定实验或推测，而非通用事实。 | 先验知识/题面给定，逻辑校验通过（符合Lost in the Middle现象及首因/近因效应的定性规律），但具体数值为经验事实且无来源直接支持，故降级。

## Search Query

lost in the middle effect position bias system prompt head tail retention rate
