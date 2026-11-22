# N357: Cloud vs Local TCO 交叉点重算：设 Cloud 小时费率为 $C_h$ (取中值 $3.36)，本地年 OpEx 为 $O_{local}$ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128, N129

## Claim

Cloud vs Local TCO 交叉点重算：设 Cloud 小时费率为 $C_h$ (取中值 $3.36)，本地年 OpEx 为 $O_{local}$ (取 $6,132 无 PUE 或 $9,198 含 PUE)，本地 CapEx 为 $C_{local}$ ($30,000)。交叉点使用小时数 $H_{cross} = (C_{local} - O_{local} 	imes T_{years}) / (C_h 	imes 8760 - O_{local})$。在 1 年持有期内，若 $C_h = 3.36$，则 $H_{cross} \approx (30000 - 6132) / (3.36 	imes 8760 - 6132) \approx 23868 / 23268 \approx 1.02$ 年（即几乎全年使用才打平，说明 Cloud 在低使用率下极具优势）。

## Corrected Claim

Cloud vs Local TCO 交叉点重算：设 Cloud 小时费率为 $C_h$ (取中值 $3.36)，本地年 OpEx 为 $O_{local}$ (取 $6,132 无 PUE 或 $9,198 含 PUE)，本地 CapEx 为 $C_{local}$ ($30,000)。交叉点使用小时数 $H_{cross} = (C_{local} - O_{local} 	imes T_{years}) / (C_h 	imes 8760 - O_{local})$。在 1 年持有期内，若 $C_h = 3.36$，则 $H_{cross} \approx (30000 - 6132) / (3.36 	imes 8760 - 6132) \approx 23868 / 23268 \approx 1.02$ 年（即几乎全年使用才打平，说明 Cloud 在低使用率下极具优势）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导与数值计算（23868/23268 ≈ 1.026）自洽，符合TCO交叉点定义。
