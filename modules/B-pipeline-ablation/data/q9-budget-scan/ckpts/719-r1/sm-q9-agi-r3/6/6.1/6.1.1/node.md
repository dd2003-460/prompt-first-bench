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

父节点级核验未通过：非正交, 不完备（子节点1指出该配置在V100上物理不可行（显存溢出），这与父节点描述的'单次生成...吞吐量约为15-25'这一既定事实直接矛盾，破坏了逻辑一致性。此外，父节点明确提到瓶颈包含HBM带宽（900GB/s），但子节点2将瓶颈归结为计算（Compute-bound），且未涵盖HBM带宽对长上下文KV Cache读取的影响，导致覆盖不全。）
