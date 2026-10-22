# 阶段 04：执行与结果核对

## 操作流程

1. 按阶段 03 的行动和依赖执行当前可执行步骤。
2. 记录实际执行的命令、修改文件、输出、观察和失败。
3. 逐项对照阶段 03 的验收方式，不把计划当作已完成结果。
4. 对未完成步骤说明原因、影响和下一步。
5. 需要外部事实时回到阶段 02，不要在执行记录里临时编造。

### 执行层通用循环防护

执行阶段是循环最高发区域。以下规则适用：

- **每步执行前**：判断任务复杂度。简单命令（ls, grep, cat, 单文件编辑）直接执行，不要思考
- **多步执行时**：如果上一步执行失败，最多重试 2 次；仍失败则记录失败原因并跳过，不要无限重试
- **工具调用时**：不要反复尝试同一个工具的不同参数 — 如果 2 次调用都失败，换工具或换方法
- **收到空响应或截断时**：降低输出长度或换方法重试
- **不要在一个命令上卡住超过 3 轮**：换命令、换方法、或标记为阻塞项

## Reviewer 质检标准

- 声明完成的步骤是否有实际结果；
- 产出文件、测试、编译或观察是否真实存在；
- 是否逐项对照验收方式；
- 失败和未完成项是否被诚实保留；
- 结果是否足够支持最终复核。

如果执行前提或事实有问题，repair_stage 写对应的 02 或 03；否则写 04。

## 操作示例

### 示例 1：GPU 测试 — 执行记录

**阶段 03 计划：**
```
步骤 1：搭建测试环境
- 动作：准备 4 台测试机器
- 验收方式：`nvidia-smi` 正常输出
```

**实际执行记录：**
```
步骤 1 执行：
- 命令：`docker run --gpus all -it nvidia/cuda:12.1-base nvidia-smi`
- 输出：
  +-----------------------------------------------------------------------------+
  | NVIDIA-SMI 535.104.05   Driver Version: 535.104.05   CUDA Version: 12.1   |
  |-------------------------------+----------------------+----------------------+
  | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
  | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
  |===============================+======================+======================|
  |   0  NVIDIA A100-SXM...  On   | 00000000:00:04.0 Off |                    0 |
  | N/A   32C    P0    43W / 400W |      0MiB / 40960MiB |      0%      Default |
  +-------------------------------+----------------------+----------------------+
- 结果：✅ 通过
- 文件：无修改
- 观察：A100 SXM4 40GB，驱动 535.104.05，CUDA 12.1

步骤 2 执行：
- 命令：`pip install torch vllm`
- 输出：
  Collecting torch
    Downloading torch-2.1.0-cp310-cp310-linux_x86_64.whl (700.8 MB)
  Collecting vllm
    Downloading vllm-0.2.0-cp310-cp310-linux_x86_64.whl (1.2 GB)
  Installing collected packages: torch, vllm
  Successfully installed torch-2.1.0 vllm-0.2.0
- 结果：✅ 通过
- 文件：无修改
- 观察：安装耗时约 15 分钟

步骤 3 执行：
- 命令：`python -c "import torch; print(torch.cuda.is_available())"`
- 输出：True
- 结果：✅ 通过
- 文件：无修改
- 观察：CUDA 可用

步骤 4 执行：
- 命令：`python benchmarks/benchmark_serving.py --model meta-llama/Llama-2-7b --tokenizer meta-llama/Llama-2-7b --num-prompts 100`
- 输出：
  Throughput: 123.45 tokens/sec
  Latency (p50): 12.3 ms
  Latency (p99): 45.6 ms
  Memory usage: 18.5 GB / 40 GB
- 结果：✅ 通过
- 文件：benchmark_results/a100_sxm4_40gb.json
- 观察：性能符合预期
```

### 示例 2：GPU 测试 — 失败处理

**阶段 03 计划：**
```
步骤 5：运行 Llama-3-8B 测试
- 动作：加载模型并运行推理
- 验收方式：模型加载成功，推理输出正常
```

**实际执行记录：**
```
步骤 5 执行：
- 命令：`python -m vllm.entrypoints.api_server --model meta-llama/Llama-3-8B --tensor-parallel-size 1`
- 输出：
  ERROR: Cannot load model meta-llama/Llama-3-8B into graph due to insufficient memory.
  Requested 22 GB, available 18.5 GB.
- 结果：❌ 失败
- 原因：Llama-3-8B 需要 22 GB 显存，A100 SXM4 40GB 扣除系统占用后仅剩 18.5 GB
- 影响：无法在 A100 SXM4 40GB 上运行 Llama-3-8B
- 下一步：
  a) 使用量化模型（AWQ/INT8）
  b) 切换到 A100 SXM4 80GB
  c) 使用更小的模型（Llama-3-70B 量化版）
- 重试 1：`python -m vllm.entrypoints.api_server --model TechxNinja/Llama-3-8B-AWQ --tensor-parallel-size 1`
- 输出：成功加载，推理正常
- 结果：✅ 通过（使用量化模型）
- 观察：量化后显存占用降至 6 GB，性能损失约 5%
```

## 通用原则

### 执行记录原则

1. **诚实记录**：成功和失败都要记录
2. **可复现**：记录所有命令和参数
3. **可追溯**：关联阶段 03 的计划和验收方式
4. **不掩盖问题**：失败原因和影响必须明确

### 验收原则

1. **对照验收**：逐项对照阶段 03 的验收方式
2. **不降低标准**：不因执行困难而降低验收标准
3. **不提前验收**：未完成不标记为完成
4. **不伪造结果**：不编造未执行的结果

### 失败处理原则

1. **记录失败**：如实记录失败原因
2. **评估影响**：判断失败对后续步骤的影响
3. **执行替代**：使用替代方案或标记为未解决
4. **不掩盖问题**：不要把失败包装成成功
