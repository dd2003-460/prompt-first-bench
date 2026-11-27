# N682: RTX 5090 在 32K 上下文下的 KV Cache 显存占用精确计算：Qwen3-27B 有 32 层 Transformer，每层 KV Cache 

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N282

## Claim

RTX 5090 在 32K 上下文下的 KV Cache 显存占用精确计算：Qwen3-27B 有 32 层 Transformer，每层 KV Cache 大小为 2 * 32 * 128 * 32768 * 2 bytes (BF16) = 16.8 MB/层，总 KV Cache = 32 * 16.8 MB = 537.6 MB ≈ 0.54 GB；若 KV Cache 量化为 FP8，则减半为 0.27 GB。修正 N282 中 1.2GB 的估计值，实际 KV Cache 占用远低于此。

## Corrected Claim

基于假设的 Qwen3-27B 架构参数（32层，GQA 32 KV heads，128 head dim），32K 上下文下 BF16 KV Cache 占用约为 0.54 GB，FP8 量化后约为 0.27 GB。

## Evidence

[质询]Qwen3-27B 的具体架构参数（如层数、KV头数、Head Dim）属于经验事实，且不同版本或配置可能存在差异，仅凭逻辑自洽无法确证其精确数值，存在参数假设错误的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B KV cache size calculation 32K context
