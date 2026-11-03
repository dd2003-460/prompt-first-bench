# Decomp: Qwen3.8-Flash-Next 部署硬件调研

> origin: ai · 2026-11-03 · goal: hw-survey-flashnext · stage: 00-decomp
> 本文件只做三件事：分解树、缺口标注、留空。不做调研、不填数字。

## 0. 任务元信息

| 字段 | 值 |
|------|-----|
| 任务名 | Flash-Next (176B MoE / 6B active) 最优部署硬件系统调研 |
| 发起时间 | 2026-11-03 |
| 产出形态 | 报告（含量化对比表 + 分场景推荐 + 采购建议） |
| 对标物 | T19-hw-report.md（27B dense 选型，方法论可复用）；pfb/experiments/stage-ablation/hardware-survey-qwen-deploy.md v3.1（已有数据但未走流程） |

## 1. 本地背景扫描

| 必查项 | 查了吗 | 搜索命令/路径 | 发现 |
|--------|--------|---------------|------|
| 相关项目目录 | ✅ | `ls projects/*D1*gpu*` + grep loop-state.json | D1-gpu-inference-hardware 存在但无活跃 loop-state；decomp 项目有 T19（27B dense 硬件选型，方法论可复用） |
| 已有调研/报告 | ✅ | `find -name "*hardware*" -o -name "*qwen*deploy*"` | pfb/experiments/stage-ablation/hardware-survey-qwen-deploy.md v3.1（137→150 行，含 M5 Ultra/R9700/5090 数据，但跳过 decomp 直接搜的）；T8-matrix 有 D3-hardware-purchase 种子题 |
| 相关记忆 | ✅ | `grep MEMORY.md` | MEMORY.md 有 Flash-Next 模型规格（176B/6B active/512 experts top-10/262K ctx）+ 本机 27B baseline（单流 200 t/s，物理红旗待确认） |
| 用户过往讨论 | ✅ | session_search（压缩前上下文） | 成璐纠正过：MoE 不吃显存容量但吃内存容量+PCIe swap 效率；AMD 有比 Strata 强的优化让 R9700 接近 5090；27B baseline 是实测数据必须用 |

**小结**：本地已有 3 项相关资产（v3.1 调研 + T19 方法论 + 模型规格记忆），本次可复用 v3.1 的数据框架和 T19 的报告结构，需新增：decomp 结构化拆解、arena 交叉验证、最新价格/引擎版本核验。

## 2. 调研对象全集（防遗漏）

| 候选 | 纳入/排除 | 理由 |
|------|-----------|------|
| Mac Studio M5 Ultra 512GB ($5,499+, 1.2TB/s) | **纳入** | 统一内存无 PCIe 墙，512GB 装完整模型+裁判，当前最强单卡推理平台 |
| Mac Studio M5 Max 128GB ($2,499+) | **纳入** | 性价比甜点，能双模型交叉验证，国内购买省心 |
| 2× Radeon AI PRO R9700 32GB + 64GB DDR5 (~$6,200 现价) | **纳入** | radiance 147 t/s 实测，AMD 生态最成熟方案 |
| 1× R9700 + 128GB RAM (~$3,800) | **纳入** | 单卡最简 AMD 方案，Strata 0.2.10 ~95-100 t/s |
| 2× RTX 5070 Ti 16GB + 96GB RAM (~$2,500-3,000) | **纳入** | NVIDIA 生态最成熟，capy-flash 374 t/s（DFlash2 待验） |
| 1× RTX 5090 32GB (~$2,500-3,000) | **纳入** | 裸带宽上限 ~313 t/s，但 32GB 装不下全部 expert 需 offload |
| 1× RTX 3090 24GB + 64GB RAM (二手 ~$1,500) | **纳入** | 总价最低，47-50 t/s，autoresearch loop 够用 |
| DGX Spark GB10 128GB ($4,699+) | **排除** | 60 t/s，贵且慢，性价比最差 |
| Xeon E5-2673 v3 2013 款 (94GB DDR3) | **排除** | 10-14 t/s，仅可行性验证用，无采购价值 |
| Strix Halo Ryzen AI Max+ 128GB unified | **排除** | 57-58 t/s code，低于所有纳入候选 |
| 自建 GPU 服务器（4× A100/H100） | **排除** | 成本 >$50k，超出个人/小团队预算范围 |

**覆盖性自检**：有没有明显该考虑但没列出来的？
- [待核验] 是否有新的消费级卡（如 RTX 5080 16GB、RX 9060 XT）值得纳入？需查最新 release notes
- [待核验] 是否有 cloud GPU 租赁方案（RunPod/Vast.ai）作为"不买硬件"的替代选项？需查价格+延迟

## 3. 正交维度拆解

### 3.1 维度定义

| 维度 | 含义 | 取值枚举 | 检查方法 |
|------|------|----------|----------|
| 架构类型 | CPU/GPU/统一内存 | Mac unified / NVIDIA discrete / AMD discrete / hybrid (CPU+GPU offload) | 每个候选归入唯一架构类型 |
| 内存容量 | 总可用内存（VRAM+RAM 或 unified） | 32GB / 64GB / 96GB / 128GB / 256GB / 512GB | 按配置列出实际可用容量 |
| 内存带宽 | 主内存/显存带宽 | <500 GB/s / 500-800 / 800-1200 / >1200 | 查官方 spec + 实测 benchmark |
| 引擎生态 | 支持的推理引擎 | MLX / Strata / radiance / llama.cpp / vLLM / SGLang | 查引擎文档 + GitHub issues |
| 功耗/噪音 | 持续运行功耗 + 噪音水平 | <200W / 200-400W / >400W | 查 TDP + 用户实测反馈 |
| 价格/渠道 | 当前市场价 + 国内可得性 | MSRP / +溢价 / 水货 / 稳定 | 查多个渠道报价（US/EU/JP/CN） |

**正交性检查**：架构类型 × 内存容量 → 能同时取不同值（Mac 512GB vs R9700 64GB）✅
内存带宽 × 引擎生态 → 能同时取不同值（M5 Ultra 1.2TB/s + MLX vs R9700 644GB/s + radiance）✅
功耗 × 价格 → 能同时取不同值（Mac 200W $5,499 vs 2×R9700 600W $6,200）✅

**完备性检查**：所有 11 个候选都能归入某个维度组合 ✅（DGX Spark = NVIDIA discrete + 128GB + 273GB/s + MLX/vLLM + 200W + $4,699）

### 3.2 分解树（拆到原子）

```
Flash-Next 硬件调研
├── A. 模型规格确认（原子：执行动作=read HF model card + 官方 blog，完成判据=参数/激活/experts/ctx 四个数字有来源）
├── B. 物理模型建立（可继续拆？→ 是）
│   ├── B1. 带宽-速度公式推导（原子：tok/s ≈ BW ÷ bytes_per_token，完成判据=公式+假设列表落盘）
│   ├── B2. MoE 内存占用计算（原子：total_params × bits/8 + KV_cache，完成判据=各配置内存需求表）
│   └── B3. PCIe offload 瓶颈分析（原子：Gen3/Gen4/Gen5 带宽 × swap 频率，完成判据=offload 惩罚系数表）
├── C. 候选硬件数据采集（可继续拆？→ 是）
│   ├── C1. Mac 系列（原子：查 Apple 官网 spec + 社区 benchmark，完成判据=M5 Ultra/Max/Pro 三档数据齐全）
│   ├── C2. AMD R9700（原子：查 Newegg/eBay/gpuprix 价格 + Strata/radiance GitHub release notes，完成判据=价格区间+引擎版本+实测 t/s）
│   ├── C3. NVIDIA 系列（原子：查 5090/5070Ti/3090 价格 + Strata/capy-flash benchmark，完成判据=同上）
│   └── C4. 其他（原子：查 DGX Spark/Strix Halo/cloud 租赁，完成判据=排除理由或纳入数据）
├── D. 交叉验证（可继续拆？→ 是）
│   ├── D1. 物理一致性检查（原子：每个 t/s 数字用 B1 公式反算，偏差 >30% 标红，完成判据=所有数字通过或标红）
│   ├── D2. 多源价格核验（原子：每个价格 ≥2 独立来源，矛盾记录，完成判据=价格表每行有 ≥2 URL）
│   └── D3. arena 外包拆解检验（原子：派 ≥2 agent 独立做 §2-§3，对比差异，完成判据=差异项有解释）
├── E. 报告撰写（原子：按 T19 结构写，完成判据=执行摘要+量化表+洞察+矛盾+决策建议五段齐全）
└── F. 验收（原子：对照 §8 验收标准逐项检查，完成判据=全勾或回退补）
```

**原子性自检**：
- A：不可再拆（读一个文档）✅
- B1/B2/B3：各自有明确公式和产出 ✅
- C1-C4：各自有明确查询目标 ✅
- D1-D3：各自有明确检查方法 ✅
- E/F：单一动作 ✅

## 4. 拆解外包与交叉检验

[待核验] 需派 ≥2 个 arena agent 独立完成 §2-§3 拆解，对比正交性/完备性/原子性。Lead 不自己拆完就往下。

派发计划：
- Agent 1：按本文件 §2-§3 做独立拆解，落盘 `projects/decomp/tasks/test/decomp-agent1.md`
- Agent 2：同任务，落盘 `projects/decomp/tasks/test/decomp-agent2.md`
- Lead 验收：对比两份拆解，差异项记录+仲裁

## 5. 回退与修正机制

| 触发条件 | 回退到 | 修改动作 | 记录 |
|----------|--------|----------|------|
| 发现新候选（§2 漏了） | §2 | 补充候选 + 重新过维度 | 改动原因 + 时间 |
| 物理模型假设被推翻（如 MTP 加速比不符） | B1 | 修正公式 + 重算所有 t/s | 改动原因 + 时间 |
| 价格数据矛盾（同一卡不同渠道差 >50%） | C2/C3 | 增加来源 + 标注不确定区间 | 矛盾点 + 处置 |
| arena 拆解结果与 Lead 差异大 | §3 | 仲裁后更新分解树 | 差异项 + 仲裁结论 |

## 6. 量化定义

| 指标 | 公式/计算方式 | 数据来源 | 单位 |
|------|---------------|----------|------|
| decode tok/s | memory_bandwidth_GBps ÷ bytes_per_token（bytes_per_token = active_params × bits/8 + routing_overhead） | 官方 spec + 实测 benchmark | tokens/s |
| 内存需求 | total_params_B × bits/8 + KV_cache（KV = layers × heads × head_dim × seq_len × batch × 2(K+V) × dtype_bytes） | 模型 config + 计算 | GB |
| 性价比 | decode_tok_s ÷ total_cost_USD（total_cost = 硬件 + 电费年摊销 + 维护） | 价格表 + 功耗 × 电价 | t/s per $ |
| 功耗效率 | decode_tok_s ÷ power_W | 实测 + TDP | t/s per W |
| 长上下文衰减率 | tok_s_at_32K ÷ tok_s_at_4K | 实测 benchmark | ratio |

## 7. 任务书（arena 外包用）

[待核验] 按 agents/arena-loop-pipeline.md §任务书模板生成，包含：
- 调研问题：Qwen3.8-Flash-Next (176B MoE / 6B active) 在 2026-11 的最优部署硬件是什么？
- 已知背景：§1 小结
- 候选范围：§2 全集（11 候选，6 纳入 5 排除）
- 拆解维度：§3 维度表 + 分解树
- 量化口径：§6 公式
- 产出要求：报告含执行摘要 + 量化对比表（≥8 行 × 6 列）+ 关键洞察 + 矛盾清单 + 分场景决策建议
- 失败降级：arena 不可用 → 本地 conf-0.2，只降通道不降流程

## 8. 验收标准（量化门禁）

- [ ] §1：本地背景 4 项全查，每项有搜索证据？
- [ ] §2：候选全集 11 项列出，5 排除项有理由？
- [ ] §3：维度 6 个正交+完备，分解树 16 个叶子节点全原子（有执行动作+完成判据）？
- [ ] §4：≥2 个 agent 独立拆解 + 交叉检验通过？
- [ ] §5：回退机制 4 种触发条件已定义？
- [ ] §6：5 个指标全有公式，无模糊词？
- [ ] §7：任务书按 arena 模板生成，含失败降级？

**全勾 = 可推进到下一阶段。任一未勾 = 回本阶段补。**

## 缺口清单

| 缺口 | 影响 | 优先级 |
|------|------|--------|
| [待核验] 本机 27B baseline 200 t/s 的机型+测量方法 | 对比叙事悬空，不确认则报告不能定稿 | P0 |
| [待核验] M5 Ultra 512GB 配置的 Flash-Next 实测 t/s（目前只有理论 ~400） | 第一梯队推荐缺乏实测支撑 | P0 |
| [待核验] radiance 引擎成熟度（Codeberg star 数/commit 频率/issue 活跃度） | 双 R9700 方案的可靠性评估 | P1 |
| [待核验] Strata 0.2.10 的 DFlash2 默认 drafter 对 Flash-Next 的实际加速比 | 影响所有 Strata 系配置的速度预期 | P1 |
| [待核验] R9700 国内水货价（目前只有 US/EU/JP/IN） | 国内采购决策 | P1 |
| [待核验] 是否有新消费级卡（5080/9060XT）值得纳入 | 候选全集完备性 | P2 |
| [待核验] cloud GPU 租赁方案（RunPod/Vast.ai）价格+延迟 | "不买硬件"替代选项 | P2 |