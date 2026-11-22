# N204: β=0.45的校准来源：基于N78中CTR与Premium的负相关系数r=-0.45，假设平台算法直接采用相关系数绝对值作为线性惩罚权重，即β = |r| = 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

β=0.45的校准来源：基于N78中CTR与Premium的负相关系数r=-0.45，假设平台算法直接采用相关系数绝对值作为线性惩罚权重，即β = |r| = 0.45；若存在非线性转换函数g()，则β = g(|r|)，需验证g()是否为恒等映射。

## Corrected Claim

β=0.45的校准基于N78中CTR与Premium的负相关系数r=-0.45，假设平台算法采用相关系数绝对值作为线性惩罚权重（β=|r|）；此假设需进一步验证平台是否存在非线性转换函数g()，若存在则β=g(|r|)。

## Evidence

[质询]该陈述将统计相关系数直接等同于算法惩罚权重（β=|r|），属于未经证实的假设。现实中平台算法通常涉及复杂的非线性优化、归一化或业务规则，直接采用相关系数绝对值作为线性惩罚权重缺乏普遍性依据，且未提供具体平台（如N78所指代系统）的算法文档支持。 | source=knowledge，逻辑上自洽（假设明确），但属于特定系统内部机制的经验性假设，缺乏外部来源直接支持该具体映射关系，故降级为定性表述。

## Search Query

platform algorithm CTR price premium correlation coefficient weight calibration
