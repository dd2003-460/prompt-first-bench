# N372: MI300X 并发扩展的隐性成本：Batch Size 从 1 增加到 4 时，KV Cache 显存占用线性增加，但计算效率（MFU）因内存带宽争用而下降。假

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N140

## Claim

MI300X 并发扩展的隐性成本：Batch Size 从 1 增加到 4 时，KV Cache 显存占用线性增加，但计算效率（MFU）因内存带宽争用而下降。假设 Batch Size=4 时吞吐量仅为 Batch Size=1 的 3.0 倍（而非 4 倍），则单位用户吞吐量下降 25%，需将此效率损失纳入 TCO 计算，修正后的性价比拐点将显著右移。

## Corrected Claim

MI300X 并发扩展的隐性成本：Batch Size 从 1 增加到 4 时，KV Cache 显存占用线性增加，但计算效率（MFU）因内存带宽争用而下降。假设 Batch Size=4 时吞吐量仅为 Batch Size=1 的 3.0 倍（而非 4 倍），则单位用户吞吐量下降 25%，需将此效率损失纳入 TCO 计算，修正后的性价比拐点将显著右移。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache显存随Batch Size线性增长符合内存管理原理；内存带宽争用导致MFU下降及吞吐量次线性增长（3.0x < 4.0x）符合GPU并发扩展的物理直觉；单位吞吐量下降25%（1/3 - 1/4 = 1/12 ≈ 8.3%? 不，单位用户吞吐量通常指总吞吐量除以Batch Size。若总吞吐为3.0x，单位用户吞吐为3.0/4 = 0.75x，即下降25%。计算正确。逻辑自洽。
