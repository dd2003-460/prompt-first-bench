# N88: 工作点 B（数据中心高容量高带宽）：H100 SXM (80GB, 2039 GB/s) 运行 Qwen3-27B BF16 (54GB) + BF16 KV 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

工作点 B（数据中心高容量高带宽）：H100 SXM (80GB, 2039 GB/s) 运行 Qwen3-27B BF16 (54GB) + BF16 KV (12.58GB)，模型在显存中总大小 66.58GB，理论 Decode 吞吐 = 2039 / 66.58 ≈ 30.6 tokens/s。此工作点展示高带宽数据中心卡在无需量化（质量无损）情况下的性能，虽然带宽极高，但模型体积大导致吞吐低于 INT4 消费卡。

## Corrected Claim

工作点 B（数据中心高容量高带宽）：H100 SXM (80GB, 2039 GB/s) 运行 Qwen3-27B BF16 (54GB) + BF16 KV (12.58GB)，模型在显存中总大小 66.58GB，理论 Decode 吞吐 = 2039 / 66.58 ≈ 30.6 tokens/s。此工作点展示高带宽数据中心卡在无需量化（质量无损）情况下的性能，虽然带宽极高，但模型体积大导致吞吐低于 INT4 消费卡。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM带宽2039GB/s与显存80GB符合规格，Qwen3-27B BF16模型大小约54GB（27B*2bytes）及KV Cache估算合理，总显存占用66.58GB未超限，Decode吞吐计算2039/66.58≈30.6 tokens/s符合算术逻辑及LLM推理带宽瓶颈原理。
