# T53-B12 阶段 04：执行与核验

- 上游：03 动作分解
- 产物：题面文件、判据 v3、3 个 blocked run 记录、报告 §6、verifier

## 1. 通道探测（真实执行，A3）

| 目标 | 命令 | 结果 |
|---|---|---|
| 生成端 | `curl -m6 http://127.0.0.1:8787/v1/models` | `curl: (7) Couldn't connect`，code=000 |
| 生成端（同 harness 路径） | `python3 urllib.request.urlopen(...)` | `URLError [Errno 111] Connection refused` |
| judge 端 | `curl -m6 http://localhost:1234/v1/models` | `curl: (7) Couldn't connect`，code=000 |
| 端口扫描 | `/dev/tcp` × 8080/8000/11434/8787 | 全 closed |
| API key | `env | grep -i -E "api|key|base_url"` | 空 |
| python 依赖 | `import openai` | `ModuleNotFoundError` |
| bash 出网 | `curl https://html.duckduckgo.com/...` | `SSL_ERROR_SYSCALL`（白名单仅 github） |

**判定：A3 = 不通 → 走 A8–A10 分支。** 任务书降级条款适用；已在报告 §6.2 与回执 `degraded` 字段登记，不是静默跳过。

## 2. 已执行动作

| # | 动作 | 产物 |
|---|---|---|
| A1 | 3 道新题（多跳统计 / 双实体比较 / 深挖口径）+ gold 要点 | `experiments/stage-ablation/questions/T53-B12-new3-questions.md` |
| A2 | 判据 v3：三层可比性 + 12 系统 L1 分表 + 五题映射 | `modules/E-sota-benchmark/research/sm-bench-sota-criteria.md` |
| A8 | 3 个 blocked run 记录（`question_sha1`，分数 null） | `runs-s5-sm-{q6-nev,q7-rd,q8-nvda}.json` |
| A9 | 报告新增 §6（五题表 + 阻塞证据 + 复跑命令 + 3 条顺带发现） | `s5-sm-bench-report.md` |
| A10 | verifier | `loop-artifacts/stages/04/verify-t53-b12.py` |

## 3. 未执行动作（不可执行，非跳过）

A4（注册 qid）、A5（S5 跑 3 reps）、A6（B-face n=3）、A7（L0 框架对照）——全部依赖 LLM 端点。

## 4. A6 防泄漏检查（本阶段新增产物）

- 3 个新 run 文件：无 `question` 字段，只有 `question_sha1` + `question_ref`；`leak_check.question_text_absent=true`。
- 判据文件与报告：不含题面原文（只有题型描述与 qid）。
- **既有违规上报**：`runs-s5-sm-{gpu,drb-2,nat}.json` 的 `question` 字段含完整题面 → 报告 §6.4-1 已登记，等待 D 裁定是否回溯清理。

## 5. verifier 结果

见 `loop-artifacts/stages/04/T53-B12-04-execution.log`（首跑若 FAIL，按 FAIL 回上游修订后二跑；记录方式同 T53-D35）。
