# N209: Decode 阶段的显存读取总量 R_decode 随上下文长度线性增长，公式为 R_decode = Weight_Size + KV_Cache_per_t

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

Decode 阶段的显存读取总量 R_decode 随上下文长度线性增长，公式为 R_decode = Weight_Size + KV_Cache_per_token * (Seq_Len - 1)；在 32K 上下文下，BF16 总读取量为 55.07 GB，FP8 总读取量为 28.07 GB，INT4 总读取量为 14.57 GB

## Corrected Claim

Decode 阶段的显存读取总量 R_decode 随上下文长度线性增长，公式为 R_decode = Weight_Size + KV_Cache_per_token * (Seq_Len - 1)；在 32K 上下文下，BF16 总读取量为 55.07 GB，FP8 总读取量为 28.07 GB，INT4 总读取量为 14.57 GB

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点结构高度对称，本质上是同一公式在不同权重精度（FP8/INT4）下的参数化实例，存在结构性冗余。此外，父节点明确列出了 BF16 的总读取量（55.07 GB），但子节点完全缺失了 BF16 权重的对应分解，导致对父节点中提到的三种精度场景覆盖不全。）

## Search Query

LLM decode memory bandwidth weight kv cache total read
