# N100: ‘$\Delta W > 5\%$ 即可改变市场均衡’的阈值验证：需计算均衡状态变量 $S$（定义为高溢价商品占比 $\rho_{high}$）对算法权重 $W

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N31

## Claim

‘$\Delta W > 5\%$ 即可改变市场均衡’的阈值验证：需计算均衡状态变量 $S$（定义为高溢价商品占比 $\rho_{high}$）对算法权重 $W$ 的弹性 $\epsilon_S = \frac{d \ln \rho_{high}}{d \ln W}$。若 $\epsilon_S > 1$，则 $\Delta W = 5\%$ 足以导致 $\rho_{high}$ 变化 $>5\%$。此弹性取决于卖家对算法信号的敏感度 $\sigma_s$ 和买家对价格变化的反应系数 $\beta_b$。公式：$\epsilon_S = \sigma_s \cdot \beta_b \cdot \frac{\partial W}{\partial P_{ask}}$。[待核验] 若缺乏平台内部日志，该数值为 [待核验]，需通过 A/B 测试（调整排序权重观察成交分布变化）来估计。

## Corrected Claim

‘ΔW > 5% 即可改变市场均衡’的阈值及弹性公式 ε_S = σ_s · β_b · (∂W/∂P_ask) 为待验证假设，需通过 A/B 测试估计，当前缺乏实证数据支持其具体数值。

## Evidence

[质询]该陈述包含具体的经验性阈值（5%）和特定的弹性公式结构，属于平台内部机制的经验事实，无法仅从第一性原理推导得出，且缺乏外部数据支持其具体数值和公式形式的准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

market equilibrium sensitivity to algorithmic ranking weights second hand goods price elasticity
