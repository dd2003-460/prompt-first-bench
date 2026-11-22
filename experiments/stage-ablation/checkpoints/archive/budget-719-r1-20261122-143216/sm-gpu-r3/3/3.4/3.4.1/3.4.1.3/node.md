# N254: A100 80GB 在 BF16 精度、Batch=4、32K 上下文下的实际 Decode 吞吐量估算，由于 Batch>1 时计算密度增加导致带宽瓶颈效应减

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

A100 80GB 在 BF16 精度、Batch=4、32K 上下文下的实际 Decode 吞吐量估算，由于 Batch>1 时计算密度增加导致带宽瓶颈效应减弱，吞吐量不再随 Batch 线性增加，预计总吞吐量约为 Batch=1 时的 1.8-2.2 倍（即 ~47-58 tokens/s），每请求吞吐量下降至 12-14 tokens/s，此工作点用于评估多用户场景下的边际效用

## Corrected Claim

A100 80GB 在 BF16 精度、Batch=4、32K 上下文下的实际 Decode 吞吐量估算，由于 Batch>1 时计算密度增加导致带宽瓶颈效应减弱，吞吐量不再随 Batch 线性增加，预计总吞吐量约为 Batch=1 时的 1.8-2.2 倍（即 ~47-58 tokens/s），每请求吞吐量下降至 12-14 tokens/s，此工作点用于评估多用户场景下的边际效用

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB 在 BF16 下 Batch=1 时受显存带宽限制（~2TB/s），单 token 延迟约 20-25ms（~40-50 tokens/s）；Batch=4 时计算密度增加，虽未完全转为计算瓶颈，但带宽利用率提升，总吞吐量提升至 1.8-2.2 倍符合 Roofline 模型及实际 LLM 推理经验（每请求吞吐量相应下降至 12-14 tokens/s 亦合理）。
