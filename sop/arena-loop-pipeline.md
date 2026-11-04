# Arena Loop 外包链路（SOP · 唯一入口）

> origin: ai · 2026-10-22 成璐指令 · R7 精简版（2026-11-04）
> **唯一 SOP 入口**：`sop/arena-outsource.md` / `sop/loop-executor.md` 仅作存档指针。
> **部署**：建目标仓库后本文件必须复制进该仓库 `sop/` 并 commit+push（与 `loop/` 同批），arena agent 读仓库内这份。
> 完整版（含历史会话台账、Battle 通道细节）冻结在 `sop/archive/arena-loop-pipeline-v1-full.md`，仅供追溯，不参与注入。

## 0. 优先级（硬规则）

1. **Arena 外包 = 必须首选通道**：调研/核验/执行类任务默认走 arena（LMArena agent mode），不自己 AI 琢磨。
2. **Loop 全程必需 · 双场景**：无论 arena agent 在仓库里执行，还是通道失败回退本地 Lead 自答，**loop 6 阶段（01→04.5）一个不少**。回退降的是**执行通道**不是流程；本地自答工件照常落盘 `loop-artifacts/`，conf 标 0.2。
3. 关系：**loop 是流程骨架（永远在），arena 是默认执行通道（首选，可降级）**。

## 1. 链路总览（6 步 · 断点 · 门禁）

| # | 步骤 | 断点 | 门禁（不过不进下一步） |
|---|------|------|----------------------|
| 1 | AI 启动 | — | goal 按 `sop/goal-template.md` §3 创建：含 SOP 索引（只引用本文件）+ 验收标准 |
| 2 | 注入 agents 原则 | — | 会话已加载 AGENTS.md/CLAUDE.md |
| 3 | 读本 SOP | — | 能说出当前任务对应哪个仓库 |
| 4 | 复制 loop + 本 SOP 到目标仓库 + push | **A**：未 push 时 arena 拉到旧版/缺文件 | push 后在目标仓库验证 `ls loop/prompt-first/*.md` 7 个 + `sop/arena-loop-pipeline.md` 存在；**硬门禁：把 commit hash + `git ls-remote` 输出记进 tasks/ 验证文件** |
| 5 | 发任务书 | **B**：未 push 时 arena 读不到 | `git log -1 -- tasks/<id>.md` 有提交；arena 侧 `cat tasks/<id>.md` 成功 |
| 6 | arena agent 读 loop + 执行 | **C**：agent 不知道要读 loop / 不知道在哪 | 任务书顶部已写强制段（§2）；arena 首条消息引用了 loop 阶段路径 |

**回退分支**（步骤 6 故障）：403/沙箱拦截 → 按 §3.3 降级本地自答，**loop 工件照常落盘**（conf 0.2），故障记 `knowledge/efficiency-bottlenecks.md`。**回退不豁免 loop。**

## 2. 任务书强制段（防断点 C · 写入 `tasks/<id>.md` 顶部）

```markdown
【执行前必读 · 阶段门控】
1. 本任务必须走 1-loop。先读 `loop/prompt-first/INDEX.md`，按路由表确定当前阶段需要的 2–3 个文件，
   只读这些文件。不要一次性读全部 7 个。
2. 每阶段产出落盘 `loop-artifacts/stages/<N>/`，阶段判定 pass 才进下一阶段；
   进下一阶段前重读 INDEX.md 确认要哪些文件（已读的不重读）。
3. 本任务书已内联当前阶段（<STAGE>）的规则包：<FILES>。其余阶段规则不在本文内联。
4. 完成后 commit + push（含全部 loop-artifacts/）。
5. 通道故障（403/沙箱）→ 报告 Lead，由 Lead 降级本地执行，不得静默跳过 loop。
```

**注入量**（o200k 实测）：
- 旧（全量注入 7 文件 + 本 SOP）：**12,086 tok/turn**（run2 基线）
- R6 阶段门控后：2,983–5,443（均值 3,913）
- **R7 压缩后：2,126–3,416（均值 2,707，−30.8% vs R6）**；不含示例时 1,654–2,982（均值 2,261）
- 单会话走完 6 阶段末态：R6 11,035 → **R7 6,523**

计量脚本：`node bench/self-opt-tester/runs/r6/count-rule-tokens.js`；账本与 M1：`node bench/self-opt-tester/runs/r6/compute-m1.js`。

## 3. 仓库映射 · 连接 · 降级

### 3.1 选仓库（按任务选，不固定连一个）

| 任务类型 | 仓库 | 说明 |
|---|---|---|
| prompt-first 流程调研 | `dd2003-460/prompt-first-bench` | 任务书在 `tasks/` |
| decomp T4 消融 | `dd2003-460/decomp-bench` | 任务书在 `tasks/`；GitHub binding 曾失效，派发前先验 ls-remote |
| 风格蒸馏 / 论文校对 / 媒体 pipeline | `persona-distill` / `academic-AI` / `d1-media-pipeline` | 任务书在 `tasks/` |
| AI 视频复刻 | `dd2003-460/d1-video-recreation` | 任务卡在 `arena-prompts/batchN/` |
| 金融调研 / 论文写作 | `dd2003-460/hermes-workspace-zero` | 分支 `arena/*`；回执核验去 agent 实际 push 的分支找 |

**会话台账（一仓一会话 · r80 + 成璐 2026-11-01 硬约束）**：派发前必须查台账复用该仓库既有会话；仅当该仓库确无会话才可新开，开完立即登记。**同一仓库两个活跃 arena 会话 = 违规**（上下文分裂、任务书版本漂移）。

- 当前台账（仓库 → 活跃会话 → 状态）见 `sop/archive/session-ledger.md`；本文件只维护规则与增量。
- 新增/关闭会话时同步更新台账文件，不写回本节。

**judge 选择条款（pfb G2 F2(a)，2026-11-02 升格）**：多 judge 交叉打分必须**异族隔离**——同底座两遍只算「上下文独立」不算「家族独立」。κ 回执须显式标注 judge 族（如 `qwen3.8-27b ×2, non-IRR`）；宣称真 IRR 需 ≥2 不同底座。

### 3.2 连接仓库（新会话可直接选仓库）

1. **选对仓库是第一原则**：开新会话按 §3.1 映射直连目标仓库，不走 pfb 中转。
2. GitHub App 授权保持 "All repositories"（含私有）。
3. 验证：`git ls-remote https://github.com/dd2003-460/<repo>.git HEAD` 返回 hash = 可达。

### 3.3 失败降级

| 故障 | 诊断 | 降级 |
|---|---|---|
| git clone 403 | `curl -s -o /dev/null -w '%{http_code}' https://github.com` | ① GitHub REST API 读写 ② 上传任务书到本机执行 ③ Lead 本地自答（conf 0.2，loop 照常落盘） |
| token 过期 | `git ls-remote` 测权限 | 重新 OAuth / `gh auth token` 换新 |
| 沙箱拦截 git | `curl https://api.github.com` 通但 clone 不通 | 走 GitHub REST API |

**降级原则**：不阻塞，降级 Lead 本地自答（conf 0.2），故障记 `knowledge/efficiency-bottlenecks.md`。

## 4. loop 阶段速览

每阶段读 `loop/prompt-first/<阶段>.md` → 产出落 `loop-artifacts/stages/<N>/` → 判定 pass/revise：

| 阶段 | 产出 |
|---|---|
| 01 目标分解 | decomposition（正交+覆盖+边界+已知vs空缺+递归到原子） |
| 02 信息调研 | research（每条 claim 带来源+conf） |
| 02.5 交叉验证 | crosscheck（关键结论 ≥2 独立来源；矛盾记录） |
| 03 行动分解 | actions（依赖+并行+owner 标注+执行级原子化） |
| 04 执行验证 | execution-log（per-step 备份→执行→review→提交） |
| 04.5 反方复核 | review（找矛盾+验证假设+回退阶段） |

**约束**：每阶段产出必须落盘；判定基于工件内容不是感觉；任务卡 ≤50 行；每读 N 个文件先写 checkpoint。

### 4.1 复制 + push 模板（断点 A）

```bash
git clone --depth 1 https://github.com/dd2003-460/<repo>.git /tmp/<repo>
rsync -av --delete /Users/a1-6/Desktop/workspace/loop/prompt-first/ /tmp/<repo>/loop/prompt-first/
cp /Users/a1-6/Desktop/workspace/sop/arena-loop-pipeline.md /tmp/<repo>/sop/
git -C /tmp/<repo> add -A && git -C /tmp/<repo> commit -m "sync: loop/prompt-first + sop $(date +%Y%m%d)"
git -C /tmp/<repo> push && git ls-remote https://github.com/dd2003-460/<repo>.git HEAD
```

`rsync --delete` 保证仓库 `loop/prompt-first/` 与 workspace 完全一致（7 个阶段文件 + `examples/` + `references/`）；**不要 rsync 整个 `loop/`**（含 archived 等无关内容）。sop 只复制本文件。push 后把 commit hash + ls-remote 输出写进 tasks/ 验证文件。

## 5. 结果核验（硬约束）

- **agent mode：不信汇报信 git**——fetch 显式 refspec → log → show 文件 → 独立复算数字。
- **battle mode**：核对揭晓模型名与记录一致；回答全文 sha256 入库；分数复算与原文对账。
- 打分通道细节（Battle 投票流程、ego-browser 选择器）见 `sop/archive/battle-channel.md`。

## 6. 维护

- 新增仓库 → 更新 §3.1 表 + 台账；新断点 → 更新 §1 表 + qanda-ledger；故障修复 → 更新 §3.3。
- 本文件变更 → commit + push（workspace + 各已部署仓库同步）。
