# N169: 排序算法中速度权重 w3 的占比可通过分析平台公开或泄露的排序特征重要性（如 SHAP 值）或 A/B 测试中移除 Velocity 特征后的 CTR 变化来反

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N49, N50, N51

## Claim

排序算法中速度权重 w3 的占比可通过分析平台公开或泄露的排序特征重要性（如 SHAP 值）或 A/B 测试中移除 Velocity 特征后的 CTR 变化来反推，若 w3 > 0.4，则表明算法显著偏向快速成交，需结合平台内部文档或学术案例验证。

## Corrected Claim

排序算法中速度相关特征的权重占比可通过分析平台公开或泄露的排序特征重要性（如 SHAP 值）或 A/B 测试中移除该特征后的 CTR 变化来反推；若该权重显著高于其他非核心特征，则表明算法偏向快速成交，具体阈值需结合平台内部文档或特定学术案例验证。

## Evidence

[质询]该陈述包含具体的经验性阈值（w3 > 0.4）和特定的特征名称（Velocity），这属于特定平台（如电商或搜索引擎）的内部工程参数，无法从第一性原理推导，且参考来源仅讨论通用排序逻辑，未提供该具体数值或特征权重的证据。 | 逻辑上通过SHAP值或A/B测试反推特征权重是合理的方法论，但具体阈值0.4及特征名Velocity属于经验事实，参考来源[1][2]仅涉及通用排序指标（相关性、权威性），未覆盖具体权重数值，故降级。

## Search Query

e-commerce ranking algorithm feature importance velocity weight SHAP value

## Retrieval Sources

- {'url': 'https://cloud.baidu.com/article/3684312&rut=76331d1756998f7ae41fa27ac5efb6a01bae6afb4c5c633789a38d5e91415cc5', 'type': 'ddg', 'title': '搜索引擎排序逻辑解密：指标与算法的深度剖析'}
- {'url': 'https://developer.baidu.com/article/detail.html?id=3684257&rut=bc514c89609523c8a57c28b6af5a31134e06314fb851c63d17ef3450c568076c', 'type': 'ddg', 'title': '搜索引擎排序机制深度解析：指标与算法协同优化-百度开发者中心'}
