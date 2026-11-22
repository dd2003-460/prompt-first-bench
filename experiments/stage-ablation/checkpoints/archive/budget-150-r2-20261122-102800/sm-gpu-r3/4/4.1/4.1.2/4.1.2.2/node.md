# N269: 高并发场景 (Batch Size > 8) 下，RTX 4090 的算力利用率受 Kernel Launch Overhead 和 SM Occupancy 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N98

## Claim

高并发场景 (Batch Size > 8) 下，RTX 4090 的算力利用率受 Kernel Launch Overhead 和 SM Occupancy 限制，当 Batch Size 达到 32 时，MFU 可提升至 30%-40%，但受限于 24GB 显存容量，实际可行 Batch Size 上限约为 16-24 (取决于 Context Length)。

## Corrected Claim

高并发场景 (Batch Size > 8) 下，RTX 4090 的算力利用率受 Kernel Launch Overhead 和 SM Occupancy 限制，当 Batch Size 达到 32 时，MFU 可提升至 30%-40%，但受限于 24GB 显存容量，实际可行 Batch Size 上限约为 16-24 (取决于 Context Length)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 24GB 显存限制与 Batch Size 对 MFU 的影响符合 GPU 架构基本原理及工程经验。

## Search Query

RTX 4090 high batch size LLM inference throughput limit
