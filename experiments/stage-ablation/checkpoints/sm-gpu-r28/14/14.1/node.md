# N309: RTX 5090 显存容量对 27B 模型 32K 上下文可行性的量化评估：若 RTX 5090 配备 32GB GDDR7，BF16 权重 (54GB) 无法

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N123

## Claim

RTX 5090 显存容量对 27B 模型 32K 上下文可行性的量化评估：若 RTX 5090 配备 32GB GDDR7，BF16 权重 (54GB) 无法单卡加载，必须依赖 INT4/W4 量化 (权重 ~14GB) 或 FP8 (权重 ~27GB)。FP8 下 27GB 权重 + 32K 上下文 KV Cache (~4-6GB) 总占用 ~31-33GB，处于 32GB 显存边缘，可能触发 OOM 或需牺牲部分上下文长度。

## Corrected Claim

RTX 5090 显存容量对 27B 模型 32K 上下文可行性的量化评估：若 RTX 5090 配备 32GB GDDR7，BF16 权重 (54GB) 无法单卡加载，必须依赖 INT4/W4 量化 (权重 ~14GB) 或 FP8 (权重 ~27GB)。FP8 下 27GB 权重 + 32K 上下文 KV Cache (~4-6GB) 总占用 ~31-33GB，处于 32GB 显存边缘，可能触发 OOM 或需牺牲部分上下文长度。

## Evidence

先验知识/题面给定，逻辑校验通过：27B模型BF16权重约54GB，FP8约27GB，INT4约14GB；32K上下文KV Cache估算4-6GB符合常规Transformer架构计算；总显存占用31-33GB接近32GB上限，逻辑自洽且数值量级合理。

## Search Query

RTX 5090 32GB VRAM Qwen3-27B FP8 KV cache memory requirement 32K context
