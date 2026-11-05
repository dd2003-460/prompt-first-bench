# 04.5 — RV3G3-threshold-crossdomain-reverify 核销轮 · 反方复核（八攻击）

> goal: queue 队列卫生修复 + 核销验证 · 分支 ralph/rv3g3-threshold-crossdomain-reverify-close · 2026-10-30
> 方法：对本轮全部动作（checkbox 翻转 + 验证增量 + 新候选）发起八项独立攻击，逐项给出成立/驳回判定。数字层先做独立重跑（攻击前置）。

## 前置：数字层独立重跑（零 mismatch 确认）

不读 04 工件，从仓库根全新执行七脚本：exit codes = [0,0,0,1,0,0,0]（crossdomain/o3-claim-list/gmr/kappa/rejudge/goldrank-threshold/w3w4），关键行（SIGNAL 文案 / 4/4 / 11 PASS / RESULT: FAIL / 31 PASS / 0 mismatch）与 04 A1 表逐字一致；`git diff main --stat` 冻结十件 = 0 行。**零 mismatch。**

## 攻击 1 — 「核销轮是刷工作量：翻一个 checkbox 配六阶段工件 = 形式主义」

**核查**：(a) 本轮的实质价值不在 checkbox 本身而在**消除 message↔状态矛盾**——97d2adf message 声称「划掉」而状态 `[ ]`，这个矛盾会误导后续 runner（把已完成 goal 当可做 goal 重复执行，或把 blocked-on-external 误判为未启动）；(b) 验证增量（七脚本基线复验 + byte-exact 捕获）不是装饰——它证明「r140 交付物在 r145 时点仍行为正确」，即核销的不是历史 commit 而是**当前 main 上的活行为**；(c) 先例 r137 docsync / r135 prior-source 均为同构核销轮且被接受。工件量与风险匹配（漏翻缺陷跨四轮未发现 → 需要显式证据链封死复发路径）。

**判定**：**驳回**。

## 攻击 2 — 「归因错误：也许 97d2adf 故意不划——batch2 没到，goal 语义上没完成」

**核查**：queue 条目原文的任务定义 = 「写 assert 脚本消费第二域 hit-matrix…」（骨架交付），其产投比依据栏明说「纯仓库内推导可先行落 assert 骨架（schema 预注册，同 r136 kappa-receipt 模式）」——**任务书自己就把范围切割成骨架交付**，batch2 实跑是另立的 RV3G3-batch2-arrival-closure 候选（97d2adf 同 commit 导出）。且 r140 结果注记自身写明「当前 ablation 面常态 = SIGNAL blocked-on-external exit 0（不伪造转绿）」+「闭环候选见上」——r140 自己的收口语义就是「本 goal 完成、后续挂 batch2 候选」。X5 已声明该归因不可从 git 区分并给出下行风险分析：即使属有意保留，补翻也是净改善。

**判定**：**驳回**（归因采信 message + 任务书范围切割双重锚点；残余不确定性已在 X5 登记）。

## 攻击 3 — 「A1 回归基线是抄的 r142/r143 工件，不是本轮实跑」

**核查**：前置节独立重跑 = 全新 shell 会话执行七脚本，输出落 /tmp/r145-*.out 后 grep/tail 提取；crossdomain 两行输出经 od -c 字节级捕获（offset 0000377 以 `\n` 结尾）。04 A1 表的每个值都可由 /tmp 文件复现，非转述。

**判定**：**驳回**。

## 攻击 4 — 「byte-exact 只查了 stdout 尾部，stderr 可能藏东西」

**核查**：实跑命令为 `python3 … > out 2>&1`——stderr 并入同一文件，od -c 捕获的是合并流全量（255 字节，恰两行），不存在未捕获的 stderr 通道。若脚本向 stderr 写任何内容，它会出现在 od 输出里。✅ 攻击前提（stderr 单独存在）不成立。

**判定**：**驳回**。

## 攻击 5 — 「新候选 RV3G3cdx-batch2-schema-lint 是给 blocked-on-external 的 batch2 加戏，数据都没到就设计 lint = 空转」

**核查**：lint 的消费时机 = 数据提供方**写入前自验**——恰好在 batch2 数据到来那一刻最有用（避免 arrival-closure 执行时 schema 往返）。设计成本 ≈ 0（字段级 schema 已在 r140 docstring 预注册，lint 规则 = 把既有校验逻辑暴露为独立入口）。工作量 ~5 回合且纯仓库内。但它确实**依赖 batch2 场景才有实际消费**——作为候选登记（不立即执行）是正确处置，攻击的「空转」指控针对的是「立即执行」而非「登记」。

**判定**：**部分成立（登记）**：候选描述已含「降低 RV3G3-batch2-arrival-closure 执行往返成本」的依附性说明，无需改文本；登记边界 = 该候选的实际价值在 batch2 到来时才兑现，在此之前执行它只有边际收益（提前暴露 lint 实现 bug）。

## 攻击 6 — 「queue-hygiene-sweep 候选是自我指涉的废话：刚发现一个漏翻就立扫尾 goal，扫完又会有新的」

**核查**：(a) 该候选的价值不在「扫出这一个」（已被本轮修掉），而在**建立例行检查机制**——97d2adf 型缺陷的检出延迟 = 4 轮（r141-r144 无人发现），说明 ad hoc 注意不可靠，需要显式扫描动作；(b) 「扫完又会有新的」恰恰是支持立项的理由（缺陷生成速率 > 0 → 需要周期性清除，如同 lint job）；(c) ~3 回合成本极低。但攻击指出一个真实弱点：sweep 的范围界定（「全部 [x]/[~] 行」）在 queue 增长后会变贵——候选文本未给终止条件。

**判定**：**部分成立（已修）**：候选描述补充范围上限——「抽查对象 = 近 20 轮收口 commit 对应的 queue 行（非全量历史），单轮成本封顶 ~3 回合」。

## 攻击 7 — 「A5 冻结面清单不全：只查了十件，ablation 目录还有 stats-*.json / judge-blindtest-r1.json 等」

**核查**：current-goal【验收标准】第 2(b) 条明确枚举冻结面 = {hit-matrix.json, prior-estimates.json, gold-tree.md, runs-C0-*}（与 r142/r143 工件沿用同一清单）。但攻击指向更强的检验：**全仓 `git diff main --stat`** = 仅 tasks/current-goal.md + tasks/goal-queue.md（本轮提交前实测，19 insertions/19 deletions 两文件）+ untracked stages 工件——即改动面封闭性已由全仓 diff 实证，强于十件清单。十件清单是「冻结数据不被触碰」的最小充分集，全仓 diff 是「无任何意外改动」的完备证明，两者都已执行。

**判定**：**驳回**（全仓 diff 已覆盖攻击面；十件清单未被当作唯一证据使用）。

## 攻击 8 — 「核销注记写进 L28 会让该行超长（已有 400+ 字结果注记），queue 可读性恶化」

**核查**：L28 现状 = 目标栏 + 结果栏共 ~500 字，本轮追加 ~60 字核销句。queue 既有条目（如 RUBRIC-V3-FULL-AUDIT L7）长度达数千字——本行远未到可读性阈值。且核销句放在注记头括号内（与 r137 docsync 条目「核销轮——核心交付物 r133/c55848f 已存在」同构位置），不侵入结果栏结构。

**判定**：**驳回**。

## 总判定

| # | 攻击 | 判定 | 处置 |
|---|------|------|------|
| 1 | 刷工作量 | 驳回 | 实质价值 = 消除 message↔状态矛盾 + 当前行为复验 |
| 2 | 故意不划 | 驳回 | 任务书范围切割 + r140 自身收口语义双锚点；残余不确定性 X5 已登记 |
| 3 | 基线是抄的 | 驳回 | 前置独立重跑 + /tmp 落盘可复现 |
| 4 | stderr 藏东西 | 驳回 | 2>&1 合并流全量 od 捕获，攻击前提不成立 |
| 5 | lint 候选空转 | 部分成立（登记） | 依附性已在候选文本说明；登记执行时机边界 |
| 6 | sweep 自我指涉 | **部分成立（已修）** | 候选补范围上限（近 20 轮收口行，成本封顶） |
| 7 | 冻结面清单不全 | 驳回 | 全仓 git diff 完备证明已执行 |
| 8 | 行超长 | 驳回 | 同构位置 + 远低于既有条目长度 |

**8 攻击：6 驳回 / 2 部分成立（其中 1 已修 = 攻击 6 候选范围上限，1 为执行时机边界登记）**。数字层独立重跑零 mismatch。verdict = **pass**（修复项随下 commit 落入 queue）。