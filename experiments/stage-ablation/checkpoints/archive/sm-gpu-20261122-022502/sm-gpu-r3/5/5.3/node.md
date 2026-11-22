# N27: 极致性价比工作点（量化+消费级）：采用 INT8 或 W4A8 量化后，1×RTX 4090 可承载 27B 模型并达到约 35-40 tokens/s，TCO

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N5

## Claim

极致性价比工作点（量化+消费级）：采用 INT8 或 W4A8 量化后，1×RTX 4090 可承载 27B 模型并达到约 35-40 tokens/s，TCO/Throughput 降至约 $0.008-$0.010/token，但需验证量化后在复杂推理任务上的准确率损失是否 < 2% [待核验]，适用于对精度敏感但预算极低的边缘计算场景。

## Corrected Claim

采用 INT8 或 W4A8 量化后，1×RTX 4090 在显存允许的情况下（可能需要 offload 或特定优化）可承载 27B 模型，吞吐量约为 35-40 tokens/s，但 TCO/Throughput 的具体数值需根据硬件折旧周期和电力成本精确计算，且需验证量化后在复杂推理任务上的准确率损失是否 < 2%。

## Evidence

[质询]数值量级与成本估算存在显著偏差：RTX 4090 的 TCO（总拥有成本）通常按硬件折旧+电力计算，若按 $1600 硬件成本分摊，$0.008-$0.010/token 的成本仅对应极短的摊销周期或极高的吞吐量假设；此外，27B 模型在 INT8 下占用约 27GB 显存，加上 KV Cache 和激活值，极易超出 4090 的 24GB 显存限制，导致无法运行或需大量 offload，从而严重降低吞吐量，35-40 tokens/s 的估计可能过于乐观。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，且具体硬件性能与成本数据属于经验事实，无法从第一性原理严格推导，故降级。

## Search Query

Qwen3 27B INT8 W4A8 quantization accuracy loss inference speed RTX 4090
