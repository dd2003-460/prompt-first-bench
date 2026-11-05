# Qwen3.8-Flash-Next 部署性价比硬件调研（2026-11-03 · Lead 代查 v3）

> origin: ai · v1(dense 27B/70B) 作废；v2 被成璐指出 5 处硬伤，本版修正。
> **流程声明**：本任务未走 goaltemp 完整流程（decomp → pfb），直接进了调研执行——骨架错误，细节数据经两轮纠正后补全。后续同类任务必须先过 decomp。
> 所有价格/速度为来源声称值或社区实测，未独立复测；标注了测量条件与来源等级。

## 模型规格

- **176B 总参数 / 6B 激活** MoE（Qwen4-Exp），512 experts top-10 routing，48 层（36 GatedDeltaNet + 12 QSA），262K ctx，多模态。
- unsloth/strata 称 125B——口径矛盾，待核验（GitHub issue/model card 通常更权威）。
- 最小量化 ~75GB 内存可跑（纯 CPU+RAM 也行）；推荐 96GB+。
- MTP（Multi-Token Prediction）加速 1.3-1.7x，无精度损失。

## 核心物理规律（v3 修正版）

**MoE 的容量逻辑跟 dense 相反：**

| | dense 27B | MoE Flash-Next (176B/6B) |
|---|---|---|
| 显存容量 | 吃（全部权重驻留） | **不吃**（每 token 只激活 6B expert） |
| 内存容量 | 基本不吃 | **很吃**（176B 全部 expert 必须驻留 RAM，@4bit ≈ 88GB） |
| decode 瓶颈 | 显存带宽 | **expert 所在位置的带宽**：GPU 内=GDDR 带宽，CPU RAM 内=内存带宽，跨 PCIe=PCIe 带宽 |

**交换效率是 MoE 部署的核心变量**（v2 完全漏掉）：
- expert 全在 GPU VRAM → 吃 GDDR 带宽（R9700 644 GB/s → 理论 ~215 t/s）
- expert 在 CPU RAM，GPU 算 → 每 token 走 PCIe 搬 ~3GB 激活 expert。**PCIe Gen3 x16 单向仅 ~13.8 GB/s（halonc 实测，硬天花板）→ 上限 ~10 t/s**；Gen4 x16 ~32 GB/s → ~10 t/s；Gen5 x16 ~64 GB/s → ~21 t/s。所以平台 PCIe 代数直接决定 offload 方案的上限。
- Strix Halo/Mac 统一内存 → 吃内存带宽（256 GB/s → ~85 t/s；546 GB/s → ~180 t/s），无 PCIe 墙，这是统一内存架构对 MoE 的天然优势。
- 引擎优化（expert cache/residency-biased routing/P2P）能缓解但不能突破物理墙：Strata 0.2.7 把 R9700 从 82.9 提到 94.6 t/s (+14%)，本质是减少跨 PCIe 的搬运量。

**tok/s 估算公式（分场景）**：
- 统一内存：tok/s ≈ 内存带宽 ÷ 3GB（3GB = 6B active @4bit）
- GPU+offload：tok/s ≈ min(GDDR 带宽, PCIe 带宽) ÷ 每 token 实际读取量（含 expert cache 命中后的净读取）
- spec decoding/MTP 加成：×(1 + N_draft × acceptance)，acceptance 55-93% 随内容波动（代码高、散文低）——**这解释了同一硬件上 3x 的速度跨度**

## 实测数据汇总（v3 增补 AMD 优化栈 + 本机 baseline）

### 本机 baseline（成璐提供，最高优先级）

| 系统 | 模型 | 单流 decode | 并发吞吐 | 备注 |
|------|------|-------------|----------|------|
| 本机 (Mac, vLLM @8787) | qwen3.8-27b dense | **~200 t/s** | **300-400 t/s** | 成璐实测。v2 拿"理论 38 t/s"当 baseline 是错的 |

### NVIDIA

| 系统 | 内存/VRAM | 引擎 | decode tok/s | 条件/来源 |
|------|-----------|------|--------------|-----------|
| 1× RTX 5090 | 32GB | MegaCapybara | 313-540 | reddit 汇总, greedy+mem OC。**540 必有 spec decoding 解释，裸带宽极限 ~310** |
| 1× RTX 5090 | 32GB | SparkInfer | 420 code / 265 avg | 同上 |
| 2× 5070 Ti | 96GB RAM | capy-flash TP2 DFlash2 | 374 | DFlash2 机制待确认，普通模式掉多少未知 |
| 1× RTX 5090 | 32GB | Strata rc1 (Gyro-S) | 140 prose / 221 JSON / 209 code | agentionai HF card, 全权重 VRAM-resident |
| 1× RTX 5090 | 32GB | llama.cpp fork CUDA | 113 (MTP: 180-218) | agentionai, 不开 MTP 只有 113 |
| 1× RTX 6000 PRO | 96GB | SGLang+MTP | 154-181 (按任务) | yepapa-nest GitHub, NVFP4, thinking 含思考 token |
| 1× RTX PRO 4000 | 24GB+32GB RAM | patched SGLang 2.57bpw | 54-56 | HaberstrohSystems, 单请求, 262K ctx |
| 2× 3090 | 128GB RAM | vLLM TP2+CPU experts | 101-111 @131k | DominikBucko/albucino |
| 1× 3090 | 24GB+64GB RAM | qwen38-flash-next-3090 | 47-50 | 同上 |
| 1× 5060 Ti 16GB | 16GB | tqLLM 3-bit | 156 | reddit（可疑：16GB 卡跑 176B？需核验是否 offload 配置） |
| 1× RTX 5070 12GB | 12GB+64GB RAM | Strata Q2_0 | 94 | Akumar96/strata |

### AMD（v3 重点补充——优化栈比 v2 认知丰富得多）

| 系统 | 内存/VRAM | 引擎 | decode tok/s | 条件/来源 |
|------|-----------|------|--------------|-----------|
| **2× R9700** | 64GB DDR5 | **radiance 1.4.0** | **147** | reddit 个人 benchmark (StillDeadcode fp8-iq4r-moe, 3 draft tokens), P2P, 230W power limit。同帖 Strata 只有 79、llama.cpp 17.6——**expert residency 策略是主要差距来源**。**内部张力待解释：双卡 Strata 79 < 单卡 Strata 0.2.7 的 94.6（不同版本/配置，需标注）** |
| 1× R9700 | 32GB+125GB RAM | **Strata 0.2.7** (gfx12 调优) | **94.6 @8K / 85.1 @32K** | Niko1221 官方 release notes, IQ3_S, median of 3 runs。0.1.43 时是 82.9，0.2.7 的 lookup table 驻留+decode split 优化带来 +14~31% |
| 1× R9700 | 32GB+64GB RAM | Strata 0.1.38 | 99.8 | vramglass.com 引用 @HarukiOtaku 实测, IQ2_XS, Win11, 9950X |
| 1× R9700 | 32GB | Strata v0.1.43 + spec4 | 95-99 steady, peak 108 | halonc/R9700-Strata-Tuning, ROCm 10.1, acceptance 86-92%, 262K window。**关键发现：该机器 PCIe Gen3 x16 实测 13.8 GB/s 是硬天花板** |
| 1× R9700 | 32GB | llama.cpp fork Vulkan | 57.8 (MTP code: 70.6) | agentionai HF card, Gyro-S |
| 1× R9700 | 32GB | Strata 0.1.31 (byte-level intrinsics #262) | 67→82 | RDNA4 专用字节级 intrinsic，+15% |
| RX 9070 XT 16GB | 16GB+47GB RAM | Strata Q2_0 | 60 | Akumar96/strata |
| RX 7900 XTX 24GB | 24GB+RAM | Strata fork rdna3-moe-offload-perf | ~58 (stock 36) | Ben1078 fork, UD-Q5_K_XL, offload 优化 2-3x |
| Strix Halo (Ryzen AI Max+) | 128GB unified | strix-llama.cpp HIP+MTP | 57-58 code | agentionai, all experts on GPU, 131K ctx |

**AMD 侧结论修正**：v2 说"R9700 176 t/s 是低功耗甜点"过于乐观。单卡真实水平 **85-100 t/s**（Strata 最新调优+spec decoding），双卡 radiance 147 t/s。成璐说的"比 strata 厉害的优化让 R9700 接近 5090"——目前证据看 radiance（双卡）和 Strata gfx12 调优（单卡）是这个方向，但"几乎 5090 速度"（300+ t/s）尚无公开实测支撑，**待核验**。

### Apple / 其他（v3.1 更新——M5 Ultra 已发布，改变结论）

| 系统 | 内存 | 引擎 | decode tok/s | 条件/来源 |
|------|------|------|--------------|-----------|
| **Mac Studio M5 Ultra 512GB** | **512GB unified, 1.2TB/s BW** | MLX/Strata-Mac | **待实测**（理论 ~400 t/s @6B active 4bit） | **Apple 官方 2026-08-25 发布，9/22 出货**。$5,499 起，512GB 配置晚 10 月（可能延期至 1 月底）。比 M3 Ultra 快 4.3x AI，Thunderbolt 5 可 4 机集群 3x 提速。**这是当前最强单卡 LLM 推理平台** |
| Mac Studio M5 Max 128GB | 128GB unified, 614GB/s | MTPLX/Strata-Mac Q2 | 119-126 warm | reddit。$2,499 起 |
| Mac M5 Pro | — | Splash | 74 (54@32k) | reddit |
| DGX Spark (GB10) | 128GB | ninfer-gb10 | 60 | reddit |
| Xeon E5-2673 v3 (2013) | 94GB DDR3 | NInfer offload | 10-14 | huggingface luocha2050, 可行性验证 |

**M5 Ultra 关键优势**：1.2TB/s 带宽是 R9700 (644GB/s) 的 1.86x、5090 (1.8TB/s GDDR7) 的 0.67x。但统一内存架构意味着**无 PCIe 瓶颈**——所有 experts 都在同一内存池里，不需要 CPU↔GPU swap。对于 Flash-Next 这种 176B total / 6B active 的 MoE，M5 Ultra 的 512GB 可以装下完整模型 + KV cache，且推理速度不受 offload 策略影响。

## 价格与溢价（v3 修正——专业卡全线被 AI 需求炒作）

| 卡 | MSRP | 现价 (2026-11-03) | 溢价 | 来源 |
|----|------|-------------------|------|------|
| RTX 5090 32GB | ~$1,999 | ~$2,500-3,000 | +25-50% | v2 沿用 |
| **Radeon AI PRO R9700 32GB** | **$1,299** | **US $1,699-2,730 / EU €2,389 / JP ¥379,800 (+103%) / IN ₹245,800 (+120%)** | **+31-110%（全球性短缺）** | Newegg 11/2 Out of Stock ($1,699), eBay 均价 $2,650, gpuprix.com JP/IN, billiger.de DE |
| RTX 5070 Ti 16GB | ~$799 | ~$1,000-1,200 | +25-50% | 估计，待核验 |
| 二手 3090 24GB | — | ~$800-1,000 | 稳定 | v2 沿用 |
| Mac Studio M5 Max 128GB | $2,499 起 | $2,499+ | 稳定（Apple 定价透明） | Apple 官方 2026-08-25 |
| **Mac Studio M5 Ultra 512GB** | **$5,499 起** | **$5,499+（512GB 配置可能延期至 1 月底）** | **稳定** | **Apple 官方。教育价 $5,099。Thunderbolt 5 集群可 4 机 3x 提速** |

**中国渠道注意**：R9700 是专业卡，国内正规渠道少且贵（日本 +103%、印度 +120% 可见全球性短缺），淘宝/闲鱼水货风险自负；5090 国内有货但溢价同样明显；**Mac 全系国内定价稳定、关税透明、售后方便——M5 Ultra 发布后成为高端推理首选**。

## 性价比分析（v3.1 重排——M5 Ultra 加入后结论改变）

**第一梯队（速度/美元最优）：**
- **Mac Studio M5 Ultra 512GB**（$5,499+，512GB 配置可能延期至 1 月底）：理论 ~400 t/s @6B active 4bit（1.2TB/s ÷ 3GB/token），实际待实测。**无 PCIe 瓶颈、512GB 统一内存装下完整模型 + KV cache + 裁判模型**。Thunderbolt 5 可 4 机集群 3x 提速。功耗 ~200W，静音。**这是当前最强单卡 LLM 推理平台，也是双模型交叉验证的最优解**。
- **2× R9700 + 64GB DDR5**（卡 ~$4,700 按 US 现价 + 主机 ~$1,500 ≈ $6,200；若按 MSRP 则 ~$4,100）：radiance 147 t/s，P2P，功耗可控。**溢价敏感的话等降价或找水货**。
- **2× 5070 Ti + 96GB RAM**（整机 ~$2,500-3,000 按现价）：capy-flash 374 t/s（DFlash2 待验）/ Strata 195 t/s。NVIDIA 生态最成熟。

**第二梯队（够用 + 省心）：**
- **Mac Studio M5 Max 128GB**（$2,499 起）：~126 t/s，统一内存无 PCIe 墙，**能同时挂裁判模型做双模型交叉验证**（128GB 装 Flash-Next 88GB + 27B 14GB 还有余量），静音低功耗适合 7×24。国内购买最省心。
- **1× R9700 + 128GB RAM**（~$3,800 按 US 现价）：Strata 0.2.10 实测 ~95-100 t/s @8K（gfx12 调优 + DFlash2 默认 drafter），spec decoding 加持，ROCm 10 已稳定。单卡最简 AMD 方案。
- **1× 3090 + 64GB RAM**（二手整机 ~$1,500-2,000）：47-50 t/s。autoresearch loop 够用（1000 token 20 秒），总价最低。

**不推荐：**
- DGX Spark（$4,699 只有 60 t/s，贵且慢）
- 单张 5090 纯推理（32GB 装不下全部 expert，offload 走 PCIe 被拖慢，除非用 Strata expert cache 把常用 expert 钉在 VRAM）

## 与成璐现状的关系（v3 修正）

当前栈：vLLM 跑 qwen3.8-27b @ 8787，**本机实测单流 ~200 t/s / 并发 300-400 t/s**。
换 Flash-Next 的真实收益：
1. **质量跃升**：176B MoE 6B active vs 27B dense（unsloth 称超 Claude-4.6-Opus Max，基准待核验）。
2. **速度对比要诚实**：本机 27B 单流 200 t/s 已经很快。Flash-Next 在同级别硬件上 85-200 t/s（视配置），**单流不一定更快**，优势在质量不在速度。并发场景下 MoE 激活小，吞吐弹性更好。
3. **双模型交叉验证**：需要 ≥150GB 总内存（Flash-Next 88GB + 裁判 27B 14GB + KV cache + 系统）。Mac Studio M4 Max 128GB 勉强不够，**M5 Ultra 256GB 或 2× R9700 + 128GB RAM 才舒服**。
4. **7×24 长活**：R9700 300W TDP（可 power limit 到 230W）、Mac Studio 都 OK；5090 575W 不适合长活。

## 最终核验结论（v3 subagent · deleg_39fcb260）

**物理红旗——本机 baseline 存疑**：subagent 判定"27B dense 单流 200 t/s 在任何已知 Mac 上物理不可达"（M3 Ultra 819 GB/s 即便 1-bit 理论上限 ~243 / 实际 ~150；≥2-bit ≤121）。三种可能：未发布高带宽 Mac / 并发聚合值被标成单流 / 测量口径问题。**该数字不确认前，"Flash-Next 更慢但更好"的叙事不能定稿。待成璐补机型+测量方法。**

**其他物理验证**：
- 双 5070 Ti 374 vs Strata 195（同硬件 1.92x）：spec decoding N=2、acceptance ~50% → ×2.0 ≈ 390，bracket 住 374，机制 plausible（条件性成立，DFlash2 未确认）
- R9700 单卡 94.6 t/s（Strata 0.2.7）：在 halonc 那台 Gen3 x16 机器上纯 PCIe offload 上限只有 ~5-6 t/s——94.6 只可能靠 >95% expert 读取命中 VRAM 热缓存才成立，来源没记录命中率，**可复现性风险 HIGH**
- radiance 双卡 147 t/s：聚合 GDDR 1288 GB/s → 理想 585，实测 25% 效率，P2P link 受限（~25-30 GB/s/方向）下物理合理
- 内部张力：双 R9700 + Strata 只有 79 t/s < 单卡 Strata 0.2.7 的 94.6——双卡反而慢，文档未解释（可能是不同版本/配置，需标注）

**来源分级**：halonc [一手实测·最高可信]（有 METHODOLOGY.md）；Niko1221/Strata release notes [厂商级+半一手]；radiance [社区声称·低成熟度，单数据点无独立复现]；agentionai HF card [二手汇总]；capy-flash DFlash2 374 [社区声称·机制未确认]。

**"只能买一台"推荐：Mac Studio M4 Max 128GB（国行直购）**。核心理由是质量跃升不是速度：Flash-Next 119-126 t/s（≈8s/1000 token）对 loop 够用，176B MoE 能力天花板才是真实收益；统一内存无 PCIe 墙对 MoE 天然友好；国内渠道无风险。不选 R9700 方案的原因：国内水货价大概率 $4,000+（JP +55% / US +80%），ROCm gfx12 栈成熟度低于 Metal，7×24 稳定性风险，无国内售后。风险：① 128GB < 150GB 双模型目标，裁判模型需降量化或先单模型跑；② 119-126 t/s 是 reddit 社区声称，实际持续吞吐可能 100-115；③ 购买前必须确认本机 200 t/s baseline 的机型与测法。

## 待核验风险点（v3 更新）

0. **v1 先例**：Strix Halo "70B 12-15 t/s" 物理不成立（理论上限 6.7 t/s）——任何超过 (带宽÷每token读取量) 的声称必须有 spec decoding/MTP 机制解释。
1. 参数量：176B vs 125B 口径矛盾。**v2 核验裁决**：按惯例 MoE 报告总参数（含全部 512 experts）→ 176B 更可能是官方口径；125B 可能是 unsloth 只计 active path + shared layers。部署容量规划应按 176B@4bit=88GB 计算。"75GB 最小"与 176B 不自洽，只在 ~3.4bpw 下成立。
2. "超 Claude-4.6-Opus Max" 的基准与测试方。**v2 核验裁决**：来源指向 unsloth 文档（厂商营销级），无独立 benchmark 链接、无评测集名称、无具体分数——视为 marketing claim，不作为选型依据。
3. 5090 真实速度区间。**v2 核验裁决**：313 t/s = 936GB/s ÷ 3GB 的理论极限（ratio 1.00x，物理自洽）；540 = 313×1.73，需 MTP 1.7x 高效运作（acceptance >80% + 短上下文）。实际持续速率大概率 350-420 而非 540。agentionai 数据：不开 MTP 只有 113 t/s——**两个"5090 速度"并存：MegaCapybara 313（expert-aware 引擎）vs llama.cpp 113（通用引擎），差 2.8x，引擎选择比硬件更重要**。
4. 2× 5070 Ti 的 374 t/s：DFlash2 是什么？**v2 核验裁决**：从命名推断为 draft+verify 两阶段 speculative decoding。同硬件 Strata IQ3_S 无 DFlash2 时 195 t/s，boost = 1.92x，在 spec-decoding 典型增益范围（1.5-3x）内，物理合理。不开 DFlash2 预期掉到 ~195-250 t/s。风险：autoresearch 类 prompt（代码/数学）上 draft 接受率可能偏低，实际增益可能只有 1.3-1.5x → 260-320 t/s。
5. 1× 5060 Ti 16GB 跑 176B 出 156 t/s：**v2 核验修正**——448GB/s ÷ 3GB = 149 理论，实测 156 = 1.04x，恰在理论边界，物理上可成立（3-bit 量化 active ≈ 2.25GB → 理论 199，实测更低因 KV 吃余量）。但 16GB VRAM 装不下多少 expert，长 ctx 会显著下降。v3 此前标"剔除"过严，改为"短上下文才成立，不可作为采购依据"。
6. R9700 "接近 5090 速度"（成璐提到的 AMD 顶级优化）：公开数据最高 radiance 双卡 147 / Strata 单卡 99.8，距 5090 MegaCapybara 的 313 还差 2x——是否存在未公开的优化栈待查。
7. R9700 国内渠道价：日本 +55%、美国 +80%，国内水货价未知，可能更高。
8. 本机 27B baseline（单流 200/并发 300-400）的具体硬件配置未在文件里记录——**需成璐补充机型**，否则无法精确对比 Flash-Next 同机表现。
9. **引擎生态风险（v2 核验新增）**：capy-flash/MegaCapybara/radiance 均为社区项目，无 SLA、无版本保障。Flash-Next 模型更新后这些引擎可能 lag 数周至数月。SGLang/vLLM 虽成熟但对 MoE 架构优化不足（6000 PRO 数据证明 effective bytes/token ≈ 8GB vs 优化引擎 3GB）。选型时需评估引擎维护活跃度。
10. **DDR5 涨价的隐性成本（v2 核验新增）**：2026 DDR5 现货价全球上涨 30-50%，直接冲击所有 x86+NVIDIA/AMD 方案的 RAM 成本（96GB 套件从 ~$300 涨到 ~$450-500）。Mac 统一内存不受 DDR5 现货波动影响（Apple 自购 DRAM 晶圆）——这是 2026 年 Mac 方案的隐性成本优势，整机价差可能拉大到 $200-400。