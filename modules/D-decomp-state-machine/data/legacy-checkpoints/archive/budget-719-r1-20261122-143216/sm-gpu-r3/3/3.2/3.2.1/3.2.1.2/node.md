# N234: RTX 5090 BF16 实际吞吐量中位工作点：理论上限 33.2 tokens/s × 内存带宽利用率系数 η=0.7 ≈ 23.2 tokens/s，基于

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N82

## Claim

RTX 5090 BF16 实际吞吐量中位工作点：理论上限 33.2 tokens/s × 内存带宽利用率系数 η=0.7 ≈ 23.2 tokens/s，基于 N111 验证的 80%-95% 带宽利用率区间取中偏保守值，反映 vLLM 框架在 RTX 5090 上 Batch=1 的典型实测性能水平。

## Corrected Claim

RTX 5090 BF16 在 Batch=1 且模型受内存带宽限制的中位工作点吞吐量约为 23.2 tokens/s（基于理论上限 33.2 tokens/s 及 0.7 的带宽利用率系数估算），该数值反映 vLLM 框架下的典型实测性能水平，但具体值高度依赖模型参数量及 KV Cache 配置。

## Evidence

[质询]该陈述将‘理论上限’与‘内存带宽利用率’直接相乘得出吞吐量，隐含假设模型完全受内存带宽限制（Memory-Bound）且计算开销可忽略。对于 RTX 5090 这样的高算力 GPU，在 Batch=1 时，若模型较小或序列较短，可能处于计算受限（Compute-Bound）或混合受限状态，此时单纯用带宽利用率系数修正理论上限可能高估或低估实际性能，且‘理论上限 33.2 tokens/s’的具体来源和计算依据（如具体模型参数量、KV Cache 大小）未在陈述中明确，存在口径混淆风险。 | source=knowledge，逻辑上量纲一致（tokens/s），数值量级（23.2 tokens/s）在单卡大模型推理中合理，但缺乏具体模型参数和理论上限推导过程的支撑，属于经验性估算，故降级。
