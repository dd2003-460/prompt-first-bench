# N357: RTT 典型值范围：同区域（如 us-east-1 内）RTT ≈ 1-5ms；跨区域（如 us-east-1 到 us-west-2）RTT ≈ 20-50m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N131, N132, N133

## Claim

RTT 典型值范围：同区域（如 us-east-1 内）RTT ≈ 1-5ms；跨区域（如 us-east-1 到 us-west-2）RTT ≈ 20-50ms；跨洲（如 us-east-1 到 eu-west-1）RTT ≈ 60-100ms；题目假设 RTT=50ms 对应跨区域场景

## Corrected Claim

RTT 典型值范围：同区域（如 us-east-1 内）RTT ≈ 1-5ms；跨区域（如 us-east-1 到 us-west-2）RTT ≈ 20-50ms；跨洲（如 us-east-1 到 eu-west-1）RTT ≈ 60-100ms；题目假设 RTT=50ms 对应跨区域场景

## Evidence

先验知识/题面给定，逻辑校验通过：同区域1-5ms、跨区域20-50ms、跨洲60-100ms符合网络物理延迟常识，RTT=50ms对应跨区域场景逻辑自洽

## Search Query

AWS S3 RTT latency cross-region 50ms
