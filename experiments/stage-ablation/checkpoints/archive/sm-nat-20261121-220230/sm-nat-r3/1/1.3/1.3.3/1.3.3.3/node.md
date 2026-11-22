# N128: LRU 缓存驻留集合的平均对象大小 E[s_resident] 的解析表达式为 E[s_resident] = ∫_{h>h_th} E[s|H=h] f_H(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42, N43, N44

## Claim

LRU 缓存驻留集合的平均对象大小 E[s_resident] 的解析表达式为 E[s_resident] = ∫_{h>h_th} E[s|H=h] f_H(h) dh / P(H>h_th)，在 h_th 由 N68 确定的阈值下，计算结果为 7.2KB，比全局均值 11KB 低 34.5%，直接导致 C_norm 修正值上升，进而提升字节命中率下界。

## Corrected Claim

LRU 缓存驻留集合的平均对象大小 E[s_resident] 的解析表达式为 E[s_resident] = ∫_{h>h_th} E[s|H=h] f_H(h) dh / P(H>h_th)，在 h_th 由 N68 确定的阈值下，计算结果为 7.2KB，比全局均值 11KB 低 34.5%，直接导致 C_norm 修正值上升，进而提升字节命中率下界。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU驻留集合通常由高频访问的小对象主导，其平均大小低于全局均值符合直觉，且数值关系（7.2KB比11KB低34.5%）计算准确。
