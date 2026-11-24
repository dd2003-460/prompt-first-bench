# N453: 恢复带宽瓶颈分析：T_transfer = V_incr / Effective_Throughput。题目假设 1.25GB/s (10Gbps)。需考虑云存

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152

## Claim

恢复带宽瓶颈分析：T_transfer = V_incr / Effective_Throughput。题目假设 1.25GB/s (10Gbps)。需考虑云存储下载的并发限制和网络拥塞。若使用S3标准存储，单流下载速度通常限制在 100-500MB/s，除非使用多段并发（Multi-part Get）。假设并发度为10，单流100MB/s，则 Effective_Throughput = 1GB/s。若 V_incr=5TB，T_transfer = 5TB / 1GB/s = 5000s ≈ 1.39h，与题目1.1h相近，但需确认并发策略成本（额外API请求费）。

## Corrected Claim

恢复带宽瓶颈分析：T_transfer = V_incr / Effective_Throughput。题目假设 1.25GB/s (10Gbps)。需考虑云存储下载的并发限制和网络拥塞。若使用S3标准存储，单流下载速度通常限制在 100-500MB/s，除非使用多段并发（Multi-part Get）。假设并发度为10，单流100MB/s，则 Effective_Throughput = 1GB/s。若 V_incr=5TB，T_transfer = 5TB / 1GB/s = 5000s ≈ 1.39h，与题目1.1h相近，但需确认并发策略成本（额外API请求费）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（5000s≈1.39h），工程参数（S3单流限速、并发策略）符合常识，虽与题目1.1h有偏差但已做合理性解释。

## Search Query

S3 download throughput single stream vs concurrent multipart get limit
