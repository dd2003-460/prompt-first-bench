# N103: E_high 的基准参照系 P_ref 必须明确为'近7天同类商品加权成交均价'，权重 w_i 按成交量或时间衰减 λ_t 计算，公式为 P_ref = Σ(P

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

E_high 的基准参照系 P_ref 必须明确为'近7天同类商品加权成交均价'，权重 w_i 按成交量或时间衰减 λ_t 计算，公式为 P_ref = Σ(P_i * w_i) / Σ(w_i)，其中 w_i = exp(-λ_t * (t_now - t_i))，λ_t 取值为 0.1/day。

## Corrected Claim

E_high 的基准参照系 P_ref 必须明确为'近7天同类商品加权成交均价'，权重 w_i 按成交量或时间衰减 λ_t 计算，公式为 P_ref = Σ(P_i * w_i) / Σ(w_i)，其中 w_i = exp(-λ_t * (t_now - t_i))，λ_t 取值为 0.1/day。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上正交（分别处理样本定义、参数敏感性、权重组合、数据清洗），无重复或矛盾。但完备性不足：父节点明确给出了具体的指数时间衰减公式 w_i = exp(-λ_t * (t_now - t_i))，而子节点3引入了'成交量权重 w_vol'并讨论'乘法组合'，这与父节点定义的单一时间衰减权重公式存在逻辑冲突（父节点未提及成交量权重，子节点3擅自扩展了权重结构，导致与父节点定义不一致）。此外，父节点中'成交量或时间衰减'是二选一或可选条件，子节点3直接假设了乘法组合，未覆盖'仅成交量'或'仅时间'的情况，且与父节点公式不符。）

## Search Query

weighted average price time decay lambda 0.1 per day
