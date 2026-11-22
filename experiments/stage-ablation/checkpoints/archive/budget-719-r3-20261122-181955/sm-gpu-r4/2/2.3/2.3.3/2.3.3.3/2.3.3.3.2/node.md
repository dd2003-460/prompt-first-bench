# N702: vLLM PagedAttention 在 Batch Size=2, Block Size=16 tokens 时的内存碎片率公式：Fragmentation

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N251, N252, N253

## Claim

vLLM PagedAttention 在 Batch Size=2, Block Size=16 tokens 时的内存碎片率公式：Fragmentation_Rate = (Allocated_Blocks - Used_Tokens / Block_Size) / Allocated_Blocks；在 32K 上下文且序列长度非 16 的整数倍时，每请求浪费空间 = (Block_Size - Seq_Len % Block_Size) * 256 KB，最大浪费 15 * 256 KB = 3.75 MB/请求。

## Corrected Claim

vLLM PagedAttention 在 Batch Size=2, Block Size=16 tokens 时，每请求因块对齐产生的最大内部碎片为 (Block_Size - Seq_Len % Block_Size) * Block_Size * Bytes_Per_Token。在 32K 上下文且序列长度非 16 的整数倍时，若每 token 占用 256KB（特定配置），最大浪费为 15 * 256 KB = 3.75 MB/请求。

## Evidence

[质询]公式中分母 Allocated_Blocks 的定义模糊，若指总分配块数而非每请求分配块数，则量纲和逻辑不自洽；且 256KB/Block 的假设缺乏通用性，属于特定硬件配置下的经验值，非通用公式。 | 先验知识/题面给定，逻辑校验通过，但 256KB/Block 为特定配置经验值，非通用公式，且无外部来源支持，故降级。

## Search Query

vLLM paged attention memory fragmentation rate calculation
