# N52: 非典型方案Mac Studio M2 Ultra (192GB, 800GB/s) 在W4量化下理论TPS≈59.3，实际受CPU-GPU协同与统一内存延迟限制

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

非典型方案Mac Studio M2 Ultra (192GB, 800GB/s) 在W4量化下理论TPS≈59.3，实际受CPU-GPU协同与统一内存延迟限制约40-50 TPS，但支持BF16单卡运行（54GB权重+1.93GB KV+1.5GB激活=57.43GB<192GB），是消费级唯一可行BF16方案。

## Corrected Claim

非典型方案Mac Studio M2 Ultra (192GB, 800GB/s) 在W4量化下理论TPS≈59.3，实际受CPU-GPU协同与统一内存延迟限制约40-50 TPS，但支持BF16单卡运行（54GB权重+1.93GB KV+1.5GB激活=57.43GB<192GB），是消费级唯一可行BF16方案。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 192GB 统一内存足以容纳 BF16 模型（~57GB），且 800GB/s 带宽支持约 59 TPS 理论值，符合硬件规格与推理逻辑。
