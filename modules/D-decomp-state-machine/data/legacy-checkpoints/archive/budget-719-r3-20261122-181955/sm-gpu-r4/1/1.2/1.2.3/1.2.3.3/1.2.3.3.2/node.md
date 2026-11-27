# N466: H100 SXM5 在 FP8 精度下的实测 Decode 吞吐量（Qwen3-27B, 32K ctx, Batch=1）约为 18-22 tokens/s，

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N158

## Claim

H100 SXM5 在 FP8 精度下的实测 Decode 吞吐量（Qwen3-27B, 32K ctx, Batch=1）约为 18-22 tokens/s，计算效率为 18/20.3 ≈ 89%（基于理论峰值 20.3 tokens/s 修正，来源：HuggingFace 社区基准测试中位数）

## Corrected Claim

H100 SXM5 在 FP8 精度下，Qwen3-27B 模型在 32K 上下文、Batch=1 的 Decode 阶段实测吞吐量约为 18-22 tokens/s（基于社区基准测试估计），该阶段主要受限于内存带宽，具体效率指标需明确为带宽利用率而非计算效率。

## Evidence

[质询]数值量级与计算效率存在逻辑矛盾：H100 SXM5 在 FP8 下理论峰值算力极高，对于 27B 模型 Batch=1 的 Decode 阶段（内存带宽受限），18-22 tokens/s 的吞吐量是合理的，但声称'计算效率为 89%'（基于 20.3 tokens/s 理论峰值）混淆了'内存带宽利用率'与'计算效率'。Decode 阶段主要受限于 HBM 带宽而非计算单元，通常用'带宽利用率'衡量，且 20.3 tokens/s 作为'理论峰值'缺乏明确的物理推导依据（通常理论峰值需基于 HBM 带宽和模型大小计算，而非直接给出一个经验值）。此外，'HuggingFace 社区基准测试中位数'作为来源不够权威，且具体数值 18-22 和 20.3 缺乏可验证的公开标准基准支持。 | 逻辑校验发现'计算效率 89%'的表述在 Decode 阶段（内存受限）语境下不准确，且理论峰值 20.3 tokens/s 的来源和推导过程不透明，存在概念混淆风险。
