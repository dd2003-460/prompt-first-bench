# N127: NVIDIA RTX 5090 的 PCIe 5.0 接口带宽（64 GB/s x4）对多卡或大模型权重加载/卸载的影响：在单卡推理中若模型权重+KV Cach

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35, N36, N37

## Claim

NVIDIA RTX 5090 的 PCIe 5.0 接口带宽（64 GB/s x4）对多卡或大模型权重加载/卸载的影响：在单卡推理中若模型权重+KV Cache 超过 32GB 需 Swap 至 CPU 内存，Swap 带宽受限于 PCIe 5.0，需计算 Swap 导致的额外延迟占比。

## Corrected Claim

NVIDIA RTX 5090 的 PCIe 5.0 接口带宽（64 GB/s x4）对多卡或大模型权重加载/卸载的影响：在单卡推理中若模型权重+KV Cache 超过 32GB 需 Swap 至 CPU 内存，Swap 带宽受限于 PCIe 5.0，需计算 Swap 导致的额外延迟占比。

## Evidence

父节点级核验未通过：不完备（子节点覆盖了触发条件、带宽参数和计算公式，逻辑上正交且无冗余。但存在关键概念错误和覆盖缺失：1. 父节点明确指RTX 5090（32GB显存），子节点1却以RTX 4090/5090 24GB为前提，且错误断言32GB显存无法容纳27B FP8(27GB)+KV Cache(1.6-3.2GB)，实际上27+3.2=30.2GB < 32GB，通常无需Swap，这与父节点“需计算Swap延迟”的前提相悖，导致后续计算基础错误。2. 父节点标题强调“多卡”影响，但子节点完全未涉及多卡场景下的PCIe拓扑、P2P通信或权重分布对带宽的影响，仅局限于单卡Swap。）
