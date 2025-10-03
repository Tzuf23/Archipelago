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
    connect_regions(Regions.KOKIRI_FOREST, world, [
        (Regions.ZR_FRONT, lambda bundle: True)
    ])
    connect_regions(Regions.ZR_FRONT, world, [
        (Regions.KOKIRI_FOREST, lambda bundle: True)
    ])

    ## ZR Front
    # Locations
    add_locations(Regions.ZR_FRONT, world, [
        (Locations.ZR_GS_TREE, lambda bundle: is_child(bundle) and
                                                      can_kill_enemy(bundle, Enemies.GOLD_SKULLTULA)),
        (Locations.ZR_NEAR_TREE_GRASS1, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS2, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS3, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS4, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS5, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS6, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS7, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS8, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS9, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS10, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS11, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_NEAR_TREE_GRASS12, lambda bundle: can_cut_shrubs(bundle))

    ])
    # Connections
    connect_regions(Regions.ZR_FRONT, world, [
        (Regions.ZORA_RIVER, lambda bundle: is_adult(bundle) or blast_or_smash(bundle)),
        (Regions.HYRULE_FIELD, lambda bundle: True)
    ])

    ## Zora River
    # Events
    add_events(Regions.ZORA_RIVER, world, [
        (EventLocations.MAGIC_BEAN_SALESMAN_SHOP, Events.CAN_BUY_BEANS, 
            lambda bundle: can_afford(10, bundle) and (world.options.shuffle_merchants.value == 0 or world.options.shuffle_merchants.value == 2)), # Bean shop not randomized
        (EventLocations.ZORAS_RIVER_SHRUB, Events.CAN_ACCESS_BUGS, lambda bundle: can_cut_shrubs(bundle))
    ])
    # Locations
    add_locations(Regions.ZORA_RIVER, world, [
        (Locations.ZR_MAGIC_BEAN_SALESMAN, lambda bundle: is_child(bundle)),
        (Locations.ZR_FROGS_OCARINA_GAME, lambda bundle: (is_child(bundle) and
                                                               can_use(Items.SONG_OF_STORMS, bundle) and
                                                               can_use(Items.SONG_OF_TIME, bundle) and
                                                               can_use(Items.ZELDAS_LULLABY, bundle) and
                                                               can_use(Items.SUNS_SONG, bundle) and
                                                               can_use(Items.EPONAS_SONG, bundle) and
                                                               can_use(Items.SARIAS_SONG, bundle))),
        (Locations.ZR_FROGS_IN_THE_RAIN, lambda bundle: is_child(bundle) and
                                                             can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_FROGS_ZELDAS_LULLABY, lambda bundle: is_child(bundle) and
                                                             can_use(Items.ZELDAS_LULLABY, bundle)),
        (Locations.ZR_FROGS_EPONAS_SONG, lambda bundle: is_child(bundle) and
                                                             can_use(Items.EPONAS_SONG, bundle)),
        (Locations.ZR_FROGS_SARIAS_SONG, lambda bundle: is_child(bundle) and
                                                             can_use(Items.SARIAS_SONG, bundle)),
        (Locations.ZR_FROGS_SUNS_SONG, lambda bundle: is_child(bundle) and
                                                           can_use(Items.SUNS_SONG, bundle)),
        (Locations.ZR_FROGS_SONG_OF_TIME, lambda bundle: is_child(bundle) and
                                                              can_use(Items.SONG_OF_TIME, bundle)),
        (Locations.ZR_NEAR_OPEN_GROTTO_FREESTANDING_POH, lambda bundle: is_child(bundle) or
                                                                              can_use(Items.HOVER_BOOTS, bundle)
                                                                              or (is_adult(bundle)
                                                                                  and can_do_trick("ZR Lower Piece of Heart without Hover Boots", bundle))),
        (Locations.ZR_NEAR_DOMAIN_FREESTANDING_POH, lambda bundle: is_child(bundle) or
                                                                              can_use(Items.HOVER_BOOTS, bundle)
                                                                              or (is_adult(bundle)
                                                                                  and can_do_trick("ZR Upper Piece of Heart without Hover Boots", bundle))),
        (Locations.ZR_GS_LADDER, lambda bundle: is_child(bundle)
                                                     and  can_attack(bundle)
                                                     and can_get_nighttime_gs(bundle)),
        (Locations.ZR_GS_NEAR_RAISED_GROTTOS, lambda bundle: is_adult(bundle) and
                                                                  (can_use(Items.HOOKSHOT, bundle)
                                                                   or can_use(Items.BOOMERANG, bundle)) and
                                                                  can_get_nighttime_gs(bundle)),
        (Locations.ZR_GS_ABOVE_BRIDGE, lambda bundle: is_adult(bundle) and
                                                           can_use(Items.HOOKSHOT, bundle) and
                                                           can_get_nighttime_gs(bundle)),
        (Locations.ZR_BEAN_SPROUT_FAIRY1, lambda bundle: is_child(bundle)
                                                              and can_use(Items.MAGIC_BEAN, bundle)
                                                              and can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_BEAN_SPROUT_FAIRY2, lambda bundle: is_child(bundle)
                                                              and can_use(Items.MAGIC_BEAN, bundle)
                                                              and can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_BEAN_SPROUT_FAIRY3, lambda bundle: is_child(bundle)
                                                              and can_use(Items.MAGIC_BEAN, bundle)
                                                              and can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_NEAR_GROTTOS_GOSSIP_STONE_FAIRY, lambda bundle: call_gossip_fairy(bundle)),
        (Locations.ZR_NEAR_GROTTOS_GOSSIP_STONE_BIG_FAIRY, lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_NEAR_DOMAIN_GOSSIP_STONE_FAIRY, lambda bundle: call_gossip_fairy(bundle)),
        (Locations.ZR_NEAR_DOMAIN_GOSSIP_STONE_BIG_FAIRY, lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_BENEATH_DOMAIN_RED_LEFT_RUPEE, lambda bundle: is_adult(bundle) and
                                                                         (has_item(Items.BRONZE_SCALE, bundle) or
                                                                          can_use(Items.IRON_BOOTS, bundle) or
                                                                          can_use(Items.BOOMERANG, bundle))),
        (Locations.ZR_BENEATH_DOMAIN_RED_MIDDLE_LEFT_RUPEE, lambda bundle: is_adult(bundle) and
                                                                         (has_item(Items.BRONZE_SCALE, bundle) or
                                                                          can_use(Items.IRON_BOOTS, bundle) or
                                                                          can_use(Items.BOOMERANG, bundle))),
        (Locations.ZR_BENEATH_DOMAIN_RED_MIDDLE_RIGHT_RUPEE, lambda bundle: is_adult(bundle) and
                                                                         (has_item(Items.BRONZE_SCALE, bundle) or
                                                                          can_use(Items.IRON_BOOTS, bundle) or
                                                                          can_use(Items.BOOMERANG, bundle))),
        (Locations.ZR_BENEATH_DOMAIN_RED_RIGHT_RUPEE, lambda bundle: is_adult(bundle) and
                                                                         (has_item(Items.BRONZE_SCALE, bundle) or
                                                                          can_use(Items.IRON_BOOTS, bundle) or
                                                                          can_use(Items.BOOMERANG, bundle))),
        (Locations.ZR_NEAR_FREESTANDING_POH_GRASS, lambda bundle: can_cut_shrubs(bundle))
    ])
    # Connections
    connect_regions(Regions.ZORA_RIVER, world, [
        (Regions.ZR_FRONT, lambda bundle: True),
        (Regions.ZR_OPEN_GROTTO, lambda bundle: True),
        (Regions.ZR_FAIRY_GROTTO, lambda bundle: blast_or_smash(bundle)), #I am not sure that there's any scenario where blast or smash wouldn't apply to here, not sure why this needs here (which checks if the other age opened it, basically)?
        (Regions.LOST_WOODS, lambda bundle: has_item(Items.SILVER_SCALE, bundle) or  can_use(Items.IRON_BOOTS, bundle)),
        (Regions.ZR_STORMS_GROTTO, lambda bundle: can_open_storms_grotto(bundle)),
        (Regions.ZR_BEHIND_WATERFALL, lambda bundle: world.options.sleeping_waterfall.value == 1 or
                                                          can_use(Items.ZELDAS_LULLABY, bundle) or
                                                          (is_child(bundle) and
                                                           can_do_trick("ZD with Cuckoo", bundle)) or
                                                          (is_adult(bundle) and
                                                           can_use(Items.HOVER_BOOTS, bundle) and
                                                           can_do_trick("ZD with Hover Boots", bundle)))

    ])
    # Events

    ## ZR From Shortcut
    # Connections
    connect_regions(Regions.ZR_FROM_SHORTCUT, world, [
        (Regions.ZORA_RIVER, lambda bundle: can_live(bundle) or
                                                 has_item(Items.BOTTLE_WITH_FAIRY, bundle) or
                                                 has_item(Items.BRONZE_SCALE, bundle)),
        (Regions.LOST_WOODS, lambda bundle: has_item(Items.SILVER_SCALE, bundle) or
                                                 can_use(Items.IRON_BOOTS, bundle))

    ])

    ## ZR Behind Waterfall
    # Connections
    connect_regions(Regions.ZR_BEHIND_WATERFALL, world, [
        (Regions.ZORA_RIVER, lambda bundle: True),
        (Regions.ZORAS_DOMAIN, lambda bundle: True)
    ])

    ## ZR Open Grotto
    # Locations
    add_locations(Regions.ZR_OPEN_GROTTO, world, [
        (Locations.ZR_OPEN_GROTTO_CHEST, lambda bundle: True),
        (Locations.ZR_OPEN_GROTTO_FISH, lambda bundle: has_bottle(bundle)),
        (Locations.ZR_OPEN_GROTTO_GOSSIP_STONE_FAIRY, lambda bundle: call_gossip_fairy(bundle)),
        (Locations.ZR_OPEN_GROTTO_GOSSIP_STONE_BIG_FAIRY, lambda bundle: can_use(Items.SONG_OF_STORMS, bundle)),
        (Locations.ZR_OPEN_GROTTO_BEEHIVE_LEFT, lambda bundle: can_break_lower_hives(bundle)),
        (Locations.ZR_OPEN_GROTTO_BEEHIVE_RIGHT, lambda bundle: can_break_lower_hives(bundle)),
        (Locations.ZR_OPEN_GROTTO_GRASS1, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_OPEN_GROTTO_GRASS2, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_OPEN_GROTTO_GRASS3, lambda bundle: can_cut_shrubs(bundle)),
        (Locations.ZR_OPEN_GROTTO_GRASS4, lambda bundle: can_cut_shrubs(bundle))
    ])
    # Connections
    connect_regions(Regions.ZR_OPEN_GROTTO, world, [
        (Regions.ZORA_RIVER, lambda bundle: True)
    ])

    ## ZR Fairy Grotto
    # Locations
    add_locations(Regions.ZR_FAIRY_GROTTO, world, [
        (Locations.ZR_FAIRY_GROTTO_FAIRY1, lambda bundle: True),
        (Locations.ZR_FAIRY_GROTTO_FAIRY2, lambda bundle: True),
        (Locations.ZR_FAIRY_GROTTO_FAIRY3, lambda bundle: True),
        (Locations.ZR_FAIRY_GROTTO_FAIRY4, lambda bundle: True),
        (Locations.ZR_FAIRY_GROTTO_FAIRY5, lambda bundle: True),
        (Locations.ZR_FAIRY_GROTTO_FAIRY6, lambda bundle: True),
        (Locations.ZR_FAIRY_GROTTO_FAIRY7, lambda bundle: True),
        (Locations.ZR_FAIRY_GROTTO_FAIRY8, lambda bundle: True)
    ])
    # Connections
    connect_regions(Regions.ZR_FAIRY_GROTTO, world, [
        (Regions.ZORA_RIVER, lambda bundle: True)
    ])

    ## ZR Storms Grotto
    # Locations
    add_locations(Regions.ZR_STORMS_GROTTO, world, [
        (Locations.ZR_DEKU_SCRUB_GROTTO_FRONT, lambda bundle: can_stun_deku(bundle)),
        (Locations.ZR_DEKU_SCRUB_GROTTO_REAR, lambda bundle: can_stun_deku(bundle)),
        (Locations.ZR_STORMS_GROTTO_BEEHIVE, lambda bundle: can_break_upper_beehives(bundle))

    ])
    # Connections
    connect_regions(Regions.ZR_STORMS_GROTTO, world, [
        (Regions.ZORA_RIVER, lambda bundle: True)
    ])
