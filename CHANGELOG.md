# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - 2025-02-22
### Added
- testing via unittest
### Changed
- Migrate to use `redis 5`
- Migrate away from deprecated redis functionality
### Removed
- Support for Python <= 3.10
- Redis <= 4
- Quart <= 0.20

## [2.0.0] - 2023-03-21
### Added
- Handle when handler is accessed when not setup
- Add connection attempt functionality, ensuring a redis connection exists before program launch (can be disabled)
### Changed
- Switch to use `redis 4` instead of `aioredis`
- Use newer Python packaging config format
- Update minimum version of Quart
- Use custom internal logger, so it can be customised by users

## [1.0.0] - 2022-01-17
### Added
- Documentation hosted at [readthedocs](https://quart-redis.readthedocs.io/en/latest/)

### Changed
- Now compatible with aioredis 2.x

### Removed
- Support for older versions of aioredis

## [0.1.1] - 2022-01-17
### Fixed
- Restrict aioredis version to v1.3.x until code gets migrated to be compatible for v2

## [0.1.0] - 2021-05-24
### Added
- Initial release

[1.0.0]: https://github.com/enchant97/quart-redis/compare/v0.1.1...v1.0.0
[0.1.1]: https://github.com/enchant97/quart-redis/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/enchant97/quart-redis/releases/tag/v0.1.0
