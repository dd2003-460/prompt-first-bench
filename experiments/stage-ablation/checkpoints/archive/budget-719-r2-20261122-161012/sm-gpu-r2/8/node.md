# N31: Apple M3 Ultra (512GB) 运行 Qwen3-27B (BF16) 的实测吞吐量（tokens/s），以及其内存带宽（800GB/s）对长上下

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Apple M3 Ultra (512GB) 运行 Qwen3-27B (BF16) 的实测吞吐量（tokens/s），以及其内存带宽（800GB/s）对长上下文（32K）Decode 阶段的限制效应，与 RTX 4090 双卡方案的性能对比。

## Corrected Claim

Apple M3 Ultra (512GB) 运行 Qwen3-27B 在 Q4_K_M 量化下估算吞吐量约为 34 tokens/s，在 Q8_0 量化下约为 17-26 tokens/s；由于 BF16 精度下内存占用极大且带宽受限，其 Decode 阶段性能通常低于量化版本，具体数值需实测，且现有来源未提供与 RTX 4090 双卡方案的直接对比数据。

## Evidence

父节点级核验未通过：不完备（子节点1聚焦于Apple M3 Ultra的理论性能上限与估算，子节点2聚焦于与RTX 4090双卡的横向对比，两者主题正交且无冗余。但父节点明确询问“实测吞吐量（tokens/s）”，而子节点1仅提供了基于带宽的理论估算（13-14 tokens/s）并标记为[待核验]，未涵盖实际硬件测试数据或更精确的实测值，导致对父节点“实测”这一关键要求的覆盖不全。）

## Retrieval Sources

- {'url': 'https://llmap.ai/can-i-run/qwen-qwen3-6-27b/apple-m3-ultra&rut=0dc029a425f3970709ca16ecdf014d8192c2d789fbaf5677b89feec3f8f3355f', 'type': 'ddg', 'title': 'Can I run Qwen3.6 27B on Apple M3 Ultra (80-core GPU)? - llmap.ai'}
- {'url': 'https://fitllm.run/can-i-run/qwen-3-6-27b-on-m3-ultra-512gb&rut=2bda3382385abe85705a4be1c4d1d616f280e7bfaff06d6eb9393db31e1e7915', 'type': 'ddg', 'title': 'Can I run Qwen 3.6 27B on a M3 Ultra 512GB Mac?'}
- {'url': 'https://canirunthisllm.com/can-i-run/qwen3-6-27b/on/m3-ultra-512/&rut=1a8358bee00e6ed7cdd89766965eac5c120f810f79220eded946c0c48903a55d', 'type': 'ddg', 'title': 'Can a Mac Studio M3 Ultra (512GB) run Qwen3.6 27B?'}
