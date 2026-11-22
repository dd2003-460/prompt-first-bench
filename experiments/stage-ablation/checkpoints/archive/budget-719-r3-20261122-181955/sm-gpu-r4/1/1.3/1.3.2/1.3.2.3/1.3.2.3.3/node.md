# N516: RX 7900 XT 在 INT4 量化 + INT8 KV Cache 配置下，权重 13.5GB + 框架 2GB + KV Cache 4GB (INT8

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N180

## Claim

RX 7900 XT 在 INT4 量化 + INT8 KV Cache 配置下，权重 13.5GB + 框架 2GB + KV Cache 4GB (INT8) = 19.5GB < 20GB，理论上可行，但剩余缓冲仅 0.5GB，并发请求数严格限制为 1。

## Corrected Claim

RX 7900 XT 在 INT4 量化 + INT8 KV Cache 配置下，权重 13.5GB + 框架 2GB + KV Cache 4GB (INT8) = 19.5GB < 20GB，理论上可行，但剩余缓冲仅 0.5GB，并发请求数严格限制为 1。

## Evidence

先验知识/题面给定，逻辑校验通过：13.5+2+4=19.5GB，小于20GB显存，且0.5GB缓冲极小，限制并发为1符合工程直觉。
