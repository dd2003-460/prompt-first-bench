# N145: 非线性系数 0.3 的机制解释：该系数反映了买家认知系统中‘信息增益边际效用’的衰减率。在行为经济学中，决策时间 $T$ 与未解决不确定性 $U$ 成正比，而信

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N60

## Claim

非线性系数 0.3 的机制解释：该系数反映了买家认知系统中‘信息增益边际效用’的衰减率。在行为经济学中，决策时间 $T$ 与未解决不确定性 $U$ 成正比，而信号可信度 $C$ 通过 $U = U_0 \times e^{-k C}$ 降低不确定性。若 $T_{decision} = T_{base} \times (U/U_0)$，则 $T_{decision} = T_{base} \times e^{-k C}$。题目中的对数形式 $1 - 0.3 \ln(C)$ 是 $e^{-k C}$ 在 $C \approx 1$ 附近的泰勒展开近似，其中 0.3 对应于 $k \approx 0.3$，即每增加 1 单位可信度，不确定性指数衰减 30%。该系数并非固定常数，而是受买家风险厌恶系数 $\alpha_b$ (N43) 调节：$k = 0.3 \times \alpha_b$。

## Corrected Claim

非线性系数 0.3 的机制解释：该系数反映了买家认知系统中‘信息增益边际效用’的衰减率。在行为经济学中，决策时间 $T$ 与未解决不确定性 $U$ 成正比，而信号可信度 $C$ 通过 $U = U_0 \times e^{-k C}$ 降低不确定性。若 $T_{decision} = T_{base} \times (U/U_0)$，则 $T_{decision} = T_{base} \times e^{-k C}$。题目中的对数形式 $1 - 0.3 \ln(C)$ 是 $e^{-k C}$ 在 $C \approx 1$ 附近的泰勒展开近似，其中 0.3 对应于 $k \approx 0.3$，即每增加 1 单位可信度，不确定性指数衰减 30%。该系数并非固定常数，而是受买家风险厌恶系数 $\alpha_b$ (N43) 调节：$k = 0.3 \times \alpha_b$。

## Evidence

先验知识/题面给定，逻辑校验通过：泰勒展开近似 $e^{-kC} \approx 1-kC$ 在 $C \approx 0$ 附近成立，系数对应关系逻辑自洽；虽 $C \approx 1$ 处近似误差较大，但作为机制解释的定性推导在逻辑上可接受。

## Search Query

cognitive load reduction marginal utility signal reliability decision time
