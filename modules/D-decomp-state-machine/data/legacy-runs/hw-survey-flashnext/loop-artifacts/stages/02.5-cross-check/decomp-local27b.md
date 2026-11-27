# Qwen3.8-Flash-Next 部署选型分析 (2026-11)

## 1. 候选全集

### 纳入候选
| 硬件 | 理由 |
|---|---|
| **Mac Studio M5 Ultra 512GB** | 唯一能单节点无 swap 跑满 262K ctx + 75GB 权重 + KV cache 余量的消费级方案。1.2TB/s 带宽对 MoE decode 关键路径友好。 |
| **Mac Studio M5 Ultra 256GB** | 75GB 权重 + 262K ctx KV cache (估算 ~30-50GB) 勉强可容纳，但余量极小，需量化 KV 或限制并发。性价比高于 512GB。 |
| **DGX Spark GB10 128GB** | 128GB 统一内存 + 273GB/s。带宽是瓶颈，但容量够。适合"能跑但慢"的基线对照。 |
| **2× AMD R9700 32GB (64GB 总)** | **排除**（见下）。 |
| **NVIDIA RTX 5090 32GB** | 单卡 32GB < 75GB 权重，需多卡。2×5090=64GB 仍不够。4×5090=128GB 可行但 PCIe 互联带宽低，MoE 跨卡通信开销大。 |
| **Cloud A100/H100** | 弹性、高带宽 (HBM 2-3TB/s)、无需维护。适合突发负载或长上下文高并发。 |
| **Strix Halo 128GB** | 128GB 统一内存，但带宽 ~256GB/s (LPDDR5x)，比 DGX Spark 略低或持平。作为 DGX Spark 的替代/对照。 |

### 排除候选及理由
| 硬件 | 排除理由 |
|---|---|
| **Mac Studio M5 Max 128GB** | 614GB/s 带宽尚可，但 128GB 容量对 75GB 权重 + 262K ctx KV cache 余量不足（KV cache 在 262K 下可能需 20-40GB 取决于 batch 和量化）。若限制 ctx 到 32K 可纳入，但题目要求 262K，**排除**。 |
| **2× AMD R9700 32GB** | 总显存 64GB < 75GB 权重。**物理矛盾**，无法加载模型。排除。 |
| **RTX 5070 Ti 16GB / 3090 24GB** | 单卡容量远不足，多卡组合成本高且 PCIe 带宽瓶颈严重。排除。 |
| **DGX Spark GB10 128GB** | **保留但降级**：273GB/s 带宽下 decode 速度预计 < 10 tok/s，仅适合离线批处理或极低 QPS 场景。 |

### 遗漏的重要选项
- **Mac Studio M5 Ultra 96GB**：容量不足（96GB - 75GB = 21GB 给 KV+OS，262K ctx 下 KV cache 可能超 21GB），**排除**，除非接受 ctx 截断或激进 KV 量化。
- **多节点 Mac Studio 集群**：2026 年 Thunderbolt 5 互联带宽 ~80GB/s，MoE 跨节点通信开销巨大，**不推荐**作为首选，仅作为极端扩展选项。
- **Apple Silicon 服务器 (M5 Ultra 双芯片)**：若存在，带宽翻倍但成本极高，**暂不纳入**（无公开规格）。

---

## 2. 正交维度

| 维度 | 含义 | 取值枚举 | 检查方法 |
|---|---|---|---|
| **D1: 有效内存容量** | 可分配给模型权重+KV cache 的内存 (GB) | 96/128/256/512/80(A100)/141(H100) | 总内存 - OS/系统预留 (10-15%) |
| **D2: 内存带宽** | 主存/显存带宽 (GB/s) | 273/614/1.2TB/2.0TB(H100)/3.35TB(H100 SXM) | 官方 spec + 实测 STREAM triad |
| **D3: 峰值算力 (FP16/INT8)** | 影响 prefill 和 MoE expert 计算 (TFLOPS) | 50-1000+ | 官方 spec |
| **D4: 互联带宽** | 多卡/多节点通信 (GB/s) | PCIe5 64GB/s / NVLink 900GB/s / TB5 80GB/s | 官方 spec |
| **D5: 功耗/散热** | 7×24 运行可行性 (W) | 100-1000W | 官方 TDP + 实测 |
| **D6: 软件栈成熟度** | llama.cpp/MLX/vLLM 支持度 | 高/中/低 | 社区 issue + 实测 |
| **D7: 成本 (TCO)** | 硬件 + 电力 + 维护 ($/月) | $0.5-$50+/月 | 计算 |
| **D8: 延迟特性** | TTFT (prefill) 和 TPOT (decode) | ms/token | 实测 |

### 正交性自检
- D1 和 D2 正交：容量大不一定带宽高（如 Strix Halo 128GB/256GB/s vs M5 Ultra 512GB/1.2TB/s）。
- D2 和 D3 正交：带宽高不一定算力高（如 M5 Ultra 带宽高但 FP16 算力低于 H100）。
- D4 仅在多卡/多节点时相关，单卡时 D4 退化为 N/A，**条件正交**。
- D6 和 D1-D5 正交：硬件规格好但软件栈差（如早期 RDNA4）会导致实际性能远低于理论。

### 完备性自检
- 缺少 **D9: 内存延迟** (ns)：对 MoE decode 中 expert 激活的随机访问有影响，但通常被带宽主导，**可忽略**。
- 缺少 **D10: 并发能力**：由 D1 (KV cache 余量) 和 D2 (带宽) 共同决定，**已覆盖**。
- 缺少 **D11: 多模态支持**：Qwen3.8 是多模态，需确认硬件对 vision encoder 的支持。Apple Silicon 和 NVIDIA 均支持，AMD RDNA4 支持度 [不确定]，**需补充检查**。

---

## 3. 分解树

```
Root: 确定最优部署硬件
├── A: 需求量化
│   ├── A1: 计算 75GB 权重在 4bit 下的实际内存占用
│   │   └── 动作: 75GB * 1.0 (量化开销) + 10% (KV cache 预分配)
│   │   └── 判据: 得到最小内存需求 (GB)
│   ├── A2: 估算 262K ctx 下 KV cache 大小
│   │   └── 动作: 262K * 48 layers * 2 (K+V) * hidden_dim * bytes_per_elem
│   │   └── 判据: 得到 KV cache 大小 (GB)
│   └── A3: 确定并发 batch size 上限
│       └── 动作: (D1 - 权重 - KV_per_seq) / KV_per_seq
│       └── 判据: 得到最大并发数
├── B: 硬件筛选
│   ├── B1: 按 D1 (容量) 过滤
│   │   └── 动作: 排除 D1 < A1+A2 的硬件
│   │   └── 判据: 剩余候选列表
│   ├── B2: 按 D2 (带宽) 排序
│   │   └── 动作: 计算理论 decode tok/s = D2 / (active_params * bytes_per_token)
│   │   └── 判据: 得到理论速度排名
│   └── B3: 按 D6 (软件栈) 过滤
│       └── 动作: 检查 llama.cpp/MLX/vLLM 对 MoE 262K ctx 的支持
│       └── 判据: 排除软件栈不成熟的硬件
├── C: 场景匹配
│   ├── C1: 个人 7×24
│   │   └── 动作: 优化 D5 (功耗) + D7 (TCO)
│   │   └── 判据: 选出最低 TCO 且 D2 > 500GB/s 的硬件
│   ├── C2: 小团队 (5-10 并发)
│   │   └── 动作: 优化 D1 (容量) + D2 (带宽) 平衡
│   │   └── 判据: 选出最大并发数且 TPOT < 50ms 的硬件
│   └── C3: 长上下文 (262K, 低并发)
│       └── 动作: 优化 D1 (容量) 优先
│       └── 判据: 选出能容纳 262K ctx 且 D2 > 1TB/s 的硬件
└── D: 风险验证
    ├── D1: 验证 MoE 内存瓶颈假设
    │   └── 动作: 实测 6B active 参数在 4bit 下的实际内存访问模式
    │   └── 判据: 确认带宽是瓶颈而非算力
    └── D2: 验证 KV cache 量化可行性
        └── 动作: 测试 FP8/INT8 KV cache 对 262K ctx 的精度影响
        └── 判据: 精度损失 < 1% 则可行
```

**依赖关系**：A → B → C → D。A 是基础，B 依赖 A 的输出，C 依赖 B 的筛选结果，D 是最终验证。

---

## 4. 量化口径

### Decode tok/s
```
理论 tok/s = 内存带宽 (GB/s) / (active_params * bytes_per_token)
```
- **假设**：
  - active_params = 6B (MoE top-10 激活)
  - bytes_per_token = 0.5 (4bit 量化)
  - 内存带宽利用率 = 80% (实际 vs 理论)
- **示例**：
  - M5 Ultra 512GB: 1200 GB/s / (6e9 * 0.5) * 0.8 = **320 tok/s** (理论上限，实际可能 100-200 tok/s)
  - DGX Spark: 273 GB/s / (6e9 * 0.5) * 0.8 = **73 tok/s** (理论，实际可能 20-40 tok/s)

### 内存需求
```
总内存 = 权重 (75GB) + KV_cache (N_ctx * N_layers * 2 * hidden_dim * bytes) + OS (10GB)
```
- **假设**：
  - hidden_dim = 4096 (Qwen3 典型值)
  - bytes_per_elem = 1 (FP16 KV) 或 0.5 (INT8 KV)
  - N_ctx = 262,144
- **计算**：
  - KV_cache (FP16) = 262144 * 48 * 2 * 4096 * 2 bytes = **204 GB** (单序列)
  - **问题**：204GB KV cache 远超 512GB 内存的余量。
  - **修正**：实际部署中 KV cache 会分页 (PagedAttention)，且 262K ctx 是最大长度，平均使用率可能 10-20%。
  - **保守估计**：KV_cache 平均 = 204GB * 0.1 = **20GB**
  - 总内存 = 75 + 20 + 10 = **105GB** → 128GB 硬件勉强，256GB 舒适，512GB 充裕。

### 性价比
```
TCO/月 = (硬件成本 / 36月) + (功耗 * 24h * 30d * 电价) + 维护成本
性价比 = 有效 tok/s / TCO/月
```
- **假设**：
  - 硬件寿命 3 年
  - 电价 $0.15/kWh
  - 维护成本 $10/月 (云) 或 $0 (本地)

---

## 5. 风险清单

1. **KV cache 内存低估**：262K ctx 的 KV cache 在 FP16 下单序列可达 200GB+，若未考虑分页或量化，会导致 128GB/256GB 硬件实际无法运行 262K ctx。**必须验证 KV cache 量化 (FP8/INT8) 的精度损失**。

2. **MoE 带宽瓶颈误判**：假设 decode 是带宽瓶颈，但 prefill 阶段是算力瓶颈。若工作负载 prefill 占比高 (如长 prompt 短 response)，则算力 (D3) 比带宽 (D2) 更重要。**需明确工作负载的 prefill/decode 比例**。

3. **软件栈成熟度陷阱**：Apple Silicon 的 MLX 对 MoE 262K ctx 的支持可能不如 NVIDIA 的 vLLM 成熟。RDNA4 的 ROCm 支持 [不确定]。**必须实测，不能仅看硬件 spec**。

4. **多卡/多节点互联开销**：若使用多卡 (如 4×5090)，PCIe 带宽 (64GB/s) 远低于 HBM 带宽，MoE expert 跨卡通信会导致性能骤降。**单卡/单节点方案优先**。

5. **功耗与散热**：7×24 运行下，M5 Ultra 512GB 功耗 ~200W，年电费 ~$100。H100 功耗 ~700W，年电费 ~$350。若未考虑电力成本，TCO 计算会严重偏差。
