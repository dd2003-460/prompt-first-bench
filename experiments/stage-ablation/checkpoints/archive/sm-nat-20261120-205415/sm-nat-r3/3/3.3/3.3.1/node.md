# N53: LFU 在高工作点（ρ=-0.3，缓存容量 C=128GB）下的理论最大字节命中率 H_LFU_max = ∑_{i∈L_f} (h_i * s_i) / ∑_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

LFU 在高工作点（ρ=-0.3，缓存容量 C=128GB）下的理论最大字节命中率 H_LFU_max = ∑_{i∈L_f} (h_i * s_i) / ∑_{i=1}^{N} (h_i * s_i)，其中 L_f 为按 h_i/s_i 排序后总大小不超过 C 的对象集合；该值构成 LFU 性能上限

## Corrected Claim

LFU 在高工作点（ρ=-0.3，缓存容量 C=128GB）下的理论最大字节命中率 H_LFU_max = ∑_{i∈L_f} (h_i * s_i) / ∑_{i=1}^{N} (h_i * s_i)，其中 L_f 为按 h_i/s_i 排序后总大小不超过 C 的对象集合；该值构成 LFU 性能上限

## Evidence

先验知识/题面给定，逻辑校验通过：LFU 的理论最优性能上限确实对应于在容量约束下选择单位字节命中率（h_i/s_i）最高的对象集合，该定义符合缓存替换算法的理论边界推导。
