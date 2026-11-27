# N186: 计算平台对均衡维持的边际贡献度 $C_p = \frac{\partial U_p}{\partial E_{equilibrium}} / \sum_{i} 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

计算平台对均衡维持的边际贡献度 $C_p = \frac{\partial U_p}{\partial E_{equilibrium}} / \sum_{i} \frac{\partial U_i}{\partial E_{equilibrium}}$。平台效用 $U_p$ 取决于 GMV 和留存率。根据 N76，若 $\eta_Q < 1$，高溢价 $E$ 提升 GMV，则 $\frac{\partial U_p}{\partial E} > 0$。需量化平台算法权重 $W_{algo}$ 中 GMV 的占比 $w_{gmv}$，若 $w_{gmv} > 0.5$，则平台有正向激励维持高 $E$，$C_p$ 为正且显著。

## Corrected Claim

计算平台对均衡维持的边际贡献度 $C_p = \frac{\partial U_p}{\partial E_{equilibrium}} / \sum_{i} \frac{\partial U_i}{\partial E_{equilibrium}}$。平台效用 $U_p$ 取决于 GMV 和留存率。根据 N76，若 $\eta_Q < 1$，高溢价 $E$ 提升 GMV，则 $\frac{\partial U_p}{\partial E} > 0$。需量化平台算法权重 $W_{algo}$ 中 GMV 的占比 $w_{gmv}$，若 $w_{gmv} > 0.5$，则平台有正向激励维持高 $E$，$C_p$ 为正且显著。

## Evidence

先验知识/题面给定，逻辑校验通过
