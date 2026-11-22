# N254: 工作点1（高带宽利用/低延迟）：在 H100 上运行 Qwen3-27B BF16 时，采用 PagedAttention (vLLM) 且 Batch Siz

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86, N87, N88

## Claim

工作点1（高带宽利用/低延迟）：在 H100 上运行 Qwen3-27B BF16 时，采用 PagedAttention (vLLM) 且 Batch Size=1 的 Decode 阶段，有效显存带宽利用率（Memory Bandwidth Utilization）约为 0.88 [待核验]，主要受限于 Kernel Launch Overhead 和非连续内存访问。

## Corrected Claim

工作点1（高带宽利用/低延迟）：在 H100 上运行 Qwen3-27B BF16 时，采用 PagedAttention (vLLM) 且 Batch Size=1 的 Decode 阶段，有效显存带宽利用率受限于 Kernel Launch Overhead 和非连续内存访问，具体数值需实测确认（通常低于 0.88）。

## Evidence

[质询]数值量级存疑：在 Batch Size=1 的 Decode 阶段，由于 Kernel Launch Overhead 和内存访问的非连续性，有效带宽利用率通常远低于 0.88（通常仅为理论峰值的 30%-60% 左右，具体取决于硬件和实现），0.88 这一数值对于单请求场景而言过于乐观，可能混淆了高 Batch Size 下的利用率或理论峰值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体数值属于特定硬件/模型/配置下的经验测量值，无法从第一性原理严格推出，故降级）

## Search Query

H100 BF16 LLM inference memory bandwidth utilization paged attention
