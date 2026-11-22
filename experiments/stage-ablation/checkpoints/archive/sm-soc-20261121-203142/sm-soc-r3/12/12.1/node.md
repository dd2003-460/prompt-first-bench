# N301: 量化‘高挂价卖家’的定义阈值：确定 P_ask > P_market * (1 + δ_threshold) 中的 δ_threshold 具体数值（如 15%

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102

## Claim

量化‘高挂价卖家’的定义阈值：确定 P_ask > P_market * (1 + δ_threshold) 中的 δ_threshold 具体数值（如 15% 或 20%），因为受损方范围直接取决于此阈值，不同阈值下受影响的卖家比例 n_affected 将呈现非线性变化。

## Corrected Claim

量化‘高挂价卖家’的定义阈值 δ_threshold 需根据具体市场环境和策略目标确定，不同阈值下受影响的卖家比例 n_affected 将呈现非线性变化，但具体数值（如 15% 或 20%）缺乏通用标准，需通过实证分析确定。

## Evidence

[质询]该陈述声称确定具体的 δ_threshold 数值（如 15% 或 20%），但参考来源中并未提供针对‘高挂价卖家’这一特定定义阈值的实证数据或行业标准，仅涉及通用的量化交易信号方法或条件单设置示例，无法支持具体数值的确定性。 | 来源 [1] 和 [2] 仅讨论了量化交易中的阈值法和挂单卖出的一般逻辑，未提供关于‘高挂价卖家’定义阈值 δ_threshold 的具体数值或非线性变化关系的直接证据，属于经验事实且缺乏来源支持。

## Search Query

threshold for high pricing sellers in second-hand platform intervention A/B test

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1981667440967574395&rut=a1d768ea59c65d571bc710b44ea619c8450189dad1d4dd195bfdf15bd2484829', 'type': 'ddg', 'title': '量化交易信号的三种经典方法：阈值法、排序法、模型预测法'}
- {'url': 'https://zhuanlan.zhihu.com/p/681500430&rut=12ca7bb907b1a1aec9c8a53f62f1f712262ba7a3dba67156be1e9b3e734b7fe7', 'type': 'ddg', 'title': '量化条件单（2）-挂单卖出 - 知乎'}
