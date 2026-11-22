# N235: H100 80GB 在 BF16 下剩余 25GB 显存，最大支持 Batch Size = 25 / 1.2 ≈ 20 个并发请求，与 A100 相同，但 H

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N109

## Claim

H100 80GB 在 BF16 下剩余 25GB 显存，最大支持 Batch Size = 25 / 1.2 ≈ 20 个并发请求，与 A100 相同，但 H100 的更高带宽使其在相同 Batch 下吞吐更高。

## Corrected Claim

H100 80GB 在 BF16 下若剩余 25GB 显存，且单请求显存占用约为 1.2GB（取决于序列长度和模型大小），则最大支持 Batch Size 约为 20 个并发请求；H100 相比 A100 具有更高带宽，在相同 Batch Size 下通常能提供更低的延迟或更高的吞吐。

## Evidence

[质询]数值量级与工程常识严重不符：1.2GB/请求的显存占用极低，通常仅适用于极短序列或特定量化场景，未说明上下文长度（Context Length）和模型大小，导致'最大支持 Batch Size'这一结论缺乏前提条件，属于经验事实且参数假设过于具体且未经验证。 | 经验事实，逻辑自洽但缺来源支持；且1.2GB/请求的假设缺乏上下文（如序列长度、模型参数量），属于特定条件下的经验参数，无法从第一性原理直接推出通用结论。
