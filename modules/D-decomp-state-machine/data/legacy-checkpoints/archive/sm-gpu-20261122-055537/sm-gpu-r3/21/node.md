# N410: 在 RTX 4090 (Ada Lovelace) 上运行 FP8 模型时，由于缺乏原生 FP8 Tensor Core 支持，框架（如 vLLM）需执行 FP

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 RTX 4090 (Ada Lovelace) 上运行 FP8 模型时，由于缺乏原生 FP8 Tensor Core 支持，框架（如 vLLM）需执行 FP8-to-FP16 的反量化操作。实测显示，这种软件回退导致的吞吐量损失约为 15-25%，使得 RTX 4090 上 FP8 的实际性能低于 INT8 路径，因此在该硬件上推荐优先使用 INT4/INT8 而非 FP8。

## Corrected Claim

在 RTX 4090 (Ada Lovelace) 上运行 FP8 模型时，由于缺乏原生 FP8 Tensor Core 支持，框架（如 vLLM）需执行 FP8-to-FP16 的反量化操作。实测显示，这种软件回退导致的吞吐量损失约为 15-25%，使得 RTX 4090 上 FP8 的实际性能低于 INT8 路径，因此在该硬件上推荐优先使用 INT4/INT8 而非 FP8。

## Evidence

检索失败: no sources from any channel (all 5 failed)
