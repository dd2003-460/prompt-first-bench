# N80: AWQ 算法通过保护显著权重（Saliency-aware）实现 W4A16 量化，其机制导致对激活值分布的敏感度低于 GPTQ，从而在相同比特数下通常具有更小

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

AWQ 算法通过保护显著权重（Saliency-aware）实现 W4A16 量化，其机制导致对激活值分布的敏感度低于 GPTQ，从而在相同比特数下通常具有更小的 PPL 损失 [knowledge]

## Corrected Claim

AWQ 算法通过保护显著权重（Saliency-aware）实现 W4A16 量化，其机制导致对激活值分布的敏感度低于 GPTQ，从而在相同比特数下通常具有更小的 PPL 损失 [knowledge]

## Evidence

先验知识/题面给定，逻辑校验通过：AWQ 基于激活值显著性保护关键权重，相比 GPTQ 的逐层误差补偿，AWQ 在 W4A16 场景下通常表现出更优的 PPL 保持能力，符合量化领域共识。
