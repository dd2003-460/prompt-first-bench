# N221: 并发吞吐非线性根源：vLLM中batch size从8增至16时，Attention算子的计算复杂度从O(N^2)变为O(2N)^2=4N^2，而GPU Ten

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86

## Claim

并发吞吐非线性根源：vLLM中batch size从8增至16时，Attention算子的计算复杂度从O(N^2)变为O(2N)^2=4N^2，而GPU Tensor Core利用率因内存带宽饱和（HBM3 ~900GB/s）而下降。实测显示，当batch size超过HBM带宽限制点（~12 seqs for 262k context）后，每新增1个seq的边际吞吐增益从~12 tok/s/seq降至~2 tok/s/seq。因此从8->16 seqs，总吞吐从~96 tok/s增至~110 tok/s（+14.5%），而非20%，且伴随P99延迟从500ms激增至2s，ROI在考虑延迟惩罚后<1.0x。

## Corrected Claim

vLLM中batch size增加会导致Attention计算复杂度增加及KV Cache显存占用上升。当batch size超过显存或带宽瓶颈点时，边际吞吐增益递减，且P99延迟显著增加。具体数值（如96 tok/s, 500ms->2s）高度依赖硬件配置、序列长度分布及系统负载，不能一概而论。

## Evidence

[质询]数值量级与物理直觉严重不符：1. 吞吐绝对值极低（96-110 tok/s 对于 262k context 的长序列推理而言，远低于现代 GPU 集群甚至单卡 H100/A100 在长上下文下的典型吞吐，通常应在数千至数万 tok/s 量级，除非是极老旧硬件或极端瓶颈场景，但未说明）；2. 延迟激增不合理：Batch size 从 8 到 16，若处于计算受限或带宽受限区，P99 延迟通常随 Batch 线性或亚线性增长，从 500ms 激增至 2s（4倍）暗示了严重的排队或调度异常，而非单纯的算力/带宽饱和；3. 'HBM3 ~900GB/s' 是单卡带宽，未指明是单卡还是多卡聚合，若为单卡，262k context 的 KV Cache 占用极大，8 个序列可能已接近显存上限，16 个序列可能导致 OOM 或 Swap，而非简单的带宽饱和导致吞吐微增。 | source=knowledge，但陈述中包含具体的经验参数（吞吐数值、延迟数值、带宽阈值），且这些数值与主流硬件（H100/H800/A100）在长上下文推理下的典型性能表现存在数量级偏差或逻辑矛盾（如延迟非线性激增缺乏充分解释），属于不可靠的经验数据堆砌，无法通过第一性原理验证其合理性。
