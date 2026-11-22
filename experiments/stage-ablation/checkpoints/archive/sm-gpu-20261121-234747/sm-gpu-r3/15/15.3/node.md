# N522: 吞吐量指标定义为Decode阶段的平均tokens/s，需明确Prefill阶段的排除方法（如仅统计生成第一个token后的时间戳差值），并给出计算公式：Thr

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N162

## Claim

吞吐量指标定义为Decode阶段的平均tokens/s，需明确Prefill阶段的排除方法（如仅统计生成第一个token后的时间戳差值），并给出计算公式：Throughput = N_output_tokens / (T_last_token - T_first_token)

## Corrected Claim

吞吐量指标定义为Decode阶段的平均tokens/s，需明确Prefill阶段的排除方法（如仅统计生成第一个token后的时间戳差值），并给出计算公式：Throughput = N_output_tokens / (T_last_token - T_first_token)

## Evidence

先验知识/题面给定，逻辑校验通过
