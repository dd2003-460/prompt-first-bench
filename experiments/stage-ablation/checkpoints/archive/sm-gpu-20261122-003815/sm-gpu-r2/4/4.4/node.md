# N25: 推理吞吐量瓶颈分析：对于 Decode 阶段，吞吐主要受限于显存带宽 (Memory Bandwidth)。所需最小带宽 = (weights_size + K

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

推理吞吐量瓶颈分析：对于 Decode 阶段，吞吐主要受限于显存带宽 (Memory Bandwidth)。所需最小带宽 = (weights_size + KV_cache_size) / latency_target。若要求 100ms/token 延迟，BF16 下需带宽 ≈ (54GB + 17.2GB) / 0.1s = 712 GB/s。

## Corrected Claim

推理吞吐量瓶颈分析：对于 Decode 阶段，吞吐主要受限于显存带宽 (Memory Bandwidth)。所需最小带宽 = (weights_size + KV_cache_size) / latency_target。若要求 100ms/token 延迟，BF16 下需带宽 ≈ (54GB + 17.2GB) / 0.1s = 712 GB/s。

## Evidence

父节点级核验未通过：有冗余（子节点2（BF16速率）和子节点3（FP8速率）本质上是同一公式在不同精度参数下的实例化，存在结构冗余；子节点4（效率折损）是对子节点2中计算过程的修正/细化，与子节点2在逻辑上耦合紧密，若子节点2未明确使用有效带宽，则子节点4是必要的补充，但二者共同构成了一个完整的计算逻辑，拆分后显得碎片化。）
