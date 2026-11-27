# N201: Apple Silicon 不支持 TensorRT-LLM，因此无法使用 TensorRT 的 FP8/INT8 内核优化。在 INT8 推理中，Apple 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

Apple Silicon 不支持 TensorRT-LLM，因此无法使用 TensorRT 的 FP8/INT8 内核优化。在 INT8 推理中，Apple 依赖 Metal 的 int8 dot product 指令，其吞吐量约为 CUDA int8 的 50-70% (基于 M2 Ultra vs A100 的对比数据推算)。这意味着在相同精度下，Apple 方案的有效算力密度低于 NVIDIA。

## Corrected Claim

Apple Silicon 不支持 TensorRT-LLM，因此无法直接利用 TensorRT 的 FP8/INT8 内核优化。在 INT8 推理中，Apple 依赖 Metal 的 int8 dot product 指令，其吞吐量通常低于同级别 NVIDIA GPU（具体比例取决于模型和硬件配置，M2 Ultra 与 A100 的对比显示其算力密度相对较低）。

## Evidence

[质询]数值量级缺乏权威基准支持：'50-70%' 的吞吐量对比是基于特定模型、序列长度和硬件配置（M2 Ultra vs A100）的推算，不同场景下差异巨大，且 M2 Ultra 与 A100 并非同代或同定位产品，直接对比得出的通用比例缺乏普适性；此外，Apple Silicon 虽不支持 TensorRT-LLM，但可通过 MLX 或 CoreML 等框架实现 INT8 优化，断言'无法使用 TensorRT 内核'虽在技术栈上正确，但后半部分的性能对比过于绝对。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该性能比值为具体硬件对比的经验数据，非第一性原理可推导）

## Search Query

Metal int8 dot product performance vs CUDA TensorRT int8
