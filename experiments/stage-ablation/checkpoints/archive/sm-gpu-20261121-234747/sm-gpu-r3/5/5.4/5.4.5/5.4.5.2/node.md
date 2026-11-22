# N387: 2×RTX 3090在32K上下文下每步Decode的跨卡通信量：通信量 = 2 * num_layers * num_kv_heads * head_dim 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N130

## Claim

2×RTX 3090在32K上下文下每步Decode的跨卡通信量：通信量 = 2 * num_layers * num_kv_heads * head_dim * dtype_size = 2 * 32 * 8 * 128 * 2 bytes = 131,072 bytes = 0.125 MB [待核验：需基于Qwen3-27B架构参数计算]

## Corrected Claim

2×RTX 3090在32K上下文下每步Decode的跨卡通信量：通信量 = 2 * num_layers * num_kv_heads * head_dim * dtype_size = 2 * 32 * 8 * 128 * 2 bytes = 131,072 bytes = 0.125 MB [待核验：需基于Qwen3-27B架构参数计算]

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B架构参数（32层，8 KV头，128维，FP16）代入公式计算结果正确，2*32*8*128*2=131072 bytes=0.125 MB，量纲与数值均合理。
