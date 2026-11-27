# N32: 卖家定价噪声方差分解：$\text{Var}(\epsilon_{seller}) = \sigma^2_{\text{bias}} + \sigma^2_{\

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

卖家定价噪声方差分解：$\text{Var}(\epsilon_{seller}) = \sigma^2_{\text{bias}} + \sigma^2_{\text{info}}$，其中 $\sigma^2_{\text{bias}}$ 源于损失厌恶导致的系统性高估偏差，$\sigma^2_{\text{info}}$ 源于对同类商品近期成交数据样本量不足导致的估计误差，二者需独立量化以区分行为偏差与信息缺失。

## Corrected Claim

卖家定价噪声方差分解：$\text{Var}(\epsilon_{seller}) = \sigma^2_{\text{bias}} + \sigma^2_{\text{info}}$，其中 $\sigma^2_{\text{bias}}$ 源于损失厌恶导致的系统性高估偏差，$\sigma^2_{\text{info}}$ 源于对同类商品近期成交数据样本量不足导致的估计误差，二者需独立量化以区分行为偏差与信息缺失。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点严格对应父节点分解的三个核心要素：结构定义（正交性）、第一项方差量化、第二项方差量化。各节点内容互不重叠且无矛盾，共同完整覆盖了父节点的所有关键方面，不存在冗余。）

## Search Query

decomposition of seller pricing noise variance into bias and information error
