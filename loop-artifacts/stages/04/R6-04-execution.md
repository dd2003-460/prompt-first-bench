# R6 · 阶段 04 执行与验证：检测器落地 + 真跑

> 规则包：`00-common-review.md` + `04-execution-verification.md` + `04.5-final-review.md`（2,314 o200k，阶段门控）

## 执行步骤（每条挂锚点）

| # | 动作 | 命令 | 结果 | 锚点 |
|---|---|---|---|---|
| S1 | 落盘检测器 | `write_file bench/self-opt-tester/runs/r6/check-route-coverage.py` | 157 行 | 文件存在 + git hash |
| S2 | 首跑（对 v1.0 路由表） | `python3 check-route-coverage.py --index /tmp/index-v1.0.md` | **FAIL，7 条 X-miss** | 输出贴在本文件 §首跑 |
| S3 | 修正路由表 | INDEX.md v1.0 → v1.1（补 `examples/` 第三列） | 6 行表格 + 变更说明 | git diff |
| S4 | 复跑（对 v1.1） | `python3 check-route-coverage.py` | **PASS，exit 0** | `--json` 回执 `x_miss=[]` |
| S5 | 负样本回归 | 再跑 v1.0 | exit **1**（非恒真） | 两次 exit code 对照 |

## 首跑输出（v1.0，剪贴）

```
index: /tmp/index-v1.0.md  stages=6  routed_files=7/7  examples=0
X-miss (rule refs not in route): 7
  - 00-common-review.md:30 -> examples/00-common-review-examples.md  missing in ['01','02','02.5','03','04','04.5']
  - 01-goal-decomposition.md:60 -> examples/01-examples.md  missing in ['01']
  - 02-information-research.md:65 -> examples/02-examples.md  missing in ['02']
  - 02.5-cross-check.md:25 -> examples/02.5-examples.md  missing in ['02.5']
  - 03-action-decomposition.md:22 -> examples/03-examples.md  missing in ['03']
  - 04-execution-verification.md:33 -> examples/04-examples.md  missing in ['04']
  - 04.5-final-review.md:24 -> examples/04.5-examples.md  missing in ['04.5']
RESULT: FAIL (exit 1)
```

## 复跑输出（v1.1，剪贴）

```
index: loop/prompt-first/INDEX.md  stages=6  routed_files=7/7  examples=7
R-miss (stage bundle < 2 files): 0
X-miss (rule refs not in route): 0
dangling (ref target absent):    0
A-miss (no artifact for stage):  2
G-miss (artifact w/o verdict):   0
RESULT: PASS (exit 0)
```

（`A-miss: 2` = 本文件落盘前 04/04.5 目录尚空；本文件 + 04.5 落盘后归零，见阶段 04.5 的复跑。）

## 关键发现（会改结论的）

**v1.0 的「规则负载下降 74%」里，有一部分是把 7 个示例文件悄悄切掉了。**
7 个 `examples/*.md` 共 **4,211 o200k**，且被 6 个规则文件明文点名（「操作示例见 `examples/xx.md`」）。
只报 7 个核心文件、不报示例，等于把 agent 实际会读的东西排除在分母外——这是**测量口径作弊**，不是优化。

修正后（v1.1，示例列为 tier-3 按需）：单 turn 规则负载均值 **3,709 o200k**（含 INDEX），
对基线 12,086 的降幅 = **−69.3%**，与任务书目标「~3,700 / −69%」几乎重合。

## 验证缺口（如实标注）

- 示例文件是否**真的**被读，本轮只能靠「规则文件点名了」推断，无服务端日志佐证 → conf 0.5。
- 若 Lead 判定示例属「指到才读、默认不读」，则应取 v1.0 口径（3,012 tok，−74%），
  此时 X-miss 仍为 7 —— **口径与风险必须成对报告，不能只取低的那个数**。

## 阶段判定

- S1–S5 五步全部有 exit code / 文件存在性锚点；检测器双向验证（FAIL/PASS 各一次）。
- **verdict: pass** → 进入阶段 04.5。
