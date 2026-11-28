# N51: 故障重试的期望吞吐损失公式为 E[Loss_Tokens] = (T_detect + T_startup) * Throughput_Decode；在标准 C

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

故障重试的期望吞吐损失公式为 E[Loss_Tokens] = (T_detect + T_startup) * Throughput_Decode；在标准 Cold Restart 模式下，E[Loss] = (0.05s + 6s) * 45 tokens/s ≈ 272 tokens；在 Warm Standby 模式下，E[Loss] = (0.05s + 0.5s) * 45 tokens/s ≈ 25 tokens；若单次科研步骤平均生成 500 tokens，Cold Restart 导致 54% 的步骤需要重算，Warm Standby 仅导致 5% 重算。

## Corrected Claim

故障重试的期望吞吐损失公式为 E[Loss_Tokens] = (T_detect + T_startup) * Throughput_Decode；在标准 Cold Restart 模式下，E[Loss] = (0.05s + 6s) * 45 tokens/s ≈ 272 tokens；在 Warm Standby 模式下，E[Loss] = (0.05s + 0.5s) * 45 tokens/s ≈ 25 tokens；若单次科研步骤平均生成 500 tokens，Cold Restart 导致 54% 的步骤需要重算，Warm Standby 仅导致 5% 重算。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算准确（(0.05+6)*45=272.25≈272; (0.05+0.5)*45=24.75≈25），比例推导正确（272/500=54.4%≈54%; 25/500=5%），符合故障恢复时间对吞吐影响的线性估算逻辑。
