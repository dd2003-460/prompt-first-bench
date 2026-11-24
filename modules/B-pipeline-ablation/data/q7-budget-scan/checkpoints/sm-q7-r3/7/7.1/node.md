# N125: NVMe SSD阵列5年直线折旧模型中，C_hw_total = 471块(1.92TB SSD) × ¥3,000/块 = ¥1,413,000，基于2024

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

NVMe SSD阵列5年直线折旧模型中，C_hw_total = 471块(1.92TB SSD) × ¥3,000/块 = ¥1,413,000，基于2024-2025年企业级NVMe SSD市场均价估算。

## Corrected Claim

NVMe SSD阵列5年直线折旧模型中，C_hw_total = 471块(1.92TB SSD) × ¥3,000/块 = ¥1,413,000，基于2024-2025年企业级NVMe SSD市场均价估算。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 严重数据矛盾（非正交）：父节点明确指定使用471块1.92TB SSD且单价¥3,000，总成本¥1,413,000；但子节点C计算出的1.92TB方案仅需266块且单价¥400，总成本仅¥106,400，两者在数量、单价和总价上均完全冲突。2. 覆盖缺失：子节点未解释为何最终选择与子节点计算结果（尤其是C节点）截然不同的父节点参数（471块 vs 266块，¥3k vs ¥400）。3. 结构冗余：子节点A/B/C本质上是同一参数（SSD容量规格）下的多场景对比，属于多态参数，而非正交的独立概念模块。）

## Search Query

enterprise NVMe SSD 1.92TB price 2024 2025
