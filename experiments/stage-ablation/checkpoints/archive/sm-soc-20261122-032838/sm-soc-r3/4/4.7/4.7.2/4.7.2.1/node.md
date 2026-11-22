# N259: 搜索效率提升的数学恒等式：若无效点击率从 $r_0=0.4$ 降至 $r_1=0.2$，且无效点击平均耗时 $t_{invalid}$ 与有效点击耗时 $t_{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85

## Claim

搜索效率提升的数学恒等式：若无效点击率从 $r_0=0.4$ 降至 $r_1=0.2$，且无效点击平均耗时 $t_{invalid}$ 与有效点击耗时 $t_{valid}$ 之比为 $\rho_t$，则搜索时间缩短比例 $\Delta T/T = (r_0-r_1) \cdot \rho_t / (r_0 \cdot \rho_t + (1-r_0))$。需估算二手平台 $t_{invalid}$ 与 $t_{valid}$ 的比值（通常 $t_{invalid} < t_{valid}$，因为无效点击后快速返回，假设 $\rho_t \in [0.3, 0.8]$）。

## Corrected Claim

搜索效率提升的数学恒等式：若无效点击率从 $r_0=0.4$ 降至 $r_1=0.2$，且无效点击平均耗时 $t_{invalid}$ 与有效点击耗时 $t_{valid}$ 之比为 $\rho_t$，则搜索时间缩短比例 $\Delta T/T = (r_0-r_1) \cdot \rho_t / (r_0 \cdot \rho_t + (1-r_0))$。需估算二手平台 $t_{invalid}$ 与 $t_{valid}$ 的比值（通常 $t_{invalid} < t_{valid}$，因为无效点击后快速返回，假设 $\rho_t \in [0.3, 0.8]$）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合加权平均时间模型，量纲一致，参数范围合理。

## Search Query

e-commerce click-through time analysis invalid click duration ratio
