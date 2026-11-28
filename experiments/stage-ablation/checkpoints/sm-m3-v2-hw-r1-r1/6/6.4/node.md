# N39: 最优混合调度策略：基于任务复杂度分级，简单任务（<1000 tokens）使用本地推理（成本最低），中等任务（1000-10000 tokens）使用本地+轻量

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

最优混合调度策略：基于任务复杂度分级，简单任务（<1000 tokens）使用本地推理（成本最低），中等任务（1000-10000 tokens）使用本地+轻量云端验证（平衡速度与成本），复杂任务（>10000 tokens 或高不确定性）使用云端 API+人工复核（保证质量）；切换阈值由边际收益递减点决定，即 d(C_total)/d(x) = 0 处

## Corrected Claim

最优混合调度策略：基于任务复杂度分级，简单任务（<1000 tokens）使用本地推理（成本最低），中等任务（1000-10000 tokens）使用本地+轻量云端验证（平衡速度与成本），复杂任务（>10000 tokens 或高不确定性）使用云端 API+人工复核（保证质量）；切换阈值由边际收益递减点决定，即 d(C_total)/d(x) = 0 处

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

hybrid scheduling strategy local cloud API cost optimization task complexity
