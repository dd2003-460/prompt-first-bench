# N328: 定义买家咨询概率 $Q_{inquiry}$ 与价格信号 $P$ 及降价幅度 $\Delta P$ 的函数关系：$Q_{inquiry} = Q_0 \cdot

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N114

## Claim

定义买家咨询概率 $Q_{inquiry}$ 与价格信号 $P$ 及降价幅度 $\Delta P$ 的函数关系：$Q_{inquiry} = Q_0 \cdot e^{-\beta \frac{\Delta P}{P_{base}}} \cdot (1 - \alpha_{noise})$，其中 $\beta$ 为价格敏感度系数，$\alpha_{noise}$ 为随机噪声项，需通过历史数据回归确定 $\beta$ 的值。

## Corrected Claim

定义买家咨询概率 $Q_{inquiry}$ 与价格信号 $P$ 及降价幅度 $\Delta P$ 的函数关系：$Q_{inquiry} = Q_0 \cdot e^{-\beta \frac{\Delta P}{P_{base}}} \cdot (1 - \alpha_{noise})$，其中 $\beta$ 为价格敏感度系数，$\alpha_{noise}$ 为随机噪声项，需通过历史数据回归确定 $\beta$ 的值。

## Search Query

second hand market inquiry rate price elasticity regression beta coefficient
