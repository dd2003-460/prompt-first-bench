# N241: 流失概率 P(churn|click_drop) 的阈值效应模型：P(churn) 并非随点击率下降线性增加，而是存在阈值 θ_click；当点击率下降幅度 Δ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N79

## Claim

流失概率 P(churn|click_drop) 的阈值效应模型：P(churn) 并非随点击率下降线性增加，而是存在阈值 θ_click；当点击率下降幅度 ΔCTR < θ_click (估计值 5%) 时，P(churn) ≈ 0.01；当 ΔCTR > θ_click 时，P(churn) 呈指数上升，P(churn) = P_base × exp(β × (ΔCTR - θ_click))，其中 β ∈ [2.0, 3.0]，需通过历史数据回归确定 β。

## Corrected Claim

流失概率 P(churn|click_drop) 可能存在阈值效应：当点击率下降幅度 ΔCTR 小于特定阈值 θ_click 时，流失率保持低位；当 ΔCTR 超过 θ_click 时，流失率可能呈非线性（如指数）上升。具体阈值 θ_click、基础概率 P_base 及增长系数 β 需通过特定业务的历史数据回归确定，不存在通用的固定数值范围。

## Evidence

[质询]该模型中的具体参数（阈值 θ_click=5%、基础概率 P_base≈0.01、指数系数 β∈[2.0, 3.0]）属于经验事实，缺乏通用理论支持，且不同业务场景下这些参数差异巨大，直接断言具体数值范围缺乏依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值参数无法从第一性原理推出）

## Search Query

user churn probability threshold click-through rate drop e-commerce
