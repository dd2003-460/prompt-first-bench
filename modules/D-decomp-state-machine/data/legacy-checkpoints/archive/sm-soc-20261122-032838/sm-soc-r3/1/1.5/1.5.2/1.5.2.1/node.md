# N151: 买家心理阈值 P_threshold 的分布而非单点值：P_threshold 并非固定为 0.9 P_ref，而是服从分布 P_threshold ~ N(μ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N49

## Claim

买家心理阈值 P_threshold 的分布而非单点值：P_threshold 并非固定为 0.9 P_ref，而是服从分布 P_threshold ~ N(μ_th, σ_th^2)。实证研究表明，二手商品买家的‘绝对不买’阈值（即认为价格离谱的上限）通常位于 P_ref 的 1.1-1.3 倍之间，而非 0.9 倍。若 μ_th = 1.2 P_ref 且 σ_th = 0.1 P_ref，则 P_low ∈ [1.02, 1.14] P_ref 时，P_low < P_threshold 的概率（即有咨询概率）为 Φ((P_low - μ_th)/σ_th)。计算得 P(有咨询) ≈ 0.8-0.9，这与‘60%无咨询’（即40%有咨询）矛盾，说明 P_threshold ≈ 0.9 P_ref 的假设过于激进，需重新校准 μ_th。

## Corrected Claim

买家心理阈值 P_threshold 的分布而非单点值：P_threshold 并非固定为 0.9 P_ref，而是服从分布 P_threshold ~ N(μ_th, σ_th^2)。若假设 μ_th = 1.2 P_ref 且 σ_th = 0.1 P_ref，则 P_low ∈ [1.02, 1.14] P_ref 时，P_low < P_threshold 的概率为 Φ((P_low - μ_th)/σ_th)。计算表明该概率显著高于 40%，说明 P_threshold ≈ 0.9 P_ref 的假设可能过于激进，需重新校准 μ_th。

## Evidence

[质询]陈述中引用的具体实证数据（阈值位于1.1-1.3倍、概率计算结果0.8-0.9）缺乏来源支持，且‘60%无咨询’这一前提本身未在当前节点中给出依据，属于经验事实断言。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体实证数值）

## Search Query

buyer willingness to pay threshold second hand goods price distribution empirical study
