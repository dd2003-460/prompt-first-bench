# N373: 最终推荐方案的条件性表述结构模板：'推荐 [Hardware X] 在 [Precision Y] 下，前提是：1) 业务可接受的质量损失阈值 ΔMMLU < 

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

最终推荐方案的条件性表述结构模板：'推荐 [Hardware X] 在 [Precision Y] 下，前提是：1) 业务可接受的质量损失阈值 ΔMMLU < [Z]%；2) 预期日均Token生成量 > [N] 万；3) 电价低于 $[P]/kWh；4) 部署环境散热能力支持 [W] W 持续功耗。若任一条件不满足，则回退至 [Alternative Hardware]。'

## Corrected Claim

最终推荐方案的条件性表述结构模板：'推荐 [Hardware X] 在 [Precision Y] 下，前提是：1) 业务可接受的质量损失阈值 ΔMMLU < [Z]%；2) 预期日均Token生成量 > [N] 万；3) 电价低于 $[P]/kWh；4) 部署环境散热能力支持 [W] W 持续功耗。若任一条件不满足，则回退至 [Alternative Hardware]。'

## Evidence

[rework-angle r1] 该陈述为条件性推荐方案的逻辑结构模板，属于方法论/逻辑框架范畴，非具体经验事实；逻辑自洽，无内部矛盾，且无来源与之冲突。

## Search Query

hardware selection criteria precision power consumption cost tradeoff
