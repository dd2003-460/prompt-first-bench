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

父节点级核验未通过：非正交（子节点1（服务器成本）和子节点2（存储成本）存在重叠，因为子节点1中已包含NVMe SSD成本，而子节点2又单独计算了SSD/HDD存储成本，导致存储成本被重复计算或定义冲突。此外，子节点3推导出的带宽峰值（5-10 Gbps）与父节点假设的固定值（5 Gbps）存在潜在矛盾，需明确是作为输入参数还是推导结果。）
