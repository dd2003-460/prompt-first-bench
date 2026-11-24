# N90: 公有云CDN下行流量单价 a_cloud 的典型区间为 0.2-0.5 元/GB（国内主流厂商标准价），且通常随月累计用量阶梯递减，导致有效指数 b_cloud

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点分别定义了基础资费标准（基准）、阶梯递减机制（规律）以及特定场景下的应用计算（实例），三者逻辑层级清晰，互不重叠且无矛盾。虽然子节点2和3都涉及具体数值，但前者描述的是通用规则，后者是基于该规则的具体推导，不属于冗余。）

## Search Query

Alibaba Cloud CDN pricing per GB 2024 tiered discount
