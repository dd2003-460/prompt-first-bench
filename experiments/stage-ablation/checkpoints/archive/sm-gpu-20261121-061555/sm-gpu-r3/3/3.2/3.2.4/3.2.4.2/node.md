# N243: 支持 INT8 张量核心的 GPU（如 RTX 4090/A100）在 W4A8 模式下推理 Qwen3-27B 的实测吞吐量（tokens/s）与 W4A16

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N82

## Claim

支持 INT8 张量核心的 GPU（如 RTX 4090/A100）在 W4A8 模式下推理 Qwen3-27B 的实测吞吐量（tokens/s）与 W4A16 模式的实测吞吐量对比，验证 1.5-2 倍提升断言是否成立，需区分内存带宽瓶颈与计算瓶颈场景。

## Corrected Claim

支持 INT8 张量核心的 GPU 在 W4A8 模式下推理 Qwen3-27B 的吞吐量通常优于 W4A16 模式，具体提升幅度取决于内存带宽与计算瓶颈的平衡，需实测数据验证。

## Evidence

[质询]该陈述涉及特定硬件（RTX 4090/A100）在特定模型（Qwen3-27B）和特定量化模式（W4A8 vs W4A16）下的实测吞吐量对比，属于具体的经验事实（硬件性能基准）。由于缺乏实测数据支持，无法验证“1.5-2倍提升”这一具体数值断言是否成立，且不同场景（内存带宽瓶颈 vs 计算瓶颈）下提升幅度差异巨大，单一数值断言可能以偏概全。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。W4A8相比W4A16通常能减少激活值内存占用并可能利用INT8 Tensor Core加速，理论上在内存带宽受限或计算密集场景下应有性能提升，但具体倍数需实测数据佐证，故降级为定性表述。

## Search Query

RTX 4090 INT8 tensor core throughput vs W4A16 LLM inference Qwen27B benchmark tokens per second
