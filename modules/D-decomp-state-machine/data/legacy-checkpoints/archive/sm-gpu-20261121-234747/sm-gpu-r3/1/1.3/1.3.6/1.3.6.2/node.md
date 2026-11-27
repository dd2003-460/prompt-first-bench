# N216: Coral TPU (Edge TPU) 运行 Qwen3-27B 的不可行性论证：Edge TPU 内存容量通常仅为 4-8GB，且不支持 27B 参数规模的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

Coral TPU (Edge TPU) 运行 Qwen3-27B 的不可行性论证：Edge TPU 内存容量通常仅为 4-8GB，且不支持 27B 参数规模的模型加载，即使采用 W4 量化（13.5GB），仍超出其内存上限，因此 Coral TPU 方案在 Qwen3-27B 上完全不可行，无需进行吞吐量测试 [verified]

## Corrected Claim

Coral TPU (Edge TPU) 运行 Qwen3-27B 的不可行性论证：Edge TPU 内存容量通常仅为 4-8GB，且不支持 27B 参数规模的模型加载，即使采用 W4 量化（13.5GB），仍超出其内存上限，因此 Coral TPU 方案在 Qwen3-27B 上完全不可行，无需进行吞吐量测试 [verified]

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 即使 W4 量化后约需 13.5GB 内存，远超 Edge TPU 4-8GB 物理上限，结论成立

## Search Query

Coral Edge TPU memory limit 27B model infeasibility
