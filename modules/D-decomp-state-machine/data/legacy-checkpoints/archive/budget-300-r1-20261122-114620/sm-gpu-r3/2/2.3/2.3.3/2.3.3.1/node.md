# N211: Jetson Orin 16GB 方案在 5 年 TCO 中，因推理吞吐仅 3-5 t/s，无法满足本地交互需求（通常需 >10 t/s），导致该方案被排除，其

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

Jetson Orin 16GB 方案在 5 年 TCO 中，因推理吞吐仅 3-5 t/s，无法满足本地交互需求（通常需 >10 t/s），导致该方案被排除，其 TCO 计算无实际意义；若强行使用，单次 100 token 生成耗时 20-33s，相比 RTX 4090 的 2s 延迟，用户等待时间增加 10-16 倍，定性上不可行。

## Corrected Claim

Jetson Orin 16GB 方案在 5 年 TCO 中，因推理吞吐仅 3-5 t/s，无法满足本地交互需求（通常需 >10 t/s），导致该方案被排除，其 TCO 计算无实际意义；若强行使用，单次 100 token 生成耗时 20-33s，相比 RTX 4090 的 2s 延迟，用户等待时间增加 10-16 倍，定性上不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：100 token / 3-5 t/s ≈ 20-33s，100 token / 50 t/s (RTX 4090典型值) ≈ 2s，倍数关系 10-16x 计算正确，且符合硬件性能常识。
