# N365: H200 在 N_batch > 1 时的吞吐量扩展性：当 Batch Size 增加到 N，吞吐量近似线性增长直至算力饱和。H200 FP8/INT8 Ten

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N131

## Claim

H200 在 N_batch > 1 时的吞吐量扩展性：当 Batch Size 增加到 N，吞吐量近似线性增长直至算力饱和。H200 FP8/INT8 Tensor Core 算力约为 1979 TFLOPS (INT8)。27B 模型每 token 计算量约 54 GFLOPS。理论算力上限吞吐 = 1979000 / 54 ≈ 36,648 tokens/s。因此，H200 在 N_batch=1 时为 151 tokens/s，在 N_batch=100 时可能达到 ~15,000 tokens/s，此时性价比 ($/token) 下降 100 倍。

## Corrected Claim

H200 在 N_batch > 1 时的吞吐量扩展性：当 Batch Size 增加到 N，吞吐量近似线性增长直至算力或内存带宽饱和。H200 FP8/INT8 Tensor Core 算力约为 1979 TFLOPS (INT8)。27B 模型每 token 计算量约 54 GFLOPS。理论算力上限吞吐 ≈ 36,648 tokens/s。实际性能受内存带宽和计算效率影响，N_batch=1 时通常受内存带宽限制，N_batch 增大后计算效率提升，吞吐量显著增加，但具体数值需实测，不能简单断言 N_batch=1 为 151 tokens/s。

## Evidence

[质询]数值量级与物理直觉严重不符：H200 单卡 FP8/INT8 算力约为 1979 TFLOPS，而 27B 模型每 token 计算量约为 54 GFLOPS（即 0.054 TFLOPS）。理论峰值吞吐应为 1979 / 0.054 ≈ 36,648 tokens/s。然而，陈述中声称 N_batch=1 时仅为 151 tokens/s，这比理论峰值低了 240 多倍，且远低于 H200 实际单卡推理性能（通常单卡 27B 模型在合理精度下可达数千 tokens/s）。此外，从 151 到 15,000 的 100 倍增长暗示 N_batch=1 时利用率极低（<1%），这与现代 GPU 在 batch=1 时虽受内存带宽限制但通常仍能维持较高吞吐（尤其是对于 27B 这种中等规模模型）的事实相悖。更关键的是，若 N_batch=100 时达到 15,000 tokens/s，则利用率仅为 15000/36648 ≈ 40%，这在 batch=100 时是可能的，但 batch=1 时的 151 tokens/s 数据极不合理，疑似混淆了不同模型规模、精度或硬件配置，或存在数量级错误。 | 逻辑校验失败：N_batch=1 时的 151 tokens/s 与 H200 硬件能力及 27B 模型计算量严重不匹配，违背基本性能直觉；且无外部来源支持该具体数值。

## Search Query

H200 INT8 tensor core TFLOPS throughput calculation
