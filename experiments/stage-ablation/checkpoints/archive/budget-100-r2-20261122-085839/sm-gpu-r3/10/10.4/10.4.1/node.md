# N311: INT8 量化下 Qwen3-27B 每生成一个 token 需读取的权重字节数 Bytes_per_token = 27.1e9 params * 1 byt

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N113

## Claim

INT8 量化下 Qwen3-27B 每生成一个 token 需读取的权重字节数 Bytes_per_token = 27.1e9 params * 1 byte/param = 27.1 GB (假设全参数参与计算且无稀疏性)

## Corrected Claim

INT8 量化下 Qwen3-27B 每生成一个 token 需读取的权重字节数 Bytes_per_token = 27.1e9 params * 1 byte/param = 27.1 GB (假设全参数参与计算且无稀疏性)

## Evidence

先验知识/题面给定，逻辑校验通过：INT8量化下每参数1字节，27.1e9参数对应27.1GB权重读取量，量纲与数值计算正确。
