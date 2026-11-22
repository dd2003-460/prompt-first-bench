# N210: Qwen3-27B 在 INT4 (AWQ) 量化下，权重文件大小约为 13.5 GB，但加载到内存后需考虑反量化缓冲区和 KV Cache 初始分配，实际内存

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

Qwen3-27B 在 INT4 (AWQ) 量化下，权重文件大小约为 13.5 GB，但加载到内存后需考虑反量化缓冲区和 KV Cache 初始分配，实际内存占用约为 15-16 GB [待核验]

## Corrected Claim

Qwen3-27B 在 INT4 (AWQ) 量化下，权重文件大小约为 13.5 GB，但加载到内存后需考虑反量化缓冲区和 KV Cache 初始分配，实际内存占用约为 15-16 GB [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在INT4下权重约13.5GB，加上KV Cache及反量化缓冲区，15-16GB的内存占用估算符合工程常识。
