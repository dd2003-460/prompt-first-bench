# N648: RTX 5090 显存带宽 1792 GB/s (GDDR7)，FP8 27B 模型单卡理论 Decode 上限 = 1792 / 27 ≈ 66.4 toke

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N199

## Claim

RTX 5090 显存带宽 1792 GB/s (GDDR7)，FP8 27B 模型单卡理论 Decode 上限 = 1792 / 27 ≈ 66.4 tokens/s；但 5090 显存仅 32 GB，无法单卡容纳 27B FP8 (27 GB) + KV Cache (32K 上下文需约 10-15 GB)，因此 2x 5090 是必要方案，每卡读取 13.5 GB，理论上限 ≈ 1792 / 13.5 ≈ 132.7 tokens/s，实测预计 90-110 tokens/s [待核验]

## Corrected Claim

若 RTX 5090 显存带宽确为 1792 GB/s 且显存为 32 GB，则 27B FP8 模型单卡理论 Decode 上限约为 66.4 tokens/s；因显存不足以容纳模型及 KV Cache，双卡方案下每卡负载 13.5 GB，理论上限约为 132.7 tokens/s，实测预计 90-110 tokens/s。

## Evidence

[质询]该陈述包含具体的硬件规格（RTX 5090 显存带宽 1792 GB/s、显存容量 32 GB）及基于这些规格的工程估算。虽然逻辑推导过程（带宽/模型大小=理论上限）在数学上自洽，但核心前提（5090 的具体参数）属于经验事实，且当前检索无可用来源支持这些具体数值，无法排除参数错误（如带宽或显存容量偏差）导致结论失效的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证 RTX 5090 具体规格及带宽数值）

## Search Query

RTX 5090 32GB VRAM 27B model FP8 KV cache memory requirement 32K context
