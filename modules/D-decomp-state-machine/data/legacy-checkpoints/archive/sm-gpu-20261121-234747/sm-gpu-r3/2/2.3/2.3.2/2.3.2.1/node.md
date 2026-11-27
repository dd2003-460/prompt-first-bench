# N245: RTX 4090 通过 TensorRT-LLM 执行 FP8 推理时，需将 FP8 权重 upcast 至 FP16 进行计算，实际有效吞吐量仅为 BF16 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N78

## Claim

RTX 4090 通过 TensorRT-LLM 执行 FP8 推理时，需将 FP8 权重 upcast 至 FP16 进行计算，实际有效吞吐量仅为 BF16 的 95-98%（因 upcast 开销极小），但显存占用减半（27GB vs 54GB），在 24GB 显存下 FP8 不可行（27GB > 24GB），必须使用 INT8 或 W4

## Corrected Claim

RTX 4090 通过 TensorRT-LLM 执行 FP8 推理时，对于权重大小超过 24GB 的模型（如约 27B 参数模型），FP8 权重（约 27GB）超出显存容量，不可行，需使用 INT8 或 W4 量化；但对于权重小于 24GB 的模型（如 7B-13B），FP8 可行，显存占用约为 BF16 的一半，吞吐量接近 BF16。

## Evidence

[质询]数值量级与硬件规格矛盾：RTX 4090 显存为 24GB，而陈述中称 FP8 权重占用 27GB，这在物理上不可能（27GB > 24GB 意味着无法加载，但陈述前半部分暗示其可执行推理仅因 upcast 开销，且后半部分才指出不可行，逻辑上若 27GB 是权重大小，则根本装不下，而非‘upcast 开销’问题；更关键的是，27GB 的 FP8 权重对应约 54GB 的 FP16 权重，即约 27B 参数模型，但通常讨论 4090 上 FP8 优势时，多指 7B-13B 模型，此时 FP8 权重远小于 24GB，陈述中的 27GB 数值缺乏具体模型上下文，疑似混淆了不同规模模型的显存占用，或错误地引用了超出 4090 容量的模型数据作为通用结论。 | 经验事实，逻辑自洽但缺来源支持；且存在内部逻辑矛盾：若 FP8 权重为 27GB，则无法在 24GB 显存的 4090 上加载，陈述前半部分‘执行 FP8 推理’与后半部分‘27GB > 24GB 不可行’在特定模型下成立，但作为通用陈述，27GB 这一具体数值缺乏模型规模限定，且与常见 4090 适用场景（如 7B/13B 模型 FP8 权重 < 24GB）不符，导致结论‘必须使用 INT8 或 W4’在 7B/13B 模型上不成立（FP8 可行）。

## Search Query

RTX 4090 TensorRT-LLM FP8 vs BF16 throughput benchmark upcast overhead
