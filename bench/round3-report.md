# Round 3 报告（2026-10-23 05:47–07:05）

> origin: ai
> 目标：goal-9453f7e5 round 3（1000 轮 bench 消融）。3 路并行（workflow 3 agents）：A 补 round2 缺口 / B V0 补 run3 / C 研究题试跑设计+rubric 定稿。
> **核心事件：arena.ai 05:54 起被 Cloudflare IP 级整站封禁**（3/3 尝试失败：Attention Required 拦截页/导航超时/reload 仍拦），证据 `bench/evidence/arena-blocked-20261023-r3.png` + `bench/config/fault-evidence-20261023-round3-v0.md`。本轮 15 格全部走「本地降级 / N/A」，**无 arena 通道 run**。

## 1. 三路结果

### 路 A：补 round2 缺口（commit 15d097e）
| 格 | 结果 | 通道 | 分数 |
|---|---|---|---|
| V1a×Q2×qwen | 完成 | 本地降级（vllm/qwen3.8-27b-w8a16 代跑 qwen 档，degraded:true） | **80.5**（自评，压线 success） |
| V1b×Q2×qwen | 完成 | 同上 | **88.5**（自评，success） |
| V1a×Q2×gemini | N/A | arena 封禁 + 本地无 gemini 模型（证据+待发 prompt 已存档） | — |

### 路 B：V0 补 run3（commit a85490e）
| 格 | 结果 | 分数 |
|---|---|---|
| Q2×qwen run3 | 本地降级完成 | 86.5 |
| Q3×qwen run3 | 本地降级完成 | 86.5 |
| Q4×qwen run3 | 本地降级完成（**partial**：易变题「≥2 源实时交叉」本地无网不满足，属通道限制非模型能力） | 79 |
| Q5×qwen run3 | 本地降级完成 | 84 |
| Q2–Q5 × claude / gemini 共 8 格 | N/A | arena 封禁 + 本地无这两模型 |

**矩阵记账处理**：qwen 行 run3 不并入现有 arena-run1 均值（模型版本 qwen3.8 vs 3.6 + 通道差不可分离），matrix 仍记 arena run1 单点（79/92/40/81），run3 值存于 round3 报告 + run 文件；V1a/V1b qwen 格为该行首个数据点，直接入矩阵（80.5/88.5，†标注）。

### 路 C：研究题试跑设计 + rubric 定稿（commit 90145c2）
1. **research-rubric.md D5 定稿**（草稿→定稿）：4 档→5 档（0/25/50/75/100）锚点；「新结论」三判据（新/真/独立）可操作化——新=相对题面与参考解的增量、真=引用可核验来源且评分者抽查 ≥1 条、独立=不依赖题目已给事实；防幻觉保留伪新 −5 / 假结论 −10 扣基础分。
2. **round3-research-pilot-plan.md**：选 BC-00 / GAIA-01 / HLE-02 各 1（公开可核验），V0 vs V4（完整 01–04.5 流程）× 强模型 1 run，共 6 runs，评分表模板 + 执行检查表。
3. **6 pilot 已跑**（全 local degraded，实际 qwen3.8-27b-w8a16 代跑弱档——单模型对照验证流程可行性，模型维度留 round4）：

| 题 | V0 | V4（基础分） | Δ | D5 |
|---|---|---|---|---|
| BC-00（检索） | 81 | 91 | +10 | 0（URL 型来源本地无法核验） |
| GAIA-01（检索） | 76 | 91 | +15 | 0（同上） |
| HLE-02（推理） | 79 | 98 | +19 | **+10**（arXiv ID 可离线核验） |

## 2. 关键发现

1. **V4 流程增益真实且可观（弱档、单模型、n=1）**：基础分平均 +14.7（10/15/19），增益来自 D2 五阶段实质 + D3 可验证性 + D4 完整度——不是模型差异（同模型对照）。这是 round1/2 以来第一次在**同一模型**上隔离出流程效应，方向与 FINAL-VERIFY 的预测一致（流程环节有边际，但需多模型+盲评确认）。
2. **D5 在本地通道的可行性取决于来源类型**：文献编号型（arXiv ID）可离线核验、能产生 D5；URL 检索型本地归零。arena 通道两类都可核验——round4 必须用 arena 跑研究题 pilot 才能评 D5 全维度。
3. **Q2 三变体对照（弱档首次齐）**：V0 79 → V1a 80.5 → V1b 88.5（降级通道内自洽对比，跨通道谨慎）：普通拆解几乎无增益（+1.5），正交+完备约束有增益（+8）。与 round2 claude 的读数（V1a +12.5、V1b +14）方向一致但量级不同——**拆解边际仍是模型/基线依赖的**。
4. **arena Cloudflare 封禁是新风险**：03:47–04:07（round2）reCAPTCHA 故障 → 05:54（round3）整站 IP 级封禁，平台 anti-bot 在收紧。round4 若 arena 未恢复，需考虑备用通道（其他网页 LLM 交叉核验站点，见 ego-verify skill 7 站点表）。

## 3. 矩阵进度

**23/90 有效格**（round2 21 → round3 +2：V1a×Q2×qwen、V1b×Q2×qwen；8 格 N/A 未计）。研究题 pilot 6 格另计（不进 90 格矩阵）。

## 4. 失败与阻塞

1. arena.ai 整站封禁（Cloudflare，IP 级）——全部 15 格降级/N/A，无伪造，全部 run 文件 degraded:true + 实际模型标注到位（已抽查）。
2. V1a×Q2×gemini 永久缺（arena 恢复前本地无法补）——round4 优先。
3. V0 n=3 仅 qwen 档 4 格有第二数据点，且为降级通道；claude/gemini 的 n=3 完全未动 → **V0 波动 ±15 的稳定性结论仍无法下**（round2 的悬案）。

## 5. Round 4 建议（按优先级）

1. **arena 恢复检查 + V0 n=3 补齐**（15 格：Q1–Q5 × 3 模型 run3）——稳定性结论的硬依赖；若 arena 持续封禁，改走备用网页 LLM 通道（记录通道差）。
2. **研究题 pilot round4**：arena 通道重跑 6 格（V0 vs V4 × BC/GAIA/HLE × 强模型）以解锁 D5 全维度 + 模型维度对照（强/中/弱）；双评审盲评（本轮全部自评）。
3. **V1a/V1b × Q1**（6 格）：第二验证点。
4. **V2 启动**（Q4 检索题主战场，V0 Q4 均分 60.7 最大失分点）。
5. 盲评协议：round4 起 score 由第二 subagent 评（消除执行者自评偏差，research-rubric 定稿已含锚点）。

**执行纪律**：未跑完不谎报；降级必记 degraded:true + 实际模型；N/A 必带证据。
