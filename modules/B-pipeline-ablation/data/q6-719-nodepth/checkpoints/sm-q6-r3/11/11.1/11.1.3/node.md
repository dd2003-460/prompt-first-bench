# N392: 长尾效应导致的缓存失效边界条件：当对象大小 s > s_threshold（如 10MB）时，缓存命中率 H(s) 骤降至 H_tail（<50%），因为大文件

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N130, N131, N132

## Claim

长尾效应导致的缓存失效边界条件：当对象大小 s > s_threshold（如 10MB）时，缓存命中率 H(s) 骤降至 H_tail（<50%），因为大文件重复访问率低且占用缓存空间大；s_threshold 需根据实际流量分布 P99 对象大小确定，若 P99(s) = 5MB，则 s_threshold = 5MB，超过此阈值的对象按 H_tail 计算成本。

## Corrected Claim

长尾效应通常导致大对象缓存命中率较低。在工程实践中，需根据实际流量分布（如P99对象大小）设定阈值 s_threshold，超过该阈值的对象因重复访问率低且占用空间大，其缓存命中率 H(s) 通常显著低于小对象，具体数值需依据实际监控数据确定。

## Evidence

[质询]该陈述将具体的工程经验参数（如10MB阈值、50%命中率、P99直接作为阈值的线性映射）表述为普适的“边界条件”或确定性规则，忽略了不同业务场景下流量分布、对象生命周期及缓存策略的巨大差异，缺乏普适性逻辑支撑。 | 先验知识/题面给定，逻辑校验通过（内部逻辑自洽，量纲合理），但具体数值（10MB, 50%, P99映射）属于经验事实，无外部来源支持且非第一性原理可推导，故降级。

## Search Query

CDN cache hit rate long tail large files threshold
