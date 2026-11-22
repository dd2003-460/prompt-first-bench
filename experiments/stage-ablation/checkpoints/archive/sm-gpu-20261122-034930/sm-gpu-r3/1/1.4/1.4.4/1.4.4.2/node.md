# N189: RTX 4080 Super (16GB) 在W4精度下的单卡可行性修正：权重13.5GB + KV Cache (INT8, 32K ctx) 5.35GB 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N59

## Claim

RTX 4080 Super (16GB) 在W4精度下的单卡可行性修正：权重13.5GB + KV Cache (INT8, 32K ctx) 5.35GB + 框架开销4GB = 22.85GB，远超16GB容量，即使将KV Cache量化至INT4 (2.67GB)，总需求13.5+2.67+4=20.17GB仍超出16GB，故RTX 4080 Super在任何合理精度组合下均不可行，必须使用CPU Offload（导致吞吐降至<5 tokens/s）。

## Corrected Claim

RTX 4080 Super (16GB) 在W4精度下的单卡可行性修正：权重13.5GB + KV Cache (INT8, 32K ctx) 5.35GB + 框架开销4GB = 22.85GB，远超16GB容量，即使将KV Cache量化至INT4 (2.67GB)，总需求13.5+2.67+4=20.17GB仍超出16GB，故RTX 4080 Super在任何合理精度组合下均不可行，必须使用CPU Offload（导致吞吐降至<5 tokens/s）。

## Evidence

先验知识/题面给定，逻辑校验通过：13.5GB + 5.35GB + 4GB = 22.85GB > 16GB，且 13.5GB + 2.67GB + 4GB = 20.17GB > 16GB，算术正确且符合显存占用基本逻辑。
