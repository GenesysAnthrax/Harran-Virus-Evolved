<?xml version="1.0" encoding="utf-8"?>
<ZombieStats modName="${MOD_NAME}" modVersion="${MOD_VERSION}">
  <Runner
    speedMultiplier="${ZOMBIE_RUNNER_MOVE_SPEED_MULTIPLIER}"
    sprintStaminaSeconds="${ZOMBIE_RUNNER_SPRINT_STAMINA_SECONDS}"
    reactionTimeSeconds="${ZOMBIE_RUNNER_REACTION_TIME_SECONDS}"
    nightBonusMultiplier="${ZOMBIE_RUNNER_NIGHT_BONUS_MULTIPLIER}"
    leapRangeMeters="${ZOMBIE_RUNNER_LEAP_RANGE_METERS}"
    healthMultiplier="${ZOMBIE_RUNNER_HEALTH_MULTIPLIER}" />

  <Biter
    speedMultiplier="${ZOMBIE_BITER_MOVE_SPEED_MULTIPLIER}"
    reactionTimeSeconds="${ZOMBIE_BITER_REACTION_TIME_SECONDS}"
    climbEnabled="${ZOMBIE_BITER_CLIMB_ENABLED}"
    healthMultiplier="${ZOMBIE_BITER_HEALTH_MULTIPLIER}" />

  <Volatile
    speedMultiplier="${ZOMBIE_VOLATILE_MOVE_SPEED_MULTIPLIER}"
    aggressionMultiplier="${ZOMBIE_VOLATILE_AGGRESSION_MULTIPLIER}"
    armorMultiplier="${ZOMBIE_VOLATILE_ARMOR_MULTIPLIER}" />
</ZombieStats>
