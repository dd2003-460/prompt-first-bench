# N242: H100 80GB 在 Qwen3-27B BF16 推理下的 Prefill 延迟量化：假设输入 32K tokens，H100 的 Prefill 计算时间

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

H100 80GB 在 Qwen3-27B BF16 推理下的 Prefill 延迟量化：假设输入 32K tokens，H100 的 Prefill 计算时间约为 0.8-1.2 秒（基于 989 TFLOPS 和内存带宽瓶颈），显著优于 A100 的 2.5-3.5 秒，满足 P99 < 2s 的潜在需求（若存在）

## Corrected Claim

H100 80GB 在 Qwen3-27B BF16 推理下的 Prefill 延迟显著优于 A100，具体数值需根据实际硬件利用率和并行策略估算，通常 H100 的 Prefill 时间约为 A100 的 1/3 至 1/2。

## Evidence

[质询]数值量级存疑：H100 80GB 在 BF16 下理论峰值算力约 989 TFLOPS，但实际 Prefill 阶段受内存带宽和计算效率限制，32K tokens 的 Prefill 延迟通常远高于 0.8-1.2 秒（通常需数秒至十几秒，取决于具体实现和并行策略），且 A100 的对比数据也缺乏具体模型配置和硬件利用率假设，直接给出精确区间缺乏严谨推导。 | 先验知识/题面给定，逻辑校验通过，但具体延迟数值属于经验事实且缺乏来源支持，故降级。
