# N8: 大小与热度的负相关结构：采用双变量帕累托或高斯-帕累托混合模型，相关系数 $\rho=-0.3$ 意味着大对象倾向于低热度，需量化联合分布 $P(S_i, R_

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

大小与热度的负相关结构：采用双变量帕累托或高斯-帕累托混合模型，相关系数 $\rho=-0.3$ 意味着大对象倾向于低热度，需量化联合分布 $P(S_i, R_i)$ 或至少确定条件期望 $E[S | R]$ 的函数形式以用于缓存容量分配。

## Corrected Claim

大小与热度通常呈现负相关结构（大对象倾向于低热度）。在建模时，可采用双变量帕累托或高斯-帕累托混合模型等统计方法，需根据具体数据集量化联合分布 P(S_i, R_i) 或确定条件期望 E[S | R] 的函数形式（例如通过拟合得到相关系数 ρ），以用于缓存容量分配。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 775)

## Search Query

bivariate Pareto distribution correlation coefficient modeling cache workload
