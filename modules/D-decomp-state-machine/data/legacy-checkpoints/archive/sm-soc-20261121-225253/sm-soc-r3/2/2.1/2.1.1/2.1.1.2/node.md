# N69: 买家从 $P_{recent}$ 回退至锚定 $P_{ask}$ 的决策阈值模型：定义锚定切换概率 $P_{anchor} = \Phi(\frac{H_{CI

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

买家从 $P_{recent}$ 回退至锚定 $P_{ask}$ 的决策阈值模型：定义锚定切换概率 $P_{anchor} = \Phi(\frac{H_{CI} - \Delta P_{diff}}{\sigma_{belief}})$，其中 $\Delta P_{diff} = |P_{ask} - P_{recent}|$，$\sigma_{belief}$ 为买家对价格信号的感知噪声方差；需确定当 $P_{anchor} > 0.5$ 时，$\Delta P_{diff}$ 与 $H_{CI}$ 的具体临界比值。

## Corrected Claim

买家从 $P_{recent}$ 回退至锚定 $P_{ask}$ 的决策阈值模型可定义为：锚定切换概率 $P_{anchor} = \Phi(\frac{H_{CI} - \Delta P_{diff}}{\sigma_{belief}})$，其中 $\Delta P_{diff} = |P_{ask} - P_{recent}|$，$\sigma_{belief}$ 为买家对价格信号的感知噪声标准差（注：原陈述称方差，但公式中作为分母通常对应标准差，此处保留原意但指出量纲需一致）。该模型的具体临界比值需根据特定市场数据或实验校准确定，现有通用资料未提供标准临界值。

## Evidence

[质询]该陈述定义了一个具体的数学模型（基于正态分布累积函数 Φ 的锚定切换概率），并声称需要确定特定临界比值。然而，参考来源 [1] 仅讨论金融交易中的“回调（Pullback）”概念，完全未涉及买家决策阈值、锚定效应（Anchoring）、感知噪声方差（σ_belief）或任何概率模型公式。来源与事实主题严重不匹配，无法提供外部支持。此外，该模型属于特定的理论构建或假设，并非通用的第一性原理或公认的经济定律，因此不能仅凭逻辑自洽判定为 verified。 | 参考来源 [1] 主题为金融回调，与买家决策阈值模型无关，无可用外部证据；该模型为特定理论假设，逻辑上自洽（量纲一致，Φ 函数定义合理），但缺乏来源支持，且属于经验/理论模型范畴，非第一性原理可推导事实。

## Search Query

price anchoring fallback mechanism buyer decision threshold confidence interval width behavioral economics

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1974005045105271968&rut=fa59f59df6bd162cc3ce7c9c72b7ee7447c39f4e771040eccb6a7dd62fa198a5', 'type': 'ddg', 'title': '交易大百科 (P字系列)——回调（Pullback） - 知乎'}
