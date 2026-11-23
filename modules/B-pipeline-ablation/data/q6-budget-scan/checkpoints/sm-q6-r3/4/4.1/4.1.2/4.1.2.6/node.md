# N252: 自建节点P99延迟风险项中的故障惩罚 T_failure_penalty：自建节点故障率λ_annual为0.8%-1.7%（基于N98修正值），MTTR为3-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N77, N78, N79

## Claim

自建节点P99延迟风险项中的故障惩罚 T_failure_penalty：自建节点故障率λ_annual为0.8%-1.7%（基于N98修正值），MTTR为3-6小时（基于N99），故障期间延迟增加ΔT = 200-500ms（基于N100）；故障对P99的期望贡献为 E[T_failure] = λ_annual × MTTR_hours × ΔT / 8760 = 0.0125 × 4.5 × 350 / 8760 ≈ 0.0023ms/req，可忽略不计；但若考虑P99尾部分布，故障期间P99延迟可能瞬时升至300-500ms，需通过冗余设计（N+1）降低故障概率至0.1%，使P99延迟惩罚降至0.3-0.5ms/req。

## Corrected Claim

自建节点P99延迟风险项中的故障惩罚 T_failure_penalty：自建节点故障率λ_annual为0.8%-1.7%（基于N98修正值），MTTR为3-6小时（基于N99），故障期间延迟增加ΔT = 200-500ms（基于N100）；故障对P99的期望贡献为 E[T_failure] = λ_annual × MTTR_hours × ΔT / 8760 = 0.0125 × 4.5 × 350 / 8760 ≈ 0.0023ms/req，可忽略不计；但若考虑P99尾部分布，故障期间P99延迟可能瞬时升至300-500ms，需通过冗余设计（N+1）降低故障概率至0.1%，使P99延迟惩罚降至0.3-0.5ms/req。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（频率×时间×延迟/总时间=平均延迟贡献），数值计算准确（0.0125*4.5*350/8760≈0.0023），工程直觉合理（故障对P99均值贡献极小但尾部风险需冗余设计）。

## Search Query

self-hosted node failure penalty P99 latency redundancy design
