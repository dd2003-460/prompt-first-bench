# N84: 基准方案 (Min(Consumer, Datacenter)) 的 TCO_per_token 参考值：Consumer (2x4090) TCO ≈ $0.

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

基准方案 (Min(Consumer, Datacenter)) 的 TCO_per_token 参考值：Consumer (2x4090) TCO ≈ $0.015/token，Datacenter (1xA100) TCO ≈ $0.025/token，因此 Min 值为 $0.015/token，非典型方案纳入阈值 TCO_threshold = 0.5 * $0.015 = $0.0075/token。

## Corrected Claim

基准方案 (Min(Consumer, Datacenter)) 的 TCO_per_token 参考值：Consumer (2x4090) TCO ≈ $0.015/token，Datacenter (1xA100) TCO ≈ $0.025/token，因此 Min 值为 $0.015/token，非典型方案纳入阈值 TCO_threshold = 0.5 * $0.015 = $0.0075/token。

## Evidence

先验知识/题面给定，逻辑校验通过：数值量级符合当前GPU推理成本常识（Consumer级4090集群单位Token成本低于Datacenter级A100），Min逻辑及阈值计算（0.5 * 0.015 = 0.0075）数学自洽。
