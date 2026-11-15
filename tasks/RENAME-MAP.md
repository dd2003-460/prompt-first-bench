# tasks/ 重命名映射表（2026-11-16 · module/stage/content 规范）

> 回滚用：`git log --follow` 或按本表 `git mv new old`。编号规则：TASK-<模块字母><两位序号>-<内容摘要>，旧编号（T53/T8/R5/S10...）保留在名字里保溯源。

## 00-ops/

| 旧名 | 新名 |
|---|---|
| `goal-queue.md` | `00-ops/goal-queue.md` |
| `current-goal.md` | `00-ops/current-goal.md` |
| `queue-format-contract.md` | `00-ops/queue-format-contract.md` |
| `ralph-loop-runner.md` | `00-ops/ralph-loop-runner.md` |
| `_TEMPLATE-arena-task-brief.md` | `00-ops/template-arena-task-brief.md` |
| `BRIDGE-REPORT.md` | `00-ops/archive/bridge-report-r200.md` |
| `BRIDGE-REPORT.md.bak-blindeval` | `00-ops/archive/bridge-report-r200.bak-blindeval` |
| `PFB-APPLY-midterm-plan.md` | `00-ops/archive/pfb-apply-midterm-plan.md` |
| `PFB-APPLY-subagent-discussion.md` | `00-ops/archive/pfb-apply-subagent-discussion.md` |
| `PFB-APPLY-subagent-opinion.md` | `00-ops/archive/pfb-apply-subagent-opinion.md` |
| `2026-11-07-nine-points.md` | `00-ops/archive/2026-11-07-d-nine-points.md` |
| `T-unattended-framework.md` | `00-ops/archive/unattended-longrun-framework.md` |
| `T53-night-autonomy.md` | `00-ops/archive/t53-night-autonomy.md` |
| `T53-night-autonomy-upgrade.md` | `00-ops/archive/t53-night-autonomy-upgrade.md` |
| `T53-restructure-plan.md` | `00-ops/archive/t53-repo-restructure-plan.md` |

## A-eval-infra/

| 旧名 | 新名 |
|---|---|
| `TASK-cj-rubric-align.md` | `A-eval-infra/TASK-A01-rubric-judge-calibration-align.md` |
| `R5-run5-task-brief.md` | `A-eval-infra/TASK-A02-r5-run5-chain-replay.md` |
| `R5.1-second-scorer-task-brief.md` | `A-eval-infra/TASK-A03-r5-second-scorer.md` |
| `R5-judge-blindtest-task-brief.md` | `A-eval-infra/TASK-A04-judge-blindtest.md` |
| `R5.2audit-C4-arena-export-task-brief.md` | `A-eval-infra/TASK-A05-r5audit-c4-arena-export.md` |
| `RUBRIC-V3-FULL-AUDIT-task-brief.md` | `A-eval-infra/TASK-A06-rubric-v3-full-audit.md` |
| `RV3G1-semantic-rejudge.md` | `A-eval-infra/TASK-A07-rv3g1-semantic-rejudge.md` |
| `G1B-FAMILY-UPGRADE-DUAL-RATER-task-brief.md` | `A-eval-infra/TASK-A08-g1b-family-upgrade-dual-rater.md` |
| `T51-judge-cal-v2.md` | `A-eval-infra/TASK-A09-judge-calibration-v2.md` |
| `T52-E3-dual-track-scoring.md` | `A-eval-infra/TASK-A10-e3-dual-track-scoring.md` |
| `TASK-judge-dual-pilot.md` | `A-eval-infra/TASK-A11-judge-dual-pilot.md` |
| `TASK-judge-dual-pilot-selfcontained.md` | `A-eval-infra/TASK-A12-judge-dual-pilot-selfcontained.md` |
| `TASK-cross-judge-arena-blind.md` | `A-eval-infra/TASK-A13-cross-judge-arena-blind.md` |
| `T8-C3v3-hetero-judge-task-brief.md` | `A-eval-infra/TASK-A14-t8-c3v3-hetero-judge.md` |
| `T8-C3v3-hetero-judge-r270-dispatch.md` | `A-eval-infra/TASK-A15-t8-c3v3-hetero-judge-r270-dispatch.md` |
| `T8-C3v3-rubric-v32-replay-task.md` | `A-eval-infra/TASK-A16-t8-c3v3-rubric-v32-replay.md` |
| `T8-C3-adversarial-check.md` | `A-eval-infra/TASK-A17-t8-c3-adversarial-check.md` |
| `T8-C3-v3-adversarial-check.md` | `A-eval-infra/TASK-A18-t8-c3v3-adversarial-check.md` |
| `T23-stage-ablation-hetero-judge-task.md` | `A-eval-infra/TASK-A19-t23-stage-ablation-hetero-judge.md` |
| `T36-hetero-q2q5-task.md` | `A-eval-infra/TASK-A20-t36-hetero-q2q5.md` |
| `T38-fullloop-hetero-judge-task.md` | `A-eval-infra/TASK-A21-t38-fullloop-hetero-judge.md` |

## B-pipeline-ablation/

| 旧名 | 新名 |
|---|---|
| `S10-combination-arm-ablation.md` | `B-pipeline-ablation/TASK-B01-s10-combination-arm-ablation.md` |
| `s8g-generalization.md` | `B-pipeline-ablation/TASK-B02-s8g-generalization.md` |
| `s9h-hybrid-review-loop.md` | `B-pipeline-ablation/TASK-B03-s9h-hybrid-review-loop.md` |
| `T8-prompt-ablation.md` | `B-pipeline-ablation/TASK-B04-t8-prompt-ablation-matrix.md` |
| `T8-matrix-run-r1.md` | `B-pipeline-ablation/TASK-B05-t8-matrix-run-r1.md` |
| `T27-n-expansion-r4.md` | `B-pipeline-ablation/TASK-B06-t27-n-expansion-r4r6.md` |
| `T52-prompt-decomposition-collision.md` | `B-pipeline-ablation/TASK-B07-t52-prompt-decomp-collision.md` |
| `T53-objective-form-ablation.md` | `B-pipeline-ablation/TASK-B08-t53-objective-form-ablation.md` |
| `T53-drb-three-arm.md` | `B-pipeline-ablation/TASK-B09-t53-drb-three-arm.md` |
| `T53-drb-c-arm-design.md` | `B-pipeline-ablation/TASK-B10-t53-drb-c-arm-design.md` |
| `T53-drb-arena-run.md` | `B-pipeline-ablation/TASK-B11-t53-drb-arena-run.md` |
| `T53-supplement-bench.md` | `B-pipeline-ablation/TASK-B12-t53-deepresearch-bench-spec.md` |
| `T53C-bench-dispatch.md` | `B-pipeline-ablation/TASK-B13-t53c-bench-dispatch.md` |
| `T26-prompt-style-research.md` | `B-pipeline-ablation/TASK-B07-t26-prompt-style-research.md` |
| `T28-criteria-implementation.md` | `B-pipeline-ablation/TASK-B08-t28-criteria-implementation.md` |
| `T29-blank-and-nopua.md` | `B-pipeline-ablation/TASK-B09-t29-blank-nopua-validation.md` |
| `T30-emotion-and-motivation.md` | `B-pipeline-ablation/TASK-B10-t30-emotion-manipulation-research.md` |

## C-objective-goodhart/

| 旧名 | 新名 |
|---|---|
| `T-PR-15-text-objective-goodhart.md` | `C-objective-goodhart/TASK-C01-tp15-text-objective-goodhart.md` |
| `T-PR-16-collision-backlog.md` | `C-objective-goodhart/TASK-C02-tp16-collision-backlog.md` |
| `T52-c1c3-paired-test.md` | `C-objective-goodhart/TASK-C03-t52-c1c3-paired-test.md` |
| `C1C3-decomposition.md` | `C-objective-goodhart/TASK-C04-c1c3-decomposition.md` |
| `T53-taste-sop-decomp.md` | `C-objective-goodhart/TASK-C05-t53-taste-sop-decomp.md` |

## D-decomp-state-machine/

| 旧名 | 新名 |
|---|---|
| `T53-decomp-state-machine.md` | `D-decomp-state-machine/TASK-D01-t53-decomp-state-machine-main.md` |
| `T53-teamer-goal-brief.md` | `D-decomp-state-machine/TASK-D02-t53-teamer-goal-brief.md` |
| `T53-r8-loop-brief.md` | `D-decomp-state-machine/TASK-D03-t53-r8-monitor-loop.md` |
| `T53-icl-mechanism-decomp.md` | `D-decomp-state-machine/TASK-D04-t53-icl-mechanism-decomp.md` |
| `T53-cc-subagent-audit.md` | `D-decomp-state-machine/TASK-D05-t53-cc-subagent-audit.md` |
| `T53-bus` | `D-decomp-state-machine/TASK-D06-t53-file-bus/` |

## E-sota-benchmark/

| 旧名 | 新名 |
|---|---|
| `T53C-sota-research.md` | `E-sota-benchmark/TASK-E01-t53c-dr-sota-research.md` |
| `T39-gold-replication-research.md` | `E-sota-benchmark/TASK-E02-t39-gold-replication-method.md` |
| `T40-gold-replication-arena.md` | `E-sota-benchmark/TASK-E03-t40-gold-replication-arena.md` |
| `T41-gold-replication-generalization.md` | `E-sota-benchmark/TASK-E04-t41-gold-replication-generalize.md` |
| `T42-gold-replication-Q4Q5.md` | `E-sota-benchmark/TASK-E05-t42-gold-replication-q4q5.md` |
| `T43-pricing-enhanced-Q3.md` | `E-sota-benchmark/TASK-E06-t43-pricing-enhanced-q3.md` |
| `T48-dual-gold-construction.md` | `E-sota-benchmark/TASK-E07-t48-dual-gold-construction.md` |
| `T49-new-question-gold-trees.md` | `E-sota-benchmark/TASK-E08-t49-new-question-gold-trees.md` |
| `T50-B1-gold-trees.md` | `E-sota-benchmark/TASK-E09-t50-b1-gold-trees.md` |
| `B1-new-questions.md` | `E-sota-benchmark/TASK-E10-b1-new-questions-selection.md` |
| `T37-related-work-research.md` | `E-sota-benchmark/TASK-E11-t37-related-work-research.md` |
| `T44-related-work-update.md` | `E-sota-benchmark/TASK-E12-t44-related-work-update.md` |
| `T8-lit-research.md` | `E-sota-benchmark/TASK-E13-t8-lit-research-interpretability.md` |
| `T8-partB-lit-survey-task.md` | `E-sota-benchmark/TASK-E14-t8-partb-pipeline-lit-survey.md` |
| `T24-decomp-prerequisite-lit-survey.md` | `E-sota-benchmark/TASK-E15-t24-decomp-prereq-lit-survey.md` |
| `T53-D35-arena-task.md` | `E-sota-benchmark/TASK-E16-t53d35-realworld-vs-analytic-arena.md` |
| `T53-D35-realworld-vs-analytic-decomp.md` | `E-sota-benchmark/TASK-E17-t53d35-realworld-vs-analytic-decomp.md` |
| `T53-longterm-vision-survey.md` | `E-sota-benchmark/TASK-E18-t53-longterm-vision-survey.md` |

## F-theory/

| 旧名 | 新名 |
|---|---|
| `v3-hardening.md` | `F-theory/TASK-F01-v3-hardening.md` |
| `v3-gold-gap.md` | `F-theory/TASK-F02-v3-gold-gap.md` |
| `decomposition-v3-gold-gap.md` | `F-theory/TASK-F03-v3-gold-gap-decomposition.md` |
| `decomposition-pfb-paper-add-t17.md` | `F-theory/TASK-F04-paper-t17-section-decomposition.md` |
| `decomposition-pfb-paper-add-t17-section.md` | `F-theory/TASK-F05-paper-t17-section-stage01.md` |
| `T46-add-t17-section.md` | `F-theory/TASK-F06-t46-paper-t17-section-exec.md` |
| `T6-effect-verify-r1.md` | `F-theory/TASK-F07-t6-effect-verify-r1.md` |
| `T6-sync-verify-r1.md` | `F-theory/TASK-F08-t6-sync-verify-r1.md` |
| `T7.1-meeting-system-r1.md` | `F-theory/TASK-F09-t71-meeting-system-r1.md` |
| `27b-hw-costperf-stage02.md` | `F-theory/TASK-F10-27b-hw-costperf-stage02.md` |
| `TASK-r6-arena-token-optimization.md` | `F-theory/TASK-F11-r6-arena-token-optimization.md` |
| `TASK-r7-rule-compression.md` | `F-theory/TASK-F12-r7-rule-compression.md` |
