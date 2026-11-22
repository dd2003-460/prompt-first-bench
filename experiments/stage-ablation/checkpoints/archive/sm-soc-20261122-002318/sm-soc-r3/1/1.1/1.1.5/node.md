# N38: 偏好噪声标准差 σ_noise 的分解公式：σ_noise = σ_info * (1 + γ_urgency)，其中 σ_info 为信息不对称导致的基础方差

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

偏好噪声标准差 σ_noise 的分解公式：σ_noise = σ_info * (1 + γ_urgency)，其中 σ_info 为信息不对称导致的基础方差，γ_urgency 为买家紧迫程度（如FOMO）对方差放大的系数。

## Corrected Claim

在特定的行为经济学模型中，偏好噪声标准差可被建模为 σ_noise = σ_info * (1 + γ_urgency)，其中 σ_info 为基础方差，γ_urgency 为紧迫程度放大系数。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的随机源定义、基础参数 σ_info 的量化估算、以及放大系数 γ_urgency 的量化定义，三者逻辑独立且互不重叠（正交）；共同覆盖了公式中所有变量的物理意义和计算/估算方法（完备）；没有发现多个子节点描述同一参数的不同取值情况（无冗余）。）

## Search Query

preference noise decomposition information asymmetry urgency coefficient

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/711471381&rut=8fcd5e57d1bfe3738c0572c34eb8ebd665003c6196f700fc3d3b0d4f89becbb7', 'type': 'ddg', 'title': '高等模拟设计——噪声 Noise - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/19339408743&rut=20197b2bed8b3d8255e077be7031cbd2ee843033520558712b019f0cd3929fc6', 'type': 'ddg', 'title': '什么是 Sigma-Delta ADC 中的 Noise Shaping？ - 知乎'}
