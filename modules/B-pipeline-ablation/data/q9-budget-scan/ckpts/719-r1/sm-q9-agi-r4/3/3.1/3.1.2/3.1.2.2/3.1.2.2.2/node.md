# N490: Qwen3.8-27B 在 NVFP4 量化下，单卡 (TP=4) 需加载的模型权重大小为 27B * 0.5 bytes / 4 = 3.375GB，而非 1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N175

## Claim

Qwen3.8-27B 在 NVFP4 量化下，单卡 (TP=4) 需加载的模型权重大小为 27B * 0.5 bytes / 4 = 3.375GB，而非 13.5GB；若按 FP16 计算则为 27B * 2 bytes / 4 = 13.5GB，原 claim 中 13.5GB 对应 FP16 而非 FP4

## Corrected Claim

Qwen3.8-27B 在 NVFP4 量化下，单卡 (TP=4) 需加载的模型权重大小为 27B * 0.5 bytes / 4 = 3.375GB，而非 13.5GB；若按 FP16 计算则为 27B * 2 bytes / 4 = 13.5GB，原 claim 中 13.5GB 对应 FP16 而非 FP4

## Evidence

先验知识/题面给定，逻辑校验通过：NVFP4通常指4-bit量化（0.5 bytes/param），27B*0.5/4=3.375GB；FP16为2 bytes/param，27B*2/4=13.5GB，计算无误且符合常识。
