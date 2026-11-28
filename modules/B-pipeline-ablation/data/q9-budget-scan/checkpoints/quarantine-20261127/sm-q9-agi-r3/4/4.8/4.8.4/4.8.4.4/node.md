# N258: 事实漂移率的累积函数拟合为指数模型 D(n) = D_base * exp(k*n)，其中 n 为推理步数，D_base = 0.05 (初始步漂移率)，k =

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N89, N90, N91

## Claim

事实漂移率的累积函数拟合为指数模型 D(n) = D_base * exp(k*n)，其中 n 为推理步数，D_base = 0.05 (初始步漂移率)，k = 0.15 (步间增长率)；该模型在 n=10 时预测漂移率为 23.2%，与 N90 声称的 15-20% 增量趋势基本一致，但需通过至少 50 个真实科研任务的轨迹数据进行回归验证以确定 k 的置信区间。

## Corrected Claim

事实漂移率可能随推理步数呈指数增长趋势，具体模型参数（如D_base和k）需通过大量真实科研任务轨迹数据的回归分析确定，当前引用的具体数值（D_base=0.05, k=0.15）缺乏公开文献直接支持。

## Evidence

[质询]该陈述包含具体的经验参数（D_base=0.05, k=0.15）及特定场景下的预测值（n=10时为23.2%），这些属于经验事实而非第一性原理可推导内容。参考来源仅讨论通用的数据/模型漂移概念，未提供针对‘推理步数’的指数拟合模型或具体参数支持，因此缺乏直接证据支撑其数值准确性。 | 逻辑计算自洽（0.05 * exp(0.15*10) ≈ 0.232），但参考来源[1]仅涉及通用漂移概念，与具体推理步数漂移模型无关，属经验事实且缺来源支持。

## Search Query

LLM long chain of thought error accumulation rate exponential model

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/693619789&rut=332c1718ba71f915b334a44171c6cd823adfe0415741b08634c1a604764c5506', 'type': 'ddg', 'title': '一文带您了解数据和模型漂移 (Drift)：漂移检测示例 - 知乎'}
