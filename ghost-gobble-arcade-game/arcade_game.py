def eat_ghost(power_pellet_active, touching_ghost):
    """
    Determine if the ghost gets eaten.

    :param power_pellet_active: bool - whether a power pellet is active.
    :param touching_ghost: bool - whether the player is touching a ghost.
    :return: bool - True if the ghost gets eaten, False otherwise.
    """
    return power_pellet_active and touching_ghost

def score(touching_power_pellet, touching_dot):
    """
    Determine if the player scores.

    :param touching_power_pellet: bool - whether the player is touching a power pellet.
    :param touching_dot: bool - whether the player is touching a dot.
    :return: bool - True if the player scores, False otherwise.
    """
    return touching_power_pellet or touching_dot

def lose(power_pellet_active, touching_ghost):
    """
    Determine if the player loses.

    :param power_pellet_active: bool - whether a power pellet is active.
    :param touching_ghost: bool - whether the player is touching a ghost.
    :return: bool - True if the player loses, False otherwise.
    """
    return not power_pellet_active and touching_ghost

def win(all_dots_eaten, power_pellet_active, touching_ghost):
    """
    Determine if the player wins.

    :param all_dots_eaten: bool - whether all dots have been eaten.
    :param power_pellet_active: bool - whether a power pellet is active.
    :param touching_ghost: bool - whether the player is touching a ghost.
    :return: bool - True if the player wins, False otherwise.
    """
    return all_dots_eaten and (not touching_ghost or (touching_ghost and power_pellet_active))