# N163: Mac Studio M2 Ultra在32K上下文、batch_size=1下的理论推理吞吐量(tokens/s) = 1200 GB/s / (13.5GB

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

Mac Studio M2 Ultra在32K上下文、batch_size=1下的理论推理吞吐量(tokens/s) = 1200 GB/s / (13.5GB权重 + 5.2GB KV Cache + 2.5GB激活) ≈ 45.9 tokens/s，基于统一内存带宽瓶颈计算

## Corrected Claim

Mac Studio M2 Ultra在32K上下文、batch_size=1下的理论推理吞吐量(tokens/s) = 1200 GB/s / (13.5GB权重 + 5.2GB KV Cache + 2.5GB激活) ≈ 45.9 tokens/s，基于统一内存带宽瓶颈计算

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点存在逻辑包含与冗余。子节点1计算了KV Cache的具体数值，子节点2不仅重复引用了该数值，还直接给出了最终吞吐量结果。子节点2实际上涵盖了子节点1的核心贡献（作为中间变量），且两者共同构成了同一个计算链路的修正，而非两个独立正交的维度。此外，子节点2直接得出了最终答案，使得子节点1显得多余或应被合并。）
