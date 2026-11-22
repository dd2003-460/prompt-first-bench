# N157: N54子节点：256GB 容量下 Tail_Byte_256 的基准计算，S_256 对应 F_S^{-1}(1 - 238000/100000)，由于 N_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

N54子节点：256GB 容量下 Tail_Byte_256 的基准计算，S_256 对应 F_S^{-1}(1 - 238000/100000)，由于 N_cache > N_total，S_256 取 x_max，Tail_Byte_256 = 1 - CDF(x_max) = 0，表明 256GB 容量完全覆盖所有对象字节，长尾占比为 0。

## Corrected Claim

N54子节点：256GB 容量下 Tail_Byte_256 的基准计算，S_256 对应 F_S^{-1}(1 - 238000/100000)，由于 N_cache > N_total，S_256 取 x_max，Tail_Byte_256 = 1 - CDF(x_max) = 0，表明 256GB 容量完全覆盖所有对象字节，长尾占比为 0。

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量（256GB）大于总数据量（N_cache > N_total）时，所有对象均可被缓存，长尾未命中部分为0，符合逻辑推导。
