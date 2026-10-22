# origin: ai · bench round 4 报告（2026-10-23）

## 1. 本轮执行

三路 workflow 并行（A 通道验证 / B V1a·V1b×Q1 / C V2×Q4），commits `78f4222` `e00cb8b` `7140107`+`931556e`，push 成功（`935ced2..e00cb8b`）。

**通道状态**：arena.ai 整站 Cloudflare 封禁持续（round3 05:54 起 → round4 06:5x 探针 Ray ID `a4ec11b18cff0507`）。备用通道 7 站点探测（`bench/config/channel-fallback.md`）：

| 站点 | 状态 |
|---|---|
| DeepSeek | ✅ 已登录可用（唯一海外替代不可用时的国内双源之一） |
| GLM | ⚠️ 访客受限（登录弹窗打断回答） |
| ChatGPT / Google AI Studio / Gemini / Perplexity / LMArena | ❌ 不可达（ERR_CONNECTION_RESET / Cloudflare） |

→ round5 通道决策：**claude/gemini 档 N/A**（arena 封禁 + 网页无对应通道），**qwen 档本地降级**（vllm/qwen3.8-27b-w8a16），**V3 交叉验证用 DeepSeek+GLM 国内双源**（标注"无海外模型交叉"限制）。round5 开跑前复检 arena。

## 2. 分数表

**路 B：V1a/V1b × Q1 × 3 模型（具体题）**

| 变体 | claude | gemini | qwen（降级） | 对照 V0（arena） |
|---|---|---|---|---|
| V0 | 88.5 (n=2) | 85 (n=2) | 82.5 (n=2) | — |
| V1a | N/A | N/A | **81** | −1.5（同模型跨通道不可直接比） |
| V1b | N/A | N/A | **87** | +4.5 |

**路 C：V2 × Q4 × 3 模型（需检索题）**

| 模型档 | V0 | V2（本轮） | Δ |
|---|---|---|---|
| claude | 47 | N/A | — |
| gemini | 95 | N/A | — |
| qwen（降级） | 40 | **80** | **+40（fail→success）** |

## 3. 两个对照的初读数

### 3.1 具体题 vs 模糊题的流程增益差异（第一个二维数据）

- **Q1 具体题**：V1b−V1a = **+6**，增益分解 D1 正确性 +0（两变体都答对核心内容）/ D3 结构正交 +2 / D4 置信度标注 +3。→ 具体题上模型"本来就知道答案"，拆解的价值从"找对方向"退化为"组织更好"，增益只在结构与标注维度。
- **Q2 模糊题**（round2/3）：V1b 增益更大且 D1 也有增益（拆解帮助找对方向），弱基线 claude +14，强基线 gemini −11（模型依赖）。
- **初读数**：拆解边际 = f(题目确定性 × 模型基线)。题目越确定 + 模型越强 → 增益越小甚至转负（gemini Q2 −11）；题目越模糊 + 基线越低 → 增益越大。

### 3.2 交叉验证（V2）对需检索题的增益

- qwen 档 Q4：40→80（**+40**）。纯记忆通道下，V2 流程（02 调研 + 02.5 两源核对 + conf 标注）把输出从"结构推断、来源泛称"提升到"7 条带 conf 的具体 claim（LMSYS 博客 2023-05-03、arXiv:2403.04132、Agent Mode 发布 2026-06-04 等）"。同通道同模型，增益可归因 prompt 流程。
- **claude 档 V0=47 的失分判定**（conf 中）：主因不是"没工具"本身，而是**裸 prompt 未声明工具缺失约束 → 退化为"你该去哪查"的元方法输出、零可计分事实**。V2 的"无工具→声明+用训练知识完成"条款在 qwen 卷实测堵住该退化。H2（claude Direct×V2 是否翻转到 gemini 水平）待 arena 解封补跑（N/A 卷已留 prompt 全文）。
- 上限：本地"双源"均为官方文档族记忆，URL 级实时核对需 arena 通道（round5+）。

## 4. 矩阵进度

**26/90 有效格**（round3 23 → round4 +3：V1a×Q1×qwen 81†、V1b×Q1×qwen 87†、V2×Q4×qwen 80†，均本地降级；round4 另 7 格 N/A 未计）。

## 5. 失败与阻塞

1. **github push 一度断**（round4 执行期 3 路均遇 `Connection reset by peer`，commit `931556e` 记录）——汇总后重试成功（`935ced2..e00cb8b`）。
2. **arena 封禁 → 强/中模型维度完全冻结**：round4 所有 claude/gemini 格 N/A。V0 n=3 补齐、V1a/V1b×Q1×强/中、V2×Q4×强/中 全部积压到 arena 恢复。
3. 跨通道可比性问题：qwen 档 V0 数据来自 arena（qwen3.6-plus），round4 数据来自本地（qwen3.8-27b-w8a16）——矩阵已按矩阵注记保持单点不并均值，"本地 qwen3.8 子行"方案待 arena 恢复后定。

## 6. Round 5 建议（按优先级）

1. **arena 复检**（开跑前一次）：解封则立即恢复 claude/gemini 档，优先补 V0 n=3（稳定性结论硬依赖）+ V1a/V1b×Q1×强/中 4 格 + V2×Q4×强/中 2 格（本轮 N/A 卷已留 prompt，可直接跑）。
2. **研究题强模型对照**（arena 恢复后）：round3 pilot 是单模型降级，V0 vs V4 × BC/GAIA/HLE × 强模型 6 格 + 双评审盲评（research-rubric 定稿已含锚点）。
3. **V2 扩题**（本地可做）：V2 × Q1/Q2/Q3 × qwen 降级 3 格——验证 V2 增益是否 Q4 专属还是通用。
4. **V3 启动**（本地可做）：DeepSeek+GLM 国内双源交叉验证，V3 × Q4 × qwen 档先跑（Q4 是 V2 增益最大点，看交叉验证能否再加一层）。
5. **盲评协议落地**：round5 起 score 由独立第二 subagent 评（round4 已改第二视角锚点对照，但仍是执行者自评）。
6. 积压清单（arena 恢复后一次性消化）：V0 n=3 × 15 格、V1a/V1b 缺格、V2 强/中档。

**执行纪律**：未跑完不谎报；降级必记 degraded:true + 实际模型；N/A 必带证据（本轮 7 格 N/A 全部附 arena 封禁探针证据）。
