"""房间重连：令牌、席位与快照：待实现的核心模块。"""


def token_binds(token_room, token_epoch, room, epoch):
    """令牌必须同时绑定房间与局次。"""
    raise NotImplementedError

def seat_reserved(disconnect_at, now, window):
    """断线后席位在窗口内保留。"""
    raise NotImplementedError

def snapshot_key(room, epoch):
    """快照按房间与局次持久化。"""
    raise NotImplementedError

def dedupe_commands(sequences, last_sequence):
    """补发指令只接受大于已处理序号的。"""
    raise NotImplementedError

def merge_state(old_state, new_state, old_seq, new_seq):
    """按序号合并状态，旧广播不覆盖新状态。"""
    raise NotImplementedError

def authoritative_time(base, elapsed):
    """多副本使用统一权威时钟。"""
    raise NotImplementedError

def restore_control(owner, player):
    """重连后从 AI 接管回玩家控制。"""
    raise NotImplementedError

def idempotent_join(existing, player_id):
    """同一玩家并发重连只占一个席位。"""
    raise NotImplementedError

def destroy_allowed(now, last_disconnect, grace):
    """最后一个玩家断线后等满窗口才销毁。"""
    raise NotImplementedError

def migrate_state(state, cooldown):
    """跨服迁移携带状态与冷却。"""
    raise NotImplementedError
