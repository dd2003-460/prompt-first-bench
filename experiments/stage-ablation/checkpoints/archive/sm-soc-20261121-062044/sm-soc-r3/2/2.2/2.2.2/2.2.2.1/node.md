# N147: λ_loss 的校准：基于 Tversky & Kahneman 前景理论，设定损失厌恶系数 λ_loss = 2.25（标准值），若平台数据显示卖家对降价的心

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N47

## Claim

λ_loss 的校准：基于 Tversky & Kahneman 前景理论，设定损失厌恶系数 λ_loss = 2.25（标准值），若平台数据显示卖家对降价的心理阻力更强，可通过回归分析校准 λ_loss，使得模型拟合优度 R² > 0.7，确保 E[Loss_high] 计算符合行为经济学事实。

## Corrected Claim

λ_loss 的校准：基于 Tversky & Kahneman 前景理论，设定损失厌恶系数 λ_loss = 2.25（标准值），若平台数据显示卖家对降价的心理阻力更强，可通过回归分析校准 λ_loss，使得模型拟合优度 R² > 0.7，确保 E[Loss_high] 计算符合行为经济学事实。

## Evidence

先验知识/题面给定，逻辑校验通过：λ=2.25是前景理论标准参数，R²>0.7作为校准阈值在统计建模中合理，整体逻辑自洽且符合行为经济学常识。

## Search Query

loss aversion coefficient calibration in seller pricing behavior
