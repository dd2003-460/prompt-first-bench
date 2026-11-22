# N86: C_infra 公式中 COP (Coefficient of Performance) 的取值需根据部署环境区分：家用/小型办公室空调环境 COP ≈ 3.0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

C_infra 公式中 COP (Coefficient of Performance) 的取值需根据部署环境区分：家用/小型办公室空调环境 COP ≈ 3.0-3.5，而多卡高密度部署若需局部风冷或液冷，有效 COP 可能降至 1.5-2.0；需引用 ASHRAE 或具体散热器规格确定修正系数。

## Corrected Claim

C_infra 公式中 COP (Coefficient of Performance) 的取值需根据部署环境区分：家用/小型办公室空调环境 COP ≈ 3.0-3.5，而多卡高密度部署若需局部风冷或液冷，有效 COP 可能降至 1.5-2.0；需引用 ASHRAE 或具体散热器规格确定修正系数。

## Evidence

先验知识/题面给定，逻辑校验通过：家用空调COP 3.0-3.5符合常规工程经验，高密度数据中心因散热效率降低导致有效COP降至1.5-2.0符合热力学及工程直觉，量级合理且无内部矛盾。
