"""Functions to prevent a nuclear meltdown."""

from enum import Enum
from typing import Union


class ReactorEfficiencyStatus(Enum):
    GREEN = 'GREEN'
    ORANGE = 'ORANGE'
    RED = 'RED'
    BLACK = 'BLACK'


class ReactorStatus(Enum):
    LOW = 'LOW'
    NORMAL = 'NORMAL'
    DANGER = 'DANGER'


def is_criticality_balanced(temperature: Union[int, float],
                            neutrons_emitted: Union[int, float]) -> bool:
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    return temperature < 800 and neutrons_emitted > 500 and (
        temperature * neutrons_emitted) < 500_000


def reactor_efficiency(voltage: Union[int, float], current: Union[int, float],
                       theoretical_max_power: Union[int, float]) -> str:
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    generated_power = voltage * current
    percentage_value = (generated_power / theoretical_max_power) * 100

    # Structural Pattern Matching can only be used since Python 3.10.
    # Reference: https://peps.python.org/pep-0636/
    # match percentage_value:
    #     case percentage if percentage >= 80:
    #         return ReactorEfficiencyStatus.GREEN.value
    #     case percentage if percentage >= 60:
    #         return ReactorEfficiencyStatus.ORANGE.value
    #     case percentage if percentage >= 30:
    #         return ReactorEfficiencyStatus.RED.value
    #     case _:
    #         return ReactorEfficiencyStatus.BLACK.value

    if percentage_value >= 80:
        return ReactorEfficiencyStatus.GREEN.value.lower()
    if percentage_value >= 60:
        return ReactorEfficiencyStatus.ORANGE.value.lower()
    if percentage_value >= 30:
        return ReactorEfficiencyStatus.RED.value.lower()

    return ReactorEfficiencyStatus.BLACK.value.lower()


def fail_safe(temperature: Union[int, float],
              neutrons_produced_per_second: Union[int, float],
              threshold: Union[int, float]) -> str:
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    # Structural Pattern Matching can only be used since Python 3.10.
    # Reference: https://peps.python.org/pep-0636/
    # match temperature * neutrons_produced_per_second:
    #     case product if product < threshold * 0.9:
    #         return ReactorStatus.LOW.value
    #     case product if product < threshold * 0.1 or product > threshold * 0.1:
    #         return ReactorStatus.NORMAL.value
    #     case _:
    #         return ReactorStatus.DANGER.value

    temperature_times_neutrons = temperature * neutrons_produced_per_second

    if temperature_times_neutrons < threshold * 0.9:
        return ReactorStatus.LOW.value

    if threshold * 0.9 <= temperature_times_neutrons <= threshold * 1.1:
        return ReactorStatus.NORMAL.value

    return ReactorStatus.DANGER.value
