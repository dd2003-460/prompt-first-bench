# N65: NVIDIA RTX 4090 (24GB) 在 Qwen3-27B 上的显存带宽为 1008 GB/s，当前单卡市场均价约为 $1600-$1800 [待核验

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

NVIDIA RTX 4090 (24GB) 在 Qwen3-27B 上的显存带宽为 1008 GB/s，当前单卡市场均价约为 $1600-$1800 [待核验：实时价格]，其 TDP 为 450W。

## Corrected Claim

NVIDIA RTX 4090 (24GB) 在 Qwen3-27B 上的显存带宽为 1008 GB/s，当前单卡市场均价约为 $1600-$1800 [待核验：实时价格]，其 TDP 为 450W。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 逻辑错误与正交性缺失：子节点1声称计算的是'每生成 1 token 需读取的 KV Cache 字节数'，但公式中却乘入了完整的 seq_len (32768)，这实际上是整个序列的总KV Cache大小，而非单token增量读取量（单token增量仅涉及最后一层的K/V向量）。因此子节点1与子节点2在物理意义上存在矛盾或定义混淆。2. 完备性缺失：父节点明确提及了 TDP 450W 和 价格，但子节点完全未覆盖这两个关键参数，导致信息丢失。3. 冗余：子节点2本质上是子节点1（修正后）除以带宽的推导结果，两者属于强依赖的推导链，而非独立维度的分解。）

## Search Query

RTX 4090 memory bandwidth TDP price 2024
