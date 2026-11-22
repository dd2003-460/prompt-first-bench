# N149: 原始购买价记忆偏差 ΔP_ref：ΔP_ref = P_ref - C_cost，其中 C_cost 为当前重置成本，ΔP_ref 通常包含购买时的通货膨胀调整

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

原始购买价记忆偏差 ΔP_ref：ΔP_ref = P_ref - C_cost，其中 C_cost 为当前重置成本，ΔP_ref 通常包含购买时的通货膨胀调整项及心理溢价，需量化其标准差 σ_ΔP 以评估对 P_reserve 的边际贡献。

## Corrected Claim

在特定的资产估值或行为经济学模型中，原始购买价记忆偏差 ΔP_ref 可定义为 P_ref - C_cost，其中包含通胀调整及心理溢价，其标准差 σ_ΔP 用于评估对 P_reserve 的影响。

## Evidence

[质询]该陈述属于特定经济/心理模型中的经验性定义，无法从第一性原理严格推导；且参考来源仅讨论通用预测误差指标（MFE, RMSE等），未涉及具体的购买价记忆偏差公式或心理溢价量化，存在来源不相关且缺乏直接支持的风险。 | 逻辑自洽（定义清晰，量纲合理），但参考来源[1]与具体事实主题无关，且该事实为经验性模型参数，缺乏直接来源支持，依据经验事实排除条款降级。

## Search Query

mental accounting original purchase price bias standard deviation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1995453293648970673&rut=1aae8b411b5aec95953baf16ab01ddb6b2505b5839acc2c64a9c6a18bbb7dd99', 'type': 'ddg', 'title': '6. 预测误差与预测偏差的核心解析 - 知乎'}
