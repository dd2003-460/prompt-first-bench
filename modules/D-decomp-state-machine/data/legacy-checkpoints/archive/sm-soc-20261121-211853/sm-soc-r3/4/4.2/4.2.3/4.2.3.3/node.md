# N95: 议价空间减少量 $\Delta S$ 的解析解：代入贝叶斯公式，$\Delta S = \frac{\sigma_{noise}^2}{\sigma_p^2 +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

议价空间减少量 $\Delta S$ 的解析解：代入贝叶斯公式，$\Delta S = \frac{\sigma_{noise}^2}{\sigma_p^2 + \sigma_{noise}^2} (P_{ask} - \mu_{market})$，表明 $\Delta S$ 仅取决于挂价偏离度 $(P_{ask} - \mu_{market})$ 和信号信噪比，与卖家主观保留价无关。

## Corrected Claim

议价空间减少量 $\Delta S$ 的解析解：代入贝叶斯公式，$\Delta S = \frac{\sigma_{noise}^2}{\sigma_p^2 + \sigma_{noise}^2} (P_{ask} - \mu_{market})$，表明 $\Delta S$ 仅取决于挂价偏离度 $(P_{ask} - \mu_{market})$ 和信号信噪比，与卖家主观保留价无关。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合贝叶斯更新下后验均值对先验均值的偏离量与信噪比（精度比）成正比的线性性质，且量纲一致（价格单位），逻辑自洽。

## Search Query

analytical solution Bayesian posterior mean price deviation
