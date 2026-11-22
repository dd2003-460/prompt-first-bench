# N26: 精度选择与硬件特性耦合：H100/A100 支持 FP8 Tensor Core，可实现 FP8 推理加速；RTX 4090/5090 不支持 FP8 推理，仅

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

精度选择与硬件特性耦合：H100/A100 支持 FP8 Tensor Core，可实现 FP8 推理加速；RTX 4090/5090 不支持 FP8 推理，仅支持 BF16/INT8，因此消费级卡上 FP8 量化无加速收益，仅减少显存占用。

## Corrected Claim

精度选择与硬件特性耦合：H100/A100 支持 FP8 Tensor Core，可实现 FP8 推理加速；RTX 4090 不支持 FP8 推理，仅支持 BF16/INT8，因此该卡上 FP8 量化无加速收益，仅减少显存占用；而 RTX 5090 支持 FP8 计算，可获得相应加速。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了消费级硬件（RTX 4090/5090）的修正事实、数据中心硬件（H100/A100）的理论性能对比，以及消费级硬件上的实际工程影响（速度与显存权衡）。三者维度清晰（硬件平台修正、数据中心基准、工程落地影响），无逻辑矛盾或重复，且完整覆盖了父节点关于不同硬件在 FP8 支持及收益上的所有关键论述。）
