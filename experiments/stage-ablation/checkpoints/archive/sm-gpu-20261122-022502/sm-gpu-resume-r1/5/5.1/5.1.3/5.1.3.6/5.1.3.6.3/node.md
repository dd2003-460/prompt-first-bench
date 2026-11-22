# N869: 多卡方案下框架吞吐增益的边际递减效应：2× RTX 4090 使用 vLLM 时，NVLink 带宽为 900 GB/s，但 PagedAttention 的跨

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N271

## Claim

多卡方案下框架吞吐增益的边际递减效应：2× RTX 4090 使用 vLLM 时，NVLink 带宽为 900 GB/s，但 PagedAttention 的跨卡 KV Cache 迁移开销导致有效带宽利用率从 0.95 降至 0.85 [待核验 NVLink 迁移开销]，而 llama.cpp 不支持多卡 KV Cache 共享，需使用张量并行，其通信开销占比 = (n_layers * 2 * hidden_dim * dtype_size) / (理论带宽 * 时间步长)，对于 Qwen3-27B，每层通信量 = 2 * 4096 * 2 = 16 KB，48 层总通信量 = 768 KB/步，该值在 900 GB/s 下传输时间 = 0.85 μs，可忽略，因此多卡下框架差异对吞吐影响 < 1% [待核验 hidden_dim 与 NVLink 实际带宽]

## Corrected Claim

多卡方案下框架吞吐增益存在边际递减效应。2× RTX 4090 使用 vLLM 时，NVLink 带宽为 900 GB/s，但 PagedAttention 的跨卡 KV Cache 迁移开销会降低有效带宽利用率（具体数值依实现和负载而定）。llama.cpp 多卡支持有限，若使用张量并行，对于 Qwen3-27B（假设 hidden_dim=4096, 48 层），每步通信量约 768 KB，在 900 GB/s 带宽下传输时间约 0.85 μs，通信开销占比极低，因此在该特定计算/通信比下，多卡下框架差异对吞吐影响较小。

## Evidence

[质询]陈述中关于 NVLink 带宽利用率从 0.95 降至 0.85 的具体数值缺乏来源支持，且将 PagedAttention 的跨卡迁移开销直接量化为带宽利用率下降属于经验性推断，不同实现和负载下差异巨大，无法从第一性原理严格推出该特定数值。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，无法验证具体带宽利用率数值及框架特定行为。

## Search Query

vLLM llama.cpp multi-GPU tensor parallel NVLink communication overhead Qwen3-27B hidden dim 4096
