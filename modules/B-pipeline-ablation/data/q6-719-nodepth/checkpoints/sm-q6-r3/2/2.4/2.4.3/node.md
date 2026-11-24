# N70: 自建单元价格 (Self_Built_Unit_Price) = (Self_Built_Monthly_Cost / Core_Requests)，其中 Se

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15, N16, N17

## Claim

自建单元价格 (Self_Built_Unit_Price) = (Self_Built_Monthly_Cost / Core_Requests)，其中 Self_Built_Monthly_Cost 包含 5 个核心 POP 的折旧、带宽及运维分摊，需从 N12/N13/N26 推导单 POP 月度成本后乘以 5 再除以核心区域请求数。

## Corrected Claim

自建单元价格 (Self_Built_Unit_Price) = (Self_Built_Monthly_Cost / Core_Requests)，其中 Self_Built_Monthly_Cost 包含 5 个核心 POP 的折旧、带宽及运维分摊，需从 N12/N13/N26 推导单 POP 月度成本后乘以 5 再除以核心区域请求数。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上正交且无冗余，分别对应分母（请求数）和分子中的三个成本维度（折旧、带宽、运维）。但存在完备性问题：父节点公式定义为 Self_Built_Monthly_Cost / Core_Requests，其中 Self_Built_Monthly_Cost 应包含 5 个 POP 的总成本。目前的子节点仅提供了‘单 POP’的成本组件和‘核心区域’的请求数，缺少一个明确的‘汇总/聚合’步骤或子节点来将单 POP 成本乘以 5 并求和，导致从子节点到父节点的计算链路在结构上是不完整的（缺少 *5 和 Sum 的操作节点）。）

## Search Query

edge node cost per request self-built vs cloud cdn unit economics
