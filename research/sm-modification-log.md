# SM 修改日志（T53 D2 · 每次改目标函数/状态转移的原因 + 前后对比）

> origin: ai (T53-D2, 成璐要求"所有相关错误、修改路径放在项目里")
> 格式：日期 / 改了什么 / 为什么 / 证据。append-only，不删历史条目。

**编号规则（2026-11-11 成璐质询后补）**：本文件 rN = 状态机工程迭代轮次（smoke test run + 代码改动批次），从 r1 起连续递增，与 v17 的 r1-r10（`s5_hierarchy.py` 单次 run 内部的 decompose 分解轮，见 `runs-s5-v17-hier-smoke-console.log`）是**不同命名空间**。

**版本线是连续的（成璐 2026-11-11 纠正）**：v17 → T53 不是"换名重启"，是同一条实验改进路线上的下一版。T53 = 这条线的当前版本，继承 v17 的问题设定（层级分解 arm）、诊断结论（Goodhart 刷分）和 bench 题集；版本号不另起 v18/v19/v20，而是用 T53 任务 ID + 本文件 rN 迭代轮定位具体改动。若未来需要大版本锚点（如架构级重写），在本文件加一行 "vN = rX+rY 合并发布" 即可，不新建编号体系。

---

## 2026-11-11 r1 — S_α recall 型 → F_β 型（necessary 过滤接入）

**改了什么**（`experiments/stage-ablation/s5_state_machine.py`）：
1. `ObjectiveConfig` 加 `fbeta_beta=0.5`、`stop_criterion="necessary"`。
2. 新增 `judge_necessary(claim, parent_claims, confirmed, cfg)`：LLM 二元裁决该节点是否引入父 claim/已确认事实中不存在的新变量、新约束或新可检索事实；失败保守返回 False（宁可少拆不多拆）。
3. 主循环 DECOMPOSE 后、进树前：每个候选节点过 necessary 裁决，不通过直接丢弃并计入 `dropped_redundant`。
4. J_stop 判据从纯 n-gram gain streak 切到 necessary 饱和 streak（`stop_criterion="gain"` 可回退旧行为做消融对照）。

**为什么**：v17 的 Goodhart 根因是 S_α = Σ[n·ln(kₙ)+α·kₙ·ln(n)] 对节点数单调增、只奖"覆盖"不罚"多余"→ 模型堆 1930 个同义变体刷分。T-PR-15 survey（Lead 验收 commit `76e64c4e`）给出修法依据：Ryu et al. 2026（arXiv:2610.33512）——recall 型奖励很快饱和而 precision 持续降，改成 F_β 后回答长度降 2.6×、胜率 10.6%→68.0%。本改动就是给 decomp 侧加 precision 项：不引入新信息的节点不再进树。

**预期 vs v17**：GPU 题节点数 1930 → 几十~百级（AC1 ≤200），正交维度保持 6-8。

**验证状态**：smoke run `proc_aeb63c95fd0d`（gpu 题，全链路含真实检索+核验+necessary 判定），日志 `runs-s5-sm-gpu-fbeta.log`。结果出来填下方。

**风险/已知局限**：
- necessary 判定本身也是 LLM 裁决（文字代理），理论上可被"措辞新颖但信息冗余"的节点骗过——n-gram dedup（0.7 阈值）仍在前一道挡着，双层防线。
- 每候选节点一次额外 LLM 调用，成本上升；若 smoke 显示太慢，下一版改成批量判定（一次 prompt 判一批）。

## 2026-11-11 r2 — 核验不再豁免 knowledge/given（AC3 修复）

**改了什么**：`_verify_batch` 原来对 source=given/knowledge 直接标 verified + evidence="模型先验/题面给定"，只有 search 节点走 LLM 核验。r1 smoke 暴露：145/170 节点是这种免检 verified，evidence 全是占位文本——AC3（≥90% 节点有真实 evidence）名存实亡。现在所有节点都过 `verify_node`（LLM 逻辑+外部核验），只是 given/knowledge 不触发联网检索。`--no-verify` 模式也改成"跳过检索但过核验"。

**为什么**：AC3 的意图是"每个进树的节点都被核验过"，不是"每个节点都有个 status 字段"。v17 的诊断里"knowledge 节点未抽查"本来就是留的坑，r1 等于把它原样搬过来了。

**代价**：每节点一次 LLM 调用（~2s），单题总时长上升（r1 全链路约 30min → r2 预计 40-60min）。可接受：bench 只有 5-10 题。

**验证状态**：smoke run `proc_4c3b399c9772`（gpu 题），日志 `runs-s5-sm-gpu-fbeta-r2.log`。

## 2026-11-11 r1b — parent_ids 索引 bug 修复

r1 里 `par_claims` 用 `int(id.lstrip("N"))-1` 当列表下标取父节点 claim——id "N81" 会取到第 80 个节点而不是 id 为 N81 的节点，necessary 判定的参照系是错的。改成 `{n.id: n.claim}` 查表。单独测了 judge_necessary：新变量节点 True / 同义变体 False，裁决方向正确（各 ~1.5s/次）。


## 2026-11-11 r3 — 可靠性三件套（E6 静默死修复）

**背景**：r2 smoke 再次静默死在 L1 之后（log 停在 `[SM] L1: 25 nodes`，无 Traceback 无 EXIT）。单发/连发 verify_node 前台全过、8787 proxy 活着——说明不是某条 claim 触发异常，是后台长进程 + LLM 调用组合下的环境性死亡。这正是成璐点名的"微信会断，状态机要可靠"。

**改了什么**（commit 见下）：
1. **每轮 checkpoint 落盘**：`run()` 每轮结束写 `checkpoints/sm-{qid}-r{rnd}.json`（完整节点树 + 计数器）。死了不丢已完成的轮次。
2. **`--resume <ckpt>`**：CLI 支持从 checkpoint 加载继续跑，NodeRecord 反序列化已验证（假 ckpt 测试通过）。
3. **call_llm retries 1→2**：proxy 抖动多扛一次（timeout 本来就是 600s，不动）。

**没改的**：启动方式仍建议走 `scripts/launch.sh`（tee + EXIT code），这样即使再死，log 最后一行有 exit code，不再是 4 行无头尸体。

**待验证**：用 launch.sh 起 r2 重跑（proc_0df18a438c91 还在前台复现 _verify_batch 25 节点，结果出来对照）。若 launch.sh 下仍静默死且 EXIT≠0 → 死因可定位；若 EXIT=0 但 log 截断 → 是日志层问题不是进程问题。


## 2026-11-11 r4 — 通道健康探针 + ego-browser 降级（E8.1+E8.2 落地）

**改了什么**：
1. `s5_state_machine.py` run() 开头加网络出口探针：纯 Python 直连 `https://en.wikipedia.org`（不走系统代理，~1s），失败则置 `self.network_degraded=True`。
2. `_verify_batch` 里 search 节点走 search_node 前检查探针：degraded 时跳过联网检索直接标 degraded（evidence 写明原因），不再让 ego-browser 坏通道把整批卡死/刷屏。
3. 探针结果落进 checkpoint（`network_degraded` 字段），resume 时继承。

**为什么**：r2/r3 两次挂死根因都是 ClashX 7890 端口掉线 → ego lite 渲染进程出站全走系统代理 → ERR_PROXY_CONNECTION_FAILED。状态机不该因为本机代理抖动而整体停摆——检索失败本来就该降级为 degraded 节点继续跑（设计里就有这个分支），只是坏通道的错误处理路径没兜住。

**没做的**：ClashX 自动切换节点（E8.3）——那是环境修复不是状态机职责，手动切 GLOBAL 已恢复出口；launch.sh 前置检查以后有需要再加。

**验证**：py_compile OK；等 --no-verify run（pid 69821）出结果对照 AC1。

## 2026-11-11 r5 — 可靠性收尾（E8.2b + E9）

**改了什么**：
1. `ablation_harness.call_llm`：重试按 HTTP 状态码分策略——5xx/429 指数退避（5s→10s→20s→40s），4xx 直接抛。修掉 r3 实际死法（连续 502 窗口 >15s 时旧版固定 sleep(5)×2 全灭）。
2. `s5_state_machine._decompose_layer` retries 2→4；`judge_necessary_batch` retries 2→3。
3. `_probe_network` 补第三路：Python 通道全挂时快速探 ego-browser（taskSpace+page 存活，~2s），ego 还活就不降级——因为 ego lite 走自己的网络栈，ClashX 挂了它不一定挂（r3 期间实测 daemon 响应正常）。

**为什么**：r3 死在 L2 decompose 的 call_llm 上（502×2 后 raise），而同期 --no-verify run 正常推进到 81 节点——说明主循环健康，死因是网络抖动 × 重试不足。这一轮把"网络抖动导致整 run 崩"的路径全部堵上：LLM 侧退避拉长、探针三路兜底、degraded 分支不阻塞。

**验证**：py_compile OK；探针单测通过（当前 ClashX 7890 仍死 → Python 两路失败 → ego-browser 探活成功 → network_degraded=False，符合预期）。

**没做的**：ClashX 端口配置修复（mixed-port=0 是用户环境的事，手动切 GLOBAL 已恢复出口，不动配置文件）。

## 2026-11-11 r4b — --resume 参数解析 bug（r3 遗留）

**症状**：`--resume checkpoints/sm-gpu-r1.json`（空格形式）被 flag 过滤器吃掉路径，resume_from=None → 静默从头跑 + 重拆 L1。
**根因**：main 里 `flags = [a for a in argv if a.startswith("--")]`，`--resume` 后的值不以 `--` 开头进了 args；旧解析逻辑只在 flags 列表内部找下一个元素，永远找不到。
**修法**：在原始 argv 上扫 `--resume <path>` 和 `--resume=<path>` 两种写法；resume 时 `_decompose_l1(skip_if_seeded=True)` 跳过重拆（L1 已在 checkpoint）。
**验证**：pid 92810 实际 resume 成功——log 出现 "resumed from ...: 81 nodes @ r1" + "L1 already seeded (81 nodes), skipping decompose"，正在跑 r2 的 gap_check/decompose。
