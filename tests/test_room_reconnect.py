import pytest

from net import room_reconnect as mod

CASES = [
    ('token_binds', ['r1', 2, 'r1', 2], True, False),
    ('token_binds', ['r1', 2, 'r1', 3], False, False),
    ('seat_reserved', [100, 110, 30], True, False),
    ('seat_reserved', [100, 140, 30], False, False),
    ('snapshot_key', ['room-a', 7], 'room-a:7', False),
    ('dedupe_commands', [[1, 2, 3, 5], 2], [3, 5], False),
    ('dedupe_commands', [[], 0], [], False),
    ('merge_state', ['old', 'new', 1, 3], 'new', False),
    ('merge_state', ['old', 'new', 4, 3], 'old', False),
    ('authoritative_time', [1000.0, 12.5], 1012.5, True),
    ('restore_control', ['ai', 'p1'], 'p1', False),
    ('restore_control', ['p2', 'p1'], 'p2', False),
    ('idempotent_join', [['p1'], 'p1'], ['p1'], False),
    ('destroy_allowed', [100, 80, 30], False, False),
    ('migrate_state', [{'seat': 1}, 12], {'seat': 1, 'cooldown': 12}, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_room_reconnect_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
