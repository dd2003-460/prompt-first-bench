# N334: 首页曝光权重比值 $w_{high}/w_{std}$ 的解析表达式：基于平台流量分配算法的加权评分函数，$w(P) \propto P^\alpha \cdo

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N117, N118, N119

## Claim

首页曝光权重比值 $w_{high}/w_{std}$ 的解析表达式：基于平台流量分配算法的加权评分函数，$w(P) \propto P^\alpha \cdot CTR_{base}^\beta$，其中 $\alpha$ 为价格权重指数，$\beta$ 为点击率权重指数，需通过平台A/B测试日志反推 $\alpha, \beta$ 的取值

## Corrected Claim

在假设平台流量分配采用基于价格和点击率的加权评分模型时，可构建形如 $w(P) \propto P^\alpha \cdot CTR_{base}^\beta$ 的解析表达式，其中 $\alpha, \beta$ 为待估参数，需通过平台A/B测试日志进行拟合反推；但该函数形式仅为一种可能的建模假设，并非平台公开的通用算法事实。

## Evidence

[质询]该陈述假设平台流量分配算法遵循特定的幂律加权评分函数（$w(P) \propto P^\alpha \cdot CTR_{base}^\beta$），但这属于对黑盒算法的特定参数化假设，并非公开事实或第一性原理可推导的通用真理。不同平台、不同时期的算法结构可能完全不同（如基于深度学习的端到端排序、多目标优化等），直接断言存在这样的解析表达式且需通过A/B日志反推具体指数，缺乏普遍性依据，属于未经证实的经验性模型假设。 | 经验事实/算法假设，逻辑自洽但缺来源支持（本轮检索无可用来源，且该具体函数形式无法从第一性原理严格推出，属于特定场景下的建模假设）

## Search Query

eBay algorithm price weighting exponent alpha beta traffic distribution model
