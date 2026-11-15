# T-soc-ckpt-team-20261116 — _save_checkpoint verify-only 落盘 bug + gate 加强（agentteam core）

**origin: ai** · 派发: zero (Hermes) · 2026-11-16 · 工作目录: /Users/a1-6/Desktop/workspace/pfb

## 背景（最小必要）
`experiments/stage-ablation/s5_state_machine.py` 的 soc 臂 `--verify-only` 模式跑了 1h+，
日志到 `verified 75/108`，但磁盘 checkpoint `checkpoints/sm-soc-r1.json` mtime 停在开始时间，
内容仍是 `verified=174, pending=77, degraded=31`（cov 0.615）。
即：verify-only 模式下 `_save_checkpoint` 没有有效落盘，1h 白跑。
日志证据：`experiments/stage-ablation/runs-s5-sm-soc-verifyonly.log`。

## 任务
1. **定位 bug**：读 `s5_state_machine.py` 的 `_save_checkpoint` 和 verify-only 调用链，找出为什么 verify-only 模式下 checkpoint 不落盘（是根本没调用？写到了别的路径？文件锁？异常被吞？）。
2. **修复**：让 verify-only 每完成一批 verify 就落盘一次 checkpoint（原子写：先写 tmp 再 rename，防半截文件）。
3. **自测**：写一个最小测试（用 2-3 个假节点跑 verify-only 一小批，断言 checkpoint 文件的 mtime 更新且 verified 计数变化）。跑通才算完成。
4. **gate 加强**：在 gate 检查逻辑里加三项机器可查断言（不能只查 cov ≥ X）：
   - final json 存在且可解析
   - node count > 阈值（283）
   - checkpoint 的 verified 计数与 final json 一致
5. **commit**：全部改完 commit 到 main（commit message 前缀 `fix(soc):`），并在本文件末尾追加"## 完成报告"一节（改了什么文件、测试输出、commit hash）。

## 约束
- 只改 `experiments/stage-ablation/` 内的文件，不碰其他目录。
- 不许把 degraded 节点批量翻成 verified（SOC 纪律：cov 必须来自真实判断）。
- 每步验证后再做下一步；测试失败就停，报告卡在哪。
- **完成报告不存在 = 任务未完成，Lead 不验收。**