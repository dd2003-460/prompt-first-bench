# T8c-CapFix-Verify 任务卡（2026-11-27 00:07 立项）

# origin: ai
# 类型：纯执行（单阶段重跑验证）
# 前置：commit 5c718d398（MAX_B_REVIEW=16384 已落地，run_exp_t8c.py）

## 背景（执行者只需知道这些）
run3-04.5 曾撞 12288 上限截断（finish_reason=length，reasoning 14866 tok）。
harness 已修：04.5 阶段单独上限 16384（MAX_B_REVIEW），其余阶段仍 12288。
本任务验证修复有效：重跑 1 个 B 臂样本，确认 04.5 不再截断。

## 执行步骤
1. 起进程必须 `setsid nohup`（executor-protocol 硬性要求，Hermes 跟踪后台≠脱离，F3 反例）。
   单 run 验证脚本已备好（`capfix_verify_single.py`，逻辑与 run_exp_t8c.run_arm_b
   单 run 同源，sidecar 写隔离目录 `t8c_stages_capfix-verify/` 不覆盖 smoke 数据）：
   ```
   cd tasks/think-trigger/exp-results
   setsid nohup python3 capfix_verify_single.py > t8c-capfix-verify-$(date +%Y%m%d-%H%M%S).log 2>&1 &
   echo $! > capfix-verify.pid
   ```
2. PID 同时写入 goal state：`~/.hermes/.stage-gate/research-agi-budget.json`
   的 context.restart_pid（防 stop_hook 等待分支失明，F1 教训）。
3. 探活：`kill -0 $(cat capfix-verify.pid)` + 日志末尾 + sidecar 落盘三件事都查
   （长跑进程三判据，executor-protocol）。预计 30-60 分钟（6 阶段串行）。
4. 完成后写回执 `tasks/agent-orchestration/receipts/T8c-CapFix-Verify.json`
   （status/finished_at/verdict/evidence：pid、log 路径、sidecar 04.5 的
   finish_reason、completion_tokens）。

## 验收标准（Lead 验收用）
- [ ] run1-04.5 的 `finish_reason == "stop"`（非 length）
- [ ] 该 run 全部 6 阶段无 finish_reason=length
- [ ] 04.5 的 completion_tokens 记录在案（对照 run3 旧值 12288 截断）
- [ ] 结果文件 `capfix-verify-outputs.json` 落盘，未覆盖 `raw_outputs_t8c.json`
- [ ] 回执 JSON 落盘

## 边界
- 不跑 A 臂、不改 harness、不动 STAGES 指令
- 不扩样、不跑 n=9
- 若 04.5 仍 length（16384 也不够）→ 如实回执 verdict=FAIL + 实际
  completion_tokens，Lead 再决策（提 20480 或加长度约束指令），不自行改 harness
