# N484: RTX 4090 双卡 (48GB) 在 FP8 权重 (27GB) + 扩展 KV (12GB) + 激活值 (2GB) 下的剩余显存计算：48 - 27 -

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N199, N200, N201

## Claim

RTX 4090 双卡 (48GB) 在 FP8 权重 (27GB) + 扩展 KV (12GB) + 激活值 (2GB) 下的剩余显存计算：48 - 27 - 12 - 2 = 7GB；该 7GB 仅支持 Batch Size=1 的长上下文推理，若需 Batch Size=2 则需额外 17.5GB 显存，总需求 44.5GB < 48GB 勉强可行，但无安全边际，一旦上下文超过 34K 即溢出。

## Corrected Claim

RTX 4090 双卡 (48GB) 在 FP8 权重 (27GB) + 扩展 KV (12GB) + 激活值 (2GB) 下剩余 7GB。若 Batch Size=2 需额外 17.5GB 显存，则总需求为 58.5GB，超出 48GB 显存上限，不可行。

## Evidence

[质询]数值逻辑存在内部矛盾：若 Batch Size=2 需额外 17.5GB，则总需求应为 48+17.5=65.5GB（或基于剩余7GB计算，需 7+17.5=24.5GB 额外空间，总占用 48-7+24.5=65.5GB），远超 48GB 显存上限；陈述中声称总需求 44.5GB < 48GB 与‘需额外 17.5GB’在算术上不自洽（48-7+17.5=58.5GB 或 27+12+2+17.5=58.5GB，均不等于 44.5GB）。此外，‘额外 17.5GB’的推导依据不明，若指 KV Cache 翻倍，12GB*2=24GB，增量应为 12GB 而非 17.5GB。 | 逻辑校验失败：算术推导存在明显错误，48-27-12-2=7 正确，但后续 Batch Size=2 的显存需求计算（44.5GB）与‘额外 17.5GB’及总显存 48GB 的限制无法自洽（58.5GB > 48GB），且来源缺失无法验证具体参数假设。

## Search Query

GPU memory calculation LLM inference batch size KV cache
