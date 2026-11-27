# N100: 工作点3（长期持有/高可靠性/高CapEx）：1x A100 80GB (Used) + BF16/FP8 量化方案。CapEx ≈ $4500 (Used A

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

工作点3（长期持有/高可靠性/高CapEx）：1x A100 80GB (Used) + BF16/FP8 量化方案。CapEx ≈ $4500 (Used A100) + $800 (Server PSU/Chassis) = $5300。OpEx_5yr ≈ 5 * (400W * 24h * 365d * $0.15/kWh) ≈ $3,200。TCO_5yr ≈ $8,500。优势：80GB 显存支持 BF16 无损推理，无需量化损失，且数据中心卡 MTBF 高于消费卡，长期维护成本更低。

## Corrected Claim

工作点3（长期持有/高可靠性/高CapEx）：1x A100 80GB (Used) + BF16/FP8 量化方案。CapEx ≈ $4500 (Used A100) + $800 (Server PSU/Chassis) = $5300。OpEx_5yr ≈ 5 * (400W * 24h * 365d * $0.15/kWh) ≈ $3,200。TCO_5yr ≈ $8,500。优势：80GB 显存支持 BF16 无损推理，无需量化损失，且数据中心卡 MTBF 高于消费卡，长期维护成本更低。

## Evidence

先验知识/题面给定，逻辑校验通过：CapEx ($5300) + OpEx ($3200) = TCO ($8500) 计算准确；A100 80GB 显存支持 BF16 推理及数据中心卡高可靠性符合工程常识。
