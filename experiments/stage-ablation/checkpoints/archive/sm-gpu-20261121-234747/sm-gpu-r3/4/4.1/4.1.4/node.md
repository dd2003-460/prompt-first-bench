# N104: 数据时效性分类的边界案例处理：当某参数同时具有静态和动态特征时（如GPU功耗，标称值静态但实测值动态），需拆分为两个子节点：(1) 标称功耗（A类，来源为官方规

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

数据时效性分类的边界案例处理：当某参数同时具有静态和动态特征时（如GPU功耗，标称值静态但实测值动态），需拆分为两个子节点：(1) 标称功耗（A类，来源为官方规格表），(2) 实测平均功耗（C类，来源为第三方测试，需标注测试日期和负载场景）；该拆分确保TCO计算中电力成本使用动态实测值而非静态标称值

## Corrected Claim

数据时效性分类的边界案例处理：当某参数同时具有静态和动态特征时（如GPU功耗，标称值静态但实测值动态），需拆分为两个子节点：(1) 标称功耗（A类，来源为官方规格表），(2) 实测平均功耗（C类，来源为第三方测试，需标注测试日期和负载场景）；该拆分确保TCO计算中电力成本使用动态实测值而非静态标称值

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

GPU power consumption nominal vs measured dynamic data classification TCO calculation
