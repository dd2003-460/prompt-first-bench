# N284: A100 40GB SXM4 的 400W TDP 中，HBM 内存功耗约占 30-40% (120-160W)，GPU 核心功耗约占 60-70% (240-

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N108

## Claim

A100 40GB SXM4 的 400W TDP 中，HBM 内存功耗约占 30-40% (120-160W)，GPU 核心功耗约占 60-70% (240-280W)；在 LLM 推理的 Decode 阶段（内存带宽受限），HBM 功耗占比更高，导致实际功耗更接近 400W 上限；而在 Prefill 阶段（计算受限），GPU 核心功耗主导，实际功耗可能降至 350W 左右，平均功耗约为 375W。

## Corrected Claim

A100 40GB SXM4 的 400W TDP 中，HBM 内存功耗占比显著高于传统 GDDR 显存，在 LLM 推理的 Decode 阶段（内存带宽受限）HBM 功耗占比更高，导致实际功耗更接近 400W 上限；而在 Prefill 阶段（计算受限），GPU 核心功耗主导，实际功耗相对较低。

## Evidence

[质询]HBM 功耗占比 30-40% 及具体瓦特数值（120-160W）属于高度依赖具体负载、频率和电压的经验数据，缺乏公开权威基准测试的直接支持，且不同工作负载下波动较大，该具体数值区间可能过于精确或基于特定未公开测试。 | 先验知识/题面给定，逻辑校验通过：HBM 功耗确实显著高于 GDDR，且 Decode 阶段内存带宽受限导致 HBM 功耗占比上升符合物理直觉；但具体数值缺乏外部来源直接支持，且属于经验事实，故降级。

## Search Query

A100 SXM4 HBM power consumption breakdown LLM inference
