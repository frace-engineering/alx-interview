#!/usr/bin/python3
""" Function that uses BFS traversal on a list of lists. """


def canUnlockAll(boxes):
    """
        Determines if all boxes can be unlocked by checking for valid keys.

        Args:
            boxes (list of list): A list of lists representing the boxes
            and their keys.

        Returns:
              bool: True if all boxes can be opened, False otherwise.
        """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    result = [0]

    """ Perform BFS traversal to visit reachable boxes """
    while result:
        current_box = result.pop()
        for key in boxes[current_box]:
            if 0 < key < n and not visited[key]:
                visited[key] = True
                result.append(key)
    """  Check if all boxes have been visited """
    return all(visited)
