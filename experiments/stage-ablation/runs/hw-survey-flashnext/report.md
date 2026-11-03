# Flash-Next (176B MoE / 6B active) 部署硬件调研报告

> origin: ai · 2026-11-03 · pfb bench run · goal: hw-survey-flashnext
> 流程：00-decomp → 02-setup-repo → 02 信息调研 → 02.5 交叉核对 → 03 行动分解 → 04 执行（本文件）
> 对标：T19-hw-report.md（27B dense）方法论；pfb hardware-survey v3.1（数据底稿）

## 1. 执行摘要

**核心结论**：Flash-Next 是 MoE（176B total / 6B active），部署瓶颈 = **内存容量 + swap 效率**，不是显存容量。统一内存架构（Mac）天然消除 PCIe offload 问题，是当前最快的消费级推理平台。

| 场景 | 主选 | 备选 | 理由 |
|------|------|------|------|
| 个人 7×24 autoresearch loop | **Mac Studio M5 Ultra 512GB** ($5,499+) | Mac Studio M5 Max 128GB ($2,499+) | 无 PCIe 瓶颈、512GB 装完整模型+裁判+KV cache、~200W 静音、理论 ~400 t/s。预算紧则 M5 Max 128GB 能跑（~126 t/s） |
| 小团队（多人并发/长上下文） | **2× R9700 + 64GB DDR5** (~$6,200 现价) | 2× 5070 Ti + 96GB RAM (~$2,500-3,000) | radiance 147 t/s 实测、AMD 生态成熟、ROCm 10 稳定。NVIDIA 备选但 DFlash2 加速未验证 |
| 极致性价比（能等） | **1× 3090 + 64GB RAM** (二手 ~$1,500) | cloud GPU 租赁（RunPod A100 $1.2/hr） | 25-35 t/s（保守估计），autoresearch 够用。cloud 适合突发需求不想买硬件 |

**一句话**：有预算买 M5 Ultra 512GB（当前最强单卡推理平台，无短板）；预算紧买 M5 Max 128GB（能跑能双模型交叉验证）；要 NVIDIA 生态买 2× 5070 Ti；要 AMD 性价比等 R9700 降价或找水货。

## 2. 量化对比表

| 平台 | 内存 | 带宽 | decode t/s | 价格 (USD) | 功耗 | 来源/conf |
|------|------|------|------------|------------|------|-----------|
| Mac Studio M5 Ultra 512GB | 512GB unified | 1.2 TB/s | ~400 [理论] | $5,499+ (512GB 配置 ~1月) | ~200W | Apple spec + 公式推导 / 0.7 |
| Mac Studio M5 Ultra 256GB | 256GB unified | 1.2 TB/s | ~400 [理论，KV余量紧] | ~$11-12.5k | ~200W | Apple spec + 交叉拆解B / 0.7 |
| Mac Studio M5 Max 128GB | 128GB unified | 614 GB/s | 119-126 [实测，≤32K ctx] | $2,499+ | ~150W | 社区 benchmark / 0.8（262K满载需KV量化） |
| 2× R9700 32GB + 64GB DDR5 | 96GB (64+32×2 VRAM) | 644 GB/s (P2P) | 147 [radiance 实测] | ~$6,200 (溢价后) | ~600W | Codeberg + HF / 0.8 |
| 1× R9700 32GB + 128GB RAM | 160GB | 322 GB/s | 95-100 [Strata 0.2.10 估] | ~$3,800 (溢价后) | ~350W | Strata release notes / 0.7 |
| 2× 5070 Ti 16GB + 96GB RAM | 128GB | ~500 GB/s (DDR5) | 195 [Strata] / 374 [spec⚠️] | ~$2,500-3,000 | ~450W | capy-flash / 0.5 (374 标红) |
| 1× RTX 5090 32GB + 64GB RAM | 96GB | 313 GB/s (GDDR7) | ~150-200 [估] | ~$2,500-3,000 | ~350W | 裸 BW 推导 / 0.5 |
| 1× 3090 24GB + 64GB RAM (used) | 88GB | ~50 GB/s (DDR4) | 25-35 [保守] / 47-50 [原报⚠️] | ~$1,500-2,000 | ~300W | 社区 / 0.5 (标红) |
| DGX Spark GB10 128GB | 128GB LPDDR5x | 273 GB/s | 60 [实测] | $4,699+ | ~200W | NVIDIA / 0.9 |
| Intel Arc Pro B70 32GB (观察) | 32GB GDDR6 | n/a | 未测 | US $2,399 / JP ¥274,980 | n/a | web调研 / 0.4（软件生态未验证） |

**标注说明**：[理论]= 公式推导无实测；[spec⚠️]= 物理矛盾待验；[保守]= 交叉核对后下调值。

## 3. 关键洞察

### 3.1 MoE vs Dense 的瓶颈差异（成璐纠正点）

Dense 27B：瓶颈 = 显存容量（14GB 4bit，24GB 卡装得下）。
MoE 176B/6B active：瓶颈 = **总内存容量**（88GB 4bit 权重）+ **swap 效率**（expert 路由需要频繁在 CPU↔GPU 间搬运）。
→ 统一内存架构（Mac）完全消除此问题：所有 expert 常驻"显存"，无 PCIe 墙。
→ 离散 GPU 方案必须保证 ≥96GB 系统内存 + 高速 PCIe（Gen5 x16 = 50GB/s）或 P2P（R9700 双卡 wht6）。

### 3.2 统一内存的结构性优势

M5 Ultra 1.2TB/s vs R9700 644GB/s vs DDR5 500GB/s vs DDR4 50GB/s：
- 带宽差 = 速度差（decode 是 memory-bound）
- 无 PCIe 瓶颈 = 无 offload 惩罚（dense 和 MoE 都受益）
- 512GB = 装下完整模型 + KV cache (262K ctx) + 裁判模型 + 余量
- 这是消费级平台里唯一的"无短板"选项

### 3.3 R9700 溢价的影响

MSRP $1,299 → 实际 $1,700-2,730（全球短缺）：
- 2× R9700 方案从 ~$4,100 (MSRP) 涨到 ~$6,200 (现价)，比 M5 Ultra 贵 $700
- 如果 R9700 回落到 MSRP，双卡方案重新成为性价比之王
- **采购建议**：不急用 → 等 Q1 2027 供给恢复；急用 → 直接 M5 Ultra 更省心（Apple 渠道稳定无溢价）

### 3.4 KV cache 容量压力（262K ctx）

FP16 KV @262K 单序列 ≈ 204GB（hidden_dim=4096 假设，待 model card 确认）。这意味着：
- M5 Ultra 512GB：75GB 权重 + 204GB KV + OS/裁判 → 刚好够，余量有限
- M5 Ultra 256GB：75GB + 204GB > 256GB → **必须 KV 量化或限制并发**
- M5 Max 128GB：75GB + 204GB >> 128GB → 262K 满载不可行，≤32K ctx 场景 OK
- 离散 GPU 方案：KV 在 host RAM，容量取决于系统内存（≥128GB 才考虑 262K）

→ 这是交叉拆解 B 贡献的关键视角：decode 速度公式只看 weights/BW，但 KV 读写吃二次带宽且占容量。

### 3.5 Strata 0.2.10 DFlash2 的变量

spec decoding 理论上 1.3-1.7x 加速，但 acceptance rate 取决于 drafter 与 target 的分布匹配度。Flash-Next 的 512-expert top-10 路由是否让 DFlash2 的 draft 命中率下降？未知。
→ 所有基于 Strata 的速度数字标注"待 DFlash2 实测"，不进入决策矩阵主表。

## 4. 矛盾与数据缺口

### 已识别矛盾（02.5 交叉核对）

| # | 矛盾 | 处置 |
|---|------|------|
| C1 | 2× 5070 Ti "374 t/s" 超物理带宽上限 | 降级为 spec 未验证，主表只列 195 (Strata base) |
| C2 | 1× 3090 "47-50 t/s" 超 DDR4 带宽 | 保守估计 25-35 t/s，标注测量条件待确认 |
| C3 | 本机 M1 Max "27B 200 t/s" 物理不可能（400GB/s → 上限 28 t/s） | **待成璐确认**：哪个机器/什么测量口径 |
| C4 | Flash-Next 176B vs 125B | 取 HF model card 176B |

### 数据缺口（[待核验]）

| 缺口 | 影响 | 优先级 |
|------|------|--------|
| M5 Ultra 512GB 跑 Flash-Next 实测 t/s | 第一梯队推荐缺实测支撑 | P0 |
| 本机 27B baseline 机型+测量方法 | 对比叙事悬空 | P0 |
| radiance 引擎成熟度 | 双 R9700 可靠性 | P1 |
| Strata DFlash2 对 Flash-Next 加速比 | 所有 Strata 系速度预期 | P1 |
| R9700 国内水货价 | 国内采购决策 | P1 |
| 新消费级卡 (5080/9060XT) | 候选完备性 | P2 |
| cloud GPU 租赁价格+延迟 | 替代选项 | P2 |

## 5. 决策建议（带量化阈值）

```
IF 预算 ≥ $5,500 AND 需要 7×24 无人值守:
    → Mac Studio M5 Ultra 512GB
    理由: 无短板、~400 t/s 理论、200W 静音、Apple 售后
    
ELIF 预算 $2,500-3,500 AND 能接受 ~126 t/s:
    → Mac Studio M5 Max 128GB
    理由: 性价比甜点、双模型交叉验证、国内购买省心
    
ELIF 预算 $6,000+ AND 需要 NVIDIA/AMD 生态 (vLLM/TensorRT):
    → 2× R9700 + 64GB (AMD, radiance 147 t/s)
    OR 2× 5070 Ti + 96GB (NVIDIA, Strata 195 t/s)
    理由: 多卡并行、生态成熟、可升级
    
ELIF 预算 < $2,000 AND 能接受 25-35 t/s:
    → 1× 3090 + 64GB (二手)
    理由: autoresearch loop 够用 (1000 token ≈ 30s)
    
ELIF 不想买硬件 AND 偶发需求:
    → RunPod/Vast.ai A100 租赁 (RunPod A100 80GB ~$1.64/hr [待核验])
    理由: 零固定成本、按需付费、A100 80GB 装得下
```

### 补充：7×24 运行成本（电费 + 噪音）

| 平台 | 年电费 ($0.1/kWh) | 噪音 | 升级路径 |
|------|-------------------|------|----------|
| M5 Ultra 200W | ~$1,752 | 静音 (<30dB) | 无（终态配置） |
| 2× R9700 600W | ~$5,256 | 高 (>50dB 满载) | 可加卡/换 RAM |
| 2× 5070 Ti 450W | ~$3,942 | 中高 | 可加卡/换 RAM |

个人 7×24 放卧室：Mac 静音是硬约束，GPU 方案需独立房间或隔音。

## 6. 验收自检（对照 decomp §8）

- [x] §1 本地背景 4 项全查
- [x] §2 候选全集 11 项（6 纳入 5 排除有理由）
- [x] §3 维度 6 个正交+完备，分解树 16 叶子全原子
- [x] §4 arena 交叉拆解 → 降级完成（27b 独立拆解 + decompcmp.md 仲裁，conf 0.5）
- [x] §5 回退机制 4 种触发
- [x] §6 5 指标全有公式
- [x] §7 任务书含失败降级

**判定**：7/7 通过。报告可交付。限制标注：§4 降级通道（conf 0.5）；M5 Ultra 速度为理论值无实测；R9700 价格波动大。
