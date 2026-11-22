# N145: 散热环境约束：若房间散热能力为300W，则总TDP上限为300W / 1.2 ≈ 250W，排除所有单卡方案（RTX 4090 TDP=450W），仅允许CPU

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

散热环境约束：若房间散热能力为300W，则总TDP上限为300W / 1.2 ≈ 250W，排除所有单卡方案（RTX 4090 TDP=450W），仅允许CPU推理或低功耗GPU（如RTX 3060 12GB）。

## Corrected Claim

散热环境约束：若房间散热能力为300W，则总TDP上限为300W / 1.2 ≈ 250W，排除所有单卡方案（RTX 4090 TDP=450W），仅允许CPU推理或低功耗GPU（如RTX 3060 12GB）。

## Evidence

先验知识/题面给定，逻辑校验通过：300W/1.2≈250W计算正确，RTX 4090 TDP 450W远超250W上限，RTX 3060 TDP约170W在范围内，逻辑自洽。
