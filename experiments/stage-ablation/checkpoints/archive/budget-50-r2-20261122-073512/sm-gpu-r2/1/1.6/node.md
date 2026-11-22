# N12: PCIe 互联拓扑限制：多卡方案中，若使用 PCIe Gen4 x16 (32 GB/s)，27B BF16 模型权重加载需 54GB/32GB/s ≈ 1.7

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

PCIe 互联拓扑限制：多卡方案中，若使用 PCIe Gen4 x16 (32 GB/s)，27B BF16 模型权重加载需 54GB/32GB/s ≈ 1.7s，且多卡并行时的 All-Reduce 通信开销占比在 2 卡配置下约为 5-10% (取决于层切分策略)。

## Corrected Claim

PCIe 互联拓扑限制：多卡方案中，若使用 PCIe Gen4 x16 (32 GB/s)，27B BF16 模型权重加载需 54GB/32GB/s ≈ 1.7s，且多卡并行时的 All-Reduce 通信开销占比在 2 卡配置下约为 5-10% (取决于层切分策略)。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑矛盾且未覆盖父节点关键信息。1. 矛盾：子节点1称双向带宽64GB/s但有效为32GB/s（通常Ring All-Reduce有效带宽受限于单向瓶颈或链路利用率，表述易混淆），而子节点2直接计算得出1687ms的通信延迟，这与父节点声称的'5-10%开销'严重不符（1.7s加载时间若作为基准，1.6s通信占比极高；若作为每层通信，总时间将远超合理范围），且子节点2将'权重加载'与'All-Reduce激活值通信'混淆，公式中使用的Model_Slice_GB是权重大小，而All-Reduce传输的是激活值或梯度，量级完全不同。2. 缺失：父节点明确提到的'模型权重加载需1.7s'这一关键约束未在子节点中独立体现或解释，子节点2错误地用权重大小去估算All-Reduce延迟。）
