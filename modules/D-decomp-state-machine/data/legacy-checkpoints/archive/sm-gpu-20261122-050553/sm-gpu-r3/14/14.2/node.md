# N348: 显存溢出临界值警报机制：当模型权重 + KV Cache 总需求与显存容量之差 ΔMem < 5% 时（例如 RTX 5090 32GB vs 需求 30.4G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

显存溢出临界值警报机制：当模型权重 + KV Cache 总需求与显存容量之差 ΔMem < 5% 时（例如 RTX 5090 32GB vs 需求 30.4GB，ΔMem = 1.6GB ≈ 5%），触发 'Manual Verification Required'，禁止直接用于排名，必须建议用户运行 vllm serve --max-model-len 32768 进行实测。

## Corrected Claim

显存溢出临界值警报机制：当模型权重 + KV Cache 总需求与显存容量之差 ΔMem < 5% 时（例如 RTX 5090 32GB vs 需求 30.4GB，ΔMem = 1.6GB ≈ 5%），触发 'Manual Verification Required'，禁止直接用于排名，必须建议用户运行 vllm serve --max-model-len 32768 进行实测。

## Evidence

先验知识/题面给定，逻辑校验通过：显存溢出临界值警报机制的描述在逻辑上自洽，数值量级合理（RTX 5090 32GB vs 需求 30.4GB，ΔMem = 1.6GB ≈ 5%），且符合工程实践中的安全边际设定。
