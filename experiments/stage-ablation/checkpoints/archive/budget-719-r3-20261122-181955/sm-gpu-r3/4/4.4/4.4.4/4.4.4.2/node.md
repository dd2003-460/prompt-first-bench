# N339: TCO_5yr 计算函数为 $TCO_5 = C_{hw} + \sum_{y=1}^{5} (P_{avg} \cdot H_{run} \cdot E_{e

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N111

## Claim

TCO_5yr 计算函数为 $TCO_5 = C_{hw} + \sum_{y=1}^{5} (P_{avg} \cdot H_{run} \cdot E_{elec} \cdot (1 + I_{inflation})^y)$，其中 $C_{hw}$ 为硬件一次性成本（含机箱/电源/散热，参考 N105-N107 数值），$H_{run}=8760$，$I_{inflation}=0.03$ (假设年电价通胀率 3%)。

## Corrected Claim

TCO_5yr 计算函数为 $TCO_5 = C_{hw} + \sum_{y=1}^{5} (P_{avg} \cdot H_{run} \cdot E_{elec} \cdot (1 + I_{inflation})^y)$，其中 $C_{hw}$ 为硬件一次性成本（含机箱/电源/散热，参考 N105-N107 数值），$H_{run}=8760$，$I_{inflation}=0.03$ (假设年电价通胀率 3%)。

## Evidence

先验知识/题面给定，逻辑校验通过：TCO公式结构符合标准全生命周期成本计算逻辑（硬件一次性成本+5年运营电费累加），H_run=8760小时/年符合全年无休运行假设，通胀因子(1+I)^y应用正确，量纲与数值量级合理。
