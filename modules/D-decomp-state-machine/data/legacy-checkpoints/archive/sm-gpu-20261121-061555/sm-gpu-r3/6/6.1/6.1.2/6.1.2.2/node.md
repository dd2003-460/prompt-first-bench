# N310: 悲观情景排名：假设 RTX 4090 吞吐量为理论峰值的 70%（vLLM 未优化/量化开销），A100 吞吐量为理论峰值的 85%（TensorRT-LLM 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

悲观情景排名：假设 RTX 4090 吞吐量为理论峰值的 70%（vLLM 未优化/量化开销），A100 吞吐量为理论峰值的 85%（TensorRT-LLM 优化良好），计算 TCO_5yr 并排序；此情景下 A100 的单位 Token 成本可能低于 4090，导致长期持有场景推荐反转。

## Corrected Claim

悲观情景排名：假设 RTX 4090 吞吐量为理论峰值的 70%（vLLM 未优化/量化开销），A100 吞吐量为理论峰值的 85%（TensorRT-LLM 优化良好），计算 TCO_5yr 并排序；此情景下 A100 的单位 Token 成本可能低于 4090，导致长期持有场景推荐反转。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 虽单卡算力高，但受限于 24GB 显存，在长上下文或大模型场景下需多卡或频繁换入换出，且消费级卡缺乏 ECC 和数据中心级稳定性，导致有效吞吐和运维成本劣势；A100 80GB 显存大、稳定性高，在特定优化下单位 Token 成本确实可能更低，逻辑自洽。
