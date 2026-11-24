# N222: RTO=4h目标下的合规性差距成本 C_gap_rto：若实际恢复时间 T_actual > 4h，超出部分 (T_actual - 4) 小时的业务损失即为此

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

RTO=4h目标下的合规性差距成本 C_gap_rto：若实际恢复时间 T_actual > 4h，超出部分 (T_actual - 4) 小时的业务损失即为此成本；对于NVMe本地，若采用热备（Hot Standby）策略，T_actual ≈ 0h，但热备硬件成本 = 500TB * SSD_Price * 0.5 (镜像冗余)

## Corrected Claim

RTO=4h目标下的合规性差距成本 C_gap_rto：若实际恢复时间 T_actual > 4h，超出部分 (T_actual - 4) 小时的业务损失即为此成本；对于NVMe本地，若采用热备（Hot Standby）策略，T_actual ≈ 0h，但热备硬件成本 = 500TB * SSD_Price * 0.5 (镜像冗余)

## Evidence

父节点级核验未通过：非正交, 有冗余（1. 正交性问题：父节点明确定义场景为'NVMe本地...采用热备（Hot Standby）'，并给出了热备下的硬件成本公式。然而，子节点1引入了冷备和温备的对比分析，这超出了父节点限定的'热备'范围，导致逻辑边界不清（父节点限定A，子节点讨论A/B/C）。2. 冗余/矛盾问题：父节点中热备硬件成本系数为0.5（可能指单盘或特定冗余理解），而子节点2中定义为1.0或1.5，两者数值矛盾且未解释差异来源（如是否包含控制器、RAID级别等），导致同一概念在父子层级间不一致。）

## Search Query

hot standby storage cost vs RTO compliance penalty
