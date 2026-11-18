# N51: TensorRT-LLM 对 AMD GPU 的支持状态：是否支持 FP8/INT8 量化内核？若不支持，回退到 BF16 推理时的显存占用增加量 (相对于 F

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

TensorRT-LLM 对 AMD GPU 的支持状态：是否支持 FP8/INT8 量化内核？若不支持，回退到 BF16 推理时的显存占用增加量 (相对于 FP8 的 2x 显存) 及对 32K 上下文窗口下 KV Cache 最大并发数的影响

## Corrected Claim

TensorRT-LLM 对 AMD GPU 的支持状态需查阅官方文档确认；若不支持 FP8/INT8 量化内核，回退到 BF16 推理时显存占用约为 FP8 的 2 倍，具体对 32K 上下文窗口下 KV Cache 最大并发数的影响需根据实际硬件配置和模型参数计算。

## Evidence

[质询]来源[4]仅提及TensorRT支持NVIDIA硬件（SM 7.5+），未明确说明对AMD GPU的支持状态或FP8/INT8内核在AMD上的具体可用性；且'2x显存'和'KV Cache并发数影响'属于具体工程数值断言，缺乏直接来源支持。 | 来源[4]确认TensorRT主要面向NVIDIA硬件，但未直接覆盖AMD支持细节及量化内核状态；逻辑上BF16相比FP8确实占用2倍显存，但具体并发数影响需实测数据支持，属经验事实缺来源。

## Search Query

TensorRT-LLM AMD GPU support FP8 INT8 quantization kernel availability fallback BF16 memory overhead

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'https://docs.nvidia.com', 'type': None, 'title': 'direct-browser: docs.nvidia.com'}
- {'url': 'https://en.wikipedia.org/wiki/GeForce_RTX_40_series', 'type': 'gpu_specs', 'title': 'GPU Specs: GeForce\xa0RTX 4060[56][57][58]'}
- {'url': 'https://docs.nvidia.com/deeplearning/tensorrt/latest/getting-started/support-matrix.html&rut=71d9b6e01a1692542b0cf56353f8efe4318c7e5316d581e837b5d37b4750aefe', 'type': 'ddg', 'title': 'Support Matrix — NVIDIA TensorRT'}
