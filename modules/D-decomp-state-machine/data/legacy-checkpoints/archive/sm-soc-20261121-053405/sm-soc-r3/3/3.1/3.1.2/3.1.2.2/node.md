# N150: 分子项 $E[R]_{old} - E[R]_{target}$ 的量化：$E[R]_{old} = \sum_{t} \frac{Commission \cd

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

分子项 $E[R]_{old} - E[R]_{target}$ 的量化：$E[R]_{old} = \sum_{t} \frac{Commission \cdot GMV_t}{(1+r)^t}$，$E[R]_{target}$ 为干预后目标收益；若目标为将成交周期 $T_{cycle}$ 缩短 $\Delta T$，则 $E[R]_{target} - E[R]_{old} \approx \frac{\partial E[R]}{\partial T_{cycle}} \cdot \Delta T$，其中 $\partial E[R] / \partial T_{cycle}$ 可通过历史数据回归估计。

## Corrected Claim

分子项 $E[R]_{old} - E[R]_{target}$ 的量化：$E[R]_{old} = \sum_{t} \frac{Commission \cdot GMV_t}{(1+r)^t}$，$E[R]_{target}$ 为干预后目标收益；若目标为将成交周期 $T_{cycle}$ 缩短 $\Delta T$，则 $E[R]_{target} - E[R]_{old} \approx \frac{\partial E[R]}{\partial T_{cycle}} \cdot \Delta T$，其中 $\partial E[R] / \partial T_{cycle}$ 可通过历史数据回归估计。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义符合金融估值逻辑，一阶泰勒展开近似在微扰条件下成立，偏导数通过回归估计是标准统计方法。
