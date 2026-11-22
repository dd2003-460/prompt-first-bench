# N461: H100 SXM5 在 BF16 精度下的实际 Prefill 效率系数：由于 Tensor Core 利用率及内存访问模式，实测 Prefill 吞吐量通常为

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N156

## Claim

H100 SXM5 在 BF16 精度下的实际 Prefill 效率系数：由于 Tensor Core 利用率及内存访问模式，实测 Prefill 吞吐量通常为理论峰值的 70%-85%，即 281.5 * 0.75 ≈ 211.1 tokens/s，需与 A100 80GB 的实测值（约 50-60 tokens/s）对比以验证 3.18 倍加速比的真实性。

## Corrected Claim

H100 SXM5 在 BF16 精度下的理论峰值算力约为 A100 的 3-4 倍。在实际 Prefill 阶段，受 Tensor Core 利用率和内存带宽限制，实测吞吐量通常为理论峰值的 70%-85%。具体吞吐量数值（如 211.1 tokens/s 或 A100 的 50-60 tokens/s）取决于模型规模、序列长度及 Batch Size 等具体配置，需结合特定基准测试数据验证加速比。

## Evidence

[质询]该陈述包含具体的经验性参数（70%-85%效率系数、211.1 tokens/s、A100 50-60 tokens/s），这些数值高度依赖于具体的模型架构、序列长度、Batch Size 及硬件配置，并非固定不变的物理常数或第一性原理可推导值。在缺乏具体测试场景（如特定 LLM 模型、输入长度）的情况下，直接断言具体的吞吐量数值和加速比缺乏严谨性，且不同基准测试（如 MLPerf 或特定框架实测）结果可能存在显著差异。 | 经验事实，逻辑自洽但缺来源支持。H100 相比 A100 在 BF16 下约有 3-4 倍的理论算力提升，70%-85% 的利用率假设在工程实践中是合理的，但具体吞吐量数值（211.1 vs 50-60）属于特定场景下的经验数据，无来源直接覆盖，故降级。

## Search Query

H100 SXM5 Qwen3-27B prefill throughput benchmark real world
