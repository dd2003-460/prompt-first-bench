# N33: 信息不对称度 I_asym 的量化指标：定义为买家无法观测到的商品真实质量分布的标准差 σ_quality_hidden。I_asym = σ_quality_

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N6

## Claim

信息不对称度 I_asym 的量化指标：定义为买家无法观测到的商品真实质量分布的标准差 σ_quality_hidden。I_asym = σ_quality_hidden / σ_quality_total。当 I_asym > 0.5 时，噪声主导决策；当 I_asym < 0.2 时，信号主导决策。需结合平台数据估算该值。

## Corrected Claim

信息不对称度 I_asym 可定义为买家无法观测到的商品真实质量分布的标准差与总质量分布标准差之比（I_asym = σ_quality_hidden / σ_quality_total）。该指标用于衡量信息不对称程度，具体阈值（如噪声主导或信号主导的界限）需根据特定平台数据或模型设定进行校准，而非通用固定值。

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性冲突：子节点1定义了观测噪声 σ_obs 为 0.1*μ_price，而子节点2将 σ_obs 分解为各分量并计算出 0.0616*μ_price，两者数值矛盾，导致 I_asym 的计算基础不一致。2. 完备性缺失：父节点核心是 I_asym = σ_hidden / σ_total，但子节点未明确给出 σ_hidden 的独立定义或计算方法（子节点1定义了总方差，子节点2定义了观测噪声，但缺少从总方差和观测噪声推导隐藏方差的逻辑链接，如 σ_hidden² = σ_total² - σ_obs² 或类似贝叶斯更新公式），导致无法直接计算 I_asym。）

## Search Query

information asymmetry quantification standard deviation hidden quality second hand market

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Principal%E2%80%93agent_problem', 'type': 'wikipedia', 'title': 'Principal–agent problem'}
- {'url': 'https://en.wikipedia.org/wiki/Neural_network_%28machine_learning%29', 'type': 'wikipedia', 'title': 'Neural network (machine learning)'}
- {'url': 'https://en.wikipedia.org/wiki/Behavioral_economics', 'type': 'wikipedia', 'title': 'Behavioral economics'}
