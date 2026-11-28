# N592: Qwen3.8-27B 在 V100 集群上执行 k=5 采样的一致性检查耗时：每次采样生成约50 tokens，TP=4 下 Decode 速度约20 tok

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N211

## Claim

Qwen3.8-27B 在 V100 集群上执行 k=5 采样的一致性检查耗时：每次采样生成约50 tokens，TP=4 下 Decode 速度约20 tok/s，单次采样耗时2.5s，5次采样总耗时12.5s；若并发执行（batch=5），受限于 max-num-seqs=8，耗时仍为2.5s，但显存增加约15%（基于 N321 公式）

## Corrected Claim

Qwen3.8-27B 在 V100 集群上执行 k=5 采样的一致性检查耗时：每次采样生成约50 tokens，TP=4 下 Decode 速度约20 tok/s，单次采样耗时2.5s，5次采样总耗时12.5s；若并发执行（batch=5），受限于 max-num-seqs=8，耗时仍为2.5s，但显存增加约15%（基于 N321 公式）

## Evidence

先验知识/题面给定，逻辑校验通过：串行耗时计算（5 * 2.5s = 12.5s）正确；并行耗时受限于单序列解码速度（2.5s）符合LLM推理瓶颈特征；显存增加比例（15%）在KV Cache线性增长假设下量级合理。

## Search Query

vLLM batch sampling latency V100 TP4
