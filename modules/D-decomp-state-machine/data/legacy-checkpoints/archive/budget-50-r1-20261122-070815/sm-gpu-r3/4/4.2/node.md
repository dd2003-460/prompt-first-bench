# N24: 电力消耗成本 (C_power) = P_avg (W) × H_hours (年运行小时数) × E_price ($/kWh) / 1000，其中 P_av

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

电力消耗成本 (C_power) = P_avg (W) × H_hours (年运行小时数) × E_price ($/kWh) / 1000，其中 P_avg 为整机平均功耗（含GPU、CPU、内存、风扇、PSU损耗），E_price 为当地电价。

## Corrected Claim

电力消耗成本 (C_power) = P_avg (W) × H_hours (年运行小时数) × E_price ($/kWh) / 1000，其中 P_avg 为整机平均功耗（含GPU、CPU、内存、风扇、PSU损耗），E_price 为当地电价。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点存在严重的冗余和结构混淆。前四个子节点（RTX 4090, A100, H100, Mac Studio）本质上都是参数 P_avg 的具体取值实例，而非独立的正交维度。在学术分解中，同一变量的多个实例不应作为并列的子节点，而应归类于该变量之下。此外，第7个子节点混合了公式计算结果和定性分析，与前6个纯参数定义的结构不一致。）
