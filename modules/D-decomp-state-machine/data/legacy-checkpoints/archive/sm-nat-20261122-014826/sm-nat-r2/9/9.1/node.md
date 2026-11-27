# N60: LFU 频率估计的相对标准误差 (RSE) 计算：RSE = sqrt(1/n_i)，其中 n_i 为对象 i 的日均请求数。对于 Top-10% 对象（ran

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

LFU 频率估计的相对标准误差 (RSE) 计算：RSE = sqrt(1/n_i)，其中 n_i 为对象 i 的日均请求数。对于 Top-10% 对象（rank < 10000），基于 Zipf(β=0.9) 分布，其总流量占比约为 85%，平均单对象请求数 n_i ≈ (0.85 * 50,000,000) / 10,000 = 425 次/天，因此 RSE ≈ 1/sqrt(425) ≈ 4.8%，而非节点 N22 声称的 <1%。

## Corrected Claim

LFU 频率估计的相对标准误差 (RSE) 计算：RSE = sqrt(1/n_i)，其中 n_i 为对象 i 的日均请求数。对于 Top-10% 对象（rank < 10000），基于 Zipf(β=0.9) 分布，其总流量占比约为 85%，平均单对象请求数 n_i ≈ (0.85 * 50,000,000) / 10,000 = 425 次/天，因此 RSE ≈ 1/sqrt(425) ≈ 4.8%，而非节点 N22 声称的 <1%。

## Evidence

先验知识/题面给定，逻辑校验通过：RSE公式符合泊松分布近似，数值计算（sqrt(1/425)≈0.048）准确，Zipf分布流量占比假设在工程估算中合理。
