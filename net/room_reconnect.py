"""房间重连：令牌、席位与快照的核心实现。"""


def token_binds(token_room, token_epoch, room, epoch):
    """令牌必须同时绑定房间与局次。"""
    return token_room == room and token_epoch == epoch

def seat_reserved(disconnect_at, now, window):
    """断线后席位在窗口内保留。"""
    return now - disconnect_at < window

def snapshot_key(room, epoch):
    """快照按房间与局次持久化。"""
    return f"{room}:{epoch}"

def dedupe_commands(sequences, last_sequence):
    """补发指令只接受大于已处理序号的。"""
    return [seq for seq in sequences if seq > last_sequence]

def merge_state(old_state, new_state, old_seq, new_seq):
    """按序号合并状态，旧广播不覆盖新状态。"""
    return new_state if new_seq > old_seq else old_state

def authoritative_time(base, elapsed):
    """多副本使用统一权威时钟。"""
    return base + elapsed

def restore_control(owner, player):
    """重连后从 AI 接管回玩家控制。"""
    return player if owner == "ai" else owner

def idempotent_join(existing, player_id):
    """同一玩家并发重连只占一个席位。"""
    if player_id in existing:
        return list(existing)
    return list(existing) + [player_id]

def destroy_allowed(now, last_disconnect, grace):
    """最后一个玩家断线后等满窗口才销毁。"""
    return now - last_disconnect >= grace

def migrate_state(state, cooldown):
    """跨服迁移携带状态与冷却。"""
    migrated = dict(state)
    migrated["cooldown"] = cooldown
    return migrated
