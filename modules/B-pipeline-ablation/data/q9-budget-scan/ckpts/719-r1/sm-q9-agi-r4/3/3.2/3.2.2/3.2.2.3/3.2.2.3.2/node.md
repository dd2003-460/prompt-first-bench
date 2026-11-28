# N526: 工作点3 (INT8) 在 128K 上下文下的单请求 P99 延迟预估公式：Latency_P99 = Prefill_Time + Decode_Time 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N187, N188, N189

## Claim

工作点3 (INT8) 在 128K 上下文下的单请求 P99 延迟预估公式：Latency_P99 = Prefill_Time + Decode_Time × Seq_Len_Decode，其中 Prefill_Time ≈ 128000 / (V100 INT8 Prefill Throughput ≈ 2000 tok/s) = 64s，Decode_Time ≈ 1 / 20 tok/s = 0.05s/tok

## Corrected Claim

工作点3 (INT8) 在 128K 上下文下的单请求 P99 延迟预估公式：Latency_P99 = Prefill_Time + Decode_Time × Seq_Len_Decode，其中 Prefill_Time ≈ 128000 / (V100 INT8 Prefill Throughput ≈ 2000 tok/s) = 64s，Decode_Time ≈ 1 / 20 tok/s = 0.05s/tok

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（128000/2000=64, 1/20=0.05），公式结构符合LLM推理延迟估算的基本逻辑（Prefill+Decode），参数量级在V100 INT8场景下合理。

## Search Query

V100 INT8 inference prefill throughput benchmark Qwen27B
