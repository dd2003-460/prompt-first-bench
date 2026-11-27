# N161: TensorRT-LLM 在静态图编译模式下，CUDA 上下文和内核编译缓存的显存占用约为 200-800 MB，具体数值取决于模型大小和编译选项，需查阅 NV

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

TensorRT-LLM 在静态图编译模式下，CUDA 上下文和内核编译缓存的显存占用约为 200-800 MB，具体数值取决于模型大小和编译选项，需查阅 NVIDIA 官方文档或实测数据。

## Corrected Claim

TensorRT-LLM 在构建/推理阶段，CUDA 上下文及内核编译缓存的显存占用通常在数百 MB 至数 GB 不等，具体数值高度依赖于模型参数量、精度（FP16/INT8）及编译优化选项，建议查阅 NVIDIA 官方文档或进行实测以获取准确数据。

## Evidence

[质询]数值范围（200-800 MB）缺乏具体模型规模（如参数量、精度）和硬件架构（如 A100/H100）的限定，不同模型和配置下该数值波动极大，直接给出固定区间可能误导用户；且‘静态图编译模式’并非 TensorRT-LLM 的标准官方术语（通常指 Inference 或 Build 阶段），存在术语混淆风险。 | 经验事实，逻辑自洽但缺来源支持；检索无可用来源，无法验证具体数值区间及术语准确性。

## Search Query

TensorRT-LLM CUDA context memory overhead static graph
