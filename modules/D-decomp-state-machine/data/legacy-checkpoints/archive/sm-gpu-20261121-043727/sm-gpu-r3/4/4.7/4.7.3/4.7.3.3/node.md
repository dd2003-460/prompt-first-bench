# N221: H100 SXM 上 FP8 vs BF16 的 T_decode 理论加速比计算：H100 HBM3 带宽 3.35 TB/s。BF16 Weight 54G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

H100 SXM 上 FP8 vs BF16 的 T_decode 理论加速比计算：H100 HBM3 带宽 3.35 TB/s。BF16 Weight 54GB + KV 33GB = 87GB，T_decode_BF16 ≈ 26us/token。FP8 Weight 27GB + KV 33GB (假设KV BF16) = 60GB，T_decode_FP8 ≈ 18us/token。理论加速比 = 87/60 = 1.45x。若 KV 也 FP8，加速比可达 1.85x。H100 支持原生 FP8 KV Cache，因此 1.85x 是更可能的上限。

## Corrected Claim

H100 SXM 上 FP8 vs BF16 的 T_decode 理论加速比计算：H100 HBM3 带宽 3.35 TB/s。BF16 Weight 54GB + KV 33GB = 87GB，T_decode_BF16 ≈ 26us/token。FP8 Weight 27GB + KV 33GB (假设KV BF16) = 60GB，T_decode_FP8 ≈ 18us/token。理论加速比 = 87/60 = 1.45x。若 KV 也 FP8，加速比可达 1.85x。H100 支持原生 FP8 KV Cache，因此 1.85x 是更可能的上限。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM HBM3带宽3.35TB/s符合硬件规格；带宽受限解码延迟与数据量成正比，87/60=1.45及(54+33)/(27+16.5)=1.85的计算逻辑自洽且量级合理。

## Search Query

H100 FP8 inference latency benchmark vs BF16
