# N43: 算术强度(Arithmetic Intensity)计算：AI = FLOPs/MemBytes = 2*P / (P + KV_cache_read)。在长上

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

算术强度(Arithmetic Intensity)计算：AI = FLOPs/MemBytes = 2*P / (P + KV_cache_read)。在长上下文(262k)下，KV读取占主导，AI < 1，处于内存带宽受限区(Memory-bound)

## Corrected Claim

算术强度(Arithmetic Intensity)计算：AI = FLOPs/MemBytes = 2*P / (P + KV_cache_read)。在长上下文(262k)下，KV读取占主导，AI < 1，处于内存带宽受限区(Memory-bound)

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数（Batch Size和Seq Len）下的具体实例化，存在高度冗余；且仅列举两个特定工作点，未能覆盖父节点中关于'长上下文下AI<1'这一通用结论的完整逻辑链条（如为何AI会小于1的推导过程或临界条件分析），导致完备性不足。）
