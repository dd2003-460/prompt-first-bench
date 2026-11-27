# 隔离注记（2026-11-27 16:25, orch 执行者 DEAD 接力）

## 隔离了什么
本目录 7 个文件来自 resume wrapper 3651 在 16:11 被 kill 时的伪产物，全部移入此处（未删除）：
- q9-300-r2-20261127-154138.json / q9-300-r3-20261127-161135.json / q9-719-r1-20261127-161149.json
- q9-300-r2.stdout / q9-300-r3.stdout / q9-719-r1.stdout / q9-719-r2.stdout

## 死因（已核磁盘，证据链闭合）
1. resume wrapper 3651（PPID=1 已脱离）15:41:38 起，补 300-r2/r3 + 719x3。
2. 16:11 Lead 发现 3651 泄漏未杀（持续重拉子进程抢 8787），kill -9 全清
   （goal state restart_pid_note 有记录；commit fa1935be1 记录了 15:50 停扫决策与 kill）。
3. **伪产物机制**：q9_budget_scan_queue.sh L35-38 在每次 run 后无条件
   `cp runs-s5-sm-q9-agi.json $OUT/q9-...json`（SM 共用固定输出文件，rc 非 0 也 cp）。
   kill 时 worker 正跑 719-r2，`runs-s5-sm-q9-agi.json` 停留在 300-r1 的内容
   （sha256 ca8b5c8daf...），被 wrapper 依次 cp 成 300-r2/300-r3/719-r1 三个 json。
4. **铁证**：3 个伪 json 与 q9-300-r1-20261127-144752.json 字节级相同
   （sha256 全 = ca8b5c8daffbaacd03489aa878da09eca802cdf4418d6e1d58190162fe182857），
   且 mtime 全落在 kill 时刻 16:11:35-16:11:55；resume log 记 rc=143(SIGTERM)/137(SIGKILL)。
   300-r2 跑了 1797s 后被杀（其 stdout 16:11:24 停在 LLM call 中段），
   300-r3 仅 14s、719-r1 仅 6s 即被杀——均不可能产出 298 节点完整 run。
5. 同批 stdout 亦为过期/中断内容（719-r1.stdout 实为 300-r1 尾部，719-r2.stdout 是 719-r2 启动 6s 即被杀的中断日志）。

## 数据现状（隔离后）
- 真 run 共 10 个（50x3 + 100x3 + 150x3 + 300-r1），sha256 全唯一，全 rc=0。
- 300/719 档按 D 15:50 停扫决策（tasks/think-trigger/decomposition.md L192，
  commit 1a6d25752「停扫+换仪器 LLM judge 覆盖判定」）正式停止，不补跑。
- 换仪器 = q9_llm_judge_coverage.py（judge pid 2887，16:11 起，glob q9-*-2026*.json）。
  注：judge 16:11-16:21 窗口内可能已读到伪文件（其 stdout 16:21 仍在写），
  其输出 llm-judge-coverage-*.json 若含 300-r2/r3、719-r1 条目 = 重复计数，
  由 Lead/监督者在验收 judge 产出时按本注核对（10 真 run 清单见上）。

## 教训（供复盘）
- wrapper 的「rc 非 0 也 cp 固定输出文件」= fail-open 伪数据源；kill 场景下必然产出过期副本。
  修向：cp 前核 rc==0 且核 json 内 n_nodes 与本次 budget 相符（或 SM 直接写目标文件）。
- kill 后必须 pgrep 确认 worker 真死（协议 00:40 硬规则），且 kill 后应立刻核 OUT 目录有无新增伪文件。
