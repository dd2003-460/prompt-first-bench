# Q7 队列 rep 复制污染：根因 + 719 兜底核验（2026-11-24 22:20）

## 现象（证据）
- `q7-300-r1-20261124-132123.json` 与 `q7-300-r2-20261124-144315.json` **sha256 字节级相同**（d716d00859194e28…），节点 claim 指纹相同（82b665fe94）。
- 队列日志：`budget=300 rep=2 rc=1 wall_s=10115` —— r2 实际运行失败（跑了 2.8h 后崩），但落盘文件是 r1 的内容。
- 曲线 JSON 已正确消化：`budget=300, n_reps=2, note:"r2 剔除 (r1 复制)"`（20:47 构建时已知）。

## 根因（本轮钉死）
队列脚本 L36：`if [ -f runs-s5-sm-q7.json ]` 只查文件**存在**，不查新鲜度/不查 rc。
rep 失败（rc≠0）时，`runs-s5-sm-q7.json` 残留上一个成功 rep 的内容 → 被 cp 成失败 rep 的"结果" → 评分照跑、分数照记 → 伪重复。
（此前笼统记作"blind cp 污染"，本轮定位到具体行。）

## 50-r2/r3 分数巧合（非污染，已排除）
50-r2 与 50-r3 的 judge 三位分相同（total 0.3577 / depth 0.600 / cov 0.115），但 sha256 不同、节点指纹不同、metacog 不同（0.0480 vs 0.3480）= 独立 run，离散分（cov=命中/units，depth 0.2 台阶）巧合。不剔除。

## 719 档兜底（本轮核验 watcher 脚本）
`q7-719-overnight-watcher.sh` L33-37 post-run 协议：跨 rep claim-set sha1 比对 + n_nodes<500 标志。
若 719-r2/r3 也 rc≠0 被残留文件污染 → watcher 报告会标"claim-set 与 X 相同 = 复制污染"。
**兜底覆盖 719 档，不覆盖其他档**（glob 只 q7-719-r*.json）——但 50/100/150/300 已全部落盘完毕，无前瞻风险。

## 明早协议
1. 读 watcher 报告 `q7-719-postrun-report-*.md`：若 r2/r3 任一标"复制污染" → 该 rep 从 cov n=3 剔除，719 档按实际独立 rep 数（2 或 3）统计。
2. 评分 JSON（q7-scan-scores.json）里被污染的 rep 条目**不要手工删**（保留审计痕迹），分析时按 watcher 报告的标志剔除。
3. 队列脚本（PID 99447 运行中）**不要改**（bash 增量读脚本，运行中编辑会损坏执行）。修复留给队列结束后：cp 前比对输出文件 mtime ≥ run 开始时间，或 rc≠0 时不 cp。

## 300-r2 崩溃根因（22:24 补查）
- 崩溃链：vLLM proxy 瞬时 502（17:29 多次 retry 失败）→ `call_llm` 重试耗尽返回 None → `s5_pipeline.py:243` `out, _ = call_llm(...)` 解包 None → TypeError FATAL（s5_state_machine.py L637 _verify_batch 线程池内抛出）。
- 性质：瞬时 infra 故障 + 代码未处理 None，非系统性 bug。r2 当前调用正常（502 已恢复）。
- **不修 s5_state_machine.py（队列运行中）**：r3 未启动，会 import 改后文件，破坏单变量前提。修复=队列 DONE 后给 call_llm 返回值加 None 守卫（follow-up）。
- 风险兜底：719-r2/r3 若踩同款崩溃 → watcher claim-set 复制标志捕获，最差 719 档 n=3→n=2，可接受。

## 状态
- 300 档：n=2，曲线已正确，无后续动作。
- 719 档：r2 在跑（~22:40 落盘），r3 排队（~00:55 完），watcher 72026 兜底。
- 队列脚本修复：队列 DONE 后做（follow-up，不阻塞）。
