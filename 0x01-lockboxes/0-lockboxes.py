#!/usr/bin/python3
from collections import deque

"""Define afunction named canUnlockAll that determines
if given boxes can be unlocked
"""


def canUnlockAll(boxes):
    """"canUnlockAll that determines
    if given boxes can be unlocked
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = deque([0])

    """Iterate through the Items in the boxes to check foe correct key"""
    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
