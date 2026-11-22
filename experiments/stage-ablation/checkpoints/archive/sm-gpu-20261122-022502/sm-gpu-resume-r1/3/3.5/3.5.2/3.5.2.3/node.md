# N235: AMD 消费级卡 (RX 7900 XTX) 在 LLM 推理中的排除理由：尽管 24GB 显存与 RTX 4090 相同，但 ROCm 对 LLM 推理的优化

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85

## Claim

AMD 消费级卡 (RX 7900 XTX) 在 LLM 推理中的排除理由：尽管 24GB 显存与 RTX 4090 相同，但 ROCm 对 LLM 推理的优化落后 NVIDIA 至少 6-12 个月，缺乏成熟的 vLLM/TensorRT 等效工具链，实际吞吐仅为理论带宽的 30-40%，性价比远低于 RTX 4090，故从候选集中排除。

## Corrected Claim

AMD 消费级卡 (RX 7900 XTX) 在 LLM 推理中的排除理由：尽管 24GB 显存与 RTX 4090 相同，但 ROCm 对 LLM 推理的软件生态和工具链成熟度显著落后于 NVIDIA CUDA 生态，缺乏同等效率的推理框架支持，导致实际推理性能通常低于同显存 NVIDIA 显卡，故从候选集中排除。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点与父节点存在严重的主题错位（Topic Mismatch）：父节点讨论的是AMD消费级卡（RX 7900 XTX）的排除理由，而所有子节点均在计算AMD数据中心卡（MI300X）的性能指标。子节点内容完全未覆盖父节点中提到的ROCm软件栈落后、vLLM支持缺失及性价比对比等关键排除理由，反而引入了与父节点逻辑无关的硬件性能计算，导致逻辑断裂。）
