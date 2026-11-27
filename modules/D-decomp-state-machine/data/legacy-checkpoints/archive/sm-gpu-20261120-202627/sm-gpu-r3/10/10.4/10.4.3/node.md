# N453: 停机机会成本量化参数：对于本地工作站场景，若替代方案为租用云端 API（如 A100 实例），每小时停机成本 = 云端推理成本 ($0.5-$2.0/h)；若替

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N148

## Claim

停机机会成本量化参数：对于本地工作站场景，若替代方案为租用云端 API（如 A100 实例），每小时停机成本 = 云端推理成本 ($0.5-$2.0/h)；若替代方案为人工等待，每小时停机成本 = 工程师时薪 ($50-$100/h) × 0.5 (闲置系数)，需根据实际业务场景选择对应参数代入停机损失公式。

## Corrected Claim

停机机会成本量化参数：对于本地工作站场景，若替代方案为租用云端 API（如 A100 实例），每小时停机成本 = 云端推理成本 ($0.5-$2.0/h)；若替代方案为人工等待，每小时停机成本 = 工程师时薪 ($50-$100/h) × 0.5 (闲置系数)，需根据实际业务场景选择对应参数代入停机损失公式。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud GPU inference cost per hour A100 vs engineer hourly rate opportunity cost
