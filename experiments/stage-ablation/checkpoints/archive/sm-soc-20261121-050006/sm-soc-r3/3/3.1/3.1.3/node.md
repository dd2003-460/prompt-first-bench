# N70: 下游投影 2（成交周期变化）：干预后成交周期 T_close_new = T_close_old * (1 - η_speed)，其中 η_speed = 0.

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

下游投影 2（成交周期变化）：干预后成交周期 T_close_new = T_close_old * (1 - η_speed)，其中 η_speed = 0.10-0.15 为速度提升系数，取决于 P(ReadLabel) 与买家决策摩擦降低幅度；若 P(ReadLabel) 低于阈值 0.4，则 η_speed 降至 0.05 以下，周期缩短效果不显著。

## Corrected Claim

下游投影 2（成交周期变化）：干预后成交周期 T_close_new = T_close_old * (1 - η_speed)，其中 η_speed = 0.10-0.15 为速度提升系数，取决于 P(ReadLabel) 与买家决策摩擦降低幅度；若 P(ReadLabel) 低于阈值 0.4，则 η_speed 降至 0.05 以下，周期缩短效果不显著。

## Evidence

父节点级核验未通过：非正交（子节点1（共享随机源）与子节点2（η_speed分解）存在逻辑重叠和层级混乱。子节点1试图解释ΔFriction的随机性来源，但ΔFriction本身只是子节点2中η_speed的一个组成变量。将‘变量的随机性来源’单独列为与‘变量公式分解’并列的子节点，破坏了正交性（一个是统计属性，一个是代数结构）。此外，子节点2已经定义了ΔFriction的公式，子节点1重复了该公式的定义部分，导致内容冗余。）
