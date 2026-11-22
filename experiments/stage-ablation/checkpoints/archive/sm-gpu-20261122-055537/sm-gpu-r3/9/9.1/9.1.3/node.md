# N352: RTX 4090 (24GB) 运行 Qwen3-27B INT4 (AWQ, ~14.5GB 权重) + 32K BF16 KV Cache (6.75GB)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N111

## Claim

RTX 4090 (24GB) 运行 Qwen3-27B INT4 (AWQ, ~14.5GB 权重) + 32K BF16 KV Cache (6.75GB) 的总显存需求为 14.5 + 6.75 + 1.5 (激活/框架) ≈ 22.75 GB，剩余显存 1.25 GB，处于 OOM 边缘，需启用 PagedAttention 以管理碎片，且 Batch Size 必须限制为 1 或 2

## Corrected Claim

RTX 4090 (24GB) 运行 Qwen3-27B INT4 (AWQ, ~14.5GB 权重) + 32K BF16 KV Cache (6.75GB) 的总显存需求为 14.5 + 6.75 + 1.5 (激活/框架) ≈ 22.75 GB，剩余显存 1.25 GB，处于 OOM 边缘，需启用 PagedAttention 以管理碎片，且 Batch Size 必须限制为 1 或 2

## Evidence

先验知识/题面给定，逻辑校验通过：24GB显存下，14.5GB权重+6.75GB KV Cache+1.5GB开销=22.75GB，剩余1.25GB确实处于OOM边缘，需PagedAttention和限制Batch Size，数值量级与工程实践一致

## Search Query

RTX 4090 24GB Qwen3-27B INT4 32k context OOM risk batch size limit
