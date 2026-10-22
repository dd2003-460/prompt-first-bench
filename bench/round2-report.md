# Round 2 报告（V0 补 Q1 + V1a/V1b × Q2 + 研究题固化）

> origin: ai · 2026-10-23 · 数据截至本地 commit b16f49d + C 路评分（未 push，网络断）

## 摘要

Round 2 四路并行：A（机制核实+V0补Q1）✅ / B（V1a×Q2）部分（1/3，平台故障）/ C（V1b×Q2）部分（2/3，qwen 未跑）/ D（研究题固化）✅。新增 6 个有效格，矩阵进度 21/90。核心初读数：**V1a/V1b 在 Q2 上对 claude 有 +12~14 提升（73→85.5/87），对 gemini 反而 -11（93→82）**——拆解的边际是模型依赖的，弱基线涨、强基线可能跌。

## 四路结果

### 路 A：机制核实 + V0 补跑 Q1（3 格，✅）

**机制结论**（`bench/config/channel-notes.md`）：arena Direct 模式每 run = 新建会话。入口 `https://arena.ai/text/direct`，首条消息发送后 URL 变 `/c/<uuid>`；同 uuid 内续聊=延续上下文，新 run 必须 goto `/text/direct` 或点 "New Chat"。模型选择器 118 个模型可搜。连续快速新建会话会触发 reCAPTCHA（点一次 checkbox 可过，每 run 间隔 ≥60s 降低触发率）。截图：`loop-artifacts/arena-launch/round2-direct-ui-{1,2}.png`。

**V0×Q1 run2 分数**（n=2/3）：

| 模型 | run1 | run2 | Δ | 备注 |
|------|------|------|---|------|
| claude-sonnet-5-high | 91 | 76 | -15 | run2 率失真章节号 §27 不可验证（-10） |
| gemini-3.1-pro-preview | 93 | 77 | -16 | run2 漏率失真里程碑（-5）+ 连续容量 "Part III §27" 结构矛盾（-10） |
| qwen3.6-plus | 91 | 74 | -17 | run2 两处章节号错误（Th.11→§16、Th.9→§10 Th.4，均与原文矛盾） |

**⚠️ run1→run2 波动 ±15-17 分，三模型一致**——提示 V0 Q1 的 run1 分数（91/93/91）可能是上界，n=2 均分 88.5/85/82.5 更接近真实水平。n<3 不下结论，但波动幅度本身是重要信号（V0 裸 prompt 的稳定性差）。

### 路 B：V1a × Q2（1/3 格，平台故障）

| 模型 | 分数 | 状态 |
|------|------|------|
| claude-sonnet-5-high | **85.5** (success) | ✅ 完成 |
| gemini-3.1-pro-preview | N/A | ❌ 9 次尝试全部失败（reCAPTCHA + "Something went wrong"，trace IDs 已记录） |
| qwen3.6-plus | N/A | ❌ 同上 |

故障特征：03:39 claude 成功后，03:47-04:07 所有后续请求触发平台级 reCAPTCHA + 统一错误页（非模型特定）。commit b16f49d 已建（本地），push 因网络层 Connection reset by peer 失败。

### 路 C：V1b × Q2（2/3 格，qwen 未跑）

| 模型 | 分数 | 状态 |
|------|------|------|
| claude-sonnet-5-high | **87** (success) | ✅ |
| gemini-3.1-pro-preview | **82** (success) | ✅ |
| qwen3.6-plus | — | ❌ 未跑（ego-browser 发送按钮 disabled 问题，调试中断） |

### 路 D：研究题固化（✅）

- `bench/tasks/research-questions.md`：30 题全部实拿题面+参考解（BrowseComp 10 / GAIA L2-3 10 / HLE 10）。来源：BrowseComp←Chat-UniVi/browsecomp list.json（1266 题明文）；GAIA←sayan1101/gaia_filtered_text_only val split（L3×5+L2×5，text-only 版）；HLE←skylenage-ai/HLE-Verified Gold part01 前 10 题 MCQ。
- `bench/rubric/research-rubric.md`：D5 加分维度（0~+20，不进 100 分制基础分；新结论需满足 新/真/独立 三条件；4 档锚点；假新结论 -10/伪新 -5 扣基础分）。标注"草稿·待 round3 验证"。
- commit 608d77a 已 push 成功（网络断前最后一批）。

## 矩阵进度：21/90

有效格：V0 15 + V0-Q1-run2 3 + V1a-Q2-claude 1 + V1b-Q2 2 = 21。
N/A/未跑：V1a gemini/qwen（平台故障）、V1b qwen（未跑）。

## 核心初读数：Q2 上 V0 vs V1a vs V1b

| 模型 | V0 Q2 | V1a Q2 | V1b Q2 | V1a−V0 | V1b−V0 | V1b−V1a |
|------|-------|--------|--------|--------|--------|---------|
| claude（强） | 73 | 85.5 | 87 | **+12.5** | **+14** | +1.5 |
| gemini（中） | 93 | N/A | 82 | — | **−11** | — |
| qwen（弱） | 79 | N/A | — | — | — | — |

**初步结论（n=1，不做强结论）**：
1. **V1a/V1b 对 claude 有效**（+12~14）：round1 中 claude Q2=73 的失分主因是"反问消歧不直接答"；V1a/V1b 的流程指令把消歧前置到分解阶段，claude 从"反问"变成"分层作答"（确定事实/条件性假设/空缺清单）。
2. **V1b 对 gemini 反而回退**（-11）：round1 gemini Q2=93 已接近满分（V0 恰好覆盖了晶体管解读且 0 事实错）；V1b 聚焦假说排查（Bell 身份未定→条件性假设），牺牲了覆盖面（漏晶体管/Bell Labs 双成果解读）。**拆解不是万能的：对已接近满分的强模型，流程约束可能限制其发挥。**
3. **模型交互效应**：拆解的边际提升是模型依赖的——弱基线（claude Q2=73）涨，强基线（gemini Q2=93）可能跌。这是 Q3（强弱模型差异化）的第一个真实信号。
4. **V1b vs V1a 差值**（+1.5，claude）：正交+完备约束在 claude 上的额外边际很小（V1a 的"列子任务"已拿到大部分收益），需 n≥3 确认。

## 失败与阻塞

1. **arena 平台级故障**（03:47-04:07）：reCAPTCHA + 统一错误页，9 次尝试全失败。非模型特定，是 anti-bot/rate-limit/backend 问题。round3 重跑时需间隔 ≥60s/run 且避免短时间批量新建会话。
2. **网络断**（04:21 起）：github.com Connection reset by peer，curl 000。本地 commit b16f49d（B 路 6 文件）+ C 路 2 个 score 文件未 push。网络恢复后需 `git push origin main`。
3. **V1b qwen 未跑**：ego-browser 发送按钮 disabled 问题（fill 未触发 React 状态更新），调试中断。round3 补跑。

## Round 3 建议

1. **补跑缺口**（优先）：V1a×Q2×gemini/qwen（2 格）+ V1b×Q2×qwen（1 格）→ 凑 n=1 完整行；
2. **V1a/V1b × Q1**（6 格）：Q2 已有初步信号，Q1 是第二个验证点（Q1 三模型 V0 基线更高 88.5/85/82.5，拆解还有多少空间？）；
3. **V0 补 run3**（15 格）：n=3 凑齐，Q1 波动 ±15 需要 n=3 才能下"V0 不稳定"的结论；
4. **V2+ 启动**（如果 V1a/V1b 信号确认）：V2 = +信息调研纪律，Q4（需检索题）是 V2 的主战场（V0 Q4 均分 60.7，claude 47/qwen 40 是最大失分点）；
5. **研究题首轮试跑**（选 3 题 × 1 模型）：验证 research-rubric D5 的可行性；
6. **网络恢复后**：push 本地 commit（b16f49d + C 路 score）。

**并行策略**：round3 继续 workflow 并行（4 路），但 arena 操作路需内置 ≥60s/run 间隔 + reCAPTCHA 自动处理（点 checkbox），避免重蹈批量触发故障。
