# N59: 消费级 GPU W4 单卡可行性判定：RTX 4090 (24GB) 在 W4 精度下（需求 28.2GB）不满足单卡需求（24GB < 28.2GB），即使 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10, N11, N12

## Claim

消费级 GPU W4 单卡可行性判定：RTX 4090 (24GB) 在 W4 精度下（需求 28.2GB）不满足单卡需求（24GB < 28.2GB），即使 KV Cache 量化至 INT8（需求 13.5+5.35+4=22.85GB），24GB 勉强可行但无余量，存在 OOM 风险；RTX 4080 (16GB) 和 RTX 3060 (12GB) 在任何精度下均不满足单卡需求。

## Corrected Claim

消费级 GPU W4 单卡可行性判定：RTX 4090 (24GB) 在 W4 精度下（需求 28.2GB）不满足单卡需求（24GB < 28.2GB），即使 KV Cache 量化至 INT8（需求 13.5+5.35+4=22.85GB），24GB 勉强可行但无余量，存在 OOM 风险；RTX 4080 (16GB) 和 RTX 3060 (12GB) 在任何精度下均不满足单卡需求。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090显存24GB小于W4需求28.2GB，且KV Cache量化后总需求22.85GB接近24GB上限，OOM风险判断合理；RTX 4080/3060显存均小于最低需求，逻辑自洽。
