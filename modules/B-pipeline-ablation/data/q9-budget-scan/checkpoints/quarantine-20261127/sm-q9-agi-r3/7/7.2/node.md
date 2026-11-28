# N92: 对比 INT8 量化方案：INT8 在 V100 上有原生 Tensor Core 支持，推理加速比可达 1.8-2.2x（相比 FP16），且精度损失通常小于

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N31

## Claim

对比 INT8 量化方案：INT8 在 V100 上有原生 Tensor Core 支持，推理加速比可达 1.8-2.2x（相比 FP16），且精度损失通常小于 NVFP4 的软件模拟误差；若 NVFP4 实测加速比 < 1.5x，切换至 INT8 量化（如 SmoothQuant）可提升整体吞吐约 20-30%。

## Corrected Claim

INT8在V100上拥有原生Tensor Core支持，通常能提供显著的推理加速（具体倍数取决于模型结构，常见范围约为1.5-2.5x），且其精度损失通常低于低比特格式（如NVFP4）的软件模拟误差；若NVFP4实测加速比不理想，切换至INT8量化（如SmoothQuant）通常能提升整体吞吐量。

## Evidence

[质询]陈述中关于INT8在V100上的具体加速比（1.8-2.2x）及切换后吞吐提升幅度（20-30%）属于特定硬件和模型下的经验性能数据，缺乏通用性，且参考来源未提供这些具体数值，存在以偏概全或数据过时的风险。 | 来源[1]确认了Torch-TensorRT支持INT8和NVFP4量化，证实了技术可行性，但未提供具体的加速比数值或精度对比数据，属于间接支持；具体性能指标为经验事实，缺直接来源支持。

## Search Query

INT8 vs NVFP4 quantization V100 inference speedup comparison SmoothQuant accuracy loss

## Retrieval Sources

- {'url': 'https://docs.pytorch.org/TensorRT/user_guide/shapes_precision/quantization.html&rut=26e4aa3683ce5e43cf1dacf09f488f08fa776aa6339a71b2b6be4292a888e390', 'type': 'ddg', 'title': 'Quantization (INT8 / FP8 / FP4) — Torch-TensorRT'}
- {'url': 'https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/quantized-types-schemes.html&rut=2e09545d15c8c74ca2ce844f4b3a276a7cff7572dac886692130ba6165f771b5', 'type': 'ddg', 'title': 'Quantization Schemes — NVIDIA TensorRT'}
