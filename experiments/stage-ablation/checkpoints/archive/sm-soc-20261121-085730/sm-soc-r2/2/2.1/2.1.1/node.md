# N59: 信号强度系数 k 的实证估计：在 T ∝ 1/(1 + k·(P - C_ref)/C_ref) 模型中，k 的估计值约为 0.35，置信区间为 [0.25, 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

信号强度系数 k 的实证估计：在 T ∝ 1/(1 + k·(P - C_ref)/C_ref) 模型中，k 的估计值约为 0.35，置信区间为 [0.25, 0.45]，需通过平台历史成交数据的最小二乘回归确定。

## Corrected Claim

在 T ∝ 1/(1 + k·(P - C_ref)/C_ref) 模型中，信号强度系数 k 需通过平台历史成交数据的最小二乘回归确定，其具体数值（如 0.35）需依据特定数据集实证得出，当前缺乏通用标准值。

## Evidence

[质询]该陈述包含具体的经验数值（k≈0.35, CI [0.25, 0.45]）和特定的业务模型公式，属于经验事实。参考来源均讨论统计学中的'信号强度'（Logistic Regression）或无线通信信号预测，与交易/平台成交数据中的'信号强度系数k'完全无关，无法提供数值支持。 | 逻辑上量纲自洽（k为无量纲系数），但参考来源[1][2][3]均与'平台历史成交数据'或'交易模型'无关，属于主题不匹配，无可用外部证据支持具体数值。

## Search Query

signal strength coefficient k regression price premium transaction cycle empirical estimation

## Retrieval Sources

- {'url': 'https://icml.cc/virtual/2026/poster/62659&rut=3a2ec4b74e8b786ed2ccfdedb9a0c34445303fca039e46d17f10ea4fc5bfeb33', 'type': 'ddg', 'title': 'ICML Poster Signal Strength Estimation in Logistic Regression Using ...'}
- {'url': 'https://link.springer.com/chapter/10.1007/978-981-15-0118-0_18&rut=e68a9bca11f31c6ddbc7e2b043f559ade183146b8c44620dd3966844118f1ebe', 'type': 'ddg', 'title': 'Wireless Communication Signal Strength Prediction Method Based on the K ...'}
- {'url': 'https://openreview.net/forum?id=ebRDSATK4K&rut=6e65e1dc97445a5040ff4cd8d5c80c8b86d2430b0ac95fd2eecbb65c8bdbf97b', 'type': 'ddg', 'title': 'Signal Strength Estimation in Logistic Regression Using ... - OpenReview'}
