# T53b 批量验证与记录脚本 — 完整测试规划

> 目标：批量执行器（t53b-batch.sh）+ watchdog（t53b-watchdog.sh）+ driver（ablation_driver.sh）
> 三条路径全部实测通过，确保 55 个 pending run 夜间无人值守跑完不出事故。

## 组件清单

| 组件 | 文件 | 职责 |
|------|------|------|
| 批量执行器 | `t53b-batch.sh` | 循环取 pending → 调 driver → 失败标记跳过 → 全完 commit |
| driver | `ablation_driver.sh` | 清场 → 跑 SM → mtime 校验 → judge → 记账 → 更新 cc-state |
| watchdog | `t53b-watchdog.sh` | 60s 轮询：8787 健康 → batch 活着？→ 防双 SM → commit+重启 |
| SM | `s5_state_machine.py` | 状态机跑一个 qid（~30min），写 synth json + checkpoints |
| judge | `judge_v2_depth.py` | score_run(qid, answer) → overall 分数 |

## 落盘机制（数据不丢的三层保障）

1. **checkpoint**：SM 每完成一个节点写 `checkpoints/sm-{qid}-r{round}.json`（运行中持续落盘）
2. **run 产物**：SM 完成 → `ablation-runs/{run}.json` + `{run}_judge.json`（完整输出）
3. **汇总**：`ablation-results.json`（去重追加）+ `ablation-notes/{run}.md`（摘要）+ `cc-state.json`（done=true）

## 测试矩阵

### T1 正常路径（mock SM 2s 完成）
- 输入：cc-state 3 个 run，r01 done，r02/r03 pending
- 预期：batch 跑完 r02+r03 → cc-state 全 done → ablation-runs 有 4 个文件（2 json + 2 judge）→ results.json 2 条 → notes 2 个 md → batch 退出
- **状态：✅ 通过**（暴露 bug 1: zsh nomatch, bug 2: RC unbound in python -c）

### T2 失败路径（mock SM 第 2 次调用 exit 1）
- 输入：同 T1，mock SM 对 r03 故意 exit 1
- 预期：r02 成功记账 → r03 失败 → driver exit 1 → batch 捕获 rc=1 → 标记 r03 done=true + note → 写 cc-to-lead.md → 不记账 r03 → batch 继续（无更多 pending）→ 退出
- **状态：✅ 通过**（暴露 bug 3: `if ! cmd` 退出码陷阱, bug 4: `$RC，` 中文标点吞字节）

### T3 watchdog 重启路径（真实环境自然验证）
- 触发：kill batch → SM 继续跑 → watchdog 检测"SM 还在跑"等待 → SM 完成 → driver 记账 → driver 退出 → watchdog 检测"无 SM/driver 残留" → commit → 重启 batch → batch 读 cc-state 取下一个 pending
- 预期：watchdog 日志出现"commit 后重启" + "已重启 PID" → 新 batch 进程出现 → 开始跑 r09
- **状态：⏳ 等待 r08 完成（01:48 启动，预计 02:20 左右结束）**

### T4 断点续跑（mock 环境）
- 输入：cc-state 5 个 run，前 2 个 done，后 3 个 pending
- 操作：启动 batch → 等第 3 个 run 跑到一半 → kill batch → 等 65s → watchdog 重启
- 预期：重启后 batch 从第 3 个 pending 继续（不重跑前 2 个）
- **状态：✅ 核心逻辑通过**（batch 启动时跳过已完成的 r01/r02、从第一个 pending 开始，已验证；"kill 中途再重启"与 T3 走同一代码路径——watchdog 重启的 batch 读 cc-state 取第一个 pending，由 T3 真实环境自然覆盖）

### T5 8787 不健康（mock 环境）
- 输入：8787 端口无服务（health URL 改到不存在的端口 9999）
- 预期：watchdog 日志"8787 不健康，等 60s" → 不重启 batch → 8787 恢复后继续
- **状态：✅ 通过**（5 次"不健康"，0 次"重启"）

### T6 全部完成后 watchdog 退出
- 输入：cc-state 全部 done=true
- 预期：watchdog 日志"全部完成，watchdog 退出" → 进程退出
- **状态：✅ 通过**（日志"全部完成，watchdog 退出"，exit 0）

### T7 记账正确性（mock 环境）
- 输入：mock SM 写不同 coverage/depth 值 + checkpoint 文件（含 verified/degraded 节点 + L1 claim）
- 预期：ablation-results.json 里每条的 coverage/depth 与 SM 输出一致 → judge 分数正确 → n_nodes/n_verified 统计正确 → L1 判据正确
- **状态：✅ 通过**（gpu/nat/soc 三个 qid 的 cov=0.6/0.7/0.8 各自正确落账；n_verified=2、n_degraded=1、l1_unc=True 全对。注意：节点统计从 checkpoints/ 读，mock 必须模拟写 checkpoint 才能验证）

### T8 防双 SM 竞态（真实环境已验证）
- 触发：kill batch 时 SM 在跑
- 预期：watchdog 日志"防双 SM 冲突" → 每 60s 等待 → SM 完成后才重启
- **状态：✅ 通过**（02:04-02:17 连续 14 条等待日志）

## 已发现的 bug（全部已修复）

| # | 位置 | 症状 | 根因 | 修复 |
|---|------|------|------|------|
| 1 | driver L32 | `rm -f sm-gpu-r*.json` 文件不存在时 zsh nomatch 报错退出 | zsh 默认 nomatch 行为 | `setopt NULL_GLOB` |
| 2 | batch L51 | `python3 -c "...$RC..."` 报 unbound variable | bash 对多行双引号字符串的变量展开边界行为 | 改 heredoc + 环境变量传递 |
| 3 | driver L40 | `if ! cmd; then RC=$?` 捕获不到 SM 真实退出码（总是 0） | `!` 反转退出码，then 里 `$?` 是 `!` 的值 | 改 `cmd \|\| RC=$?` + `if [ $RC -ne 0 ]` |
| 4 | batch L67 | `echo "rc=$RC，查..."` 报 unbound variable | bash C-locale 下 `$RC，` 变量名后紧跟多字节字符吞字节 | 改 `${RC}` 花括号显式界定 |

## 测试环境

- 位置：`/tmp/t53b-test/`（完全隔离，不碰真实数据）
- mock SM：2 秒完成 + 写假 synth json（T2 用计数器让第 2 次调用 exit 1）
- mock judge：固定返回 overall=0.7
- mock cc-state：3 个 run（gpu_formula_r01/r02/r03）
- 隔离方式：sed 替换 cd 路径 + LOG 路径，0 处残留真实路径

## 验收标准

- T1-T8 全部通过
- 真实环境 r08 跑完后 watchdog 自动重启 batch（T3 自然验证）
- 55 个 pending run 夜间跑完，ablation-results.json 有 55+ 条记录
- 无数据丢失（checkpoint + run 产物 + 汇总三层完整）
