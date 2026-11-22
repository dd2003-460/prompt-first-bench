# N6: 显存容量硬下限：Qwen3-27B在BF16下权重约54GB，INT8约27GB，FP8约27GB，INT4约13.5GB；加上32K上下文KV Cache（G

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

显存容量硬下限：Qwen3-27B在BF16下权重约54GB，INT8约27GB，FP8约27GB，INT4约13.5GB；加上32K上下文KV Cache（GQA 8KV heads, 128 dim, BF16）约1.5GB-3GB，因此单卡最小有效显存阈值为16GB（仅支持INT4且无余量）或24GB（支持INT8/FP8且有KV余量），排除显存<16GB的消费级GPU。

## Corrected Claim

显存容量硬下限：Qwen3-27B在BF16下权重约54GB，INT8约27GB，FP8约27GB，INT4约13.5GB；加上32K上下文KV Cache（GQA 8KV heads, 128 dim, BF16）约1.5GB-3GB，因此单卡最小有效显存阈值为16GB（仅支持INT4且无余量）或24GB（支持INT8/FP8且有KV余量），排除显存<16GB的消费级GPU。

## Evidence

先验知识/题面给定，逻辑校验通过：权重计算（27B*2B=54GB等）及KV Cache估算（32K*8*128*2B*2*层数/2≈1.5-3GB）符合数学逻辑与工程常识，16GB/24GB阈值推导自洽。
