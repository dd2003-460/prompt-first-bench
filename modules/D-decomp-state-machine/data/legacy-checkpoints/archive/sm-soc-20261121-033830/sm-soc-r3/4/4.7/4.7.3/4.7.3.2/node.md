# N285: 交叉验证（k-Fold CV）的偏差-方差权衡工作点：选择 k=5 作为标准工作点以平衡计算成本与泛化误差估计精度；若 k=10 与 k=5 的误差估计差异 >

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

交叉验证（k-Fold CV）的偏差-方差权衡工作点：选择 k=5 作为标准工作点以平衡计算成本与泛化误差估计精度；若 k=10 与 k=5 的误差估计差异 > 5%，则表明模型存在高方差，需增加数据量或正则化，而非简单增加 k 值。

## Corrected Claim

交叉验证（k-Fold CV）的偏差-方差权衡工作点：选择 k=5 作为标准工作点以平衡计算成本与泛化误差估计精度；若 k=10 与 k=5 的误差估计差异 > 5%，则表明模型存在高方差，需增加数据量或正则化，而非简单增加 k 值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

k-fold cross validation bias variance tradeoff optimal k
