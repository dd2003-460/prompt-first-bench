# N302: 风险感知修正项 R_risk 的量化模型：R_risk = λ_risk * (P_ask / P_median - 1)^γ * I(defect_flag)

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N103

## Claim

风险感知修正项 R_risk 的量化模型：R_risk = λ_risk * (P_ask / P_median - 1)^γ * I(defect_flag)，其中 λ_risk 为风险厌恶系数，γ 为价格偏离敏感度，I(defect_flag) 为硬伤存在指示变量，需通过买家对高溢价瑕疵商品的退货率或咨询中断率估算 λ_risk。

## Corrected Claim

风险感知修正项 R_risk 的一种可能量化模型为：R_risk = λ_risk * (P_ask / P_median - 1)^γ * I(defect_flag)，其中参数需根据具体市场数据（如退货率）进行校准，该模型并非通用标准。

## Evidence

[质询]该公式为特定场景下的经验性启发式模型，并非通用物理或数学定律，其参数（λ_risk, γ）的具体估算方法（如通过退货率估算）缺乏普适性理论支撑，且不同市场环境下模型形式可能完全不同，存在将特定经验模型误认为通用量化标准的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该模型属于特定业务场景下的经验公式，非第一性原理可推导的通用事实）

## Search Query

consumer risk perception high price defect signal fraud heuristic
