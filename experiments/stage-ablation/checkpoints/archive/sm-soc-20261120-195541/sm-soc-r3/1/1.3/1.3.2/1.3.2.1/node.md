# N88: N29中T_deal<5天时P_ask*接近C_acq+1/α的近似误差界：当T_deal=5, α=0.01时，精确值P_ask* = C_acq + 100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29, N30, N31

## Claim

N29中T_deal<5天时P_ask*接近C_acq+1/α的近似误差界：当T_deal=5, α=0.01时，精确值P_ask* = C_acq + 100*(1-e^-0.05) ≈ C_acq + 4.88，而近似值C_acq+1/α = C_acq+100，相对误差达95.1%，表明该线性近似仅在α*T_deal << 1（如<0.01）时成立，需补充泰勒展开二阶修正项。

## Corrected Claim

N29中T_deal<5天时P_ask*接近C_acq+1/α的近似误差界：当T_deal=5, α=0.01时，精确值P_ask* = C_acq + 100*(1-e^-0.05) ≈ C_acq + 4.88，而近似值C_acq+1/α = C_acq+100，相对误差达95.1%，表明该线性近似仅在α*T_deal << 1（如<0.01）时成立，需补充泰勒展开二阶修正项。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1-e^-0.05 ≈ 0.04877，精确值增量 4.877，近似值增量 100，相对误差 (100-4.877)/100 ≈ 95.1%，数值与结论均自洽。
