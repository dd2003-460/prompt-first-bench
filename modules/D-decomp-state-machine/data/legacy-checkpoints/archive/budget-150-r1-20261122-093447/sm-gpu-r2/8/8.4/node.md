# N119: Intel Arc A770 (16GB) 双卡方案可行性：总显存 32GB，但 PCIe 4.0 x4 带宽仅 ~16GB/s，远低于显存带宽 560GB/s

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Intel Arc A770 (16GB) 双卡方案可行性：总显存 32GB，但 PCIe 4.0 x4 带宽仅 ~16GB/s，远低于显存带宽 560GB/s，导致多卡间 KV Cache 同步成为瓶颈，理论吞吐下降 > 50%；且 Arc 驱动对 LLM 推理优化不足，不推荐作为主力方案 [待核验：需实测双卡 A770 跑 27B 的 tokens/s]

## Corrected Claim

Intel Arc A770 (16GB) 双卡方案总显存 32GB，但 PCIe 4.0 x4 带宽（~16GB/s）远低于显存带宽（~512GB/s），多卡间 KV Cache 同步可能成为瓶颈，导致理论吞吐显著下降；且 Arc 驱动对 LLM 推理优化不足，不推荐作为主力方案 [待核验：需实测双卡 A770 跑 27B 的 tokens/s]

## Evidence

[质询]「理论吞吐下降 > 50%」这一具体数值缺乏严谨的理论推导支持，且将PCIe带宽瓶颈直接等同于整体吞吐下降比例属于过度简化；此外，Arc A770的显存带宽实际约为512GB/s（而非560GB/s），且双卡间KV Cache同步机制在主流推理框架中并非默认或高效实现，该陈述混淆了硬件极限与软件实际表现。 | 先验知识/题面给定，逻辑校验通过：PCIe 4.0 x4带宽（~16GB/s）确实远低于显存带宽（~512GB/s），多卡同步瓶颈存在；但具体吞吐下降比例和显存带宽数值存在偏差，且缺乏实测数据支持，故降级为定性表述。

## Search Query

Intel Arc A770 dual GPU LLM inference bottleneck
