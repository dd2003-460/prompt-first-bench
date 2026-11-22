# N37: 显存容量可行性边界：RTX 4090 (24GB) 无法在 BF16 下运行 Qwen3-27B (需 ~56-60GB)；但在 INT4/W4 量化下，权重占

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

显存容量可行性边界：RTX 4090 (24GB) 无法在 BF16 下运行 Qwen3-27B (需 ~56-60GB)；但在 INT4/W4 量化下，权重占用降至 ~13.5GB (27B * 0.5 bytes)，加上 KV Cache (128MB*2 for 2 seq) 和 Overhead，总占用约 16-18GB，可在 24GB 卡上单卡运行 2 路并发 32K 上下文。

## Corrected Claim

RTX 4090 (24GB) 在 INT4 量化下可运行 Qwen3-27B，但 2 路并发 32K 上下文时 KV Cache 占用较大，显存余量紧张，可能面临 OOM 风险或需降低并发/上下文长度。

## Evidence

[质询]KV Cache 估算严重低估：32K 上下文、2 路并发下，Qwen3-27B 的 KV Cache 占用远超 256MB（通常需数 GB），导致总显存占用可能超过 24GB 或极度紧张，'游刃有余'的结论存疑。 | 来源[1]指出 24GB 显存在长上下文（>16K）和多模型并行场景下是硬瓶颈，与 claim 中'单卡运行 2 路并发 32K 上下文'的乐观估计存在潜在矛盾；且 claim 中 KV Cache 数值（128MB*2）对于 32K 上下文而言量级过小，缺乏来源直接支持该具体数值，属于经验事实但逻辑上存在低估风险。

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2063675360831599245&rut=3d8e975827b00acfc06f6bf5a19c5779715ae5a7345f2f71a90a7f9adac1d9c1', 'type': 'ddg', 'title': 'Rtx 4090的24gb显存，什么时候会成为你的瓶颈？ - 知乎'}
