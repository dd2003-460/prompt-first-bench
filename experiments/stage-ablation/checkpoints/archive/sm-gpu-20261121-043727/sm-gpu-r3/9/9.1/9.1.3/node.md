# N262: MI300X (FP8) 在 32K 上下文、Batch=1 下的理论峰值 Throughput：基于 N77 修正公式，T_decode ≈ (14GB权重 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N97

## Claim

MI300X (FP8) 在 32K 上下文、Batch=1 下的理论峰值 Throughput：基于 N77 修正公式，T_decode ≈ (14GB权重 + 33GB KV) / 5.3TB/s ≈ 9us/token，理论上限 Throughput ≈ 111,111 tok/s；考虑 ROCm 生态成熟度及 HBM3 效率，实际工作点估算为 20,000 - 35,000 tok/s [待核验：需 AMD 官方白皮书或第三方评测]

## Corrected Claim

MI300X (FP8) 在 32K 上下文、Batch=1 下，若需读取 14GB 权重和 33GB KV Cache，基于 5.3TB/s 带宽，理论最小延迟约为 8.8ms/token，理论上限吞吐量约为 113 tok/s。实际工作点受计算与内存重叠影响，通常远低于此理论上限，具体数值需实测。

## Evidence

[质询]数值量级严重违背物理直觉与硬件规格常识。MI300X 的 HBM3 带宽约为 5.3 TB/s，若每 token 需读取 47GB 数据（14GB 权重 + 33GB KV），单次延迟应为 47GB / 5.3TB/s ≈ 8.8ms (8800us)，而非 9us。9us 对应的是约 47MB 的数据量，相差三个数量级。此外，111,111 tok/s 的理论上限远超任何现有 LLM 推理硬件的极限（通常 Batch=1 时受限于内存带宽，吞吐量在数百到数千 tok/s 量级，除非模型极小或上下文极短）。 | 逻辑校验失败：单位换算错误（GB/ (GB/us) 或 GB/ (TB/s) 的量级混淆），9us 延迟对应 47GB 数据在 5.3TB/s 带宽下是不可能的（应为 ~8.8ms）。该陈述存在硬逻辑错误（量纲/量级错误）。

## Search Query

AMD MI300X FP8 LLM inference throughput tokens per second benchmark
