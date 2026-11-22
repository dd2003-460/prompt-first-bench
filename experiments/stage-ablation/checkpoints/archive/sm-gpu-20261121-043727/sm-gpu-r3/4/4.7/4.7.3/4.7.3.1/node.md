# N219: RTX 4090 上 FP8 vs BF16 的 T_decode 理论加速比上限计算：基于 N77 修正公式，T_decode_FP8 = (Weight_F

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

RTX 4090 上 FP8 vs BF16 的 T_decode 理论加速比上限计算：基于 N77 修正公式，T_decode_FP8 = (Weight_FP8 + KV_FP8) / Bandwidth。假设 KV Cache 保持 BF16 (常见配置)，Weight 减半 (54GB -> 27GB)，总读取量从 87GB 降至 60GB (假设KV 33GB不变)，理论加速比 = 87/60 = 1.45x。若 KV 也量化为 FP8，总读取量降至 47GB，加速比 = 87/47 = 1.85x。需确认主流推理引擎 (vLLM/TensorRT-LLM) 在 Ada 架构下是否支持 KV FP8 存储。

## Corrected Claim

RTX 4090 上 FP8 vs BF16 的 T_decode 理论加速比上限计算：基于 N77 修正公式，T_decode_FP8 = (Weight_FP8 + KV_FP8) / Bandwidth。假设 KV Cache 保持 BF16 (常见配置)，Weight 减半 (54GB -> 27GB)，总读取量从 87GB 降至 60GB (假设KV 33GB不变)，理论加速比 = 87/60 = 1.45x。若 KV 也量化为 FP8，总读取量降至 47GB，加速比 = 87/47 = 1.85x。需确认主流推理引擎 (vLLM/TensorRT-LLM) 在 Ada 架构下是否支持 KV FP8 存储。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（87/60=1.45, 87/47=1.85），且符合内存带宽受限场景下量化加速的理论推导逻辑。

## Search Query

vLLM RTX 4090 FP8 KV cache support Ada Lovelace
