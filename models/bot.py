"""
Provides functionality related to automated players which can play the game without user
interaction according to various strategies.
"""

import random

from enum import Enum, auto

from models.deck import Card, Color, Wild, DrawFourWild, can_play_card
from models.game_state import GameError


class Strategy(Enum):
    """
    The strategy the bot will use.
    """

    RANDOM = auto()


def play_card(strategy: Strategy, hand: list[Card], top: Card) -> Card | None:
    """
    Chooses a card from the hand provided according to the bot's strategy, returning it.
    It returns None if it can't find any playable cards. Also randomly selects color for wilds.
    """

    valid_cards = []
    for i, card in enumerate(hand):
        if can_play_card(top, card):
            valid_cards.append(i)

    if len(valid_cards) == 0:
        return None

    if strategy == Strategy.RANDOM:
        index = random.randint(0, len(valid_cards) - 1)
    else:
        raise GameError("Invalid bot strategy chosen")

    card = hand[index]

    if isinstance(card, (Wild, DrawFourWild)):
        colors = [Color.RED, Color.YELLOW, Color.BLUE, Color.GREEN]
        random.shuffle(colors)
        card.color = colors[0]

    return card
