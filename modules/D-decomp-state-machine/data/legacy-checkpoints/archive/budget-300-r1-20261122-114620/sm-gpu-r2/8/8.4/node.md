# N130: 精度敏感任务（代码/数学）下的硬件约束：若坚持 BF16 精度，Qwen3-27B (54GB) + 32K KV Cache (1.6GB) + 框架开销 (

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

精度敏感任务（代码/数学）下的硬件约束：若坚持 BF16 精度，Qwen3-27B (54GB) + 32K KV Cache (1.6GB) + 框架开销 (10GB) ≈ 65.6GB，单卡 RTX 4090 (24GB) 不可行，必须选择 A100 80GB ($15000) 或双卡 RTX 4090 (48GB, 需 offload 部分权重至 CPU 或降低上下文至 8K) 方案，此时双卡方案因 PCIe 通信瓶颈导致吞吐下降约 15-20%。

## Corrected Claim

精度敏感任务（代码/数学）下的硬件约束：若坚持 BF16 精度，Qwen3-27B (54GB) + 32K KV Cache (1.6GB) + 框架开销 (10GB) ≈ 65.6GB，单卡 RTX 4090 (24GB) 不可行，必须选择 A100 80GB ($15000) 或双卡 RTX 4090 (48GB, 需 offload 部分权重至 CPU 或降低上下文至 8K) 方案，此时双卡方案因 PCIe 通信瓶颈导致吞吐显著下降（具体比例依 offload 策略和硬件配置而定，通常可达 15-20% 或更高）。

## Evidence

[质询]双卡 RTX 4090 总显存为 48GB，而模型+KV Cache+开销总计约 65.6GB，即使 offload 部分权重至 CPU，剩余需驻留 GPU 的显存需求仍远超 48GB，且 15-20% 的吞吐下降数值缺乏通用基准支持，属于特定配置下的经验估计，易受 offload 策略和 PCIe 版本影响。 | 先验知识/题面给定，逻辑校验通过：单卡 24GB < 65.6GB 不可行成立；双卡 48GB < 65.6GB 需 offload 成立；但具体吞吐下降比例 15-20% 为经验值，无来源支持，故降级。
