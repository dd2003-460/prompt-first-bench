# N303: 从 24GB 单卡切换至 48GB 双卡 (2x RTX 4090) 的 TCO 增量与性能损失：硬件成本增加约 $1599 (第二张卡) + $500-100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

从 24GB 单卡切换至 48GB 双卡 (2x RTX 4090) 的 TCO 增量与性能损失：硬件成本增加约 $1599 (第二张卡) + $500-1000 (主板/电源升级)，总 CapEx 从 ~$2100 增至 ~$4200-4700；同时引入 PCIe 互联延迟，预计 Decode 吞吐下降 10-20% (从单卡 74.6 tokens/s 降至 ~60-67 tokens/s)。

## Corrected Claim

从 24GB 单卡切换至 48GB 双卡 (2x RTX 4090) 的 TCO 增量与性能损失：硬件成本增加约 $1599 (第二张卡) + $500-1000 (主板/电源升级)，总 CapEx 从 ~$2100 增至 ~$4200-4700；同时引入 PCIe 互联延迟，预计 Decode 吞吐下降 10-20% (从单卡 74.6 tokens/s 降至 ~60-67 tokens/s)。

## Evidence

先验知识/题面给定，逻辑校验通过：硬件成本估算符合市场常识（RTX 4090价格及升级配件费用），双卡PCIe互联导致的通信开销及吞吐下降幅度（10-20%）符合分布式推理的工程经验规律，数值量级合理且内部自洽。

## Search Query

2x RTX 4090 PCIe bandwidth overhead inference throughput loss
