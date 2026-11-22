# N128: 工作点 A（高成本/低延迟）：1× H100 80GB 运行 W4A8 Qwen3-27B (32K ctx)，显存占用 27.32 GB，剩余显存可支持大 B

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

工作点 A（高成本/低延迟）：1× H100 80GB 运行 W4A8 Qwen3-27B (32K ctx)，显存占用 27.32 GB，剩余显存可支持大 Batch 或更长上下文，单卡 TCO 约 $25k-$30k + $984/年电力，适合高并发生产环境。

## Corrected Claim

工作点 A（高成本/低延迟）：1× H100 80GB 运行 W4A8 Qwen3-27B (32K ctx)，显存占用约 27 GB，剩余显存可支持大 Batch 或更长上下文，单卡 TCO 约 $25k-$30k + $984/年电力，适合高并发生产环境。

## Evidence

[质询]显存占用数值（27.32 GB）与单卡TCO（$25k-$30k）均为具体经验参数，缺乏来源支持，且H100单卡价格随市场波动较大，该区间可能过时或不准确。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

H100 80GB Qwen3-27B W4A8 32k context batch size throughput
