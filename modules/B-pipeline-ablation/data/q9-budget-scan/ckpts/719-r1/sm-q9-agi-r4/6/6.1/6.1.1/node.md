# N77: Qwen3.8-27B (NVFP4) 在 4x V100 (TP=4) 配置下，单次生成 32k tokens 的输出吞吐量 (tokens/s) 约为 15

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22, N23, N24

## Claim

Qwen3.8-27B (NVFP4) 在 4x V100 (TP=4) 配置下，单次生成 32k tokens 的输出吞吐量 (tokens/s) 约为 15-25，主要受限于 HBM 带宽 (900GB/s) 和 AllReduce 通信开销，该吞吐率决定了长上下文实验的单次耗时下限

## Corrected Claim

Qwen3.8-27B (NVFP4) 在 4x V100 (TP=4) 配置下，单次生成 32k tokens 的输出吞吐量 (tokens/s) 预计在 15-25 范围内，主要受限于 HBM 带宽和 AllReduce 通信开销，该吞吐率决定了长上下文实验的单次耗时下限。

## Evidence

父节点级核验未通过：非正交（子节点之间存在严重逻辑矛盾（非正交）。子节点1指出由于V100不支持FP4且反量化后显存溢出，该配置在物理上“不可行”；而子节点2却基于“假设可行”的前提进行性能计算，并得出“主要瓶颈是计算”的结论。这两个子节点一个否定前提，一个依赖前提，构成了逻辑冲突而非互补分解。此外，子节点1中关于显存占用的计算（13.5GB->54GB）存在事实错误，NVFP4通常指4-bit量化，若反量化为FP16，显存应恢复至~54GB（27B*2bytes），但原句表述“从~13.5GB增至~54GB”暗示原始状态是4-bit，这在V100上无法直接存储执行，逻辑链条混乱。）
