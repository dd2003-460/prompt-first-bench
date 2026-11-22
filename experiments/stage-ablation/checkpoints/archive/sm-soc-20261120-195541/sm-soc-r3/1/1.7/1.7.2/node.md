# N41: 单商品提示成本 γ 并非仅包含静态展示成本，还应包含动态数据维护成本，总成本公式为 γ = γ_display + γ_data_update * f_upda

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11, N12, N13

## Claim

单商品提示成本 γ 并非仅包含静态展示成本，还应包含动态数据维护成本，总成本公式为 γ = γ_display + γ_data_update * f_update_freq，其中 f_update_freq 为基准价 P_market_avg 的更新频率，若更新频率过高，γ 将显著超过 $0.01 的初始假设。

## Corrected Claim

单商品提示成本 γ 并非仅包含静态展示成本，还应包含动态数据维护成本，总成本公式为 γ = γ_display + γ_data_update * f_update_freq，其中 f_update_freq 为基准价 P_market_avg 的更新频率，若更新频率过高，γ 将显著超过 $0.01 的初始假设。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2和3存在逻辑重叠和冗余。子节点2通过具体数值示例（f=1）计算总成本，而子节点3通过边界条件（f>2, f=4）计算总成本。两者本质上都是在演示公式 γ = γ_display + γ_data_update * f 在不同频率下的结果，属于同一逻辑维度的不同实例，而非正交的独立概念。此外，子节点2中混合了参数定义（γ_data_update的计算）和特定场景下的总成本验证，导致与子节点3的职责边界模糊。）
