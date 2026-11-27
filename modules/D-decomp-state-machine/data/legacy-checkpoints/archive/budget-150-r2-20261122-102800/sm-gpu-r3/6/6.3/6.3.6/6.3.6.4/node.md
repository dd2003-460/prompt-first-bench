# N363: RX 7900 XTX 的 INT8 吞吐量具体数值：在 ROCm 环境下，其 INT8 峰值算力约为 395 TOPS，而 H100 的 INT8 峰值算力约

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N142

## Claim

RX 7900 XTX 的 INT8 吞吐量具体数值：在 ROCm 环境下，其 INT8 峰值算力约为 395 TOPS，而 H100 的 INT8 峰值算力约为 989 TOPS，实际 LLM 推理中由于带宽瓶颈，RX 7900 XTX 的 tokens/s 通常仅为 H100 的 20-30%，这一差距在计算其性价比时必须作为关键权重因子。

## Corrected Claim

RX 7900 XTX 的 INT8 峰值算力约为 395 TOPS，H100 约为 989 TOPS。在实际 LLM 推理中，受带宽瓶颈影响，RX 7900 XTX 的吞吐量通常显著低于 H100（具体比例视模型和场景而定，常处于较低水平），这一性能差距是评估其性价比的关键因素。

## Evidence

[质询]具体数值（395 TOPS, 989 TOPS, 20-30%）属于经验事实，缺乏来源支持，且不同模型/精度下实际推理速度比波动较大，固定为20-30%可能过于绝对。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RX 7900 XTX INT8 TOPS vs H100 LLM inference tokens per second
