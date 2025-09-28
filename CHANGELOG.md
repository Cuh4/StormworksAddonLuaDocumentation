# 📚 | Changelog
Last updated for game version: v1.14.3 (The Firefighter SCBA Update)
Note that even if the above version is outdated on the latest version of this repo, it means no 
functions were added, changed or removed from the game since the update.

Corrections and changes to the documentation may still be made after the game version is outdated
anyway.

The following changelog entries are in DD/MM/YY format.

## 28/09/2025
- Fix invalid return annotation for `server.getCharacterItem` (return type and name were swapped).

## 25/07/2025
- `SWEquipmentTypeEnum` is now the return type instead of `integer` for `server.getCharacterItem`.

## 10/07/2025
- Fix incorrect fact in `server.setPopupScreen` (-1 is top for vertical offset, not bottom).

## 25/05/2025
- Added new `firefighter_scba` equipment type.
- Refactored a few comments.

## 07/05/2025
- Fixed the messed up description for `server.getObjectSimulating`.

## 14/04/2025
- Added more information to `debug.log` description such as how to view the logs.

## 09/04/2025
- Added `SWAITeamEnum` enum.
- Added hidden deprecated functions: `server.getPlaylistIndexByName`, `server.getPlaylistPath` and `server.spawnMissionLocation`
- Fixed typo with `server.spawnVehicleSavefile`
- Added missing function `server.isLocationClear`
- Added new v1.14.2 AI functions: `server.setAICharacterTeam`, `server.setAIVehicleTeam` and `server.setAICharacterTargetTeam`

## 06/04/2025
- Removed unmaintained documentation screenshots in the repo.
- Clarified the above comment about the version being outdated.
- Set param names to lowercase in `server.getSeasonalEvent`, `server.setCharacterItem` and `server.getCharacterItem`
- In `server.setGameSetting`, `GameSettingString` was renamed to `game_setting` to stay consistent. This was done in some other functions too.

The below is thanks to [issue #3](https://github.com/Cuh4/StormworksAddonLuaDocumentation/issues/3).
- Fixed funky param annotations with `server.addMapObject`, `server.setCharacterItem`, `server.notify`, and more.
- Added missing description for `server.spawnAddonComponent` and `server.getPlayers()`.
- Fixed inconsistent comment style for the `server.command` function.
- Removed a typo in `server.spawnObject`.
- Fixed type annotations that reference enums always having the actual type in the comment, eg: `---@param setting SWGameSettingEnum string, this is a description`

## 15/01/2024
- Added `group_id` return value to `server.spawnAddonVehicle` and `server.spawnVehicle` as the new game update v1.13.4 now returns the vehicle group ID with the aforementioned functions.

## 30/10/2024
- Fix `server.getVehicleSign` and `server.getVehicleSeat` having their `name` parameter hinted as a number instead of a string

## 02/09/2024
- Fix `server.spawnVolcano` having an invalid number of arguments too (again, `magnitude` argument doesn't exist)
- Fix `server.spawnTornado` having an invalid number of arguments (`magnitude` argument doesn't exist)

## 28/08/2024
- `SWGameSettingEnum` and `SWGameSettings` are now up-to-date
- Fixed `SWGameSettingEnum` using `---@class` instead of `---@alias`

## 17/08/2024
- Fixed up `server.setAIState` `AI_STATE` parameter description. It didn't cover all AI states
- Made `server.setCreatureTooltip` an alias instead of it having its own function

## 14/08/2024
- Added the new lobsters and crabs to `SWEquipmentTypeEnum`
- Fixed incorrect `SWNotificationTypeEnum` names
- Fixed `SWNotificationTypeEnum` being spelt as `SWNotifiationTypeEnum`

## 03/08/2024
- Changed overall structure for tidying reasons.

## 02/08/2024
- Updated `SWRopeTypeEnum`.
- Added description comments to server, property, debug, etc

## 04/07/2024
- Replaced "--- " with "-- ". Personal preference yet again

## 03/07/2024
- Replaced "-- @" with "---@" as it's my personal preference and it's pretty much the standard
- Added `server.getVehiclesByName()`
- Added `SWVehicleAuthor` class
- Updated vehicle class for v1.11.6 (add "name" and "authors" field)

## 19/06/2024
- Fixed `matrix.rotationToFaceXZ` return type should be `SWMatrix`

## 14/06/2024
- Added missing fluid types to `SWTankFluidTypeEnum`

## 07/06/2024
- Added `---@meta _` see https://luals.github.io/wiki/annotations/#meta

## 12/05/2024
- Switched around `server.setCharacterSeated` and `server.setSeated` (`server.setSeated` is no longer an alias but the actual thing)
- Added `server.setCreatureSeated` as an alias of `server.setSeated`

## 08/05/2024
- Added descriptions for `server.spawnTornado`, `server.spawnMeteor`, `server.spawnMeteorShower`, `server.spawnVolcano`, `server.getVolcanos`, `server.spawnWhirlpool`, `server.spawnTsunami`
- Added `server.getFishData`, `server.getFishHotspots`
- Added `SWFishData` and `SWFishHotSpotData` classes
- Int states for fish equipment types are now shown in the equipment type description

## 06/05/2024
- Rename `SWOreTypeEnum` to `SWResourceTypeEnum`
- Add missing resources to `SWResourceTypeEnum` (`solid_propellant` and `fishes`)

## 05/05/2024
- Fix description for server.getWeather

## 26/04/2024
- General formatting fixes

## 25/04/2024
- Add `---@deprecated` tag to all undocumented hidden alias functions

## 24/04/2024
- Added `creature_type`, `interactable`, and `animal_type` fields to `SWAddonComponentData` (From v1.10.10 update)

## 23/04/2024
- Added `server.setSeated` alias for `server.setCharacterSeated`
- Removed function descriptions for alias functions

## 19/04/2024
- Fixed `SWVehicleComponents` class

## 12/04/2024
- Add `solid_propellant` parameter to `server.setTileInventory()`
- Added missing argument for `server.spawnMeteor()`, `is_spawn_tsunami`

## 28/03/2024
- Added documentation for `server.clearOilSpill()`
- Added documentation for callback `onClearOilSpill()`
- Added `solid_propellant` return annotation for `server.getTileInventory()`

## 02/03/2024
- Fix return annotation for `server.spawnVehicle` (group_id --> primary_vehicle_id)

## 21/02/2024
- Add missing documentation for `server.spawnMeteorShower`

## 15/02/2024
- Documented hidden undocumented functions. They are mainly aliases of existing functions  
    These undocumented functions are untested. I found them in the global `server` table, but I've never used them.  
    This means they might not even be callable, they do nothing, or I may have aliased it to the wrong function
- Removed "BUG REPORT" text, couldn't find hyperlink for it

## 01/02/2024
- Added `drill_rod` and `fishing_lure` to object type enum
- Added new map label types to map label type enum
- Added new equipment types to equipment type enum

## 02/01/2024
- Added missing `object_id` attribute to the `SWPlayer` class.

## 18/12/2023
- Fixed return annotation for `server.spawnAddonVehicle` being "group_id" and not "vehicle_id"
- Added missing `is_success` return annotation for `server.getVehicleGroup`

## 12/12/2023
- Added `server.dlcSpace()`, forgot to add it earlier

## 30/11/2023
- Fixed `server.spawnAddonVehicle` docs
- Fixed `server.spawnVehicle` docs
- Removed `server.getVehicleName`