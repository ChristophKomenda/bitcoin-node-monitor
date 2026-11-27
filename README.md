# Bitcoin Node Monitor — Bitcoin Core Monitoring for Home Assistant

**Local-first · Restricted RPC · MQTT discovery**

Experimental Home Assistant OS app for monitoring an existing Bitcoin Core node.
No bundled blockchain, wallet, mining, Docker socket or node lifecycle management.

[![CI](https://github.com/ChristophKomenda/bitcoin-node-monitor/actions/workflows/validate.yml/badge.svg)](https://github.com/ChristophKomenda/bitcoin-node-monitor/actions/workflows/validate.yml)

[![Add repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FChristophKomenda%2Fbitcoin-node-monitor)

## At a glance

| Feature | Status |
| --- | --- |
| 19 MQTT discovery entities | Implemented; unit tests |
| Bitcoin Core RPC method allowlist | Implemented in client; server restriction required |
| ARM64 / AMD64 | Build targets; CI verification pending |
| HAOS / real Bitcoin Core / MQTT runtime | Experimental; validation pending |
| Free space on remote node | Not available through the supported RPC calls |

## Getting started

1. Read the [configuration and security guide](bitcoin-node-monitor/DOCS.md).
2. Add this repository to HAOS and install the experimental app.
3. Configure dedicated, server-restricted RPC credentials and an MQTT broker.
4. Start the app and verify its logs, MQTT availability and Home Assistant entities.

Do not expose Bitcoin RPC to the internet or change a working node's RPC binding just to use this app. Keep the existing host-side [Bitcoin Pi Node](https://github.com/ChristophKomenda/bitcoin-pi-node) publisher if it already meets your needs. Use separate entity IDs to avoid mixing publishers.

## Monitoring

Block/header height, verification progress, peer counts, blockchain data size, prune height, chain, Core version, uptime, network totals, initial block download, pruning, synchronization, no peers and observed initial-sync stall duration/status.

## Development

`python3 -m unittest discover -s tests -v`

Build tests are not runtime tests. No image publishing is configured. Also available through the experimental [Home Assistant Community Apps](https://github.com/ChristophKomenda/home-assistant-apps) catalog. Live RPC and HAOS runtime validation remain pending.

MIT licensed. Independent community project; not affiliated with Bitcoin Core or Home Assistant.

<!-- github-seo:begin -->

## Frequently asked questions — quick answers

### Can Home Assistant monitor an existing Bitcoin Core node?

This experimental app queries an existing node over restricted RPC and publishes data through MQTT discovery. See the validation status and security requirements before installation.

### Does this app run its own Bitcoin node?

No. It does not bundle Bitcoin Core or a blockchain. Use an existing node and dedicated, restricted RPC credentials; never expose Bitcoin RPC to the public internet.

<!-- github-seo:end -->
