# N34: 偏好噪声方差 σ²_pref 随商品特征向量 x 的条件异方差性函数形式，具体量化为 σ²_pref(x) = σ_base² * exp(λ_x · x)，其

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

偏好噪声方差 σ²_pref 随商品特征向量 x 的条件异方差性函数形式，具体量化为 σ²_pref(x) = σ_base² * exp(λ_x · x)，其中 λ_x 为特征敏感度系数

## Corrected Claim

偏好噪声方差 σ²_pref 具有随商品特征向量 x 变化的条件异方差性，即 σ²_pref = f(x)，其中 f(x) 为依赖于具体模型和数据分布的函数（如指数形式 σ_base² * exp(λ_x · x) 仅为一种可能的参数化假设）。

## Evidence

[质询]该陈述声称存在一个具体的、通用的量化函数形式 σ²_pref(x) = σ_base² * exp(λ_x · x)，这属于特定的经验模型假设。然而，条件异方差性（Heteroscedasticity）仅指方差依赖于输入，其具体函数形式（如线性、指数、多项式等）取决于具体数据集和模型设定，并非由“条件异方差性”这一概念本身唯一确定或推导出的标准公式。将特定的指数形式断言为“具体量化为”的通用事实，缺乏普遍性依据，且参考来源中未提及此特定公式。 | 来源[1]和[3]确认了条件异方差性（方差依赖于输入/时间）的存在和概念，但未支持该特定的指数函数形式 σ²_pref(x) = σ_base² * exp(λ_x · x) 为通用标准；该公式属于特定模型假设，非第一性原理可推导的通用事实，故降级。

## Search Query

heteroscedasticity in buyer reservation price conditional on product features used market

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29549793/article/details/161841510&rut=c61ca844cc0e8b56d10e91b1efbb94271e29476476ab2b6239cb7a1ee0bfedac', 'type': 'ddg', 'title': '自监督学习中的条件异方差问题与AdaSSL框架解析-CSDN博客'}
- {'url': 'https://www.volcengine.com/article/523736&rut=c18cc4173e07a699ec59044c36152fe1779d921f4d619034d093386cfe150f66', 'type': 'ddg', 'title': '如何开展偏差-方差-噪声分解？含实践方法及噪声估算问询'}
- {'url': 'https://qihongruan.github.io/tsay-time-series/chapters/ch03.html&rut=7e9a5abd9b8dcd176776a5e6ab2db8e9afc9f7945a1bef2af3d41b8ca9c238f3', 'type': 'ddg', 'title': '第3章 条件异方差模型 — 金融时间序列分析笔记'}
