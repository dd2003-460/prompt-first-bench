# N50: A100 80GB SXM4 的显存带宽为 2039 GB/s，显存容量为 80 GB HBM2e，TDP 为 400W，NVLink 带宽为 600 GB/s

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9, N10, N11

## Claim

A100 80GB SXM4 的显存带宽为 2039 GB/s，显存容量为 80 GB HBM2e，TDP 为 400W，NVLink 带宽为 600 GB/s。

## Corrected Claim

A100 80GB SXM4 的显存带宽为 2039 GB/s，显存容量为 80 GB HBM2e，TDP 为 400W，NVLink 带宽为 600 GB/s。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 正交性失败：子节点1-4大量重复计算相同的KV Cache数值（17.2GB/8.6GB），且子节点2和4针对同一模型精度（W4）和上下文（32K）在不同硬件上重复了相同的显存需求计算逻辑，存在内容重叠。2. 完备性失败：父节点明确提及A100的TDP为400W，但子节点中完全缺失关于功耗/散热/能效比的任何信息，未覆盖该关键方面。3. 冗余性失败：子节点1-4本质上是“不同硬件+不同精度”对同一模型（Qwen3-27B）在特定上下文下的显存可行性分析，属于同一类参数化场景的枚举，应合并为一张对比表或单一综合节点，而非拆分为4个独立节点。）

## Search Query

A100 80GB SXM4 specs memory bandwidth NVLink
