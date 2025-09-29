from typing import TYPE_CHECKING
from ...Enums import *
from ...LogicHelpers import *


if TYPE_CHECKING:
    from worlds.oot_soh import SohWorld


class EventLocations(str, Enum):
    ZORAS_RIVER_SHRUB = "Zora's River Shrub"
    MAGIC_BEAN_SALESMAN_SHOP = "Magic Bean Salesman Shop"


def set_region_rules(world: "SohWorld") -> None:
    player = world.player
    
    # TODO: Temporary to test generation
    connect_regions(Regions.KOKIRI_FOREST.value, world, [
        [Regions.ZR_FRONT.value, lambda state: True]
    ])
    connect_regions(Regions.ZR_FRONT.value, world, [
        [Regions.KOKIRI_FOREST.value, lambda state: True]
    ])

    ## ZR Front
    # Locations
    add_locations(Regions.ZR_FRONT.value, world, [
        [Locations.ZR_GS_TREE.value, lambda state: is_child(state, world) and
                                                      can_kill_enemy(state, world, Enemies.GOLD_SKULLTULA)],
        [Locations.ZR_NEAR_TREE_GRASS1.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_NEAR_TREE_GRASS2.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_NEAR_TREE_GRASS3.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_NEAR_TREE_GRASS4.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_NEAR_TREE_GRASS5.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_NEAR_TREE_GRASS6.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_NEAR_TREE_GRASS7.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_NEAR_TREE_GRASS8.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_NEAR_TREE_GRASS9.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_NEAR_TREE_GRASS10.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_NEAR_TREE_GRASS11.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_NEAR_TREE_GRASS12.value, lambda state: can_cut_shrubs(state, world)]

    ])
    # Connections
    connect_regions(Regions.ZR_FRONT.value, world, [
        [Regions.ZORA_RIVER.value, lambda state: is_adult(state, world) or blast_or_smash(state, world)],
        [Regions.HYRULE_FIELD.value, lambda state: True]
    ])

    ## Zora River
    # Events
    add_events(Regions.ZORA_RIVER.value, world, [
        [EventLocations.MAGIC_BEAN_SALESMAN_SHOP.value, Events.CAN_BUY_BEANS.value, 
            lambda state: has_item(Items.CHILD_WALLET.value, state, world) and (world.options.shuffle_merchants == 0 or world.options.shuffle_merchants == 2)], # Bean shop not randomized
        [EventLocations.ZORAS_RIVER_SHRUB.value, Events.BUG_ACCESS.value, lambda state: can_cut_shrubs(state, world)]
    ])
    # Locations
    add_locations(Regions.ZORA_RIVER.value, world, [
        [Locations.ZR_MAGIC_BEAN_SALESMAN.value, lambda state: is_child(state, world)],
        [Locations.ZR_FROGS_OCARINA_GAME.value, lambda state: (is_child(state, world) and
                                                               can_use(Items.SONG_OF_STORMS.value, state, world) and
                                                               can_use(Items.SONG_OF_TIME.value, state, world) and
                                                               can_use(Items.ZELDAS_LULLABY.value, state, world) and
                                                               can_use(Items.SUNS_SONG.value, state, world) and
                                                               can_use(Items.EPONAS_SONG.value, state, world) and
                                                               can_use(Items.SARIAS_SONG.value, state, world))],
        [Locations.ZR_FROGS_IN_THE_RAIN.value, lambda state: is_child(state, world) and
                                                             can_use(Items.SONG_OF_STORMS.value, state, world)],
        [Locations.ZR_FROGS_ZELDAS_LULLABY.value, lambda state: is_child(state, world) and
                                                             can_use(Items.ZELDAS_LULLABY.value, state, world)],
        [Locations.ZR_FROGS_EPONAS_SONG.value, lambda state: is_child(state, world) and
                                                             can_use(Items.EPONAS_SONG.value, state, world)],
        [Locations.ZR_FROGS_SARIAS_SONG.value, lambda state: is_child(state, world) and
                                                             can_use(Items.SARIAS_SONG.value, state, world)],
        [Locations.ZR_FROGS_SUNS_SONG.value, lambda state: is_child(state, world) and
                                                           can_use(Items.SUNS_SONG.value, state, world)],
        [Locations.ZR_FROGS_SONG_OF_TIME.value, lambda state: is_child(state, world) and
                                                              can_use(Items.SONG_OF_TIME.value, state, world)],
        [Locations.ZR_NEAR_OPEN_GROTTO_FREESTANDING_POH.value, lambda state: is_child(state, world) or
                                                                              can_use(Items.HOVER_BOOTS.value, state, world)
                                                                              or (is_adult(state, world)
                                                                                  and can_do_trick("ZR Lower Piece of Heart without Hover Boots", state, world))],
        [Locations.ZR_NEAR_DOMAIN_FREESTANDING_POH.value, lambda state: is_child(state, world) or
                                                                              can_use(Items.HOVER_BOOTS.value, state, world)
                                                                              or (is_adult(state, world)
                                                                                  and can_do_trick("ZR Upper Piece of Heart without Hover Boots", state, world))],
        [Locations.ZR_GS_LADDER.value, lambda state: is_child(state, world)
                                                     and  can_attack(state, world)
                                                     and can_get_nighttime_gs(state, world)],
        [Locations.ZR_GS_NEAR_RAISED_GROTTOS.value, lambda state: is_adult(state, world) and
                                                                  (can_use(Items.PROGRESSIVE_HOOKSHOT.value, state, world)
                                                                   or can_use(Items.BOOMERANG.value, state, world)) and
                                                                  can_get_nighttime_gs(state, world)],
        [Locations.ZR_GS_ABOVE_BRIDGE.value, lambda state: is_adult(state, world) and
                                                           can_use(Items.PROGRESSIVE_HOOKSHOT.value, state, world) and
                                                           can_get_nighttime_gs(state, world)],
        [Locations.ZR_BEAN_SPROUT_FAIRY1.value, lambda state: is_child(state, world)
                                                              and can_use(Items.MAGIC_BEAN.value, state, world)
                                                              and can_use(Items.SONG_OF_STORMS.value, state, world)],
        [Locations.ZR_BEAN_SPROUT_FAIRY2.value, lambda state: is_child(state, world)
                                                              and can_use(Items.MAGIC_BEAN.value, state, world)
                                                              and can_use(Items.SONG_OF_STORMS.value, state, world)],
        [Locations.ZR_BEAN_SPROUT_FAIRY3.value, lambda state: is_child(state, world)
                                                              and can_use(Items.MAGIC_BEAN.value, state, world)
                                                              and can_use(Items.SONG_OF_STORMS.value, state, world)],
        [Locations.ZR_NEAR_GROTTOS_GOSSIP_STONE_FAIRY.value, lambda state: call_gossip_fairy(state, world)],
        [Locations.ZR_NEAR_GROTTOS_GOSSIP_STONE_BIG_FAIRY.value, lambda state: can_use(Items.SONG_OF_STORMS.value, state, world)],
        [Locations.ZR_NEAR_DOMAIN_GOSSIP_STONE_FAIRY.value, lambda state: call_gossip_fairy(state, world)],
        [Locations.ZR_NEAR_DOMAIN_GOSSIP_STONE_BIG_FAIRY.value, lambda state: can_use(Items.SONG_OF_STORMS.value, state, world)],
        [Locations.ZR_BENEATH_DOMAIN_RED_LEFT_RUPEE.value, lambda state: is_adult(state, world) and
                                                                         (state.has(Items.BRONZE_SCALE.value) or
                                                                          can_use(Items.IRON_BOOTS.value, state, world) or
                                                                          can_use(Items.BOOMERANG.value, state, world))],
        [Locations.ZR_BENEATH_DOMAIN_RED_MIDDLE_LEFT_RUPEE.value, lambda state: is_adult(state, world) and
                                                                         (state.has(Items.BRONZE_SCALE.value) or
                                                                          can_use(Items.IRON_BOOTS.value, state, world) or
                                                                          can_use(Items.BOOMERANG.value, state, world))],
        [Locations.ZR_BENEATH_DOMAIN_RED_MIDDLE_RIGHT_RUPEE.value, lambda state: is_adult(state, world) and
                                                                         (state.has(Items.BRONZE_SCALE.value) or
                                                                          can_use(Items.IRON_BOOTS.value, state, world) or
                                                                          can_use(Items.BOOMERANG.value, state, world))],
        [Locations.ZR_BENEATH_DOMAIN_RED_RIGHT_RUPEE.value, lambda state: is_adult(state, world) and
                                                                         (state.has(Items.BRONZE_SCALE.value) or
                                                                          can_use(Items.IRON_BOOTS.value, state, world) or
                                                                          can_use(Items.BOOMERANG.value, state, world))],
        [Locations.ZR_NEAR_FREESTANDING_PO_HGRASS.value, lambda state: can_cut_shrubs(state, world)]
    ])
    # Connections
    connect_regions(Regions.ZORA_RIVER.value, world, [
        [Regions.ZR_FRONT.value, lambda state: True],
        [Regions.ZR_OPEN_GROTTO.value, lambda state: True],
        [Regions.ZR_FAIRY_GROTTO.value, lambda state: blast_or_smash(state, world)], #I am not sure that there's any scenario where blast or smash wouldn't apply to here, not sure why this needs here (which checks if the other age opened it, basically)?
        [Regions.LOST_WOODS.value, lambda state: state.has(Items.SILVER_SCALE.value) or  can_use(Items.IRON_BOOTS, state, world)],
        [Regions.ZR_STORMS_GROTTO.value, lambda state: can_open_storms_grotto(state, world)],
        [Regions.ZR_BEHIND_WATERFALL.value, lambda state: world.options.sleeping_waterfall.value==1 or
                                                          can_use(Items.ZELDAS_LULLABY.value, state, world) or
                                                          (is_child(state, world) and
                                                           can_do_trick("ZD with Cuckoo", state, world)) or
                                                          (is_adult(state, world) and
                                                           can_use(Items.HOVER_BOOTS.value, state, world) and
                                                           can_do_trick("ZD with Hover Boots", state, world))]

    ])
    # Events

    ## ZR From Shortcut
    # Connections
    connect_regions(Regions.ZR_FROM_SHORTCUT.value, world, [
        [Regions.ZORA_RIVER.value, lambda state: can_live(state, world) or
                                                 state.has(Items.BOTTLE_WITH_FAIRY.value) or
                                                 state.has(Items.BRONZE_SCALE.value)],
        [Regions.LOST_WOODS.value, lambda state: state.has(Items.SILVER_SCALE.value) or
                                                 can_use(Items.IRON_BOOTS.value, state, world)]

    ])

    ## ZR Behind Waterfall
    # Connections
    connect_regions(Regions.ZR_BEHIND_WATERFALL.value, world, [
        [Regions.ZORA_RIVER.value, lambda state: True],
        [Regions.ZORAS_DOMAIN.value, lambda state: True]
    ])

    ## ZR Open Grotto
    # Locations
    add_locations(Regions.ZR_OPEN_GROTTO.value, world, [
        [Locations.ZR_OPEN_GROTTO_CHEST.value, lambda state: True],
        [Locations.ZR_OPEN_GROTTO_FISH.value, lambda state: has_bottle(state, world)],
        [Locations.ZR_OPEN_GROTTO_GOSSIP_STONE_FAIRY.value, lambda state: call_gossip_fairy(state, world)],
        [Locations.ZR_OPEN_GROTTO_GOSSIP_STONE_BIG_FAIRY.value, lambda state: can_use(Items.SONG_OF_STORMS.value, state, world)],
        [Locations.ZR_OPEN_GROTTO_BEEHIVE_LEFT.value, lambda state: can_break_lower_hives(state, world)],
        [Locations.ZR_OPEN_GROTTO_BEEHIVE_RIGHT.value, lambda state: can_break_lower_hives(state, world)],
        [Locations.ZR_OPEN_GROTTO_GRASS1.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_OPEN_GROTTO_GRASS2.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_OPEN_GROTTO_GRASS3.value, lambda state: can_cut_shrubs(state, world)],
        [Locations.ZR_OPEN_GROTTO_GRASS4.value, lambda state: can_cut_shrubs(state, world)]
    ])
    # Connections
    connect_regions(Regions.ZR_OPEN_GROTTO.value, world, [
        [Regions.ZORA_RIVER.value, lambda state: True]
    ])

    ## ZR Fairy Grotto
    # Locations
    add_locations(Regions.ZR_FAIRY_GROTTO.value, world, [
        [Locations.ZR_FAIRY_GROTTO_FAIRY1.value, lambda state: True],
        [Locations.ZR_FAIRY_GROTTO_FAIRY2.value, lambda state: True],
        [Locations.ZR_FAIRY_GROTTO_FAIRY3.value, lambda state: True],
        [Locations.ZR_FAIRY_GROTTO_FAIRY4.value, lambda state: True],
        [Locations.ZR_FAIRY_GROTTO_FAIRY5.value, lambda state: True],
        [Locations.ZR_FAIRY_GROTTO_FAIRY6.value, lambda state: True],
        [Locations.ZR_FAIRY_GROTTO_FAIRY7.value, lambda state: True],
        [Locations.ZR_FAIRY_GROTTO_FAIRY8.value, lambda state: True]
    ])
    # Connections
    connect_regions(Regions.ZR_FAIRY_GROTTO.value, world, [
        [Regions.ZORA_RIVER.value, lambda state: True]
    ])

    ## ZR Storms Grotto
    # Locations
    add_locations(Regions.ZR_STORMS_GROTTO.value, world, [
        [Locations.ZR_DEKU_SCRUB_GROTTO_FRONT.value, lambda state: can_stun_deku(state, world)],
        [Locations.ZR_DEKU_SCRUB_GROTTO_REAR.value, lambda state: can_stun_deku(state, world)],
        [Locations.ZR_STORMS_GROTTO_BEEHIVE.value, lambda state: can_break_upper_hives(state, world)]

    ])
    # Connections
    connect_regions(Regions.ZR_STORMS_GROTTO.value, world, [
        [Regions.ZORA_RIVER.value, lambda state: True]
    ])
