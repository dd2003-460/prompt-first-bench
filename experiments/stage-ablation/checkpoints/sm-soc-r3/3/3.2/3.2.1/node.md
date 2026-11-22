# N58: 卖家实际成本 C_cost 的分解：C_cost = C_acquisition + C_holding + C_disposition，其中 C_acquis

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

卖家实际成本 C_cost 的分解：C_cost = C_acquisition + C_holding + C_disposition，其中 C_acquisition 为获取成本（对二手卖家通常为 0 或历史折旧值），C_holding 为持有成本（资金占用利息 + 仓储/心理占用），C_disposition 为处置成本（时间精力、物流）。

## Corrected Claim

卖家实际成本 C_cost 的分解：C_cost = C_acquisition + C_holding + C_disposition，其中 C_acquisition 为获取成本（对二手卖家通常为 0 或历史折旧值），C_holding 为持有成本（资金占用利息 + 仓储/心理占用），C_disposition 为处置成本（时间精力、物流）。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点公式中的三个独立变量（获取、持有、处置），概念上互不重叠（正交），且完整覆盖了公式的所有组成部分（完备）。每个子节点针对特定的‘工作点’（如个人卖家、高流动性、高时间投入）进行了具体的量化和逻辑推导，虽然都服务于定价底线分析，但各自聚焦的成本驱动因素不同（沉没成本vs持有焦虑vs硬性处置支出），不存在简单的参数取值冗余，而是不同维度的成本量化。）

## Search Query

seller opportunity cost decomposition holding cost secondary market
