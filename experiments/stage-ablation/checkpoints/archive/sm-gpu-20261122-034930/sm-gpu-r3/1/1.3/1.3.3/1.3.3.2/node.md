# N178: 基于 N156 (TRT-LLM/A100: 1.8GB) 和 N158 (TRT-LLM/Act: 1.5GB)，在 A100 上使用 TensorRT-LL

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

基于 N156 (TRT-LLM/A100: 1.8GB) 和 N158 (TRT-LLM/Act: 1.5GB)，在 A100 上使用 TensorRT-LLM 运行 Qwen3-27B INT8 时，非权重/KV 开销的保守预留值应修正为 3.3 GB。结合 N124 中 INT8 权重+KV 约 37.7GB，总需求为 41.0GB，这证实了 N127 中关于 N10 (41.7GB) 与 N16 (37.7GB) 矛盾的解释：41.0-41.7GB 是含框架开销的真实可行阈值，37.7GB 仅为理论最小值。

## Corrected Claim

基于 N156 (TRT-LLM/A100: 1.8GB) 和 N158 (TRT-LLM/Act: 1.5GB)，在 A100 上使用 TensorRT-LLM 运行 Qwen3-27B INT8 时，非权重/KV 开销的保守预留值应修正为 3.3 GB。结合 N124 中 INT8 权重+KV 约 37.7GB，总需求为 41.0GB，这证实了 N127 中关于 N10 (41.7GB) 与 N16 (37.7GB) 矛盾的解释：41.0-41.7GB 是含框架开销的真实可行阈值，37.7GB 仅为理论最小值。

## Evidence

先验知识/题面给定，逻辑校验通过：1.8GB + 1.5GB = 3.3GB，37.7GB + 3.3GB = 41.0GB，数值计算自洽，且符合TensorRT-LLM框架开销的工程常识。
