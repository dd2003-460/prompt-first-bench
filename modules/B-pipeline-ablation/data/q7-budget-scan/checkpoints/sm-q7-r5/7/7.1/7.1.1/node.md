# N257: NVMe SSD阵列物理总容量需求 C_phys = 500TB / 0.98 (RAID6 N=42冗余因子) ≈ 510.2TB，用于确定SSD采购基数

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N125

## Claim

NVMe SSD阵列物理总容量需求 C_phys = 500TB / 0.98 (RAID6 N=42冗余因子) ≈ 510.2TB，用于确定SSD采购基数

## Corrected Claim

NVMe SSD阵列物理总容量需求 C_phys = 500TB / 0.98 (RAID6 N=42冗余因子) ≈ 510.2TB，用于确定SSD采购基数

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点1和子节点2在核心逻辑上高度重叠且存在矛盾。子节点1指出0.98对应超大组并需修正，子节点2直接给出了基于24盘位的修正结果（545.3TB）。两者都涉及“从理论因子到实际硬件限制”的推导过程，导致信息冗余。此外，子节点1中列举的12盘组和24盘组案例与子节点2的最终计算案例重复，且子节点1未明确最终采用哪个配置，而子节点2直接跳到了24盘组的结论，缺乏连贯性。）
