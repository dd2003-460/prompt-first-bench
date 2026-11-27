# N305: 随机偏好噪声 ε_noise 的演化来源分解：将买家偏好噪声分解为‘探索性噪声’ ε_explore（源于演化中的多样性偏好，σ_explore ≈ 0.05）

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

随机偏好噪声 ε_noise 的演化来源分解：将买家偏好噪声分解为‘探索性噪声’ ε_explore（源于演化中的多样性偏好，σ_explore ≈ 0.05）和‘信息处理噪声’ ε_process（源于认知负荷，σ_process ≈ 0.03）。需计算总噪声 σ_total = sqrt(σ_explore² + σ_process²) ≈ 0.058，以验证该噪声水平是否足以解释 15-25% 挂价偏差中的随机部分。

## Corrected Claim

随机偏好噪声可分解为探索性噪声与信息处理噪声，若假设两者独立且标准差分别为0.05和0.03，则总噪声标准差约为0.058；具体数值需依据特定实证数据或模型设定确定。

## Evidence

[质询]具体数值（σ_explore ≈ 0.05, σ_process ≈ 0.03）及分解方式属于特定模型假设或经验参数，缺乏通用理论支持，且参考来源未提供这些具体数值，存在将特定案例参数泛化为通用事实的风险。 | 逻辑上独立噪声方差相加推导正确（sqrt(0.05^2+0.03^2)≈0.058），但具体噪声分量数值为经验事实，参考来源[1]仅涉及随机效用模型的一般框架，未直接支持具体数值分解，故降级。

## Retrieval Sources

- {'url': 'https://github.com/leey163/my_private_decision_preference_and_game_course/blob/main/D2-%E9%9A%8F%E6%9C%BA%E6%95%88%E7%94%A8%E4%B8%8E%E5%81%8F%E5%A5%BD%E8%A1%A8%E7%A4%BA.md&rut=c8763c36c9b62531d8428f17620ba2d92e12070474f7e97a006b3cc8c0b2752e', 'type': 'ddg', 'title': 'D2-随机效用与偏好表示.md - GitHub'}
