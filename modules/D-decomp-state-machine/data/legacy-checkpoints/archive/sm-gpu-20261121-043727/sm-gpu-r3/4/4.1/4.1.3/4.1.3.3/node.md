# N167: 32K 上下文下 GQA vs MHA 的显存节省量化：MHA 占用 = 32768 * 0.25 MB * 4 (因 MHA 头数是 GQA 的 4 倍) =

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N64

## Claim

32K 上下文下 GQA vs MHA 的显存节省量化：MHA 占用 = 32768 * 0.25 MB * 4 (因 MHA 头数是 GQA 的 4 倍) = 32,768 MB ≈ 32 GB；GQA 占用 = 32768 * 0.25 MB = 8,192 MB ≈ 8 GB。节省显存 = 32 GB - 8 GB = 24 GB。这 24 GB 的差异直接决定了 RTX 4090 (24GB) 是否能在 BF16 下容纳 32K 上下文（结论：GQA 下勉强可容纳，MHA 下不可行）

## Corrected Claim

32K 上下文下 GQA 相比 MHA 可显著减少 KV Cache 显存占用（通常减少 50%-75%），具体节省量取决于模型架构（层数、头数、维度）。对于 RTX 4090 (24GB)，GQA 通常能容纳 32K 上下文，而 MHA 可能因显存不足而受限，但具体数值需依据特定模型参数计算，而非固定的 24 GB 差异。

## Evidence

[质询]数值量级与硬件常识严重不符：32K 上下文下，即使采用 MHA，KV Cache 占用通常仅为几 GB 至十几 GB（取决于模型层数和头数），绝不可能达到 32 GB；且 RTX 4090 显存为 24 GB，若 MHA 占用 32 GB，则物理上无法运行，这与‘MHA 下不可行’的结论虽逻辑一致，但前提数值（32 GB）远超单卡显存上限，暗示计算模型或参数假设（如 0.25 MB/token 的系数）存在严重错误，导致量化结论失真。 | 逻辑校验失败：32768 * 0.25 MB = 8192 MB = 8 GB，而非 32 GB；且 MHA 占用 32 GB 超过 RTX 4090 的 24 GB 显存，虽结论‘不可行’正确，但量化数值（32 GB）与常见 LLM 架构参数不符，属于经验事实错误。
