# N455: A/B 测试中固定随机种子的实施边界：Qwen3.8-27B 的随机性不仅来自 temperature 采样，还来自 KV Cache 的非确定性内存访问顺序和

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N159

## Claim

A/B 测试中固定随机种子的实施边界：Qwen3.8-27B 的随机性不仅来自 temperature 采样，还来自 KV Cache 的非确定性内存访问顺序和 Tensor Parallelism 的浮点求和顺序；固定 seed 仅保证同一硬件拓扑、同一 Batch 填充率下结果可复现，若 Batch 大小变化（max-num-seqs=8 动态填充），即使 seed 相同，输出 token 概率分布也会有 <1% 的漂移

## Corrected Claim

A/B 测试中固定随机种子的实施边界：Qwen3.8-27B 的随机性不仅来自 temperature 采样，还受 Tensor Parallelism 浮点求和顺序及底层硬件非确定性的影响；固定 seed 仅在严格控制的硬件拓扑和 Batch 配置下保证完全复现，Batch 大小变化可能导致输出概率分布出现微小漂移（具体幅度依硬件和框架实现而异，通常较小但非绝对零）。

## Evidence

[质询]具体数值'<1%'缺乏通用基准支持，且'KV Cache非确定性内存访问顺序'作为主要随机源在标准推理框架中通常被批处理调度掩盖，其影响量级可能远低于浮点求和顺序的影响，存在夸大次要因素的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

LLM inference determinism tensor parallelism floating point accumulation error
