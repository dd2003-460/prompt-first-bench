# N426: 候选硬件集筛选边界定义：排除显存容量 < 24GB 的所有消费级/专业级 GPU（因无法容纳 W4 量化权重 ~14.6GB + 32K KV Cache ~2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

候选硬件集筛选边界定义：排除显存容量 < 24GB 的所有消费级/专业级 GPU（因无法容纳 W4 量化权重 ~14.6GB + 32K KV Cache ~2-4GB + 激活值 ~2GB，总需求 ~19-20GB，且需保留 >10% 余量以应对 OOM 风险），排除单卡显存 < 32GB 且无多卡互联能力（如 NVLink/PCIe P2P）的数据中心卡，确保所有纳入比较的硬件在 W4/INT8/BF16 至少一种精度下具备 32K 上下文可行性。

## Corrected Claim

候选硬件集筛选边界定义：排除显存容量 < 24GB 的所有消费级/专业级 GPU（因无法容纳 W4 量化权重 ~14.6GB + 32K KV Cache ~2-4GB + 激活值 ~2GB，总需求 ~19-20GB，且需保留 >10% 余量以应对 OOM 风险），排除单卡显存 < 32GB 且无多卡互联能力（如 NVLink/PCIe P2P）的数据中心卡，确保所有纳入比较的硬件在 W4/INT8/BF16 至少一种精度下具备 32K 上下文可行性。

## Evidence

检索失败: no sources from any channel (all 5 failed)
