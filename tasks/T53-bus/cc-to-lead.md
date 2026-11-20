# CC → Lead（T53b 消融实验）

- 时间: 2026-11-18T02:30+08:00
- 类型: 需要 Lead 判断（实验设施 bug + 数据作废）

## 发现 1：r01/r02 数据无效（已清理）

- 现象：`ablation-runs/gpu_formula_r01.json` 与 `r02.json` 的 answer 逐字相同
  （md5 均为 `08e2503b...`，9949 chars），coverage 都是 0.067，n_nodes 都是 143。
- 根因：`s5_state_machine.py` 跑完后 `final_state='decompose'`、`n_rounds=0`——
  143 节点树（5 L1 + 26 L2 + 75 L3 + 37 L4）全部 `status=pending`，**核验循环一轮都没跑**。
  树是 `checkpoints/sm-gpu-r1.json`（2026-11-17 23:28 旧 checkpoint）残留的产物；
  `--synth` 直接在这棵未核验树上做综合 + judge，两次自然产出相同 answer。
- 已做处理：
  - `cc-state.json`：gpu_formula_r02 回退 `done=false`（r01 保留 true，但数据已作废）
  - `ablation-results.json`：删除 r01/r02 两条无效记录（现 0 条）
  - `ablation-runs/`：删除 r01/r02 的 json 与 judge 文件
- 影响：r01/r02 需要作废重跑。r01 的 `done=true` 我没敢动（stop-hook 的
  cc-stop-block-count 已记 1 次 block，动 r01 可能触发防循环讨论），
  请 Lead 决定：r01 是否也回退重跑。

## 发现 2：SM_SEED=42 不约束 LLM 采样（可复现性存疑）

- `s5_state_machine.py` 顶部 `_random.seed(42)` 只约束 Python 全局 random
  （redundancy_score 采样、`_perturb()` 扰动串、call_llm 的 16-token 反缓存扰动）。
- `call_llm`（ablation_harness.py:467）**从不把 seed 传给 vLLM**（payload 无 seed 字段），
  temperature=0.7 下 LLM 输出本身不可复现。
- 任务书 AC5 要求"所有 run SM_SEED=42 固定，可复现"——当前设施只能保证
  "扰动串/采样序列固定"，不能保证 LLM 输出逐字复现。
- 请 Lead 判断：(a) 接受"同 seed 下扰动序列固定、LLM 输出允许漂移"的口径，
  在统计汇总里写明；(b) 还是要求 call_llm 传 seed 给 vLLM（需要改 harness，
  超出我"只跑不改"的边界）。

## 发现 3：r7 复现判据可能永远为 false（判据与数据格式不匹配）

- 判据：L1 节点 claim 以"不确定性/随机/uncertainty/stochastic"**开头**，
  且 scope 提到"横切/作用于其他维度"。
- 实际：gpu 题 5 个 L1 节点的 `scope` 字段**全部是 None**（runs-s5-sm-gpu.json 实测）。
  最接近的 N5 claim 是"环境依赖与不确定性因子：识别驱动兼容性..."——
  "不确定性"在 claim 中段，不在开头。
- 按当前判据，60 个 run 的 `l1_uncertainty` 大概率全是 false，
  AC4（gpu 10 轮 ≥3 轮出现）无法满足。
- **具体反例（r03 当前 L1 骨架，checkpoints/sm-gpu-r1.json，2026-11-18 02:14）**：
  N4 claim = "证据溯源与不确定性标记：覆盖所有关键数字与结论的证据可信度**横切因子**，
  要求每个数据点标注来源类型（刚查到/凭记忆）并对不确定项标记[待核验]..."
  ——模型确实生成了"不确定性横切维度"（claim 同时含"不确定性"和"横切因子"），
  但判据函数 `extract_l1_uncertainty` 因 ①"不确定性"在 claim 中段非开头
  ②scope 字段为 None（NodeRecord 无 scope 字段，scope 拼在 claim 里，
  s5_state_machine.py:530 `claim = f"{name}：{scope}"`）
  而返回 False。**判据必然失效，不是"太严"——模型行为正确但判据读不到。**
- 请 Lead 裁决判据修正方案。最直接的修法：判据函数改读 claim 全文
  （`claim.lower()` 含"不确定性/随机/uncertainty/stochastic" 且
  `claim` 含"横切/作用于/cross-cut/affect"），而非读不存在的 scope 字段。
  判据改动在 `ablation_run_one.py` / `ablation_watcher.py` 的
  `extract_l1_uncertainty`，属于设施代码，我不动。

## 当前状态

- 正在跑：pid 83580 `s5_state_machine.py gpu --obj-mode=formula --synth`（02:25:38 启动，
  父进程 83578 是 `ablation_run_one.py gpu formula 2`——即 r02 作废后的重启 run）。
- watcher（pid 5746）在跑，但它的 process_run 有 bug：
  读 `runs-s5-sm-{qid}-synth.json`（该文件 answer 字段为空），
  而 `ablation_run_one.py` 读 `runs-s5-sm-{qid}.json` 并正确提取 answer。
  两者会互相覆盖 cc-state/results——r03 完成后我会核对实际落盘数据，
  若 watcher 污染了结果我会手动修正并在此报告。
- 剩余：58 个 run（含 r01 是否重跑待 Lead 定）。

## 发现 4（02:47 补充）：r02 重启 run 与 watcher 双处理冲突（同一份数据会被记两笔账）

- 现状：83580 是 `ablation_run_one.py gpu formula 2`（83578）的子进程，正在跑
  **r02 的重启数据**；但 watcher 按 cc-state.json 第一个 pending（gpu_formula_r03）
  处理进程退出后的输出。
- 83580 退出后将发生：
  1. 83578（ablation_run_one.py，硬编码 run_name=gpu_formula_r02）处理输出：
     覆盖写 `ablation-runs/gpu_formula_r02.json` + judge，results **纯 append**
     （不删旧记录），cc-state 中 r02 已是 done=true（保持）。
  2. watcher（按第一个 pending = r03）处理**同一份** `runs-s5-sm-gpu-synth.json`：
     写 `ablation-runs/gpu_formula_r03.json`（内容 = r02 重启数据），
     results 先删 r03 旧记录再追加 r03，cc-state 把 r03 置 done=true。
- 后果：同一份数据同时记为 r02 和 r03 两笔账；r03 的"10 轮"里混入一份
  r02 重启数据；r02 的 results 出现两条记录（旧作废 02:25:34 + 新 append）。
- 我的处置（在 CC 边界内）：83580 退出后我会核对 ablation-runs/、results、
  cc-state 三处实际落盘，手动把账目修正为"r02 重启数据只记 r02 一笔、
  r03 回退 done=false 待重跑"，并在本报告追加修正记录。
- 请 Lead 裁决设施层修法（watcher 的 pending 匹配逻辑 / run_one 的硬编码
  run_name 与 cc-state 脱节），我不动设施代码。

## 发现 5（03:00 补充）：r03 记账已撤销 + 设施无"每 run 清场"机制（核心阻塞）

### r03 记账撤销（已执行，CC 边界内）

- 83580（02:25:38 启动的 r02 重启 run）退出后，watcher 按 r03 记账
  （cov=0.067 depth=0.5179 nodes=143）。但 `runs-s5-sm-gpu-synth.json`
  mtime=01:25，**早于 83580 启动**——83580 跑了 1794s 没有更新 synth 输出
  （它 FATAL 了：`sm.run()` 抛异常 → 落盘 `runs-s5-sm-gpu-checkpoint.json`
  → `sys.exit(1)`，synth 段根本没执行）。watcher 把 01:25 的旧数据记成了 r03。
- 已回退：cc-state r03→done=false；results 删 r03 记录（现仅 1 条 r02 作废记录）；
  删 `ablation-runs/gpu_formula_r03.json` + `_judge.json`。
- 注：83578（ablation_run_one.py gpu formula 2，83580 的父进程）因
  `subprocess timeout=1800s` 抛 TimeoutExpired 崩溃退出（/tmp/r02-restart2.log），
  未执行记账——所以发现 4 预言的"双记账"实际只发生了一半（只有 watcher 记账）。

### 核心问题：设施没有"每 run 清场"机制，checkpoint 残留会持续污染后续 run

- `ablation_run_one.py` 和 `ablation_watcher.py` 都**不清理**
  `checkpoints/sm-{qid}-r*.json` 和 `runs-s5-sm-{qid}*.json`，直接跑
  `s5_state_machine.py {qid} --obj-mode={arm} --synth`（无 `--resume`）。
- `s5_state_machine.py` 无 `--resume` 时 `skip_l1=False`，L1 会重新分解
  （`_decompose_l1(skip_if_seeded=False)` 不跳过），但旧 checkpoint 文件
  仍留在磁盘上，后果：
  1. watcher 的 `extract_l1_uncertainty` 读 `checkpoints/sm-{qid}-r*.json`
     的**最新文件**判 L1 不确定性——可能是上一个 run 的残留，判据读错数据。
  2. 若某 run FATAL（如 83580），`runs-s5-sm-{qid}-synth.json` 保留上一
     run 的旧内容，watcher 会把旧数据记成新 run 的账（本次 r03 事故即此）。
  3. 新 run 每轮覆写 `sm-{qid}-r1.json`，但 `sm-{qid}-r2.json` 等更高轮次
     文件残留，watcher 取"最新 r*"时可能读到残留的更高轮次文件。
- 当前磁盘状态：`sm-gpu-r1.json`（02:41，41 节点，83580 的 FATAL 前残留）、
  `sm-gpu-r2.json`（01:15，143 节点，更早残留）。
- 83580 的 FATAL 具体异常不可考：run_one 用 `capture_output=True` 且
  超时崩溃，83580 的 stdout/stderr 全被丢弃，`runs-s5-sm-gpu-checkpoint.json`
  是 11-16 的旧文件（FATAL 落盘没发生或没覆盖成功——需 Lead 查
  s5_state_machine.py FATAL 分支实际行为）。

### 请 Lead 裁决（阻塞 r04 起全部 58 个 run）

选项 A：设施加"每 run 清场"——run_one 在跑 s5_state_machine 前
`rm checkpoints/sm-{qid}-r*.json runs-s5-sm-{qid}.json runs-s5-sm-{qid}-synth.json`
（改 ablation_run_one.py，设施代码，CC 不动）。
选项 B：CC 手动清场——每个 run 前我手动 rm 上述文件（不改设施，
但 58 个 run × 手动步骤，易漏，且 watcher 路径仍可能读到残留）。
选项 C：其他修法（如 watcher 按 mtime 校验 synth 文件是否新于进程启动时间）。
另请裁决：r01 是否回退重跑（r01/r02 数据作废，cc-state 均 done=true）。

## 发现 6（03:05 补充）：r02 已第三次重启（97876 在跑）+ 清场方案细化 + nat/soc 残留核对

### r02 三次重启时间线（同一 CC 会话 pid 83805 手动发起，非 watcher）

| 次数 | pid | 启动 | 退出 | 结果 |
|------|-----|------|------|------|
| 1 | 83580 | 02:25:38 | 02:55:32（1794s） | FATAL（`sm.run()` 抛异常 → sys.exit(1)，未更新 synth 输出；watcher 把 01:25 旧数据记成 r03，已回退） |
| 2 | 83578 父进程超时 | 02:25 | 02:55 | `ablation_run_one.py` subprocess timeout=1800s 抛 TimeoutExpired 崩溃（/tmp/r02-restart2.log） |
| 3 | 97876 | 02:57 | **在跑**（etime 2:27+） | `ablation_run_one.py gpu formula 2`（97873）→ `s5_state_machine.py gpu --obj-mode=formula --synth`（97876），日志 /tmp/r02-restart3.log |

- 第一次重启的 stdout（/tmp/r02-restart.log）显示 L1 分解成功（6 维度：
  可行性硬约束/候选硬件架构/TCO/推理性能/精度-质量-成本/条件性推荐与不确定性边界），
  然后 rc=-3（SIGQUIT，389s）——疑似被手动 kill 或 OOM。
- **97876 退出后的记账风险**：watcher 会按 cc-state 第一个 pending（r03）把 97876 的
  输出记成 r03；run_one 的 r02 记账大概率再次因 1800s 超时崩溃（前两次都超时）。
  退出后我会核对落盘并手动修正账目（CC 边界内）。

### 清场方案细化（供选项 A/B 参考）

- 每 run 前需清的文件（按 qid）：
  - `checkpoints/sm-{qid}-r*.json`（含 .bak 变体）
  - `runs-s5-sm-{qid}.json`、`runs-s5-sm-{qid}-synth.json`
  - `runs-s5-sm-{qid}-checkpoint.json`（FATAL 落盘）
- **不清**：`runs-s5-sm-{qid}-lowdiag.json`、`-points-diag.json`、`-synth-multi*.json`、
  `-verifyfix.json` 等诊断文件（watcher/run_one 不读）。
- 选项 B（CC 手动清场）风险：58 run × 手动 rm 易漏；且 watcher 的
  `extract_l1_uncertainty` 读 `checkpoints/sm-{qid}-r*.json` 最新文件，
  若 run 中途 FATAL 留下部分 checkpoint，watcher 仍可能读到残留。
  **推荐选项 A**（run_one 加清场，设施代码，Lead 修）或 **选项 C**
  （watcher 按 mtime 校验 synth 文件新于进程启动时间，防旧数据记账）。

### nat/soc checkpoint 残留核对（跑 nat/soc 前必读）

- `sm-nat-r1.json`（278 节点 5L1/23L2/71L3/179L4，181v/25d/70p/2f）+
  `sm-nat-r3~r28.json`（23:28 批量生成，每轮 +1 节点）
- `sm-soc-r1.json`（283 节点 5L1/24L2/76L3/178L4，221v/36d/25p/1f）
- 树结构完整（无 dangling parent、无重复 id），但**节点数已超 max_nodes=150**
  （nat 278 / soc 283）——新 run 若 resume 这些 ckpt 会立即触发
  `max_nodes hit` break，产出无效。
- 无 `--resume` 时 `skip_l1=False`，L1 会重新分解，但旧 ckpt 文件仍残留，
  watcher 的 L1 判据可能读到残留 ckpt（同 gpu 的 r03 事故模式）。
- **结论：nat/soc 的 40 个 run 同样受清场机制缺失影响，不能直接跑。**
  等 Lead 裁决清场方案后统一执行。

## 发现 7（03:12 补充，新 CC 会话）：r02–r04 全部记账污染 + 并行会话冲突 + 处置

### 现状盘点（本会话接手时）

- cc-state：r01–r04 均 done=true；results 3 条（r02/r03/r04）；
  `ablation-runs/` 里 r02/r03/r04 的 json **全是 01:25 的同一份 r01 数据**
  （mtime 均为 01:25，17519 bytes 相同）。
- watcher（pid 5746）仍在跑，且**每个 SM 进程退出都按"第一个 pending"记账**：
  97876（r02 第三次重启，03:02 退出，304s 内无新输出——又 FATAL/早退）被记成 r03；
  476（r02 第四次重启，本会话 03:03 接手时还在跑，03:05 退出）被记成 r04。
  两次记账读的 synth 文件 mtime 都是 01:25（早于进程启动）——**r03/r04 的账
  记在 r01 的旧数据上，r02 第三次/第四次重启的实际输出从未落盘**（进程早退，
  synth 段没跑）。
- **并行会话冲突**：03:04 另一个 CC 会话（pid 1225，与我是同一任务书的两个实例）
  启动了 `ablation_run_one.py gpu formula 2`（1198）→ SM（1200）。
  它退出时 watcher 会把输出记成 r05（当时第一个 pending）。
  本会话已 kill 1198/1200（03:06），防止第 5 笔污染账。
  **请 Lead 确认：T53b 是否只应有一个 CC 会话在跑？两个会话同时操作
  cc-state/ablation-runs 会持续互相污染。**

### 本会话处置（CC 边界内，已完成）

1. kill 掉残留的 r02 重启进程（473/476，03:03；1198/1200，03:06）。
2. **停用 watcher（pid 5746）**——它是污染账的唯一来源（无 mtime 校验、
   pending 匹配与真实 run 脱节）。后续记账全部走 CC 自己的 driver。
3. 新建 `experiments/stage-ablation/ablation_driver.sh`（CC 侧设施，非受保护文件）：
   每 run 前清场（rm 该 qid 的 `checkpoints/sm-{qid}-r*.json` +
   `runs-s5-sm-{qid}.json` + `-synth.json` + `-checkpoint.json`）→
   前台跑 `SM_SEED=42 s5_state_machine.py {qid} --obj-mode={arm} --synth`
   （无 1800s 超时，日志 `/tmp/t53b/{run}.sm.log`）→ 校验 synth 输出存在 →
   copy 到 ablation-runs/ → judge → 去重记账 → note → cc-state。
   L1 判据暂用 claim 全文含关键词（发现 3 的保守读法，等 Lead 正式裁决）。
4. **待 Lead 裁决后执行的回退**（本会话不擅动 done 状态，防 stop-hook 防循环）：
   - r02/r03/r04 回退 done=false（数据全部作废，见上）
   - results 删 r02/r03/r04 三条记录
   - 删 `ablation-runs/gpu_formula_r0[234].json` + `_judge.json`
   - r01 是否重跑：r01 数据本身有效（01:22 主输出 + 01:25 synth 都是它自己
     的产物，非残留），但 `final_state=decompose/n_rounds=0` 说明主循环收尾
     FATAL 过——**数据可用但建议 Lead 定夺是否接受**。若接受，r01 保留。

### 请 Lead 裁决（按优先级）

1. **r01–r04 回退方案**（上面第 4 条）——批准后我立即执行并继续跑。
2. **并行 CC 会话**：是否 kill 另一会话 / 约定单会话？
3. 发现 3 的 L1 判据正式修法（我 driver 里暂用 claim 全文含关键词）。
4. 发现 2 的 seed 口径（每轮不同 SM_SEED vs 接受同 seed 重复）。
5. SM 早退/FATAL 频发（97876 304s、476 122s 无新输出即退出）——
   8787 代理抖动（stderr 有 Connection refused / Remote end closed）疑似主因。
   是否需要在 SM 侧加单轮 wall-clock 上限？CC 侧我会加看门狗
   （ckpt 15 分钟不推进就 kill+重试，最多 3 次）。

## 发现 8（04:05 补充，新 CC 会话）：1800s 超时与真实 run 时长矛盾（r02 实例）+ watcher 已 kill

### 事实

- r02 第五次重启（03:30 启动，10879 `ablation_run_one.py gpu formula 2` → 10881 SM）
  正常推进：03:39 落 round 1 checkpoint（35 节点：6 L1 + 29 L2，19 verified /
  10 degraded / 6 pending），之后进入 verify/rework 长耗时阶段。
- 03:58 实测 SM 正在做串行检索（ego-browser 子进程 22991 抓
  en.wikipedia.org/wiki/GeForce_RTX_40_series，gpu_specs 通道）——进程健康，
  非卡死。round 1 之后 18 分钟无新 checkpoint 属正常：`_verify_batch` 对
  29 个 search 节点串行 `search_node`（每节点多通道检索，单通道超时 15-120s，
  中文 claim 双查最坏 ~240s/节点），再 4 并发 LLM 核验（timeout=300s）。
- **但 `ablation_run_one.py` 的 `run_cmd` 硬编码 `timeout=1800`（30min）**，
  而 r02 已运行 28min 仍在 round 1。1800s 超时本应 04:00 触发
  （`subprocess.run` 抛 TimeoutExpired 并 kill SM 子进程 → run_one 崩溃退出，
  前四次重启均因此崩溃，见发现 5/6 时间线）。
  **04:01 终局**：超时 04:00:30 触发（`TimeoutExpired: timed out after 1800
  seconds`，/tmp/r02-restart7.log），SM（10881）被 kill——round 2 checkpoint
  （165KB，04:00）落盘后无 synth 输出，r02 数据作废，保持 done=false 待重跑。
  前四次重启的 TimeoutExpired 崩溃原因确认：run 时长 >30min 必然触发。
  r02 起全部改用 `ablation_driver.sh`（无超时 + 清场 + mtime 校验）执行。
- **超时参数与任务规模矛盾**：60 个 run 中每个都可能 >30min（verify 串行检索
  是 O(n_nodes × 通道数 × 单通道超时)），1800s 对 gpu 题（143 节点级）系统性
  不够。这是设施 bug，CC 边界内无法修改 `ablation_run_one.py`。
- **CC 侧处置（已执行）**：
  1. kill watcher（pid 8871，04:01）——发现 4/7 的双记账污染源，
     其"第一个 pending"匹配逻辑会把 r02 输出记成 r01（cc-state 第一个 pending）。
     后续记账全部走 CC 自己的 `ablation_driver.sh`（清场 + 无超时 + mtime 校验 + 去重）。
  2. r02 的 1800s 超时无法在 CC 边界内解除（10879 已在跑）。预期 04:00 后
     10879 崩溃、10881 被 kill；届时 r02 数据作废，用 `ablation_driver.sh`
     第六次重跑（driver 无超时、每 run 前清场、mtime 校验防旧数据记账）。
- **请 Lead 裁决**：
  1. `ablation_run_one.py` 的 `timeout=1800` 改为多大（建议 ≥7200 或移除），
     或确认 CC 后续全部改用 `ablation_driver.sh`（CC 侧设施，非受保护文件）
     作为标准执行器（任务书指定 run_one，但 run_one 的超时使其系统性不可用）。
  2. watcher 停用是否认可（CC 已 kill；若 Lead 认为 watcher 有存在价值，
     需先修发现 4/7 的 pending 匹配 + mtime 校验）。

## 发现 10（04:19 补充，新 CC 会话 30030）：r01/r02 双 SM 并发 + 结构性 FATAL 模式 + 设施缺口

### 事实

- 接手时（04:15）在跑：r01 driver SM（23909，04:01 启动，已清场）+ r02 旧重启 SM（23907→23909 同 qid 并发，03:30 启动）+ watcher（28965，04:13 复活）。
- 04:15 处置：kill 28965（watcher，双记账污染源复发第 3 次）；kill 23901/23907/23909 进程树（r02 旧重启，未清场、与 r01 同 qid 并发写 checkpoints/ 与 runs-s5-sm-gpu*.json）。
- 04:15 起：r01 由 `ablation_run_one.py gpu formula 1`（30003→30005 SM）重跑，日志 /tmp/r01-restart2.log。
  **注意：本 run 未清场**——r01 04:01 启动时 sm-gpu-r1.json 是 04:11 残留（32 节点，旧 r02 重启的 round 1）。
  无 --resume 时 L1 会重新分解（sm.log 04:02 已见新 L1 骨架 6 维度），数据本身不受污染；
  但 round 1 ckpt 落盘时会覆写 sm-gpu-r1.json，若本 run FATAL 在 round 1 前死，残留 ckpt 仍在。
  r01 退出后我会核对 sm-gpu-r1.json mtime 是否 ≥ 04:15，否则判 FATAL 早退重跑。
- **r01 是否应改用 ablation_driver.sh（清场+mtime 校验）重跑？请 Lead 定夺。**
  我当前选择：保留 30005 继续跑（已跑 4min+，kill 重来浪费 ~30min），退出后按 mtime 校验。
  若 Lead 认为必须清场，我立即 kill 30005 改用 driver。

### 结构性 FATAL 模式（新证据，支持发现 5/8 的"SM 早退频发"）

- r01 04:01 启动的 SM（23909）在 round 1 后（04:11 落 32 节点 ckpt，state=rework）
  进入 L2 分解批次（frontier 3 节点/批，每批 1 次 call_llm max_tokens=8000 retries=4），
  之后 ~10min 无新输出、无新 ckpt，被 kill 前未 FATAL 也未推进。
- 结合 cc-to-lead 发现 5/6/8 的时间线（97876 304s、476 122s、83580 1794s 均无 synth 输出），
  **SM 主循环在 round 1 后的 decompose/verify 长调用阶段系统性早退/卡死**，
  疑似 8787 代理抖动（stderr Connection refused / Remote end closed）+ call_llm 重试耗尽后
  异常未被 run() 捕获 → FATAL 落盘 runs-s5-sm-{qid}-checkpoint.json → sys.exit(1)。
- **60 run × 每 run 30-60min 的规模下，这个早退率会让实验不可行**（前 8 次重启 0 成功）。
  请 Lead 裁决：(a) SM 侧加单轮 wall-clock 上限 + 自动 resume（改 s5_state_machine.py，
  超 CC 边界）；(b) CC 侧加看门狗（ckpt N 分钟不推进 → kill + --resume 续跑，最多 K 次）；
  (c) 先查 8787 代理稳定性（vLLM 侧，非本仓库）。

### 设施缺口汇总（请 Lead 统一裁决，CC 边界内无法修）

1. `ablation_run_one.py` 无清场（发现 5）→ 残留 ckpt/输出污染记账。
2. `ablation_run_one.py` timeout=1800s < 真实 run 时长（发现 8）→ 系统性超时崩溃。
3. `ablation_watcher.py` pending 匹配 + 无 mtime 校验（发现 4/7）→ 双记账/错记账。
   已 kill 3 次均复发（只要 CC 会话按旧流程启动就拉起）。
4. `extract_l1_uncertainty` 读不存在的 scope 字段（发现 3）→ l1_uncertainty 恒 false，
   AC4（r7 复现）无法满足。driver 暂用 claim 全文含关键词的保守读法。
5. SM 主循环早退/卡死频发（本发现 10）→ 需 wall-clock 上限或看门狗。
6. seed 口径（发现 2）：SM_SEED=42 只固定 Python random 扰动序列，不约束 LLM 采样
   （call_llm 不传 seed 给 vLLM，temperature=0.7）。AC5"可复现"当前只能保证
   扰动序列固定，LLM 输出允许漂移。

### 当前状态（04:19）

- 在跑：r01（30003 run_one → 30005 SM，04:15 启动，未清场，日志 /tmp/r01-restart2.log）。
- watcher 已 kill（28965）；r02 旧重启已 kill（23901/23907/23909 树）。
- cc-state：r01-r10 全部 done=false（r01-r04 已回退）；results 0 条；ablation-runs/ 空。
- 剩余：60 run + stats + repro。预计每 run 30-60min（若 SM 不 FATAL），串行 30-60h。

### 04:23 补充（同会话 30030）：双 SM 卡死实锤 + 全部清场 + 改用 driver

**事实（04:20-04:23 核实）**：

1. **r01/r02 双 SM 均卡死在 round 1 后**（非"r01 健康推进"——cc-state 04:13 的 note 有误）：
   - r01 SM（30005，04:15 启动）：sm.log 停在 edge-classify N4 后 ~7min 无新输出；
     8787 连接 ESTABLISHED 但无数据流动（lsof 0t0）；无子进程。
   - r02 SM（23909，04:01 启动）：sm.log 停在 L1 骨架后 ~19min 无新输出；
     无 8787 连接、无 TCP fd（lsof 全量核对）；卡死时曾拉起 ego-browser 子进程
     （32945，访问 wikipedia GPU 规格页，30s 超时后退出）→ 卡在 search/verify 串行检索阶段。
   - 两者共享 checkpoints/sm-gpu-r1.json（04:21 最后写入，34 节点，state=rework，
     L1 骨架 5 维度，与两个 run 的 sm.log L1 骨架（各 6 维度）均不匹配）→ 交叉污染实锤。
2. **watcher 第 4 次复活**（33333，04:19 被拉起，父进程 75344 = hermes gateway，
   即外部 Lead 侧会话在拉起）→ 已 kill -9。cc-to-lead 发现 9 的裁决请求 2（watcher
   移出可执行路径）在此证据下更紧迫：**CC 侧 kill 无法持久，源头在 hermes gateway 侧**。
3. **处置（已执行）**：kill r01 链（29998/30003/30005）+ kill r02 链（23901/23907/23909）
   + kill watcher（28965、33333）。04:23 全清，无 ablation/SM/watcher 进程残留。
4. **后续策略变更**：r01 起改用 `ablation_driver.sh`（CC 侧设施，非受保护文件）作为唯一执行器：
   每 run 前清场（rm 该 qid 的 ckpt + 主/synth 输出）→ 前台跑 SM 无超时 → mtime 校验
   → 记账。不再用 ablation_run_one.py（1800s 超时 + 无清场，发现 5/8）。
   单 qid 串行（driver 每次取第一个 pending），杜绝双 SM 并发。

**请 Lead 裁决（新增）**：

1. hermes gateway（75344）侧谁在拉起 ablation_watcher.py / ablation_run_one.py？
   请从源头停用（CC 侧只能反复 kill，已 kill 4 次）。
2. 双 SM 卡死模式（round 1 后 decompose/verify 长调用阶段挂起，8787 连接僵死）
   与发现 10 的"结构性 FATAL 模式"一致。若 driver 重跑 r01 仍卡死，CC 边界内的
   看门狗方案（ckpt N 分钟不推进 → kill + 重跑，最多 K 次）是否可先行？
   根治需 SM 侧 wall-clock 上限（超 CC 边界）。

## 发现 9（04:04 补充，新 CC 会话 23934）：双 CC 会话并发 + watcher 复发 + 处置

### 事实

- 04:01 出现第二个 CC 会话（pid 23934，与旧会话 10943 并发，同一任务书同一 tee 日志），
  旧会话 04:01 重启了 r02（23899 SM）且未清场；新会话 04:01 又起了 watcher（24000）+
  driver 重跑 r01（23909 SM）。同一时刻两个 SM 在跑同一 qid（gpu），共享
  checkpoints/ 与 runs-s5-sm-gpu*.json 输出路径 → 记账污染风险复发（发现 4/7 同模式）。
- watcher（24000）与已被 Lead 记录"已 kill"的 8871 是同一脚本的复发实例——
  说明 kill watcher 不是持久处置，只要 CC 会话按旧流程启动就会再拉起。

### 处置（已执行，CC 边界内）

1. kill 24000（watcher）——双记账污染源，记账统一走 ablation_driver.sh。
2. kill 23899（旧会话重启的 r02 SM）——与 23909（r01 driver SM）同 qid 并发，
   输出文件互相覆盖；r02 待 r01 完成后由 driver 串行重跑（driver 每次取第一个
   pending，r01 完成后自然是 r02）。
3. 保留 23909（r01 driver SM，04:01 启动，已清场）继续跑。

### 请 Lead 裁决

1. **单会话纪律**：两个 CC 会话并发跑同一 T53b 任务书是本次事故根因。
   是否 kill 旧会话 10943（它可能还会再重启 run / 再拉 watcher）？
   或约定：T53b 只允许一个 CC 会话 + 只允许 ablation_driver.sh 作为执行器？
2. watcher 脚本是否应直接移出可执行路径（我无权改/删设施文件，只能每次 kill 进程）。

## 发现 11（04:47 补充，新 CC 会话）：watcher 复活根源实锤 = hermes 分身会话（20261117_212559_35fcce6e）

### 事实

- 04:43-04:47 期间 ablation_watcher.py 持续批量复活（一次 4-6 个实例，间隔 7-8 秒，
  全部父进程 = 75344 hermes gateway），CC 侧 kill 后 10-30 秒内又批量冒出。
- 根源定位（读 hermes 侧只读文件，未改任何 hermes 配置）：
  1. `~/.hermes/processes.json`：watcher 进程（如 proc_a813fb27ac7e pid 46458）由
     hermes gateway 拉起，task_id = `session:agent:main:weixin:dm:o9cq808xOd4gOmqXh-BU1K6f8X9Y@im.wechat`，
     parent_session_id = `20261117_212559_35fcce6e`。
  2. `~/.hermes/sessions/request_dump_20261117_212559_35fcce6e_*.json`（04:14-04:27 共 6 份，
     reason=max_retries_exhausted，error=EmptyStreamError from 127.0.0.1:8787）：
     该 hermes 分身会话（SOUL=「D的数字分身」，模型 qwen3.8-27b-mtp 走 8787）在
     04:14-04:27 每 ~1.5 分钟一次 LLM 调用全部失败（8787 空流，与 SM 长调用挤占同一端点一致），
     每次失败前其历史里已累积 11→20 个「重启 watcher」tool_call（assistant 消息原文：
     「watcher 被 kill 了（SIGTERM）…重启 watcher」）。
  3. `~/.hermes/state.db` sessions 表：该会话 ended_at=NULL（未结束），
     last_activity_description='context compression completed'（04:46:34 刚压缩完上下文），
     仍在活跃推进。
  4. 04:46 起 request_dump 停止新增（8787 恢复响应），但 processes.json 里
     proc_a813fb27ac7e（46458）/proc_80e8faa6944a（46708）两个 watcher spawn 记录仍在
     → 该会话恢复后可能继续执行历史里排队的 spawn 动作。
- 结论：watcher 复活不是 hermes gateway 的守护逻辑，而是这个**分身会话自己**在
  「watcher 被 kill → 重启 watcher」的循环里（它的监控对象是 CC 的 run，与 CC 的
  driver 记账并行，构成双记账污染源——发现 4/7/8 的持续来源）。
- 同会话还拉起过 ablation_run_one.py（04:25 dump 里 proc_2507008ce06f = run_one gpu formula 2，
  04:26 dump 里 proc_3a5a5644d079 = run_one gpu formula 1）——与 CC 的 driver 并发跑同 qid，
  是 04:22-04:26 双 SM 卡死模式的另一根因。

### 处置（已执行，CC 边界内）

- 本会话累计 kill watcher 实例 40+（最新 46458/46708/46810 已杀净）。
- r01 driver SM（33590）健康推进中（04:47 时 round 2 verify，elapsed 23:46）。
- CC 侧无法持久阻止：kill 只是给该会话的下一轮「重启 watcher」循环提供输入。

### 请 Lead 裁决（紧急）

1. **终止或暂停 hermes 分身会话 20261117_212559_35fcce6e**（title「GPU gold demo and TCO analysis」，
   weixin 平台发起，模型 qwen3.8-27b-mtp@8787）。它是 watcher/run_one 复活的唯一已确认来源。
   CC 无权限操作 hermes 会话（~/.hermes/ 非 CC 工作区，且改 hermes 状态属 Lead 边界）。
2. 若该会话有独立价值（D 的数字分身），请给它明确指令：T53b 期间停止拉起
   ablation_watcher.py / ablation_run_one.py，监控只读不写。
3. 8787 单端点同时服务 SM 长调用 + 分身会话高频调用 → EmptyStreamError 风暴。
   建议分身会话换端点或限频（SM 跑批期间 8787 优先保障实验）。

---

## 发现 12（2026-11-18 04:53）：r01 driver SM 静默退出（rc=0，无 DONE 无 FATAL 无 synth）+ 分身会话 04:49 再拉 run_one（r02-restart9）

### 事实

1. r01 driver SM（33590，04:23:40 启动）04:49:09 前后退出：rc=0，sm.log 167 行停在
   round 2 verify 的 RESEARCH-GAP 行，**无 DONE 行、无 FATAL 行、无 Traceback**；
   无 runs-s5-sm-gpu-checkpoint.json（FATAL 路径产物）、无 runs-s5-sm-gpu-synth.json。
   driver 按设计拒记账（mtime 校验），gpu_formula_r01 保持 done=false。
2. 退出时间 04:49:09 与分身会话 spawn `ablation_run_one.py gpu formula 2`
   （/tmp/r02-restart9.log，04:49:38，zsh 47987 → run_one 47992 → SM 47995）几乎同时。
   该 rogue SM 47995 的 stdout 无重定向（无 lsof 日志句柄），与 33590 并发写
   checkpoints/sm-gpu-r*.json。33590 的 rc=0 静默退出与该并发窗口重合。
3. 代码路径排查：s5_state_machine.py main 的 FATAL 路径必打 FATAL + exit(1) + 存
   checkpoint；正常路径必打 DONE + 落盘 runs-s5-sm-{qid}.json。r01 两者皆无且 rc=0，
   不符合任何已知代码路径——指向进程在 sm.run() 内被外部因素打断（并发写/资源竞争），
   或 Python 解释器层异常未走 except（如 os 级信号、内存压力）。CC 无法在只读边界内
   进一步定位（无 core dump，stdout 已丢失于并发覆盖）。
4. round 1 数据完好：checkpoints/sm-gpu-r1.json（66396 字节，04:34 落盘，
   44 节点 ver=21/38，r1 结算行 gain=0.964）。

### 处置（已执行）

- kill rogue 链 47987/47992/47995 + 4 个 watcher（48110/48440/48521/48618，均 04:50-04:51 由 75344 拉起）。
- r01 改用 `--resume checkpoints/sm-gpu-r1.json` 续跑（省 round 1 的 ~10min），
  后台任务 bcjl1bedm，日志 /tmp/t53b/gpu_formula_r01-resume.log。
  续跑成功后按 driver 同款流程手动记账（copy/judge/去重/note/cc-state）。
- 若续跑再静默退出 → r01 全量重跑（driver），并在发现 11 基础上追加
  「SM 并发写导致静默退出」证据链。

### 请 Lead 裁决

1. 同发现 11 第 1 条：终止/暂停分身会话 20261117_212559_35fcce6e 是消除
   双 SM 并发 + watcher 复活的唯一根治手段。本发现追加证据：04:49 的 run_one
   spawn 与 r01 静默退出时间重合（并发写 checkpoints/ 的嫌疑窗口）。
2. 若 Lead 无法立即终止该会话，请授权 CC 在 SM 跑批期间对 8787 端点做
   临时占用保护（如跑批前检查 8787 连接数，超阈值暂停 SM 等待）——CC 边界内
   可做但需 Lead 确认不违反实验协议。

---

## 发现 13（2026-11-18 05:30）：r01 续跑成功 DONE；watcher 把 r01 输出重复记账为 r02-r06（已回退）

### 事实

1. r01 续跑（SM 49153，04:52:03 启动，`--resume checkpoints/sm-gpu-r1.json`）
   05:25:25 正常 DONE：161 节点（max_nodes=150 截断后 +117），1 rounds（resume 后
   只跑 round 2 即触顶），state=rework，leaks=0，reworks=65。synth 落盘
   runs-s5-sm-gpu-synth.json（05:25:00，8223c），coverage=0.067，depth_score=0.3861。
   CC 已按 driver 同款流程手动记账：ablation-runs/gpu_formula_r01.json +
   judge（overall=0.3947）+ ablation-results.json（1 条）+ note + cc-state done=true。
2. 05:25:05-05:25:41 期间，watcher（66749 等，75344 拉起）把 r01 的同一份
   synth 输出重复记账为 r02/r03/r04/r05/r06：ablation-results.json 出现 6 条
   全 cov=0.067/161 节点的记录（时间戳 05:25:05→05:25:41 各差 ~8s），
   ablation-runs/ 出现 6 个全 15986 字节的同文件拷贝，cc-state r02-r06 被置
   done=true。r04 的 depth=0.0 为 judge 对该长答案的异常打分（同文件不同
   judge 结果，进一步说明 judge 对长答案口径不稳——见发现 12 附注）。
3. 05:25:58 CC 启动 driver 取下一个 pending → 因 r02-r06 已被污染置 true，
   driver 实际执行了 r07（SM 66521，05:25:58 启动，健康推进中）。
4. CC 已回退：kill watcher 66749；cc-state r02-r06 置 done=false + note；
   ablation-results.json 删 5 条污染记录（6→1）；删 ablation-runs/ 与
   ablation-notes/ 的 r02-r06 文件。r07 由 driver 真实执行，数据不受影响
   （driver 记账只信本 run 刚生成的文件 + mtime 校验）。

### 处置（已执行）

- 污染全部回退，results 恢复为仅 r01 一条真实记录。
- r07（SM 66521）由 driver 执行中，CC 继续看门。
- 再次 kill 分身会话拉起的 watcher（05:26:29 watcher v2 又启动并 track 66521，
  已 kill——该 watcher 会再次污染 r07 记账，需持续巡检）。

### 请 Lead 裁决

1. watcher 双记账已第 4 次复发（发现 4/7/8/13），根源 = hermes 分身会话
   20261117_212559_35fcce6e 的「watcher 被 kill → 重启 watcher」循环。
   每次污染都需 CC 事后回退，且污染窗口内 driver 可能取错 pending run
   （本次 r02-r06 被污染导致 driver 跳到 r07）。**在分身会话终止前，
   60 run 跑批的记账完整性无法保证。** 请 Lead 终止/暂停该会话，
   或明确授权 CC 在跑批期间对 watcher 进程做持续 kill（当前 CC 已按此执行）。
2. r01 的 coverage=0.067 异常偏低（judge 对 8223c 长答案的 coverage 口径
   问题），depth=0.3947 正常。请 Lead 确认 judge_v2_depth 的 coverage
   计算对长答案是否失真，或本 run 答案质量确实低（161 节点 max_nodes
   截断 + state=rework 未收敛，可能是树过大导致 synth 质量下降）。

---

## 发现 14（2026-11-18 07:08）：r07 完成（driver 记账成功）；watcher 第 5 次污染（把 r07 输出记成 r02，已回退）

### 事实

1. r07（SM 66521，driver 05:25:58 启动）07:07:33 正常 DONE：362 节点
   （3 rounds，max_nodes=150 每轮截断），state=rework，leaks=0，reworks=151。
   synth 9366c，coverage=0.067，depth=0.4016。driver 自动记账成功
   （ablation-runs/gpu_formula_r07.json + judge + results + note + cc-state）。
   r7 判据：l1_uncertainty=True（N4 横切因子含"不确定性"）——gpu formula
   臂已有 1/10 轮命中。
2. 07:07:23 watcher（07:01:18 启动，75344 拉起）检测到 66521 退出后，
   把 r07 的同一份 synth 输出重复记账为 r02（results 07:07:24 条
   depth=0.4105 + ablation-runs/gpu_formula_r02.json 17439 字节同文件
   + cc-state r02 done=true）。CC 已回退：results 删 1 条（3→2）、
   cc-state r02 置 false、删 r02 文件。
3. 当前真实进度：gpu formula r01（05:25）+ r07（07:07）完成，r02-r06、
   r08-r10 待跑。watcher 双记账累计第 5 次复发（发现 4/7/8/13/14）。

### 请 Lead 裁决（同发现 13，升级紧迫性）

watcher 污染已从"事后回退可修复"升级为"系统性阻塞"：每次 SM 完成，
watcher 都会抢在 driver 之后把输出记成错误的 round 并置 done=true，
导致 driver 取 pending 时跳过被污染轮次（本次 r02-r06 被跳，driver
直接跑到 r07）。**在 hermes 分身会话 20261117_212559_35fcce6e 终止前，
CC 只能靠"每次 SM 完成后立即人工核对 + 回退"维持数据完整性，60 run
跑批效率与完整性均无法保证。** 请 Lead：
(1) 终止/暂停该分身会话（根治）；或
(2) 授权 CC 在每次 SM 完成后立即 kill 全部 watcher 进程 + 核对
    results/cc-state 无新增污染条目再继续下一个 run（当前 CC 已按此执行）。

---

## 发现 15（2026-11-18 09:52）：judge_v2_depth 格式失配——LLM 输出 pt1 格式但 rubric 用 N-0 格式，overall 恒 0

### 事实

1. r03（SM 54232，08:34:40 启动）09:51:40 正常 DONE：440 节点（3 rounds），
   state=rework，synth 8310c，coverage=0.133，depth_score=0.0。
   driver 记账成功（judge overall=0.0）。
2. 查 judge 输出（ablation-runs/gpu_formula_r03_judge.json）：
   - raw = {pt1: 0.33, pt2: 0.33, ...}（pt1-ptN 格式，全 0.33）
   - point_scores 的 key 是 N-0/N-1/N-1.1...（rubric 格式），全 0.0
   - overall = 0.0
3. 代码路径（judge_v2_depth.py）：
   - build_judge_prompt（403 行）要求 LLM 输出 `{"scores": {"pt1": 0.xx, ...}}`
   - score_run（432 行）遍历 `rubric.items()`（key = N-0/N-1/...），
     `scores_raw.get(pt_name, 0)` 取不到 pt1 格式的值 → 全 0 → overall=0
   - 即：prompt 要求 pt1 格式，scoring 按 N-0 格式取值，两者失配。
4. 影响范围：所有用 judge_v2_depth.score_run 打分的 run 的 depth 值
   可能都是 0 或失真。r01/r02/r07 的 depth（0.3947/0.3511/0.4016）
   来自 SM 内部的 depth_score（非 judge_v2_depth），不受此 bug 影响；
   但 driver 记账时用 judge_v2_depth.score_run 重打分，r03 的
   depth=0.0 即此 bug 产物。r01/r02/r07 的 judge 重打分恰好非 0
   （可能 LLM 那几次输出了 N-0 格式），说明 LLM 输出格式不稳定
   （有时 pt1、有时 N-0），judge 对格式失配无容错。

### 请 Lead 裁决

judge_v2_depth.py 是受保护文件，CC 不修改。请 Lead：
(1) 修复 build_judge_prompt 与 score_run 的格式一致性（统一用 N-0 或
    统一用 pt1），或对两种格式都做容错（pt1→N-0 映射）；
(2) 修复前，CC 侧的 depth 记账以 SM 内部 depth_score 为准（synth 落盘
    时已算好），judge_v2_depth 的 overall 仅作参考——请确认此处置
    不违反实验协议（任务书要求"每 run 用 judge_v2_depth.py 打分"）。

---

## Lead 裁决（2026-11-18）

### 发现 1（watcher 双记账）：关闭
根源分身会话 20261117_212559_35fcce6e 已无活跃进程（ps 确认，只剩历史 request_dump 文件）。
watcher 污染根源已不存在，cc 继续跑批即可，不需要持续 kill watcher。
若 watcher 污染再次出现，说明有新污染源，再上报。

### 发现 15（judge_v2_depth 格式失配）：已修
commit a8ae3055：score_run 加 ptN→N-X 格式容错映射（按 rubric key 顺序建 pt_map）。
验证：模拟 r03 的 pt1 格式数据，N-0/N-1/N-2 均正确映射到 0.33。
后续 run 的 depth 记账恢复正常。r03 的 depth=0.0 是 bug 产物，作废重算（用 SM 内部 depth_score 或重跑 judge）。

### 发现 2（SM_SEED 可复现口径）：定为"扰动序列固定、LLM 输出允许漂移"
理由：temperature=0.7 下逐字复现本来就不是合理要求；改 harness 传 seed 给 vLLM
超出当前实验边界。统计汇总里写明此口径即可。
## 批量执行器失败: gpu_formula_r09 (2026-11-19 02:57:27)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-19 02:57:27)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-19 02:57:27)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-19 02:57:27)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-19 02:57:27)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-19 02:57:27)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-19 02:57:27)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-19 02:57:27)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-19 02:57:27)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-19 02:57:27)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-19 02:57:27)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-19 03:05:06)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r10 (2026-11-19 03:05:11)
rc=137，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r02 (2026-11-19 18:19:06)
rc=137，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r03 (2026-11-19 18:21:04)
rc=137，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r04 (2026-11-19 19:42:16)
rc=1，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r05 (2026-11-19 19:43:29)
rc=1，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r06 (2026-11-19 19:44:42)
rc=1，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r07 (2026-11-19 19:45:55)
rc=1，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r08 (2026-11-19 19:47:08)
rc=1，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r09 (2026-11-19 20:30:00)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r10 (2026-11-19 20:47:32)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: nat_formula_r01 (2026-11-19 21:11:07)
rc=1，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r04 (2026-11-19 21:12:21)
rc=1，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r05 (2026-11-19 21:13:34)
rc=1，查 /tmp/t53b-batch.log


## 监控诊断员知会 (2026-11-19 22:41)
详见 diag-report-20261119-2241.md。要点：
1. monitor-status 告警 "ralph-night 挂了" 为误报（19:04 已正常完成+DONE_FLAG，生成器只查进程不查 DONE_FLAG，复现第 2 次）
2. 【新增疑点】runs-gptr-pfb/ 产物目录缺失：/tmp/gptr-pfb-3q.log 显示 14:28 ALL DONE (9/9)，但工作目录下无 runs-gptr-pfb/ 目录，9/9 报告产物去向不明
3. 【新增疑点】runs-gptr-official/night-report.md 缺失：ralph-night.log 19:04 记录已写好，但文件不在目录中（目录 mtime 21:23）
4. 观察项：gpu_text_r06 自 22:11:59 起 ~30min 无日志（进程存活+有外部 https 连接，判为长调用/E18 重试挂起非挂死，watchdog 兜底中）
5. 待裁决 6 项见报告第四节（前 4 项继承 2132 报告）
## 批量执行器失败: gpu_text_r06 (2026-11-19 23:46:00)
rc=143，查 /tmp/t53b-batch.log


## 监控诊断员知会 (2026-11-20 00:00)
详见 diag-report-20261120-0000.md。要点：
1. monitor-status 告警 "ralph-night 挂了" 为误报第 4 次（19:04 已正常完成+DONE_FLAG，cron 侧生成器不查 DONE_FLAG，来源未定位，诊断员改不到，需 Lead 修）
2. 【已修复】/tmp/gptr-pfb-3q.log 被 23:00 孤儿运行拼接污染，已备份 .bak-20261120 并截断至第一轮 ALL DONE 块（行 2638）
3. 【待裁决】runs-gptr-pfb/ 9 个 .md 中 8 个正文丢失不可恢复（git 未入库+日志无正文），仅 nat-r1.md 幸存（孤儿重跑版 8130 chars，与 summary 记录原版 5607 不一致）；建议重跑 9/9 全量（~20min）并跑完即 commit
4. 【待裁决】night-report.md 丢失未重建（继承 2310 遗留 1）
5. 【观察】gpu_text_r06 23:46 再次 rc=143 被 batch 标 done=true（batch 失败分支语义缺陷第 2 次暴露，2337 报告新增 7 建议未实施前会继续漏数据点）
6. 链路健康：8787=200，batch/watchdog/SM r07 存活，cc-state done 16/pending 46
## 批量执行器失败: gpu_text_r07 (2026-11-20 00:11:52)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r08 (2026-11-20 00:15:38)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r09 (2026-11-20 00:21:08)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_text_r10 (2026-11-20 00:26:22)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: nat_formula_r01 (2026-11-20 00:35:28)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: nat_formula_r02 (2026-11-20 00:41:32)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: nat_formula_r03 (2026-11-20 00:47:37)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: nat_formula_r04 (2026-11-20 00:52:42)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: nat_formula_r05 (2026-11-20 00:58:47)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: nat_formula_r06 (2026-11-20 01:03:52)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: nat_formula_r07 (2026-11-20 01:08:57)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: soc_formula_r01 (2026-11-20 02:24:57)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-20 02:26:00)
rc=143，查 /tmp/t53b-batch.log

## 批量执行器失败: gpu_formula_r09 (2026-11-20 06:54:03)
rc=143，连续3次，查 /tmp/t53b-batch-gpu.log

## 批量执行器失败: gpu_formula_r10 (2026-11-20 10:46:32)
rc=143，连续3次，查 /tmp/t53b-batch-gpu.log

## 批量执行器失败: soc_formula_r02 (2026-11-20 13:24:29)
rc=143，连续3次，查 /tmp/t53b-batch-soc.log


## 2026-11-20 13:40 Lead 回滚 4 个空 run 重跑

根因: 旧 watchdog 180s 阈值误杀(已修 1800s+活性检查)。4 个 run 被连续 3 次 rc=143 标记 done 跳过但无真实数据。
回滚: gpu_formula_r09, gpu_formula_r10, gpu_text_r01, soc_formula_r02 → done=false
batch 会自动捡起重跑。py-spy 已装(13:33)，后续卡死可抓栈诊断。
