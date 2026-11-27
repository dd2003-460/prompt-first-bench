# N310: H100 80GB 运行 FP8 Qwen3-27B (128K) 的实际 Decode 吞吐受限于 FP8 权重读取带宽 (2039 GB/s) 与 KV C

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N110, N111, N112

## Claim

H100 80GB 运行 FP8 Qwen3-27B (128K) 的实际 Decode 吞吐受限于 FP8 权重读取带宽 (2039 GB/s) 与 KV Cache 读取带宽的耦合，理论上限 ≈ 2039 / 27 ≈ 75.5 tokens/s，但实测因 PCIe/NVLink 通信开销及内存控制器效率，通常降至 60-70 tokens/s，比 4090 方案 (18.7 tokens/s) 高 3-4 倍。

## Corrected Claim

H100 80GB 运行 FP8 Qwen3-27B (128K) 的 Decode 吞吐主要受限于 KV Cache 读取带宽。由于 128K 上下文导致 KV Cache 体积巨大，实际吞吐远低于仅基于权重带宽估算的 75.5 tokens/s，具体数值取决于 KV Cache 量化策略及硬件带宽利用率，通常显著低于短上下文场景。

## Evidence

[质询]理论上限计算存在逻辑漏洞：Decode 阶段的瓶颈通常是 KV Cache 的读取带宽（随序列长度线性增长），而非仅权重读取。对于 128K 上下文，KV Cache 的读取量远超权重读取量，因此将吞吐上限简单估算为 2039/27 (仅基于权重) 是错误的，实际理论上限会远低于 75.5 tokens/s。此外，'60-70 tokens/s' 的实测数据缺乏来源支持，且对于 128K 长上下文，该吞吐量在物理上极难达到（受限于 HBM 带宽和 KV 大小）。 | 逻辑校验失败：Decode 吞吐受限于 KV Cache 读取带宽，128K 上下文下 KV 读取量巨大，仅用权重带宽计算上限（2039/27）忽略了主要瓶颈，导致理论值高估；且无外部来源支持具体实测数值。

## Search Query

H100 FP8 Qwen3-27B decode throughput benchmark
