# N379: 单流传输时间 $T_{transfer}$ 对 P99 延迟的贡献占比：在 $s_{avg}=1\text{MB}$ 场景下，$T_{transfer} \ap

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N142

## Claim

单流传输时间 $T_{transfer}$ 对 P99 延迟的贡献占比：在 $s_{avg}=1\text{MB}$ 场景下，$T_{transfer} \approx 819 \text{ ms}$，若 $L_{edge}+L_{processing} \approx 10 \text{ ms}$，则 $T_{transfer}$ 占 P99 延迟的 $819/(819+10) \approx 98.8\%$；在 $s_{avg}=5\text{MB}$ 场景下，占比仍为 $99.75\%$，表明传输时间是 P99 延迟的主导因素。

## Corrected Claim

单流传输时间 $T_{transfer}$ 对 P99 延迟的贡献占比：在 $s_{avg}=1\text{MB}$ 场景下，$T_{transfer} \approx 819 \text{ ms}$，若 $L_{edge}+L_{processing} \approx 10 \text{ ms}$，则 $T_{transfer}$ 占 P99 延迟的 $819/(819+10) \approx 98.8\%$；在 $s_{avg}=5\text{MB}$ 场景下，占比仍为 $99.75\%$，表明传输时间是 P99 延迟的主导因素。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 819/(819+10) ≈ 0.9879 (98.8%) 正确；5MB 场景下传输时间线性增加至约 4095ms，占比 4095/(4095+10) ≈ 99.75% 正确，符合大文件传输中带宽延迟积主导延迟的物理直觉。
