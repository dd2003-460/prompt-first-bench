# N208: Qwen3-27B 在 32K 上下文下的 KV Cache 总大小为 1.07 GB，计算公式为 KV_Cache = 2 * N_layers * N_he

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N100

## Claim

Qwen3-27B 在 32K 上下文下的 KV Cache 总大小为 1.07 GB，计算公式为 KV_Cache = 2 * N_layers * N_heads * Head_Dim * Seq_Len * Bytes_per_Element；其中 N_layers=40, N_heads=40, Head_Dim=128, Seq_Len=32768, Bytes_per_Element=2 (BF16)，单 Token 增量约为 32.8 KB

## Corrected Claim

Qwen3-27B 在 32K 上下文下的 KV Cache 总大小为 1.07 GB，计算公式为 KV_Cache = 2 * N_layers * N_heads * Head_Dim * Seq_Len * Bytes_per_Element；其中 N_layers=40, N_heads=40, Head_Dim=128, Seq_Len=32768, Bytes_per_Element=2 (BF16)，单 Token 增量约为 32.8 KB

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点之间在量化方案上互斥，满足正交性；但父节点明确给出了 BF16 的具体数值和单 Token 增量，子节点仅涵盖了 FP8 和 INT4 两种量化变体，遗漏了父节点核心的 BF16 基准数据，导致信息不完备；此外，两个子节点本质上是同一计算公式在不同精度参数下的实例化，存在结构性冗余。）

## Search Query

Qwen3-27B KV cache size 32k context formula
