# N22: RTO目标值（小时）：基于业务连续性要求，定义最大允许中断时间 T_rto [待核验：需业务方确认，假设温数据中断导致分析任务停滞，冷数据无实时性要求，取温数据

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

RTO目标值（小时）：基于业务连续性要求，定义最大允许中断时间 T_rto [待核验：需业务方确认，假设温数据中断导致分析任务停滞，冷数据无实时性要求，取温数据RTO=4h，冷数据RTO=24h]

## Corrected Claim

RTO目标值（小时）：基于业务连续性要求，定义最大允许中断时间 T_rto [待核验：需业务方确认，假设温数据中断导致分析任务停滞，冷数据无实时性要求，取温数据RTO=4h，冷数据RTO=24h]

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1和2分别独立量化了温、冷数据的RTO依据（互不重叠）；节点3专注于RTO变动对技术方案选择的敏感性影响（与节点1/2的静态依据区分开）。三者共同覆盖了‘定义依据’、‘量化基础’和‘约束边界’，无冗余重复。）

## Search Query

internal data lake RTO requirement standard hours
