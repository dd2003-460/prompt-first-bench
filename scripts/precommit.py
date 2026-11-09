#!/usr/bin/env python3
"""precommit.py — pfb 提交前检查（~20 行，只拦硬错误，不拦风格）。

规则:
  1. 本次 diff 改动的 .py 文件必须 py_compile 通过（语法错 = 拒提交）
  2. 其余情况一律放行。引用扫描等"提醒类"检查不进 hook——hook 只做
     "失败即不可用"的最小集，避免检查工具自己成为故障源。
退出码: 0=放行, 1=拒绝。任何内部异常 → 放行 + stderr 警告（hook 坏了不能卡死工作流）。
用法: git pre-commit 直接调; 手动: python3 scripts/precommit.py
"""
import subprocess, sys

def main():
    # status --porcelain 覆盖 staged 的增/改/删；diff --cached 看不到已删除项
    out = subprocess.run(["git", "status", "--porcelain", "-z"],
                         capture_output=True).stdout.split(b"\0")
    import os
    pys = set()
    for item in out:
        if len(item) > 3 and item[3:].decode(errors="replace").endswith(".py"):
            p = item[3:].decode(errors="replace")
            if os.path.exists(p):  # 被删的文件没有可编译内容，跳过
                pys.add(p)
    pys = sorted(pys)
    for f in pys:
        r = subprocess.run([sys.executable, "-m", "py_compile", f], capture_output=True)
        if r.returncode != 0:
            print(f"[precommit] REJECT {f}: syntax error\n{r.stderr.decode()[:500]}")
            return 1
    if pys:
        print(f"[precommit] OK ({len(pys)} .py compiled)")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[precommit] WARN hook failed ({e}); allowing commit", file=sys.stderr)
        sys.exit(0)