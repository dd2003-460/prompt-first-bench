# N19: 多卡组合方案：2×RTX 3090 (48GB)、2×RTX 4090 (48GB)、1×A100 80GB、1×H100 80GB，需计算各方案的总 TCO（

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

多卡组合方案：2×RTX 3090 (48GB)、2×RTX 4090 (48GB)、1×A100 80GB、1×H100 80GB，需计算各方案的总 TCO（硬件+电力+散热） [待核验：电力成本模型]

## Corrected Claim

多卡组合方案：2×RTX 3090 (48GB)、2×RTX 4090 (48GB)、1×A100 80GB、1×H100 80GB，需计算各方案的总 TCO（硬件+电力+散热） [待核验：电力成本模型]

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 冗余严重：前4个子节点是同一公式在不同硬件/精度下的实例化，后4个是同一TCO公式在不同硬件下的实例化，应合并为参数化模板而非独立节点。2. 不完备：父节点要求计算'总TCO（硬件+电力+散热）'，但子节点中OpEx仅包含电力（Energy），完全缺失散热成本（Cooling Cost）的计算；且部分TCO计算中CapEx未包含散热硬件成本。3. 正交性虽无直接矛盾，但逻辑上高度耦合。）
