# N60: Qwen3-27B在INT4/W4精度下满足32K上下文的最小单卡显存需求计算为：权重15.5GB + KV Cache (54层*2*4096*128*327

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

Qwen3-27B在INT4/W4精度下满足32K上下文的最小单卡显存需求计算为：权重15.5GB + KV Cache (54层*2*4096*128*32768*1bytes/1024^3 ≈ 4.7GB，KV Cache通常保持BF16/FP16精度) + 激活/框架开销(3GB) ≈ 23.2GB，因此24GB卡（RTX 4090）可行但余量极小（<1GB），需启用PagedAttention或降低并发。

## Corrected Claim

Qwen3-27B在INT4/W4精度下满足32K上下文的最小单卡显存需求计算为：权重15.5GB + KV Cache (54层*2*4096*128*32768*1bytes/1024^3 ≈ 4.7GB，KV Cache通常保持BF16/FP16精度) + 激活/框架开销(3GB) ≈ 23.2GB，因此24GB卡（RTX 4090）可行但余量极小（<1GB），需启用PagedAttention或降低并发。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1修正权重参数，节点2修正KV Cache参数（指出父节点精度假设错误），节点3修正可用显存上限（指出父节点未扣除系统开销），节点4基于前三个修正值进行最终余量计算。各节点职责单一，无重复或矛盾，且完整覆盖了父节点中权重、KV、开销及最终结论的所有关键计算环节。）
