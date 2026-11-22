# N127: 降价决策噪声 ε_seller 的来源分解：将 ε_seller 分解为信息不对称噪声 ε_info 和情绪波动噪声 ε_emotion，即 ε_seller 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N34

## Claim

降价决策噪声 ε_seller 的来源分解：将 ε_seller 分解为信息不对称噪声 ε_info 和情绪波动噪声 ε_emotion，即 ε_seller = ε_info + ε_emotion，分别估计其方差贡献率

## Corrected Claim

在特定模型假设下，可将降价决策噪声 ε_seller 分解为信息不对称噪声 ε_info 和情绪波动噪声 ε_emotion，即 ε_seller = ε_info + ε_emotion，并分别估计其方差贡献率。

## Evidence

[质询]该分解属于特定的建模假设，并非博弈论或经济学中的通用定理。参考来源仅讨论了非对称信息的一般性后果，并未提及将噪声分解为信息不对称和情绪波动两个具体分量，也未涉及方差贡献率的估计方法。 | 逻辑上，将总噪声分解为不同来源的分量是合理的建模手段，且各分量方差之和等于总方差在数学上自洽。但参考来源[1]仅涉及非对称信息的一般理论，未直接支持该特定分解模型或方差估计方法，属于间接相关或无关，故降级。

## Search Query

seller pricing noise information asymmetry emotional fluctuation variance decomposition

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1909629305962607541&rut=c2998433d70d5bb19218d4187c64a96a4f14873379bca35d31bee442f5e9d680', 'type': 'ddg', 'title': '博弈论-高微Ⅱ：6.专题-Asymmetric information(1)-Optimal Auction Design'}
