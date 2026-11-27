# N303: CPU Offload 的内存带宽瓶颈精确量化：当 Offload 数据量 D_offload = 3GB 时，每生成 1 token 需从内存读取 3GB 权

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

CPU Offload 的内存带宽瓶颈精确量化：当 Offload 数据量 D_offload = 3GB 时，每生成 1 token 需从内存读取 3GB 权重，理论延迟 L_offload = 3GB / MemBW_DDR；若 MemBW_DDR = 50 GB/s (单通道 DDR4)，L_offload = 60ms/token，即最大吞吐 16.7 tok/s；若 MemBW_DDR = 100 GB/s (双通道 DDR5)，L_offload = 30ms/token，即 33.3 tok/s

## Corrected Claim

CPU Offload 的内存带宽瓶颈精确量化：当 Offload 数据量 D_offload = 3GB 时，每生成 1 token 需从内存读取 3GB 权重，理论延迟 L_offload = 3GB / MemBW_DDR；若 MemBW_DDR = 50 GB/s (单通道 DDR4)，L_offload = 60ms/token，即最大吞吐 16.7 tok/s；若 MemBW_DDR = 100 GB/s (双通道 DDR5)，L_offload = 30ms/token，即 33.3 tok/s

## Evidence

先验知识/题面给定，逻辑校验通过：3GB/50GB/s=0.06s=60ms，1/0.06≈16.7；3GB/100GB/s=0.03s=30ms，1/0.03≈33.3，计算无误且符合内存带宽瓶颈的基本物理直觉。
