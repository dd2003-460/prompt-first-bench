# N253: 在混合负载工作点（重建期间集群仍有20%正常业务I/O），由于CPU上下文切换与缓存污染，校验计算耗时增加至IO时间的15%，即 T_parity_calc ≈

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

在混合负载工作点（重建期间集群仍有20%正常业务I/O），由于CPU上下文切换与缓存污染，校验计算耗时增加至IO时间的15%，即 T_parity_calc ≈ 0.15 * T_read_write；此时Parity_Calc_Overhead系数取中值15%，反映典型生产环境下的干扰效应

## Corrected Claim

在混合负载工作点（重建期间集群仍有20%正常业务I/O），由于CPU上下文切换与缓存污染，校验计算耗时增加至IO时间的15%，即 T_parity_calc ≈ 0.15 * T_read_write；此时Parity_Calc_Overhead系数取中值15%，反映典型生产环境下的干扰效应

## Evidence

父节点级核验未通过：非正交（子节点3（重叠度）与父节点结论存在逻辑冲突：父节点断言校验耗时直接增加至IO时间的15%（暗示无重叠或重叠已包含在内），而子节点3指出高重叠度下实际延迟仅增加3%，二者对'最终耗时影响'的定义不一致。此外，子节点1和2是导致该耗时的微观机制，子节点3是宏观调度策略，三者维度不完全统一。）
