# N514: RX 7900 XT (20GB) 在 Qwen3-27B BF16 推理下，因权重 54GB 远超 20GB 显存，单卡可行性判定为‘不可行’，必须启用 IN

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N180

## Claim

RX 7900 XT (20GB) 在 Qwen3-27B BF16 推理下，因权重 54GB 远超 20GB 显存，单卡可行性判定为‘不可行’，必须启用 INT4/INT8 量化或 CPU Offload 才能启动推理。

## Corrected Claim

RX 7900 XT (20GB) 在 Qwen3-27B BF16 推理下，因权重 54GB 远超 20GB 显存，单卡可行性判定为‘不可行’，必须启用 INT4/INT8 量化或 CPU Offload 才能启动推理。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 参数量约 27B，BF16 精度下权重占用约 54GB (27 * 2 bytes)，远超 RX 7900 XT 的 20GB 显存，故单卡无法加载完整模型，必须量化或 Offload。
