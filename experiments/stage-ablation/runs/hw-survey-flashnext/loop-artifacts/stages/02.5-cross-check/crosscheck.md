# 02.5 交叉核对 — Flash-Next 硬件

> origin: ai · 2026-11-03T23:20+08:00 · **v2 更新 2026-11-04**
> 方法：物理公式反算 + 多源价格比对 + 矛盾记录
> **v2 变更**：M5 Ultra 实测数据到位后重做 §1（~400 t/s 理论值被推翻）；§2 补 CN 价格；§4 arena 交叉拆解降级为本地 27b 独立拆解（decomp-local27b.md）。

## 1. 物理一致性检查（带宽→速度反算）

公式：decode_tok_s ≈ memory_bandwidth_GBps ÷ bytes_per_token
Flash-Next 4bit：active 6B params × 0.5 bytes = 3GB/token（不含 KV cache 和 routing overhead）

| 平台 | BW (GB/s) | 理论 t/s（纯权重） | 实测 t/s | 偏差/说明 | 判定 |
|------|-----------|----------|-------------|------|------|
| M5 Ultra 256/512GB | 1200 | 400 | **60-100+ [实测]**（短 prompt >100，128K ~61，256K ctx 写速 74.7；MacStories oQ4e） | 实测 = 理论的 15-25%。MoE decode 实际瓶颈含 KV cache 读写 + routing + 引擎调度，纯权重带宽公式严重高估 | ✅ **修正**：~400 作废，采用实测区间 |
| M5 Max 128GB | 614 | 205 | 119-126 (实测) | -38~-42% | ⚠️ 实测低于理论（KV cache + routing + 引擎开销合理解释） |
| 2× R9700 (radiance) | 644 (双卡 P2P) | 215 | 137-147 (两个独立第三方实测) | -32~-36% | ✅ 合理（PCIe P2P 非全速 + expert streaming from host pool）。**v2 新增第二复现源**（Level1Techs 137 / Reddit P620 147.2） |
| 1× R9700 (Strata) | 322 (单卡) | 107 | 94.6 (Strata 0.1.42, Reddit bench 同机对照 79.1) | -12~-26% | ✅ 合理（不同 Strata 版本差异大，DFlash2 变量未定） |
| 2× 5070 Ti (capy) | ~500 (DDR5 系统内存) | 167 | 374 (spec) | +124% | 🔴 **矛盾**：374 t/s 需要 1.1TB/s 有效带宽，2× 5070Ti 系统 DDR5 只有 ~500GB/s。DFlash2 spec decoding 可能 2x 加速 → 374/2=187 仍超带宽上限。**此数字不可信，需标注"spec 未验证"** |
| 1× 3090 + 64GB | ~50 (DDR4) | 17 | 47-50 (原报) | +180% | 🔴 **矛盾**：47 t/s 需要 141GB/s 有效带宽，DDR4 双通道只有 ~50GB/s。除非 3090 VRAM 24GB 装下了大部分 expert（176B 4bit=88GB，24GB 只装 27%）→ offload 走 PCIe Gen4 25GB/s → 混合带宽 ~(24×∞ + 64×50)/88 ≈ 不太可能到 47。**需重新核实测量条件** |
| DGX Spark | 273 | 91 | 60 (实测) | -34% | ✅ 合理（引擎开销） |

**结论（v2 更新）**：
1. **M5 Ultra 的 ~400 t/s 理论值被 MacStories 实测推翻**——实际 60-100+ t/s（ctx 相关）。这不影响"M5U 是消费级最快推理平台"的结论（对比对象里没人超过它），但报告中的速度数字必须改用实测区间。物理教训：MoE decode 的有效带宽利用率远低于 dense（KV cache 随 ctx 增长、routing 开销、引擎调度），`BW ÷ bytes_per_token` 只是上限。
2. 2× 5070 Ti 的 374 t/s 和 1× 3090 的 47-50 t/s 两个数字有物理矛盾风险（维持原判）。前者可能是 DFlash2 理论值被误标为实测；后者可能测量条件不同（短序列/小 batch/KV 复用）。报告中必须标注不确定区间。

## 2. 多源价格核验

| 硬件 | 来源 1 | 来源 2 | 来源 3 | 矛盾？ |
|------|--------|--------|--------|--------|
| R9700 US | Newegg $1,699.99 (OOS) | eBay avg $2,650 / ASRock 挂单 $1,413（v2 新增）/ Micro Center $1,700 | gpuprix $1,699-2,730；camelcamelcamel Amazon 3P $2,634 (Nov 1) | ⚠️ 范围大（$1,400-2,730），取中值 ~$2,200 ± 35%。注意：eBay 挂单价 ≠ 成交价，Micro Center $1,700 是最低实售锚点 |
| R9700 JP | ¥379,800 (+103%) | ツクモ PowerColor ¥369,000 / GIGABYTE ¥399,800 (v2 新增) | — | ✅ 两源一致区间 ¥369k-400k |
| R9700 IN | ₹245,800 (+120%) | — | — | 单源，conf 降 |
| **R9700 CN** (v2 新增) | 闲鱼聚合 ¥16,900（区间 ¥15,000-18,000，16 件，30 天 +43%） | 淘宝行货 ¥16,099-17,800（华硕/技嘉涡轮版）；XFX 海外版 ¥29,999 | pconline 行货参考价 ¥10,999-12,999（无成交记录） | ⚠️ 二手/水货 ¥15-18k vs 行货参考价 ¥11-13k 差 40-50%，但后者无实际成交。**采用 ¥15-18k（≈$2,300-2,600）为采购决策价** |
| M5 Ultra 96GB base | Apple $5,499 | progressiverobot/CNET 同价 | — | ✅ 一致（这是 96GB 基础款，不是 512GB） |
| **M5 Ultra 512GB** (v2 修正) | MacRumors 2026-10-28: **$22,299 起**（$6,799 顶配芯片 + $15,500 内存升级） | voltgridnews 转述同构 | CNET 测 256GB/4TB ≈ $12,300 | 🔴 **原报告 "$5,499+" 错误**——那是 96GB 基础款。512GB 真实价格 $22,299+，比 2×R9700 方案贵 3 倍多 |
| M5 Ultra 256GB | Engadget 测试配置 $11,299 (2TB) | CNET 256GB/4TB ≈ $12,300 | — | ✅ 一致区间 $11-12.5k |
| 2× 5070 Ti | ~$2,000/card × 2（US 溢价后） | 淘宝 TUF 5070 Ti ¥8,499 / ROG ¥8,999 (v2 新增) | — | ⚠️ US ~$4k vs CN ¥17-18k（~$2,400），CN 反而便宜 |
| 3090 used | ~$700-800/card | — | — | 二手市场波动大 |
| RunPod A100 80GB (v2 新增) | runpod.io 官方 $1.19/hr (PCIe Community) / $1.79 (Secure) | computeprices.com 同价 (10/28) | dev.to 引 $1.79 | ✅ 一致。原报告 "$1.2-2/hr" 准确 |

## 3. 矛盾记录与处置

| # | 矛盾 | 涉及 | 处置 |
|---|------|------|------|
| C1 | 2× 5070 Ti "374 t/s" vs 物理带宽上限 | v3.1 第一梯队推荐 | **降级为"spec 未验证"**，不进入决策矩阵主表，仅列参考值 |
| C2 | 1× 3090 "47-50 t/s" vs DDR4 带宽 | v3.1 第二梯队 | **标注"测量条件待确认"**，保守估计 25-35 t/s |
| C3 | 本机 M1 Max 27B "200 t/s" vs 400GB/s 物理上限 28 t/s | MEMORY.md baseline | **物理不可能**。200 t/s 必来自其他机器或不同测量口径（如 aggregate throughput with batching ≠ single-stream decode）。标记为 [待成璐确认] |
| C4 | Flash-Next 总参数 176B vs 125B（两来源） | 模型规格 | 取 HF model card 为准（176B），125B 可能是旧版本或 active-only 误读。**注：MacStories/YouTube 引述中也有 "125 billion parameters" 的说法**——HF model card 的 176B 含 vision tower + MTP head 的可能性更大，纯 LLM 部分可能 ~125B。不影响内存需求结论（以 .rad 容器实测 113.6GiB 为准） |
| **C5** (v2) | M5 Ultra 512GB "$5,499+" vs MacRumors $22,299 | 原报告 §1/§2 | **原报告错误**。$5,499 = 96GB 基础款（30-core/64-core）；512GB 必须顶配芯片 + $15,500 内存升级 = $22,299+。修正后 M5U 512GB 不再是"比 2×R9700 贵 $700"，而是贵 ~$16k。性价比叙事需重写 |
| **C6** (v2) | M5 Ultra "~400 t/s 理论" vs MacStories 实测 60-100+ | 原报告核心卖点 | **理论值作废**。实测区间 60-100+ t/s（ctx 相关）。M5U 仍是消费级最快，但速度优势从"碾压"变为"领先 ~1.5-2x"（vs 2×R9700 137-147） |

## 4. arena 交叉拆解检验

[已完成 · v2] 按 decomp §4 要求做 ≥2 agent 独立拆解。arena 不可用（Perplexity 登录态失效 + stage-ablation subagent 占资源），**降级为本地 27b 独立拆解**：
- Agent A（Lead 自拆）：decomposition.md §2-§3
- Agent B（本地 qwen3.8-27b @ 8787，temp=0，独立 prompt 不给答案）：`decomp-local27b.md`
- 对比与仲裁：见 `decompcmp.md`（差异项 + 处置）
- conf：0.5（单模型非真独立——同族模型共享训练偏差；且 27b 知识截止可能早于 2026-11 行情，只用于结构/方法论审查，不用于事实核验）

**停止理由记录**（对抗核验 r29 补丁要求）：arena 通道穷尽（ego-browser Perplexity 登录态失效，重登需人工扫码 = 个人信息搜集瓶颈）→ 降级本地，流程不豁免。

## 5. 自检

- [x] 关键结论 ≥2 独立来源？→ 价格类 ✅（R9700 US/JP/CN 各 ≥2 源；M5U 定价 MacRumors+CNET+progressiverobot）；速度类 ✅（M5U Flash-Next 实测：MacStories + voltgridnews + llmcheck + YouTube 引述；2×R9700 radiance：Level1Techs + Reddit P620 两个独立复现）
- [x] 矛盾已记录并给出处置？→ 6 条矛盾（C1-C6），全部有处置
- [x] 物理一致性全查？→ 7 个平台全过，2 个标红（5070Ti 374 / 3090 47-50），1 个修正（M5U 400→实测区间）
- [x] arena 交叉拆解？→ 降级本地 27b（decomp-local27b.md + decompcmp.md），conf 0.5
- [x] 对抗核验（r29）：对核验方结论做过主动质疑？→ C6 的质疑点：MacStories 是媒体不是实验室，oQ4e 量化格式未说明是否等于 radiance .rad 容器 → 处置：保留区间表述"60-100+"而非单点值，标注量化格式差异风险。停止理由：穷尽可查渠道（Apple MLR 官方无 Flash-Next 数字），碰到个人信息搜集瓶颈
