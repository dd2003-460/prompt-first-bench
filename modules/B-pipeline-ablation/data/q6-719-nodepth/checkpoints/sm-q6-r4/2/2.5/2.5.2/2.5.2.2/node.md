# N199: C_bw_pop 的单 POP 带宽成本：C_bw_pop = B_pop_peak * P_bw_monthly；假设单 POP 峰值带宽 5Gbps，P_b

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

C_bw_pop 的单 POP 带宽成本：C_bw_pop = B_pop_peak * P_bw_monthly；假设单 POP 峰值带宽 5Gbps，P_bw_monthly = ¥2000/Gbps/月，则 C_bw_pop = 5 * 2000 = ¥10,000/月/POP；此值基于运营商专线报价，需根据实际地域和带宽需求调整

## Corrected Claim

C_bw_pop 的单 POP 带宽成本：C_bw_pop = B_pop_peak * P_bw_monthly；假设单 POP 峰值带宽 5Gbps，P_bw_monthly = ¥2000/Gbps/月，则 C_bw_pop = 5 * 2000 = ¥10,000/月/POP；此值基于运营商专线报价，需根据实际地域和带宽需求调整

## Evidence

父节点级核验未通过：非正交, 不完备（1. 严重逻辑矛盾与正交性破坏：父节点明确定义为 C_bw_pop（带宽成本），但子节点中混入了服务器、存储、人力、监控等完全无关的成本项，导致子节点集合不再正交于父节点定义。2. 内部数据矛盾：子节点4给出的带宽单价范围（1500-2500）与父节点及子节点隐含的基准值（2000）虽一致，但子节点6声称监控成本“低于N200假设的¥1,000/月”，而实际计算为¥6,000/月，存在事实性错误且与父节点语境脱节。3. 完备性缺失：若父节点仅指带宽成本，则多余子节点应删除；若父节点意指单POP总成本，则缺少电力、机柜租赁等关键项，且命名错误。）
