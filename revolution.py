import sys
import time

# アニメーションの各フレーム
frames = ['-', '\\', '|', '/']

# 無限ループでアニメーションを表示
try:
    while True:
        for frame in frames:
            sys.stdout.write('\r' + frame)
            sys.stdout.flush()
            time.sleep(0.1)  # 表示を0.1秒ごとに更新
except KeyboardInterrupt:
    pass  # Ctrl+Cでループを停止