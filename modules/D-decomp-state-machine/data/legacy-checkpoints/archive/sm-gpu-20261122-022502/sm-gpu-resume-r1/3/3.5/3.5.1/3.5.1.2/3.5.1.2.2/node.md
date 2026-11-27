# N750: TensorRT-LLM 对 RTX 4090 支持 FP8 KV Cache 的具体版本门槛：首个支持 FP8 KV Cache 的 TRT-LLM 版本号，

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N231

## Claim

TensorRT-LLM 对 RTX 4090 支持 FP8 KV Cache 的具体版本门槛：首个支持 FP8 KV Cache 的 TRT-LLM 版本号，以及该版本中 FP8 解码速度相比 BF16 的加速比 (speedup ratio)，若不支持则标记为 [待核验: 需确认是否仅支持 FP8 权重而不支持 KV Cache]

## Corrected Claim

TensorRT-LLM 在较新版本中支持 RTX 4090 的 FP8 KV Cache，具体首个支持版本号及相比 BF16 的加速比需查阅官方 Release Notes 或基准测试报告确认。

## Evidence

[质询]具体版本号及加速比属于经验事实，缺乏来源支持，且不同硬件/驱动组合下表现可能差异巨大，无法仅凭逻辑推导确定具体数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

TensorRT-LLM FP8 KV cache support version RTX 4090
