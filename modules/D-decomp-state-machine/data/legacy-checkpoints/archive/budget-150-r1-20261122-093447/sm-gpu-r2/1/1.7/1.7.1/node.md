# N64: NVFP4/W4 精度下 Qwen3-27B 总内存需求为 20.7GB，该数值表明单卡 24GB 消费级 GPU（如 RTX 4090）在理论内存容量上可行，

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

NVFP4/W4 精度下 Qwen3-27B 总内存需求为 20.7GB，该数值表明单卡 24GB 消费级 GPU（如 RTX 4090）在理论内存容量上可行，但需扣除 1.5GB 运行时开销后剩余 22.5GB 需覆盖 20.7GB 负载，安全边际仅 1.8GB

## Corrected Claim

NVFP4/W4 精度下 Qwen3-27B 总内存需求为 20.7GB，该数值表明单卡 24GB 消费级 GPU（如 RTX 4090）在理论内存容量上可行，但需扣除 1.5GB 运行时开销后剩余 22.5GB 需覆盖 20.7GB 负载，安全边际仅 1.8GB

## Evidence

先验知识/题面给定，逻辑校验通过：24GB - 1.5GB = 22.5GB，22.5GB - 20.7GB = 1.8GB，数值计算自洽且符合GPU显存管理常识。
