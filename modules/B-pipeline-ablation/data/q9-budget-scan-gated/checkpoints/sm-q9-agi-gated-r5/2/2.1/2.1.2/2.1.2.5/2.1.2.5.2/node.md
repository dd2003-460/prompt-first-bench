# N133: 重新计算 500 tokens 生成的总延迟：Prefill 120ms + Decode 500 * T_avg。基于 N74 修正后的 T_avg，当 α=

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N62

## Claim

重新计算 500 tokens 生成的总延迟：Prefill 120ms + Decode 500 * T_avg。基于 N74 修正后的 T_avg，当 α=0.7 时，Decode 时间 = 500 * 4.84ms ≈ 2420ms，总延迟 ≈ 2540ms (2.54s)；当 α=0.5 时，T_avg = 15 / (1 + 1.5) = 6ms，Decode 时间 = 3000ms，总延迟 ≈ 3120ms (3.12s)。这表明 N62 原估算的 8.2s 存在数量级高估，可能未正确应用投机解码加速或包含了错误的批处理等待时间。

## Corrected Claim

重新计算 500 tokens 生成的总延迟：Prefill 120ms + Decode 500 * T_avg。基于 N74 修正后的 T_avg，当 α=0.7 时，Decode 时间 = 500 * 4.84ms ≈ 2420ms，总延迟 ≈ 2540ms (2.54s)；当 α=0.5 时，T_avg = 15 / (1 + 1.5) = 6ms，Decode 时间 = 3000ms，总延迟 ≈ 3120ms (3.12s)。这表明 N62 原估算的 8.2s 存在数量级高估，可能未正确应用投机解码加速或包含了错误的批处理等待时间。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（500*4.84=2420, 2420+120=2540; 500*6=3000, 3000+120=3120），且基于给定的T_avg参数推导符合逻辑。

## Search Query

recalculate total generation latency with corrected speculative decoding speedup
