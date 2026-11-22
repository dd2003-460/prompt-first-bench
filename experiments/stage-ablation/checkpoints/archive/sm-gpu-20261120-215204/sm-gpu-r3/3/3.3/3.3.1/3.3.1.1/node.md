# N253: Qwen3-27B (假设64层, GQA 8 KV Heads, Head Dim 128) 在32K上下文下的BF16 KV Cache理论总大小为 2 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88, N89, N90

## Claim

Qwen3-27B (假设64层, GQA 8 KV Heads, Head Dim 128) 在32K上下文下的BF16 KV Cache理论总大小为 2 * 64 * 8 * 128 * 32768 * 2 bytes ≈ 8.6 GB，N88中声称的20GB KV Cache估算偏高，需核实是否包含冗余或计算错误。

## Corrected Claim

Qwen3-27B (假设64层, GQA 8 KV Heads, Head Dim 128) 在32K上下文下的BF16 KV Cache理论总大小为 2 * 64 * 8 * 128 * 32768 * 2 bytes ≈ 8.6 GB，N88中声称的20GB KV Cache估算偏高，需核实是否包含冗余或计算错误。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache大小计算公式为 2 (K/V) * 层数 * KV头数 * 头维度 * 序列长度 * 字节数，代入数值 2*64*8*128*32768*2 = 8,589,934,592 bytes ≈ 8.6 GB，计算准确且量级合理。
