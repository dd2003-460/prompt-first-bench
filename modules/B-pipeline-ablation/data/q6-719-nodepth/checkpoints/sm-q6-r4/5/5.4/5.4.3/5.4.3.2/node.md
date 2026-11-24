# N329: 损失值与营收匹配度检验公式：Match_Ratio = Assumed_Loss / (DAU_per_POP × ARPU)，若 Match_Ratio < 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N115

## Claim

损失值与营收匹配度检验公式：Match_Ratio = Assumed_Loss / (DAU_per_POP × ARPU)，若 Match_Ratio < 0.2，则假设损失仅为营收的 20% 以下，属于“部分服务降级”场景（如延迟升高导致体验下降但用户未流失）；若 Match_Ratio > 0.5，则属于“服务中断”场景。当前 50k / 500k = 0.1，符合部分降级场景，需确认 N115 的 5k 风险溢价是否仅覆盖降级损失而非中断损失。

## Corrected Claim

损失值与营收匹配度检验公式：Match_Ratio = Assumed_Loss / (DAU_per_POP × ARPU)，若 Match_Ratio < 0.2，则假设损失仅为营收的 20% 以下，属于“部分服务降级”场景（如延迟升高导致体验下降但用户未流失）；若 Match_Ratio > 0.5，则属于“服务中断”场景。当前 50k / 500k = 0.1，符合部分降级场景，需确认 N115 的 5k 风险溢价是否仅覆盖降级损失而非中断损失。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义清晰，数值计算 50k/500k=0.1 正确，且 0.1 < 0.2 符合‘部分服务降级’的逻辑判定条件，内部自洽。

## Search Query

CDN risk premium partial degradation vs full outage loss modeling
