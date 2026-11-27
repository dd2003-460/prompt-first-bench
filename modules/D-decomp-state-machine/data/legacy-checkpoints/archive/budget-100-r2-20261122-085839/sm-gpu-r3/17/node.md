# N351: 非典型硬件方案（如 Apple M3 Ultra/Max）的纳入与排除逻辑：虽然 M3 Ultra 在 W4 量化下显存容量充足且电力成本低，但因缺乏 CUDA

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

非典型硬件方案（如 Apple M3 Ultra/Max）的纳入与排除逻辑：虽然 M3 Ultra 在 W4 量化下显存容量充足且电力成本低，但因缺乏 CUDA 生态优化及 Prefill 阶段算力瓶颈（约为 RTX 4090 的 1/10），其仅在‘极低延迟要求（<10 tokens/s）且高电力敏感’的特定边界条件下具备性价比优势，否则因软件适配成本（ROCm/MLX 后端稳定性）和 Prefill 延迟劣势被排除出主推荐列表。

## Corrected Claim

非典型硬件方案（如 Apple M3 Ultra/Max）的纳入与排除逻辑：虽然 M3 Ultra 在 W4 量化下显存容量充足且电力成本低，但因缺乏 CUDA 生态优化及 Prefill 阶段算力瓶颈（约为 RTX 4090 的 1/10），其仅在‘极低延迟要求（<10 tokens/s）且高电力敏感’的特定边界条件下具备性价比优势，否则因软件适配成本（ROCm/MLX 后端稳定性）和 Prefill 延迟劣势被排除出主推荐列表。

## Evidence

检索失败: no sources from any channel (all 5 failed)
