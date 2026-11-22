# N210: Qwen3-27B 在 INT4 (AWQ) 量化下，权重文件大小约为 13.5 GB，但加载到内存后需考虑反量化缓冲区和 KV Cache 初始分配，实际内存

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

Qwen3-27B 在 INT4 (AWQ) 量化下，权重文件大小约为 13.5 GB，但加载到内存后需考虑反量化缓冲区和 KV Cache 初始分配，实际内存占用约为 15-16 GB [待核验]

## Corrected Claim

Qwen3-27B 在 INT4 (AWQ) 量化下，权重文件大小约为 13.5 GB，但加载到内存后需考虑反量化缓冲区和 KV Cache 初始分配，实际内存占用约为 15-16 GB [待核验]

## Evidence

父节点级核验未通过：非正交（子节点1计算得出的总内存占用（21.75 GB）与父节点声称的“实际内存占用约为 15-16 GB”存在严重矛盾，导致逻辑不连贯。此外，子节点2完全依赖子节点1中得出的21.75 GB这一与父节点冲突的数据进行后续推导，因此两个子节点在核心数值上并不正交，而是处于冲突状态。）
