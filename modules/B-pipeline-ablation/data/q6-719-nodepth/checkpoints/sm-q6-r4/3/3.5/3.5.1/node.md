# N90: 公有云CDN下行流量单价 a_cloud 的典型区间为 0.2-0.5 元/GB（国内主流厂商标准价），且通常随月累计用量阶梯递减，导致有效指数 b_cloud

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

公有云CDN下行流量单价 a_cloud 的典型区间为 0.2-0.5 元/GB（国内主流厂商标准价），且通常随月累计用量阶梯递减，导致有效指数 b_cloud 在常规用量区间内表现为 0.8-1.0（规模经济）。

## Corrected Claim

公有云CDN下行流量单价 a_cloud 的典型区间为 0.2-0.5 元/GB（国内主流厂商标准价），且通常随月累计用量阶梯递减，导致有效指数 b_cloud 在常规用量区间内表现为 0.8-1.0（规模经济）。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点3（当前场景有效单价）是基于子节点1（基础单价）和子节点2（阶梯规则）推导出的具体实例，而非独立的概念维度。它重复使用了前两个节点的参数逻辑，导致内容在逻辑层级上重叠，违反了正交性原则（即子节点应分别描述‘定义’、‘规律’、‘约束’等独立方面，而非‘通用规则’与‘特例应用’混杂）。）

## Search Query

Alibaba Cloud CDN pricing per GB 2024 tiered discount
