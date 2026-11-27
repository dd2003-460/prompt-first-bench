# N67: NVLink vs PCIe 互联带宽对比：NVLink 4.0 (H100) 带宽 900 GB/s (双向)，PCIe 4.0 x16 带宽 64 GB/s

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

NVLink vs PCIe 互联带宽对比：NVLink 4.0 (H100) 带宽 900 GB/s (双向)，PCIe 4.0 x16 带宽 64 GB/s (单向)。若使用 2x H100 通过 NVLink 互联，T_comm = 6.29GB / 900 GB/s ≈ 0.007s，总延迟 ≈ 0.020s/token，吞吐 ≈ 50 tokens/s，比 PCIe 互联 (9.0 tokens/s) 高 455%。因此，多卡方案必须使用 NVLink 或更高带宽互联才能接近单卡性能。

## Corrected Claim

NVLink vs PCIe 互联带宽对比：NVLink 4.0 (H100) 带宽 900 GB/s (双向)，PCIe 4.0 x16 带宽 64 GB/s (单向)。若使用 2x H100 通过 NVLink 互联，T_comm = 6.29GB / 900 GB/s ≈ 0.007s，总延迟 ≈ 0.020s/token，吞吐 ≈ 50 tokens/s，比 PCIe 互联 (9.0 tokens/s) 高 455%。因此，多卡方案必须使用 NVLink 或更高带宽互联才能接近单卡性能。

## Evidence

父节点级核验未通过：不完备（子节点1和子节点2分别聚焦于NVLink有效带宽修正和PCIe版本升级影响，主题不重叠且无矛盾，正交性良好。但父节点的核心结论是‘多卡必须使用NVLink才能接近单卡性能’，而子节点1指出实际通信占比<1%、瓶颈在算力/带宽而非互联，这直接削弱了父节点结论的必要性；子节点2也强调PCIe升级对TP推理边际收益极低。两者共同表明‘互联带宽’并非主要瓶颈，与父节点强调‘必须使用高带宽互联’存在逻辑冲突，未覆盖父节点中关于‘接近单卡性能’的真实限制因素（如计算/显存带宽），导致完备性不足。）
