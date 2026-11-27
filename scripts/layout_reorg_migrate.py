#!/usr/bin/env python3
"""LAYOUT-Reorg 迁移脚本 (2026-11-27).

读 tasks/layout-reorg-mapping.json → 按批迁移 experiments/stage-ablation/
旧数据/脚本/文档到 modules/{A,B,D,E,F} 与 archive/。

批次定义 (任务书):
  1 = 数据目录 (checkpoints / runs-* / s10-runs / hetero-q2q5-payload)
  2 = 脚本 (*.py / *.sh)
  3 = 文档与散件 (*.md/*.log/*.txt/*.bak*/.gitignore/*.json 散件 + 其余目录整体搬)

规则:
- 只 git mv (未跟踪的用普通 mv), 绝不 rm
- 排除清单内的文件/目录绝对不动
- src 不存在 → skip + warn, 不 fail
- 目标重名冲突 → fail 该项, 不硬移
- 结果写 tasks/layout-reorg-migrate-result.json (moved/skipped/failed + 清单)
- 输出流只打 1 行状态 (明细全在 result json)

用法:
  python3 scripts/layout_reorg_migrate.py --batch 1 [--dry-run]
"""
import argparse
import json
import os
import subprocess
import sys

BASE = "experiments/stage-ablation"
MAPPING = "tasks/layout-reorg-mapping.json"
RESULT = "tasks/layout-reorg-migrate-result.json"

# ---- 排除清单 (绝对不动) ----
EXCLUDE_FILES = {
    "q9_budget_scan_queue.sh",
    "s5_state_machine.py",
    "ablation_harness.py",
    "research_hook.py",
}
EXCLUDE_DIRS = {
    "gold",        # Q9G-V1 依赖, 不动
    "questions",   # Q9G-V1 依赖, 不动
}
# modules/B-pipeline-ablation/data/q9-budget-scan/ 在 BASE 之外, 天然不动

# ---- 7 个 [待判] 目录的归属判定 (2026-11-27, 按内容+owner 启发式) ----
# gold/questions 已在排除清单; 其余 7 个:
PENDING_DIR_DEST = {
    # lit-survey: T24 文献调研回执 (B 管线调研产物)
    "lit-survey": "modules/B-pipeline-ablation/research/legacy-lit-survey/",
    # loop-artifacts: 1-loop 阶段执行日志 (B 管线实验过程记录)
    "loop-artifacts": "modules/B-pipeline-ablation/research/legacy-loop-artifacts/",
    # research: 撞车调研/先验调研/校准分析 (B 管线研究笔记)
    "research": "modules/B-pipeline-ablation/research/legacy-research/",
    # social: 专家邮件草稿 (B 管线 G4 产出)
    "social": "modules/B-pipeline-ablation/research/legacy-social/",
    # spec: t53b 实验 spec (D 状态机 t53b run 的实验定义)
    "spec": "modules/D-decomp-state-machine/data/legacy-spec/",
    # web-llm: 交叉验证回执 (D 状态机 run 的验证产物)
    "web-llm": "modules/D-decomp-state-machine/data/legacy-web-llm/",
    # logs: 状态机 run 日志 (与散落 .log 同归 archive/logs)
    "logs": "archive/logs/",
}

# ---- 目录整体搬: 显式目标路径 (目录本身 → 该路径) ----
# 大部分目录的 mapping dest 本身就是新路径 (legacy-* 命名);
# 下面 3 个是特殊语义, 显式覆盖:
DIR_MOVE_TARGET = {
    # tasks/ → 根 tasks/stage-ablation/ (mapping 注释: 根 tasks/ 已有同名结构)
    "tasks": "tasks/stage-ablation",
    # 两个 .research-cache* → archive/runtime-cache/ 下 (去点前缀, 防混淆)
    ".research-cache": "archive/runtime-cache/research-cache",
    ".research-cache-backup-20261112-072330":
        "archive/runtime-cache/research-cache-backup-20261112-072330",
}

SCRIPT_EXTS = {".py", ".sh"}
DATA_DIR_PREFIXES = ("runs", "checkpoints")
DATA_DIR_NAMES = {"s10-runs", "hetero-q2q5-payload"}


def clean_dest(raw):
    """mapping dest 可能带中文注释 (xxx（说明)), 取路径部分."""
    return raw.split("（")[0].strip().rstrip("/")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()


def move(src, dest):
    """git mv 优先; 未跟踪文件/目录用普通 mv. 返回 (ok, msg)."""
    rc, _ = run(["git", "ls-files", "--error-unmatch", src])
    if rc == 0:
        rc, out = run(["git", "mv", src, dest])
    else:
        rc, out = run(["mv", src, dest])
    return (rc == 0), out


def classify_item(kind, name, raw_dest):
    """返回批次号 1/2/3."""
    if kind == "dir":
        if name.startswith(DATA_DIR_PREFIXES) or name in DATA_DIR_NAMES:
            return 1
        return 3
    ext = os.path.splitext(name)[1]
    if ext in SCRIPT_EXTS:
        return 2
    return 3  # 散件 (含 .json/.jsonl/.md/.log/.txt/.bak*/.gitignore)


def dir_target(name, raw_dest):
    """目录整体搬的目标完整路径."""
    if name in DIR_MOVE_TARGET:
        return DIR_MOVE_TARGET[name]
    return clean_dest(raw_dest)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", type=int, choices=[1, 2, 3], required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    m = json.load(open(MAPPING))
    files, dirs = m["files"], m["dirs"]

    moved, skipped, failed = [], [], []

    def record(kind, src_rel, dest_full, note, ok, reason=""):
        if ok:
            moved.append({"kind": kind, "src": src_rel, "dest": dest_full,
                          "note": note, "dry_run": args.dry_run})
        elif reason == "missing":
            skipped.append({"kind": kind, "src": src_rel,
                            "reason": "src 不存在"})
        else:
            failed.append({"kind": kind, "src": src_rel, "reason": reason})

    def do_move_file(name, meta):
        src = os.path.join(BASE, name)
        dest_dir = clean_dest(meta["dest"])
        dest_full = os.path.join(dest_dir, name)
        if not os.path.exists(src):
            record("file", name, dest_full, "", False, "missing")
            return
        if os.path.exists(dest_full):
            record("file", name, dest_full, "", False,
                   f"目标已存在: {dest_full}")
            return
        if args.dry_run:
            record("file", name, dest_full, f"owner={meta.get('module','')}", True)
            return
        os.makedirs(dest_dir, exist_ok=True)
        ok, msg = move(src, dest_full)
        record("file", name, dest_full, f"owner={meta.get('module','')}", ok, msg)

    def do_move_dir(name, raw_dest):
        src = os.path.join(BASE, name)
        dest_full = dir_target(name, raw_dest)
        if not os.path.exists(src):
            record("dir", name, dest_full, "", False, "missing")
            return
        if os.path.exists(dest_full):
            record("dir", name, dest_full, "", False,
                   f"目标已存在: {dest_full}")
            return
        if args.dry_run:
            record("dir", name, dest_full, "", True)
            return
        os.makedirs(os.path.dirname(dest_full), exist_ok=True)
        ok, msg = move(src, dest_full)
        record("dir", name, dest_full, "", ok, msg)

    # 文件
    for name, meta in files.items():
        if name in EXCLUDE_FILES:
            continue
        if classify_item("file", name, "") != args.batch:
            continue
        do_move_file(name, meta)

    # 目录 (tasks 目录必须先于 dest 落在 tasks/stage-ablation/ 下的目录)
    ordered = sorted(dirs, key=lambda n: (n != "tasks", n))
    for name in ordered:
        if name in EXCLUDE_DIRS:
            continue
        raw = str(dirs[name].get("dest", ""))
        if "待判" in raw:
            if name in PENDING_DIR_DEST:
                raw = PENDING_DIR_DEST[name]
            else:
                skipped.append({"kind": "dir", "src": name,
                                "reason": "[待判] 且无判定, 跳过"})
                continue
        if classify_item("dir", name, raw) != args.batch:
            continue
        do_move_dir(name, raw)

    # 结果落盘 (合并已有批次结果)
    prev = {}
    if os.path.exists(RESULT):
        prev = json.load(open(RESULT))
    prev[f"batch{args.batch}"] = {
        "moved": len(moved),
        "skipped": len(skipped),
        "failed": len(failed),
        "moved_items": moved,
        "skipped_items": skipped,
        "failed_items": failed,
        "dry_run": args.dry_run,
    }
    if not args.dry_run:
        with open(RESULT, "w") as fh:
            json.dump(prev, fh, ensure_ascii=False, indent=1)

    print(f"BATCH{args.batch} done: moved={len(moved)} skipped={len(skipped)} "
          f"failed={len(failed)}"
          + (" [dry-run]" if args.dry_run else ""))


if __name__ == "__main__":
    main()
