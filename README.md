# 房间重连：令牌、席位与快照

玩家断线重连后房间席位和战斗状态对不上：令牌不绑房间局次、席位立即释放、快照只在内存、补发指令不去重、全量广播覆盖新状态、多副本无权威时钟、AI 接管后不交回、并发重连不幂等、销毁不等窗口、跨服迁移丢状态。

## 目录结构

```
README.md
conftest.py
.gitignore
net/__init__.py
net/room_reconnect.py
tests/test_room_reconnect.py
```

## 当前状态

`net/room_reconnect.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_room_reconnect.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 重连令牌绑定房间与局次
2. 席位保留窗口
3. 战斗快照持久化
4. 补发指令按序号去重
5. 增量状态合并
6. 多副本权威时钟
7. 重连后控制权交回
8. 并发重连幂等
9. 房间销毁等待重连窗口
10. 跨服迁移携带席位与冷却

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `net/room_reconnect.py`
后 15 条用例应全部通过。
