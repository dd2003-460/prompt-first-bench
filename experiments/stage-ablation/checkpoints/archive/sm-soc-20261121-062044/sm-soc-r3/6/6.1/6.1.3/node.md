# N245: 工作点C（高信号/高噪声）：当基线咨询数 Inquiry_base > 50 时，相对误差 < 14%，直接采用原始比值 E = (ΔInquiry/Inqui

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

工作点C（高信号/高噪声）：当基线咨询数 Inquiry_base > 50 时，相对误差 < 14%，直接采用原始比值 E = (ΔInquiry/Inquiry_base) / (ΔP/P) 计算，无需修正；但若 ΔP/P < 1%（微小降价），则 E 对测量误差极度敏感，需设定 ΔP_min = 2% 作为有效计算门槛，低于此值的样本 E 值不纳入统计。

## Corrected Claim

工作点C（高信号/高噪声）：当基线咨询数 Inquiry_base > 50 时，相对误差 < 14%，直接采用原始比值 E = (ΔInquiry/Inquiry_base) / (ΔP/P) 计算，无需修正；但若 ΔP/P < 1%（微小降价），则 E 对测量误差极度敏感，需设定 ΔP_min = 2% 作为有效计算门槛，低于此值的样本 E 值不纳入统计。

## Evidence

先验知识/题面给定，逻辑校验通过
