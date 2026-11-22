# N567: MI300X 在 BF16 下的 Prefill 阶段 FLOPS 峰值为 1307 TFLOPS (Dense)，但实际 MFU 在 AMD ROCm 生态下

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N236

## Claim

MI300X 在 BF16 下的 Prefill 阶段 FLOPS 峰值为 1307 TFLOPS (Dense)，但实际 MFU 在 AMD ROCm 生态下通常低于 NVIDIA (约 25%-35%)，因此 32K 输入的单请求 TTFT 理论下限为 1.77e12 / (1307e12 * 0.3) ≈ 4.5s，远超 N236 隐含的 '高并发低延迟' 假设，需结合 N237 的 Prefill 瓶颈分析修正其性价比结论。

## Corrected Claim

MI300X 在 BF16 下的 Prefill 阶段 FLOPS 峰值为 1307 TFLOPS (Dense)。鉴于 AMD ROCm 生态下实际 MFU 通常低于 NVIDIA（具体数值依负载而异，常处于较低区间），32K 输入的单请求 TTFT 理论下限显著高于理想峰值计算值，需结合具体 MFU 实测数据修正性价比结论。

## Evidence

[质询]MFU 25%-35% 的具体数值范围属于经验性工程数据，缺乏通用标准，且不同模型架构、序列长度及硬件配置下波动较大，直接作为理论下限计算的固定系数存在精度风险。 | source=knowledge，逻辑推导自洽（1.77e12 / (1307e12 * 0.3) ≈ 4.5s 计算正确），但 MFU 具体数值为经验事实，无外部来源直接支持该特定区间，故降级。

## Search Query

MI300X BF16 TFLOPS dense ROCm MFU inference latency
