---
title: SpaceTraders API v2.0.0
language_tabs:
  - python: Python
language_clients:
  - python: ""
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="spacetraders-api">SpaceTraders API v2.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

SpaceTraders is an open-universe game and learning platform that offers a set of HTTP endpoints to control a fleet of ships and explore a multiplayer universe.

The API is documented using [OpenAPI](https://github.com/SpaceTradersAPI/api-docs). You can send your first request right here in your browser to check the status of the game server.

```json http
{
  "method": "GET",
  "url": "https://api.spacetraders.io/v2",
}
```

Unlike a traditional game, SpaceTraders does not have a first-party client or app to play the game. Instead, you can use the API to build your own client, write a script to automate your ships, or try an app built by the community.

We have a [Discord channel](https://discord.com/invite/jh6zurdWk5) where you can share your projects, ask questions, and get help from other players.

Base URLs:

* <a href="https://api.spacetraders.io/v2">https://api.spacetraders.io/v2</a>

Email: <a href="mailto:joel@spacetraders.io">Joel Brubaker</a> 
License: <a href="https://choosealicense.com/no-permission/">No Permission</a>

# Authentication

- HTTP Authentication, scheme: bearer When you register a new agent you will be granted a private bearer token which grants authorization to use the API.

<h1 id="spacetraders-api-default">Default</h1>

## get-status

<a id="opIdget-status"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.spacetraders.io/v2/', headers = headers)

print(r.json())

```

`GET /`

*Get Status*

Return the status of the game server.
This also includes a few global elements, such as announcements, server reset dates and leaderboards.

> Example responses

> 200 Response

```json
{
  "status": "string",
  "version": "string",
  "resetDate": "string",
  "description": "string",
  "stats": {
    "agents": 0,
    "ships": 0,
    "systems": 0,
    "waypoints": 0
  },
  "leaderboards": {
    "mostCredits": [
      {
        "agentSymbol": "string",
        "credits": 0
      }
    ],
    "mostSubmittedCharts": [
      {
        "agentSymbol": "string",
        "chartCount": 0
      }
    ]
  },
  "serverResets": {
    "next": "string",
    "frequency": "string"
  },
  "announcements": [
    {
      "title": "string",
      "body": "string"
    }
  ],
  "links": [
    {
      "name": "string",
      "url": "string"
    }
  ]
}
```

<h3 id="get-status-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Fetched status successfully.|Inline|

<h3 id="get-status-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» status|string|true|none|The current status of the game server.|
|» version|string|true|none|The current version of the API.|
|» resetDate|string|true|none|The date when the game server was last reset.|
|» description|string|true|none|none|
|» stats|object|true|none|none|
|»» agents|integer|true|none|Number of registered agents in the game.|
|»» ships|integer|true|none|Total number of ships in the game.|
|»» systems|integer|true|none|Total number of systems in the game.|
|»» waypoints|integer|true|none|Total number of waypoints in the game.|
|» leaderboards|object|true|none|none|
|»» mostCredits|[object]|true|none|Top agents with the most credits.|
|»»» agentSymbol|string|true|none|Symbol of the agent.|
|»»» credits|integer(int64)|true|none|Amount of credits.|
|»» mostSubmittedCharts|[object]|true|none|Top agents with the most charted submitted.|
|»»» agentSymbol|string|true|none|Symbol of the agent.|
|»»» chartCount|integer|true|none|Amount of charts done by the agent.|
|» serverResets|object|true|none|none|
|»» next|string|true|none|The date and time when the game server will reset.|
|»» frequency|string|true|none|How often we intend to reset the game server.|
|» announcements|[object]|true|none|none|
|»» title|string|true|none|none|
|»» body|string|true|none|none|
|» links|[object]|true|none|none|
|»» name|string|true|none|none|
|»» url|string|true|none|none|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, AgentToken
</aside>

## register

<a id="opIdregister"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('https://api.spacetraders.io/v2/register', headers = headers)

print(r.json())

```

`POST /register`

*Register New Agent*

Creates a new agent and ties it to an account. 
The agent symbol must consist of a 3-14 character string, and will be used to represent your agent. This symbol will prefix the symbol of every ship you own. Agent symbols will be cast to all uppercase characters.

This new agent will be tied to a starting faction of your choice, which determines your starting location, and will be granted an authorization token, a contract with their starting faction, a command ship that can fly across space with advanced capabilities, a small probe ship that can be used for reconnaissance, and 150,000 credits.

> #### Keep your token safe and secure
>
> Save your token during the alpha phase. There is no way to regenerate this token without starting a new agent. In the future you will be able to generate and manage your tokens from the SpaceTraders website.

If you are new to SpaceTraders, It is recommended to register with the COSMIC faction, a faction that is well connected to the rest of the universe. After registering, you should try our interactive [quickstart guide](https://docs.spacetraders.io/quickstart/new-game) which will walk you through basic API requests in just a few minutes.

> Body parameter

```json
{
  "faction": "COSMIC",
  "symbol": "BADGER",
  "email": "string"
}
```

<h3 id="register-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» faction|body|[FactionSymbol](#schemafactionsymbol)|true|The symbol of the faction.|
|» symbol|body|string|true|Your desired agent symbol. This will be a unique name used to represent your agent, and will be the prefix for your ships.|
|» email|body|string|false|Your email address. This is used if you reserved your call sign between resets.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» faction|COSMIC|
|» faction|VOID|
|» faction|GALACTIC|
|» faction|QUANTUM|
|» faction|DOMINION|
|» faction|ASTRO|
|» faction|CORSAIRS|
|» faction|OBSIDIAN|
|» faction|AEGIS|
|» faction|UNITED|
|» faction|SOLITARY|
|» faction|COBALT|
|» faction|OMEGA|
|» faction|ECHO|
|» faction|LORDS|
|» faction|CULT|
|» faction|ANCIENTS|
|» faction|SHADOW|
|» faction|ETHEREAL|

> Example responses

> 201 Response

```json
{
  "data": {
    "agent": {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    },
    "contract": {
      "id": "string",
      "factionSymbol": "string",
      "type": "PROCUREMENT",
      "terms": {
        "deadline": "2019-08-24T14:15:22Z",
        "payment": {
          "onAccepted": 0,
          "onFulfilled": 0
        },
        "deliver": [
          {
            "tradeSymbol": "string",
            "destinationSymbol": "string",
            "unitsRequired": 0,
            "unitsFulfilled": 0
          }
        ]
      },
      "accepted": false,
      "fulfilled": false,
      "expiration": "2019-08-24T14:15:22Z",
      "deadlineToAccept": "2019-08-24T14:15:22Z"
    },
    "faction": {
      "symbol": "COSMIC",
      "name": "string",
      "description": "string",
      "headquarters": "string",
      "traits": [
        {
          "symbol": "BUREAUCRATIC",
          "name": "string",
          "description": "string"
        }
      ],
      "isRecruiting": true
    },
    "ship": {
      "symbol": "string",
      "registration": {
        "name": "string",
        "factionSymbol": "string",
        "role": "FABRICATOR"
      },
      "nav": {
        "systemSymbol": "string",
        "waypointSymbol": "string",
        "route": {
          "destination": {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0
          },
          "origin": {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0
          },
          "departureTime": "2019-08-24T14:15:22Z",
          "arrival": "2019-08-24T14:15:22Z"
        },
        "status": "IN_TRANSIT",
        "flightMode": "DRIFT"
      },
      "crew": {
        "current": 0,
        "required": 0,
        "capacity": 0,
        "rotation": "STRICT",
        "morale": 100,
        "wages": 0
      },
      "frame": {
        "symbol": "FRAME_PROBE",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "moduleSlots": 0,
        "mountingPoints": 0,
        "fuelCapacity": 0,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "reactor": {
        "symbol": "REACTOR_SOLAR_I",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "powerOutput": 1,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "engine": {
        "symbol": "ENGINE_IMPULSE_DRIVE_I",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "speed": 1,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "cooldown": {
        "shipSymbol": "string",
        "totalSeconds": 0,
        "remainingSeconds": 0,
        "expiration": "2019-08-24T14:15:22Z"
      },
      "modules": [
        {
          "symbol": "MODULE_MINERAL_PROCESSOR_I",
          "capacity": 0,
          "range": 0,
          "name": "string",
          "description": "string",
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        }
      ],
      "mounts": [
        {
          "symbol": "MOUNT_GAS_SIPHON_I",
          "name": "string",
          "description": "string",
          "strength": 0,
          "deposits": [
            "QUARTZ_SAND"
          ],
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        }
      ],
      "cargo": {
        "capacity": 0,
        "units": 0,
        "inventory": [
          {
            "symbol": "PRECIOUS_STONES",
            "name": "string",
            "description": "string",
            "units": 1
          }
        ]
      },
      "fuel": {
        "current": 0,
        "capacity": 0,
        "consumed": {
          "amount": 0,
          "timestamp": "2019-08-24T14:15:22Z"
        }
      }
    },
    "token": "string"
  }
}
```

<h3 id="register-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Succesfully registered.|Inline|

<h3 id="register-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» agent|[Agent](#schemaagent)|true|none|Agent details.|
|»»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»»» symbol|string|true|none|Symbol of the agent.|
|»»» headquarters|string|true|none|The headquarters of the agent.|
|»»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»»» startingFaction|string|true|none|The faction the agent started with.|
|»»» shipCount|integer|true|none|How many ships are owned by the agent.|
|»» contract|[Contract](#schemacontract)|true|none|Contract details.|
|»»» id|string|true|none|ID of the contract.|
|»»» factionSymbol|string|true|none|The symbol of the faction that this contract is for.|
|»»» type|string|true|none|Type of contract.|
|»»» terms|[ContractTerms](#schemacontractterms)|true|none|The terms to fulfill the contract.|
|»»»» deadline|string(date-time)|true|none|The deadline for the contract.|
|»»»» payment|[ContractPayment](#schemacontractpayment)|true|none|Payments for the contract.|
|»»»»» onAccepted|integer|true|none|The amount of credits received up front for accepting the contract.|
|»»»»» onFulfilled|integer|true|none|The amount of credits received when the contract is fulfilled.|
|»»»» deliver|[[ContractDeliverGood](#schemacontractdelivergood)]|false|none|The cargo that needs to be delivered to fulfill the contract.|
|»»»»» tradeSymbol|string|true|none|The symbol of the trade good to deliver.|
|»»»»» destinationSymbol|string|true|none|The destination where goods need to be delivered.|
|»»»»» unitsRequired|integer|true|none|The number of units that need to be delivered on this contract.|
|»»»»» unitsFulfilled|integer|true|none|The number of units fulfilled on this contract.|
|»»» accepted|boolean|true|none|Whether the contract has been accepted by the agent|
|»»» fulfilled|boolean|true|none|Whether the contract has been fulfilled|
|»»» expiration|string(date-time)|true|none|Deprecated in favor of deadlineToAccept|
|»»» deadlineToAccept|string(date-time)|false|none|The time at which the contract is no longer available to be accepted|
|»» faction|[Faction](#schemafaction)|true|none|Faction details.|
|»»» symbol|[FactionSymbol](#schemafactionsymbol)|true|none|The symbol of the faction.|
|»»» name|string|true|none|Name of the faction.|
|»»» description|string|true|none|Description of the faction.|
|»»» headquarters|string|true|none|The waypoint in which the faction's HQ is located in.|
|»»» traits|[[FactionTrait](#schemafactiontrait)]|true|none|List of traits that define this faction.|
|»»»» symbol|[FactionTraitSymbol](#schemafactiontraitsymbol)|true|none|The unique identifier of the trait.|
|»»»» name|string|true|none|The name of the trait.|
|»»»» description|string|true|none|A description of the trait.|
|»»» isRecruiting|boolean|true|none|Whether or not the faction is currently recruiting new agents.|
|»» ship|[Ship](#schemaship)|true|none|Ship details.|
|»»» symbol|string|true|none|The globally unique identifier of the ship in the following format: `[AGENT_SYMBOL]-[HEX_ID]`|
|»»» registration|[ShipRegistration](#schemashipregistration)|true|none|The public registration information of the ship|
|»»»» name|string|true|none|The agent's registered name of the ship|
|»»»» factionSymbol|string|true|none|The symbol of the faction the ship is registered with|
|»»»» role|[ShipRole](#schemashiprole)|true|none|The registered role of the ship|
|»»» nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»»»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»»»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|
|»»» crew|[ShipCrew](#schemashipcrew)|true|none|The ship's crew service and maintain the ship's systems and equipment.|
|»»»» current|integer|true|none|The current number of crew members on the ship.|
|»»»» required|integer|true|none|The minimum number of crew members required to maintain the ship.|
|»»»» capacity|integer|true|none|The maximum number of crew members the ship can support.|
|»»»» rotation|string|true|none|The rotation of crew shifts. A stricter shift improves the ship's performance. A more relaxed shift improves the crew's morale.|
|»»»» morale|integer|true|none|A rough measure of the crew's morale. A higher morale means the crew is happier and more productive. A lower morale means the ship is more prone to accidents.|
|»»»» wages|integer|true|none|The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint.|
|»»» frame|[ShipFrame](#schemashipframe)|true|none|The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.|
|»»»» symbol|string|true|none|Symbol of the frame.|
|»»»» name|string|true|none|Name of the frame.|
|»»»» description|string|true|none|Description of the frame.|
|»»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»»» moduleSlots|integer|true|none|The amount of slots that can be dedicated to modules installed in the ship. Each installed module take up a number of slots, and once there are no more slots, no new modules can be installed.|
|»»»» mountingPoints|integer|true|none|The amount of slots that can be dedicated to mounts installed in the ship. Each installed mount takes up a number of points, and once there are no more points remaining, no new mounts can be installed.|
|»»»» fuelCapacity|integer|true|none|The maximum amount of fuel that can be stored in this ship. When refueling, the ship will be refueled to this amount.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»»»» power|integer|false|none|The amount of power required from the reactor.|
|»»»»» crew|integer|false|none|The number of crew required for operation.|
|»»»»» slots|integer|false|none|The number of module slots required for installation.|
|»»» reactor|[ShipReactor](#schemashipreactor)|true|none|The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.|
|»»»» symbol|string|true|none|Symbol of the reactor.|
|»»»» name|string|true|none|Name of the reactor.|
|»»»» description|string|true|none|Description of the reactor.|
|»»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»»» powerOutput|integer|true|none|The amount of power provided by this reactor. The more power a reactor provides to the ship, the lower the cooldown it gets when using a module or mount that taxes the ship's power.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» engine|[ShipEngine](#schemashipengine)|true|none|The engine determines how quickly a ship travels between waypoints.|
|»»»» symbol|string|true|none|The symbol of the engine.|
|»»»» name|string|true|none|The name of the engine.|
|»»»» description|string|true|none|The description of the engine.|
|»»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»»» speed|integer|true|none|The speed stat of this engine. The higher the speed, the faster a ship can travel from one point to another. Reduces the time of arrival when navigating the ship.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»»» modules|[[ShipModule](#schemashipmodule)]|true|none|Modules installed in this ship.|
|»»»» symbol|string|true|none|The symbol of the module.|
|»»»» capacity|integer|false|none|Modules that provide capacity, such as cargo hold or crew quarters will show this value to denote how much of a bonus the module grants.|
|»»»» range|integer|false|none|Modules that have a range will such as a sensor array show this value to denote how far can the module reach with its capabilities.|
|»»»» name|string|true|none|Name of this module.|
|»»»» description|string|true|none|Description of this module.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» mounts|[[ShipMount](#schemashipmount)]|true|none|Mounts installed in this ship.|
|»»»» symbol|string|true|none|Symbo of this mount.|
|»»»» name|string|true|none|Name of this mount.|
|»»»» description|string|false|none|Description of this mount.|
|»»»» strength|integer|false|none|Mounts that have this value, such as mining lasers, denote how powerful this mount's capabilities are.|
|»»»» deposits|[string]|false|none|Mounts that have this value denote what goods can be produced from using the mount.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»»» name|string|true|none|The name of the cargo item type.|
|»»»»» description|string|true|none|The description of the cargo item type.|
|»»»»» units|integer|true|none|The number of units of the cargo item.|
|»»» fuel|[ShipFuel](#schemashipfuel)|true|none|Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.|
|»»»» current|integer|true|none|The current amount of fuel in the ship's tanks.|
|»»»» capacity|integer|true|none|The maximum amount of fuel the ship's tanks can hold.|
|»»»» consumed|object|false|none|An object that only shows up when an action has consumed fuel in the process. Shows the fuel consumption data.|
|»»»»» amount|integer|true|none|The amount of fuel consumed by the most recent transit or action.|
|»»»»» timestamp|string(date-time)|true|none|The time at which the fuel was consumed.|
|»» token|string|true|none|A Bearer token for accessing secured API endpoints.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PROCUREMENT|
|type|TRANSPORT|
|type|SHUTTLE|
|symbol|COSMIC|
|symbol|VOID|
|symbol|GALACTIC|
|symbol|QUANTUM|
|symbol|DOMINION|
|symbol|ASTRO|
|symbol|CORSAIRS|
|symbol|OBSIDIAN|
|symbol|AEGIS|
|symbol|UNITED|
|symbol|SOLITARY|
|symbol|COBALT|
|symbol|OMEGA|
|symbol|ECHO|
|symbol|LORDS|
|symbol|CULT|
|symbol|ANCIENTS|
|symbol|SHADOW|
|symbol|ETHEREAL|
|symbol|BUREAUCRATIC|
|symbol|SECRETIVE|
|symbol|CAPITALISTIC|
|symbol|INDUSTRIOUS|
|symbol|PEACEFUL|
|symbol|DISTRUSTFUL|
|symbol|WELCOMING|
|symbol|SMUGGLERS|
|symbol|SCAVENGERS|
|symbol|REBELLIOUS|
|symbol|EXILES|
|symbol|PIRATES|
|symbol|RAIDERS|
|symbol|CLAN|
|symbol|GUILD|
|symbol|DOMINION|
|symbol|FRINGE|
|symbol|FORSAKEN|
|symbol|ISOLATED|
|symbol|LOCALIZED|
|symbol|ESTABLISHED|
|symbol|NOTABLE|
|symbol|DOMINANT|
|symbol|INESCAPABLE|
|symbol|INNOVATIVE|
|symbol|BOLD|
|symbol|VISIONARY|
|symbol|CURIOUS|
|symbol|DARING|
|symbol|EXPLORATORY|
|symbol|RESOURCEFUL|
|symbol|FLEXIBLE|
|symbol|COOPERATIVE|
|symbol|UNITED|
|symbol|STRATEGIC|
|symbol|INTELLIGENT|
|symbol|RESEARCH_FOCUSED|
|symbol|COLLABORATIVE|
|symbol|PROGRESSIVE|
|symbol|MILITARISTIC|
|symbol|TECHNOLOGICALLY_ADVANCED|
|symbol|AGGRESSIVE|
|symbol|IMPERIALISTIC|
|symbol|TREASURE_HUNTERS|
|symbol|DEXTEROUS|
|symbol|UNPREDICTABLE|
|symbol|BRUTAL|
|symbol|FLEETING|
|symbol|ADAPTABLE|
|symbol|SELF_SUFFICIENT|
|symbol|DEFENSIVE|
|symbol|PROUD|
|symbol|DIVERSE|
|symbol|INDEPENDENT|
|symbol|SELF_INTERESTED|
|symbol|FRAGMENTED|
|symbol|COMMERCIAL|
|symbol|FREE_MARKETS|
|symbol|ENTREPRENEURIAL|
|role|FABRICATOR|
|role|HARVESTER|
|role|HAULER|
|role|INTERCEPTOR|
|role|EXCAVATOR|
|role|TRANSPORT|
|role|REPAIR|
|role|SURVEYOR|
|role|COMMAND|
|role|CARRIER|
|role|PATROL|
|role|SATELLITE|
|role|EXPLORER|
|role|REFINERY|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|
|rotation|STRICT|
|rotation|RELAXED|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="spacetraders-api-agents">Agents</h1>

Agents

## get-my-agent

<a id="opIdget-my-agent"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('https://api.spacetraders.io/v2/my/agent', headers = headers)

print(r.json())

```

`GET /my/agent`

*Get Agent*

Fetch your agent's details.

> Example responses

> 200 Response

```json
{
  "data": {
    "accountId": "string",
    "symbol": "string",
    "headquarters": "string",
    "credits": 0,
    "startingFaction": "string",
    "shipCount": 0
  }
}
```

<h3 id="get-my-agent-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched agent details.|Inline|

<h3 id="get-my-agent-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[Agent](#schemaagent)|true|none|Agent details.|
|»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»» symbol|string|true|none|Symbol of the agent.|
|»» headquarters|string|true|none|The headquarters of the agent.|
|»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»» startingFaction|string|true|none|The faction the agent started with.|
|»» shipCount|integer|true|none|How many ships are owned by the agent.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## get-agents

<a id="opIdget-agents"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.spacetraders.io/v2/agents', headers = headers)

print(r.json())

```

`GET /agents`

*List Agents*

Fetch agents details.

<h3 id="get-agents-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|What entry offset to request|
|limit|query|integer|false|How many entries to return per page|

> Example responses

> 200 Response

```json
{
  "data": [
    {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    }
  ],
  "meta": {
    "total": 0,
    "page": 1,
    "limit": 10
  }
}
```

<h3 id="get-agents-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched agents details.|Inline|

<h3 id="get-agents-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[[Agent](#schemaagent)]|true|none|[Agent details.]|
|»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»» symbol|string|true|none|Symbol of the agent.|
|»» headquarters|string|true|none|The headquarters of the agent.|
|»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»» startingFaction|string|true|none|The faction the agent started with.|
|»» shipCount|integer|true|none|How many ships are owned by the agent.|
|» meta|[Meta](#schemameta)|true|none|Meta details for pagination.|
|»» total|integer|true|none|Shows the total amount of items of this kind that exist.|
|»» page|integer|true|none|A page denotes an amount of items, offset from the first item. Each page holds an amount of items equal to the `limit`.|
|»» limit|integer|true|none|The amount of items in each page. Limits how many items can be fetched at once.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, AgentToken
</aside>

## get-agent

<a id="opIdget-agent"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.spacetraders.io/v2/agents/{agentSymbol}', headers = headers)

print(r.json())

```

`GET /agents/{agentSymbol}`

*Get Public Agent*

Fetch agent details.

<h3 id="get-agent-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|agentSymbol|path|string|true|The agent symbol|

> Example responses

> 200 Response

```json
{
  "data": {
    "accountId": "string",
    "symbol": "string",
    "headquarters": "string",
    "credits": 0,
    "startingFaction": "string",
    "shipCount": 0
  }
}
```

<h3 id="get-agent-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched agent details.|Inline|

<h3 id="get-agent-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[Agent](#schemaagent)|true|none|Agent details.|
|»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»» symbol|string|true|none|Symbol of the agent.|
|»» headquarters|string|true|none|The headquarters of the agent.|
|»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»» startingFaction|string|true|none|The faction the agent started with.|
|»» shipCount|integer|true|none|How many ships are owned by the agent.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, AgentToken
</aside>

<h1 id="spacetraders-api-contracts">Contracts</h1>

Contracts

## get-contracts

<a id="opIdget-contracts"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('https://api.spacetraders.io/v2/my/contracts', headers = headers)

print(r.json())

```

`GET /my/contracts`

*List Contracts*

Return a paginated list of all your contracts.

<h3 id="get-contracts-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|What entry offset to request|
|limit|query|integer|false|How many entries to return per page|

> Example responses

> 200 Response

```json
{
  "data": [
    {
      "id": "string",
      "factionSymbol": "string",
      "type": "PROCUREMENT",
      "terms": {
        "deadline": "2019-08-24T14:15:22Z",
        "payment": {
          "onAccepted": 0,
          "onFulfilled": 0
        },
        "deliver": [
          {
            "tradeSymbol": "string",
            "destinationSymbol": "string",
            "unitsRequired": 0,
            "unitsFulfilled": 0
          }
        ]
      },
      "accepted": false,
      "fulfilled": false,
      "expiration": "2019-08-24T14:15:22Z",
      "deadlineToAccept": "2019-08-24T14:15:22Z"
    }
  ],
  "meta": {
    "total": 0,
    "page": 1,
    "limit": 10
  }
}
```

<h3 id="get-contracts-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Succesfully listed contracts.|Inline|

<h3 id="get-contracts-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[[Contract](#schemacontract)]|true|none|[Contract details.]|
|»» id|string|true|none|ID of the contract.|
|»» factionSymbol|string|true|none|The symbol of the faction that this contract is for.|
|»» type|string|true|none|Type of contract.|
|»» terms|[ContractTerms](#schemacontractterms)|true|none|The terms to fulfill the contract.|
|»»» deadline|string(date-time)|true|none|The deadline for the contract.|
|»»» payment|[ContractPayment](#schemacontractpayment)|true|none|Payments for the contract.|
|»»»» onAccepted|integer|true|none|The amount of credits received up front for accepting the contract.|
|»»»» onFulfilled|integer|true|none|The amount of credits received when the contract is fulfilled.|
|»»» deliver|[[ContractDeliverGood](#schemacontractdelivergood)]|false|none|The cargo that needs to be delivered to fulfill the contract.|
|»»»» tradeSymbol|string|true|none|The symbol of the trade good to deliver.|
|»»»» destinationSymbol|string|true|none|The destination where goods need to be delivered.|
|»»»» unitsRequired|integer|true|none|The number of units that need to be delivered on this contract.|
|»»»» unitsFulfilled|integer|true|none|The number of units fulfilled on this contract.|
|»» accepted|boolean|true|none|Whether the contract has been accepted by the agent|
|»» fulfilled|boolean|true|none|Whether the contract has been fulfilled|
|»» expiration|string(date-time)|true|none|Deprecated in favor of deadlineToAccept|
|»» deadlineToAccept|string(date-time)|false|none|The time at which the contract is no longer available to be accepted|
|» meta|[Meta](#schemameta)|true|none|Meta details for pagination.|
|»» total|integer|true|none|Shows the total amount of items of this kind that exist.|
|»» page|integer|true|none|A page denotes an amount of items, offset from the first item. Each page holds an amount of items equal to the `limit`.|
|»» limit|integer|true|none|The amount of items in each page. Limits how many items can be fetched at once.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PROCUREMENT|
|type|TRANSPORT|
|type|SHUTTLE|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## get-contract

<a id="opIdget-contract"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('https://api.spacetraders.io/v2/my/contracts/{contractId}', headers = headers)

print(r.json())

```

`GET /my/contracts/{contractId}`

*Get Contract*

Get the details of a contract by ID.

<h3 id="get-contract-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|contractId|path|string|true|The contract ID|

> Example responses

> 200 Response

```json
{
  "data": {
    "id": "string",
    "factionSymbol": "string",
    "type": "PROCUREMENT",
    "terms": {
      "deadline": "2019-08-24T14:15:22Z",
      "payment": {
        "onAccepted": 0,
        "onFulfilled": 0
      },
      "deliver": [
        {
          "tradeSymbol": "string",
          "destinationSymbol": "string",
          "unitsRequired": 0,
          "unitsFulfilled": 0
        }
      ]
    },
    "accepted": false,
    "fulfilled": false,
    "expiration": "2019-08-24T14:15:22Z",
    "deadlineToAccept": "2019-08-24T14:15:22Z"
  }
}
```

<h3 id="get-contract-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched contract.|Inline|

<h3 id="get-contract-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[Contract](#schemacontract)|true|none|Contract details.|
|»» id|string|true|none|ID of the contract.|
|»» factionSymbol|string|true|none|The symbol of the faction that this contract is for.|
|»» type|string|true|none|Type of contract.|
|»» terms|[ContractTerms](#schemacontractterms)|true|none|The terms to fulfill the contract.|
|»»» deadline|string(date-time)|true|none|The deadline for the contract.|
|»»» payment|[ContractPayment](#schemacontractpayment)|true|none|Payments for the contract.|
|»»»» onAccepted|integer|true|none|The amount of credits received up front for accepting the contract.|
|»»»» onFulfilled|integer|true|none|The amount of credits received when the contract is fulfilled.|
|»»» deliver|[[ContractDeliverGood](#schemacontractdelivergood)]|false|none|The cargo that needs to be delivered to fulfill the contract.|
|»»»» tradeSymbol|string|true|none|The symbol of the trade good to deliver.|
|»»»» destinationSymbol|string|true|none|The destination where goods need to be delivered.|
|»»»» unitsRequired|integer|true|none|The number of units that need to be delivered on this contract.|
|»»»» unitsFulfilled|integer|true|none|The number of units fulfilled on this contract.|
|»» accepted|boolean|true|none|Whether the contract has been accepted by the agent|
|»» fulfilled|boolean|true|none|Whether the contract has been fulfilled|
|»» expiration|string(date-time)|true|none|Deprecated in favor of deadlineToAccept|
|»» deadlineToAccept|string(date-time)|false|none|The time at which the contract is no longer available to be accepted|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PROCUREMENT|
|type|TRANSPORT|
|type|SHUTTLE|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## accept-contract

<a id="opIdaccept-contract"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/contracts/{contractId}/accept', headers = headers)

print(r.json())

```

`POST /my/contracts/{contractId}/accept`

*Accept Contract*

Accept a contract by ID. 

You can only accept contracts that were offered to you, were not accepted yet, and whose deadlines has not passed yet.

<h3 id="accept-contract-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|contractId|path|string|true|The contract ID to accept.|

> Example responses

> 200 Response

```json
{
  "data": {
    "agent": {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    },
    "contract": {
      "id": "string",
      "factionSymbol": "string",
      "type": "PROCUREMENT",
      "terms": {
        "deadline": "2019-08-24T14:15:22Z",
        "payment": {
          "onAccepted": 0,
          "onFulfilled": 0
        },
        "deliver": [
          {
            "tradeSymbol": "string",
            "destinationSymbol": "string",
            "unitsRequired": 0,
            "unitsFulfilled": 0
          }
        ]
      },
      "accepted": false,
      "fulfilled": false,
      "expiration": "2019-08-24T14:15:22Z",
      "deadlineToAccept": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="accept-contract-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Succesfully accepted contract.|Inline|

<h3 id="accept-contract-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» agent|[Agent](#schemaagent)|true|none|Agent details.|
|»»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»»» symbol|string|true|none|Symbol of the agent.|
|»»» headquarters|string|true|none|The headquarters of the agent.|
|»»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»»» startingFaction|string|true|none|The faction the agent started with.|
|»»» shipCount|integer|true|none|How many ships are owned by the agent.|
|»» contract|[Contract](#schemacontract)|true|none|Contract details.|
|»»» id|string|true|none|ID of the contract.|
|»»» factionSymbol|string|true|none|The symbol of the faction that this contract is for.|
|»»» type|string|true|none|Type of contract.|
|»»» terms|[ContractTerms](#schemacontractterms)|true|none|The terms to fulfill the contract.|
|»»»» deadline|string(date-time)|true|none|The deadline for the contract.|
|»»»» payment|[ContractPayment](#schemacontractpayment)|true|none|Payments for the contract.|
|»»»»» onAccepted|integer|true|none|The amount of credits received up front for accepting the contract.|
|»»»»» onFulfilled|integer|true|none|The amount of credits received when the contract is fulfilled.|
|»»»» deliver|[[ContractDeliverGood](#schemacontractdelivergood)]|false|none|The cargo that needs to be delivered to fulfill the contract.|
|»»»»» tradeSymbol|string|true|none|The symbol of the trade good to deliver.|
|»»»»» destinationSymbol|string|true|none|The destination where goods need to be delivered.|
|»»»»» unitsRequired|integer|true|none|The number of units that need to be delivered on this contract.|
|»»»»» unitsFulfilled|integer|true|none|The number of units fulfilled on this contract.|
|»»» accepted|boolean|true|none|Whether the contract has been accepted by the agent|
|»»» fulfilled|boolean|true|none|Whether the contract has been fulfilled|
|»»» expiration|string(date-time)|true|none|Deprecated in favor of deadlineToAccept|
|»»» deadlineToAccept|string(date-time)|false|none|The time at which the contract is no longer available to be accepted|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PROCUREMENT|
|type|TRANSPORT|
|type|SHUTTLE|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## deliver-contract

<a id="opIddeliver-contract"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/contracts/{contractId}/deliver', headers = headers)

print(r.json())

```

`POST /my/contracts/{contractId}/deliver`

*Deliver Cargo to Contract*

Deliver cargo to a contract.

In order to use this API, a ship must be at the delivery location (denoted in the delivery terms as `destinationSymbol` of a contract) and must have a number of units of a good required by this contract in its cargo.

Cargo that was delivered will be removed from the ship's cargo.

> Body parameter

```json
{
  "shipSymbol": "string",
  "tradeSymbol": "string",
  "units": 0
}
```

<h3 id="deliver-contract-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» shipSymbol|body|string|true|Symbol of a ship located in the destination to deliver a contract and that has a good to deliver in its cargo.|
|» tradeSymbol|body|string|true|The symbol of the good to deliver.|
|» units|body|integer|true|Amount of units to deliver.|
|contractId|path|string|true|The ID of the contract.|

> Example responses

> 200 Response

```json
{
  "data": {
    "contract": {
      "id": "string",
      "factionSymbol": "string",
      "type": "PROCUREMENT",
      "terms": {
        "deadline": "2019-08-24T14:15:22Z",
        "payment": {
          "onAccepted": 0,
          "onFulfilled": 0
        },
        "deliver": [
          {
            "tradeSymbol": "string",
            "destinationSymbol": "string",
            "unitsRequired": 0,
            "unitsFulfilled": 0
          }
        ]
      },
      "accepted": false,
      "fulfilled": false,
      "expiration": "2019-08-24T14:15:22Z",
      "deadlineToAccept": "2019-08-24T14:15:22Z"
    },
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    }
  }
}
```

<h3 id="deliver-contract-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully delivered cargo to contract.|Inline|

<h3 id="deliver-contract-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» contract|[Contract](#schemacontract)|true|none|Contract details.|
|»»» id|string|true|none|ID of the contract.|
|»»» factionSymbol|string|true|none|The symbol of the faction that this contract is for.|
|»»» type|string|true|none|Type of contract.|
|»»» terms|[ContractTerms](#schemacontractterms)|true|none|The terms to fulfill the contract.|
|»»»» deadline|string(date-time)|true|none|The deadline for the contract.|
|»»»» payment|[ContractPayment](#schemacontractpayment)|true|none|Payments for the contract.|
|»»»»» onAccepted|integer|true|none|The amount of credits received up front for accepting the contract.|
|»»»»» onFulfilled|integer|true|none|The amount of credits received when the contract is fulfilled.|
|»»»» deliver|[[ContractDeliverGood](#schemacontractdelivergood)]|false|none|The cargo that needs to be delivered to fulfill the contract.|
|»»»»» tradeSymbol|string|true|none|The symbol of the trade good to deliver.|
|»»»»» destinationSymbol|string|true|none|The destination where goods need to be delivered.|
|»»»»» unitsRequired|integer|true|none|The number of units that need to be delivered on this contract.|
|»»»»» unitsFulfilled|integer|true|none|The number of units fulfilled on this contract.|
|»»» accepted|boolean|true|none|Whether the contract has been accepted by the agent|
|»»» fulfilled|boolean|true|none|Whether the contract has been fulfilled|
|»»» expiration|string(date-time)|true|none|Deprecated in favor of deadlineToAccept|
|»»» deadlineToAccept|string(date-time)|false|none|The time at which the contract is no longer available to be accepted|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PROCUREMENT|
|type|TRANSPORT|
|type|SHUTTLE|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## fulfill-contract

<a id="opIdfulfill-contract"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/contracts/{contractId}/fulfill', headers = headers)

print(r.json())

```

`POST /my/contracts/{contractId}/fulfill`

*Fulfill Contract*

Fulfill a contract. Can only be used on contracts that have all of their delivery terms fulfilled.

<h3 id="fulfill-contract-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|contractId|path|string|true|The ID of the contract to fulfill.|

> Example responses

> 200 Response

```json
{
  "data": {
    "agent": {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    },
    "contract": {
      "id": "string",
      "factionSymbol": "string",
      "type": "PROCUREMENT",
      "terms": {
        "deadline": "2019-08-24T14:15:22Z",
        "payment": {
          "onAccepted": 0,
          "onFulfilled": 0
        },
        "deliver": [
          {
            "tradeSymbol": "string",
            "destinationSymbol": "string",
            "unitsRequired": 0,
            "unitsFulfilled": 0
          }
        ]
      },
      "accepted": false,
      "fulfilled": false,
      "expiration": "2019-08-24T14:15:22Z",
      "deadlineToAccept": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="fulfill-contract-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fulfilled a contract.|Inline|

<h3 id="fulfill-contract-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» agent|[Agent](#schemaagent)|true|none|Agent details.|
|»»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»»» symbol|string|true|none|Symbol of the agent.|
|»»» headquarters|string|true|none|The headquarters of the agent.|
|»»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»»» startingFaction|string|true|none|The faction the agent started with.|
|»»» shipCount|integer|true|none|How many ships are owned by the agent.|
|»» contract|[Contract](#schemacontract)|true|none|Contract details.|
|»»» id|string|true|none|ID of the contract.|
|»»» factionSymbol|string|true|none|The symbol of the faction that this contract is for.|
|»»» type|string|true|none|Type of contract.|
|»»» terms|[ContractTerms](#schemacontractterms)|true|none|The terms to fulfill the contract.|
|»»»» deadline|string(date-time)|true|none|The deadline for the contract.|
|»»»» payment|[ContractPayment](#schemacontractpayment)|true|none|Payments for the contract.|
|»»»»» onAccepted|integer|true|none|The amount of credits received up front for accepting the contract.|
|»»»»» onFulfilled|integer|true|none|The amount of credits received when the contract is fulfilled.|
|»»»» deliver|[[ContractDeliverGood](#schemacontractdelivergood)]|false|none|The cargo that needs to be delivered to fulfill the contract.|
|»»»»» tradeSymbol|string|true|none|The symbol of the trade good to deliver.|
|»»»»» destinationSymbol|string|true|none|The destination where goods need to be delivered.|
|»»»»» unitsRequired|integer|true|none|The number of units that need to be delivered on this contract.|
|»»»»» unitsFulfilled|integer|true|none|The number of units fulfilled on this contract.|
|»»» accepted|boolean|true|none|Whether the contract has been accepted by the agent|
|»»» fulfilled|boolean|true|none|Whether the contract has been fulfilled|
|»»» expiration|string(date-time)|true|none|Deprecated in favor of deadlineToAccept|
|»»» deadlineToAccept|string(date-time)|false|none|The time at which the contract is no longer available to be accepted|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PROCUREMENT|
|type|TRANSPORT|
|type|SHUTTLE|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

<h1 id="spacetraders-api-factions">Factions</h1>

Factions

## get-factions

<a id="opIdget-factions"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.spacetraders.io/v2/factions', headers = headers)

print(r.json())

```

`GET /factions`

*List Factions*

Return a paginated list of all the factions in the game.

<h3 id="get-factions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|What entry offset to request|
|limit|query|integer|false|How many entries to return per page|

> Example responses

> 200 Response

```json
{
  "data": [
    {
      "symbol": "COSMIC",
      "name": "string",
      "description": "string",
      "headquarters": "string",
      "traits": [
        {
          "symbol": "BUREAUCRATIC",
          "name": "string",
          "description": "string"
        }
      ],
      "isRecruiting": true
    }
  ],
  "meta": {
    "total": 0,
    "page": 1,
    "limit": 10
  }
}
```

<h3 id="get-factions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Succesfully fetched factions.|Inline|

<h3 id="get-factions-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[[Faction](#schemafaction)]|true|none|[Faction details.]|
|»» symbol|[FactionSymbol](#schemafactionsymbol)|true|none|The symbol of the faction.|
|»» name|string|true|none|Name of the faction.|
|»» description|string|true|none|Description of the faction.|
|»» headquarters|string|true|none|The waypoint in which the faction's HQ is located in.|
|»» traits|[[FactionTrait](#schemafactiontrait)]|true|none|List of traits that define this faction.|
|»»» symbol|[FactionTraitSymbol](#schemafactiontraitsymbol)|true|none|The unique identifier of the trait.|
|»»» name|string|true|none|The name of the trait.|
|»»» description|string|true|none|A description of the trait.|
|»» isRecruiting|boolean|true|none|Whether or not the faction is currently recruiting new agents.|
|» meta|[Meta](#schemameta)|true|none|Meta details for pagination.|
|»» total|integer|true|none|Shows the total amount of items of this kind that exist.|
|»» page|integer|true|none|A page denotes an amount of items, offset from the first item. Each page holds an amount of items equal to the `limit`.|
|»» limit|integer|true|none|The amount of items in each page. Limits how many items can be fetched at once.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|COSMIC|
|symbol|VOID|
|symbol|GALACTIC|
|symbol|QUANTUM|
|symbol|DOMINION|
|symbol|ASTRO|
|symbol|CORSAIRS|
|symbol|OBSIDIAN|
|symbol|AEGIS|
|symbol|UNITED|
|symbol|SOLITARY|
|symbol|COBALT|
|symbol|OMEGA|
|symbol|ECHO|
|symbol|LORDS|
|symbol|CULT|
|symbol|ANCIENTS|
|symbol|SHADOW|
|symbol|ETHEREAL|
|symbol|BUREAUCRATIC|
|symbol|SECRETIVE|
|symbol|CAPITALISTIC|
|symbol|INDUSTRIOUS|
|symbol|PEACEFUL|
|symbol|DISTRUSTFUL|
|symbol|WELCOMING|
|symbol|SMUGGLERS|
|symbol|SCAVENGERS|
|symbol|REBELLIOUS|
|symbol|EXILES|
|symbol|PIRATES|
|symbol|RAIDERS|
|symbol|CLAN|
|symbol|GUILD|
|symbol|DOMINION|
|symbol|FRINGE|
|symbol|FORSAKEN|
|symbol|ISOLATED|
|symbol|LOCALIZED|
|symbol|ESTABLISHED|
|symbol|NOTABLE|
|symbol|DOMINANT|
|symbol|INESCAPABLE|
|symbol|INNOVATIVE|
|symbol|BOLD|
|symbol|VISIONARY|
|symbol|CURIOUS|
|symbol|DARING|
|symbol|EXPLORATORY|
|symbol|RESOURCEFUL|
|symbol|FLEXIBLE|
|symbol|COOPERATIVE|
|symbol|UNITED|
|symbol|STRATEGIC|
|symbol|INTELLIGENT|
|symbol|RESEARCH_FOCUSED|
|symbol|COLLABORATIVE|
|symbol|PROGRESSIVE|
|symbol|MILITARISTIC|
|symbol|TECHNOLOGICALLY_ADVANCED|
|symbol|AGGRESSIVE|
|symbol|IMPERIALISTIC|
|symbol|TREASURE_HUNTERS|
|symbol|DEXTEROUS|
|symbol|UNPREDICTABLE|
|symbol|BRUTAL|
|symbol|FLEETING|
|symbol|ADAPTABLE|
|symbol|SELF_SUFFICIENT|
|symbol|DEFENSIVE|
|symbol|PROUD|
|symbol|DIVERSE|
|symbol|INDEPENDENT|
|symbol|SELF_INTERESTED|
|symbol|FRAGMENTED|
|symbol|COMMERCIAL|
|symbol|FREE_MARKETS|
|symbol|ENTREPRENEURIAL|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, AgentToken
</aside>

## get-faction

<a id="opIdget-faction"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('https://api.spacetraders.io/v2/factions/{factionSymbol}', headers = headers)

print(r.json())

```

`GET /factions/{factionSymbol}`

*Get Faction*

View the details of a faction.

<h3 id="get-faction-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|factionSymbol|path|string|true|The faction symbol|

> Example responses

> 200 Response

```json
{
  "data": {
    "symbol": "COSMIC",
    "name": "string",
    "description": "string",
    "headquarters": "string",
    "traits": [
      {
        "symbol": "BUREAUCRATIC",
        "name": "string",
        "description": "string"
      }
    ],
    "isRecruiting": true
  }
}
```

<h3 id="get-faction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched a faction.|Inline|

<h3 id="get-faction-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[Faction](#schemafaction)|true|none|Faction details.|
|»» symbol|[FactionSymbol](#schemafactionsymbol)|true|none|The symbol of the faction.|
|»» name|string|true|none|Name of the faction.|
|»» description|string|true|none|Description of the faction.|
|»» headquarters|string|true|none|The waypoint in which the faction's HQ is located in.|
|»» traits|[[FactionTrait](#schemafactiontrait)]|true|none|List of traits that define this faction.|
|»»» symbol|[FactionTraitSymbol](#schemafactiontraitsymbol)|true|none|The unique identifier of the trait.|
|»»» name|string|true|none|The name of the trait.|
|»»» description|string|true|none|A description of the trait.|
|»» isRecruiting|boolean|true|none|Whether or not the faction is currently recruiting new agents.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|COSMIC|
|symbol|VOID|
|symbol|GALACTIC|
|symbol|QUANTUM|
|symbol|DOMINION|
|symbol|ASTRO|
|symbol|CORSAIRS|
|symbol|OBSIDIAN|
|symbol|AEGIS|
|symbol|UNITED|
|symbol|SOLITARY|
|symbol|COBALT|
|symbol|OMEGA|
|symbol|ECHO|
|symbol|LORDS|
|symbol|CULT|
|symbol|ANCIENTS|
|symbol|SHADOW|
|symbol|ETHEREAL|
|symbol|BUREAUCRATIC|
|symbol|SECRETIVE|
|symbol|CAPITALISTIC|
|symbol|INDUSTRIOUS|
|symbol|PEACEFUL|
|symbol|DISTRUSTFUL|
|symbol|WELCOMING|
|symbol|SMUGGLERS|
|symbol|SCAVENGERS|
|symbol|REBELLIOUS|
|symbol|EXILES|
|symbol|PIRATES|
|symbol|RAIDERS|
|symbol|CLAN|
|symbol|GUILD|
|symbol|DOMINION|
|symbol|FRINGE|
|symbol|FORSAKEN|
|symbol|ISOLATED|
|symbol|LOCALIZED|
|symbol|ESTABLISHED|
|symbol|NOTABLE|
|symbol|DOMINANT|
|symbol|INESCAPABLE|
|symbol|INNOVATIVE|
|symbol|BOLD|
|symbol|VISIONARY|
|symbol|CURIOUS|
|symbol|DARING|
|symbol|EXPLORATORY|
|symbol|RESOURCEFUL|
|symbol|FLEXIBLE|
|symbol|COOPERATIVE|
|symbol|UNITED|
|symbol|STRATEGIC|
|symbol|INTELLIGENT|
|symbol|RESEARCH_FOCUSED|
|symbol|COLLABORATIVE|
|symbol|PROGRESSIVE|
|symbol|MILITARISTIC|
|symbol|TECHNOLOGICALLY_ADVANCED|
|symbol|AGGRESSIVE|
|symbol|IMPERIALISTIC|
|symbol|TREASURE_HUNTERS|
|symbol|DEXTEROUS|
|symbol|UNPREDICTABLE|
|symbol|BRUTAL|
|symbol|FLEETING|
|symbol|ADAPTABLE|
|symbol|SELF_SUFFICIENT|
|symbol|DEFENSIVE|
|symbol|PROUD|
|symbol|DIVERSE|
|symbol|INDEPENDENT|
|symbol|SELF_INTERESTED|
|symbol|FRAGMENTED|
|symbol|COMMERCIAL|
|symbol|FREE_MARKETS|
|symbol|ENTREPRENEURIAL|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

<h1 id="spacetraders-api-fleet">Fleet</h1>

Fleet

## get-my-ships

<a id="opIdget-my-ships"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('https://api.spacetraders.io/v2/my/ships', headers = headers)

print(r.json())

```

`GET /my/ships`

*List Ships*

Return a paginated list of all of ships under your agent's ownership.

<h3 id="get-my-ships-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|What entry offset to request|
|limit|query|integer|false|How many entries to return per page|

> Example responses

> 200 Response

```json
{
  "data": [
    {
      "symbol": "string",
      "registration": {
        "name": "string",
        "factionSymbol": "string",
        "role": "FABRICATOR"
      },
      "nav": {
        "systemSymbol": "string",
        "waypointSymbol": "string",
        "route": {
          "destination": {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0
          },
          "origin": {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0
          },
          "departureTime": "2019-08-24T14:15:22Z",
          "arrival": "2019-08-24T14:15:22Z"
        },
        "status": "IN_TRANSIT",
        "flightMode": "DRIFT"
      },
      "crew": {
        "current": 0,
        "required": 0,
        "capacity": 0,
        "rotation": "STRICT",
        "morale": 100,
        "wages": 0
      },
      "frame": {
        "symbol": "FRAME_PROBE",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "moduleSlots": 0,
        "mountingPoints": 0,
        "fuelCapacity": 0,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "reactor": {
        "symbol": "REACTOR_SOLAR_I",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "powerOutput": 1,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "engine": {
        "symbol": "ENGINE_IMPULSE_DRIVE_I",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "speed": 1,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "cooldown": {
        "shipSymbol": "string",
        "totalSeconds": 0,
        "remainingSeconds": 0,
        "expiration": "2019-08-24T14:15:22Z"
      },
      "modules": [
        {
          "symbol": "MODULE_MINERAL_PROCESSOR_I",
          "capacity": 0,
          "range": 0,
          "name": "string",
          "description": "string",
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        }
      ],
      "mounts": [
        {
          "symbol": "MOUNT_GAS_SIPHON_I",
          "name": "string",
          "description": "string",
          "strength": 0,
          "deposits": [
            "QUARTZ_SAND"
          ],
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        }
      ],
      "cargo": {
        "capacity": 0,
        "units": 0,
        "inventory": [
          {
            "symbol": "PRECIOUS_STONES",
            "name": "string",
            "description": "string",
            "units": 1
          }
        ]
      },
      "fuel": {
        "current": 0,
        "capacity": 0,
        "consumed": {
          "amount": 0,
          "timestamp": "2019-08-24T14:15:22Z"
        }
      }
    }
  ],
  "meta": {
    "total": 0,
    "page": 1,
    "limit": 10
  }
}
```

<h3 id="get-my-ships-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Succesfully listed ships.|Inline|

<h3 id="get-my-ships-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[[Ship](#schemaship)]|true|none|[Ship details.]|
|»» symbol|string|true|none|The globally unique identifier of the ship in the following format: `[AGENT_SYMBOL]-[HEX_ID]`|
|»» registration|[ShipRegistration](#schemashipregistration)|true|none|The public registration information of the ship|
|»»» name|string|true|none|The agent's registered name of the ship|
|»»» factionSymbol|string|true|none|The symbol of the faction the ship is registered with|
|»»» role|[ShipRole](#schemashiprole)|true|none|The registered role of the ship|
|»» nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|
|»» crew|[ShipCrew](#schemashipcrew)|true|none|The ship's crew service and maintain the ship's systems and equipment.|
|»»» current|integer|true|none|The current number of crew members on the ship.|
|»»» required|integer|true|none|The minimum number of crew members required to maintain the ship.|
|»»» capacity|integer|true|none|The maximum number of crew members the ship can support.|
|»»» rotation|string|true|none|The rotation of crew shifts. A stricter shift improves the ship's performance. A more relaxed shift improves the crew's morale.|
|»»» morale|integer|true|none|A rough measure of the crew's morale. A higher morale means the crew is happier and more productive. A lower morale means the ship is more prone to accidents.|
|»»» wages|integer|true|none|The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint.|
|»» frame|[ShipFrame](#schemashipframe)|true|none|The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.|
|»»» symbol|string|true|none|Symbol of the frame.|
|»»» name|string|true|none|Name of the frame.|
|»»» description|string|true|none|Description of the frame.|
|»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»» moduleSlots|integer|true|none|The amount of slots that can be dedicated to modules installed in the ship. Each installed module take up a number of slots, and once there are no more slots, no new modules can be installed.|
|»»» mountingPoints|integer|true|none|The amount of slots that can be dedicated to mounts installed in the ship. Each installed mount takes up a number of points, and once there are no more points remaining, no new mounts can be installed.|
|»»» fuelCapacity|integer|true|none|The maximum amount of fuel that can be stored in this ship. When refueling, the ship will be refueled to this amount.|
|»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»»» power|integer|false|none|The amount of power required from the reactor.|
|»»»» crew|integer|false|none|The number of crew required for operation.|
|»»»» slots|integer|false|none|The number of module slots required for installation.|
|»» reactor|[ShipReactor](#schemashipreactor)|true|none|The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.|
|»»» symbol|string|true|none|Symbol of the reactor.|
|»»» name|string|true|none|Name of the reactor.|
|»»» description|string|true|none|Description of the reactor.|
|»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»» powerOutput|integer|true|none|The amount of power provided by this reactor. The more power a reactor provides to the ship, the lower the cooldown it gets when using a module or mount that taxes the ship's power.|
|»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»» engine|[ShipEngine](#schemashipengine)|true|none|The engine determines how quickly a ship travels between waypoints.|
|»»» symbol|string|true|none|The symbol of the engine.|
|»»» name|string|true|none|The name of the engine.|
|»»» description|string|true|none|The description of the engine.|
|»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»» speed|integer|true|none|The speed stat of this engine. The higher the speed, the faster a ship can travel from one point to another. Reduces the time of arrival when navigating the ship.|
|»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»» modules|[[ShipModule](#schemashipmodule)]|true|none|Modules installed in this ship.|
|»»» symbol|string|true|none|The symbol of the module.|
|»»» capacity|integer|false|none|Modules that provide capacity, such as cargo hold or crew quarters will show this value to denote how much of a bonus the module grants.|
|»»» range|integer|false|none|Modules that have a range will such as a sensor array show this value to denote how far can the module reach with its capabilities.|
|»»» name|string|true|none|Name of this module.|
|»»» description|string|true|none|Description of this module.|
|»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»» mounts|[[ShipMount](#schemashipmount)]|true|none|Mounts installed in this ship.|
|»»» symbol|string|true|none|Symbo of this mount.|
|»»» name|string|true|none|Name of this mount.|
|»»» description|string|false|none|Description of this mount.|
|»»» strength|integer|false|none|Mounts that have this value, such as mining lasers, denote how powerful this mount's capabilities are.|
|»»» deposits|[string]|false|none|Mounts that have this value denote what goods can be produced from using the mount.|
|»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|
|»» fuel|[ShipFuel](#schemashipfuel)|true|none|Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.|
|»»» current|integer|true|none|The current amount of fuel in the ship's tanks.|
|»»» capacity|integer|true|none|The maximum amount of fuel the ship's tanks can hold.|
|»»» consumed|object|false|none|An object that only shows up when an action has consumed fuel in the process. Shows the fuel consumption data.|
|»»»» amount|integer|true|none|The amount of fuel consumed by the most recent transit or action.|
|»»»» timestamp|string(date-time)|true|none|The time at which the fuel was consumed.|
|» meta|[Meta](#schemameta)|true|none|Meta details for pagination.|
|»» total|integer|true|none|Shows the total amount of items of this kind that exist.|
|»» page|integer|true|none|A page denotes an amount of items, offset from the first item. Each page holds an amount of items equal to the `limit`.|
|»» limit|integer|true|none|The amount of items in each page. Limits how many items can be fetched at once.|

#### Enumerated Values

|Property|Value|
|---|---|
|role|FABRICATOR|
|role|HARVESTER|
|role|HAULER|
|role|INTERCEPTOR|
|role|EXCAVATOR|
|role|TRANSPORT|
|role|REPAIR|
|role|SURVEYOR|
|role|COMMAND|
|role|CARRIER|
|role|PATROL|
|role|SATELLITE|
|role|EXPLORER|
|role|REFINERY|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|
|rotation|STRICT|
|rotation|RELAXED|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## purchase-ship

<a id="opIdpurchase-ship"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships', headers = headers)

print(r.json())

```

`POST /my/ships`

*Purchase Ship*

Purchase a ship from a Shipyard. In order to use this function, a ship under your agent's ownership must be in a waypoint that has the `Shipyard` trait, and the Shipyard must sell the type of the desired ship.

Shipyards typically offer ship types, which are predefined templates of ships that have dedicated roles. A template comes with a preset of an engine, a reactor, and a frame. It may also include a few modules and mounts.

> Body parameter

```json
{
  "shipType": "SHIP_PROBE",
  "waypointSymbol": "string"
}
```

<h3 id="purchase-ship-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» shipType|body|[ShipType](#schemashiptype)|true|Type of ship|
|» waypointSymbol|body|string|true|The symbol of the waypoint you want to purchase the ship at.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» shipType|SHIP_PROBE|
|» shipType|SHIP_MINING_DRONE|
|» shipType|SHIP_SIPHON_DRONE|
|» shipType|SHIP_INTERCEPTOR|
|» shipType|SHIP_LIGHT_HAULER|
|» shipType|SHIP_COMMAND_FRIGATE|
|» shipType|SHIP_EXPLORER|
|» shipType|SHIP_HEAVY_FREIGHTER|
|» shipType|SHIP_LIGHT_SHUTTLE|
|» shipType|SHIP_ORE_HOUND|
|» shipType|SHIP_REFINING_FREIGHTER|
|» shipType|SHIP_SURVEYOR|

> Example responses

> 201 Response

```json
{
  "data": {
    "agent": {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    },
    "ship": {
      "symbol": "string",
      "registration": {
        "name": "string",
        "factionSymbol": "string",
        "role": "FABRICATOR"
      },
      "nav": {
        "systemSymbol": "string",
        "waypointSymbol": "string",
        "route": {
          "destination": {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0
          },
          "origin": {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0
          },
          "departureTime": "2019-08-24T14:15:22Z",
          "arrival": "2019-08-24T14:15:22Z"
        },
        "status": "IN_TRANSIT",
        "flightMode": "DRIFT"
      },
      "crew": {
        "current": 0,
        "required": 0,
        "capacity": 0,
        "rotation": "STRICT",
        "morale": 100,
        "wages": 0
      },
      "frame": {
        "symbol": "FRAME_PROBE",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "moduleSlots": 0,
        "mountingPoints": 0,
        "fuelCapacity": 0,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "reactor": {
        "symbol": "REACTOR_SOLAR_I",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "powerOutput": 1,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "engine": {
        "symbol": "ENGINE_IMPULSE_DRIVE_I",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "speed": 1,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "cooldown": {
        "shipSymbol": "string",
        "totalSeconds": 0,
        "remainingSeconds": 0,
        "expiration": "2019-08-24T14:15:22Z"
      },
      "modules": [
        {
          "symbol": "MODULE_MINERAL_PROCESSOR_I",
          "capacity": 0,
          "range": 0,
          "name": "string",
          "description": "string",
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        }
      ],
      "mounts": [
        {
          "symbol": "MOUNT_GAS_SIPHON_I",
          "name": "string",
          "description": "string",
          "strength": 0,
          "deposits": [
            "QUARTZ_SAND"
          ],
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        }
      ],
      "cargo": {
        "capacity": 0,
        "units": 0,
        "inventory": [
          {
            "symbol": "PRECIOUS_STONES",
            "name": "string",
            "description": "string",
            "units": 1
          }
        ]
      },
      "fuel": {
        "current": 0,
        "capacity": 0,
        "consumed": {
          "amount": 0,
          "timestamp": "2019-08-24T14:15:22Z"
        }
      }
    },
    "transaction": {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "shipType": "string",
      "price": 0,
      "agentSymbol": "string",
      "timestamp": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="purchase-ship-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Purchased ship successfully.|Inline|

<h3 id="purchase-ship-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» agent|[Agent](#schemaagent)|true|none|Agent details.|
|»»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»»» symbol|string|true|none|Symbol of the agent.|
|»»» headquarters|string|true|none|The headquarters of the agent.|
|»»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»»» startingFaction|string|true|none|The faction the agent started with.|
|»»» shipCount|integer|true|none|How many ships are owned by the agent.|
|»» ship|[Ship](#schemaship)|true|none|Ship details.|
|»»» symbol|string|true|none|The globally unique identifier of the ship in the following format: `[AGENT_SYMBOL]-[HEX_ID]`|
|»»» registration|[ShipRegistration](#schemashipregistration)|true|none|The public registration information of the ship|
|»»»» name|string|true|none|The agent's registered name of the ship|
|»»»» factionSymbol|string|true|none|The symbol of the faction the ship is registered with|
|»»»» role|[ShipRole](#schemashiprole)|true|none|The registered role of the ship|
|»»» nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»»»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»»»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|
|»»» crew|[ShipCrew](#schemashipcrew)|true|none|The ship's crew service and maintain the ship's systems and equipment.|
|»»»» current|integer|true|none|The current number of crew members on the ship.|
|»»»» required|integer|true|none|The minimum number of crew members required to maintain the ship.|
|»»»» capacity|integer|true|none|The maximum number of crew members the ship can support.|
|»»»» rotation|string|true|none|The rotation of crew shifts. A stricter shift improves the ship's performance. A more relaxed shift improves the crew's morale.|
|»»»» morale|integer|true|none|A rough measure of the crew's morale. A higher morale means the crew is happier and more productive. A lower morale means the ship is more prone to accidents.|
|»»»» wages|integer|true|none|The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint.|
|»»» frame|[ShipFrame](#schemashipframe)|true|none|The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.|
|»»»» symbol|string|true|none|Symbol of the frame.|
|»»»» name|string|true|none|Name of the frame.|
|»»»» description|string|true|none|Description of the frame.|
|»»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»»» moduleSlots|integer|true|none|The amount of slots that can be dedicated to modules installed in the ship. Each installed module take up a number of slots, and once there are no more slots, no new modules can be installed.|
|»»»» mountingPoints|integer|true|none|The amount of slots that can be dedicated to mounts installed in the ship. Each installed mount takes up a number of points, and once there are no more points remaining, no new mounts can be installed.|
|»»»» fuelCapacity|integer|true|none|The maximum amount of fuel that can be stored in this ship. When refueling, the ship will be refueled to this amount.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»»»» power|integer|false|none|The amount of power required from the reactor.|
|»»»»» crew|integer|false|none|The number of crew required for operation.|
|»»»»» slots|integer|false|none|The number of module slots required for installation.|
|»»» reactor|[ShipReactor](#schemashipreactor)|true|none|The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.|
|»»»» symbol|string|true|none|Symbol of the reactor.|
|»»»» name|string|true|none|Name of the reactor.|
|»»»» description|string|true|none|Description of the reactor.|
|»»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»»» powerOutput|integer|true|none|The amount of power provided by this reactor. The more power a reactor provides to the ship, the lower the cooldown it gets when using a module or mount that taxes the ship's power.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» engine|[ShipEngine](#schemashipengine)|true|none|The engine determines how quickly a ship travels between waypoints.|
|»»»» symbol|string|true|none|The symbol of the engine.|
|»»»» name|string|true|none|The name of the engine.|
|»»»» description|string|true|none|The description of the engine.|
|»»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»»» speed|integer|true|none|The speed stat of this engine. The higher the speed, the faster a ship can travel from one point to another. Reduces the time of arrival when navigating the ship.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»»» modules|[[ShipModule](#schemashipmodule)]|true|none|Modules installed in this ship.|
|»»»» symbol|string|true|none|The symbol of the module.|
|»»»» capacity|integer|false|none|Modules that provide capacity, such as cargo hold or crew quarters will show this value to denote how much of a bonus the module grants.|
|»»»» range|integer|false|none|Modules that have a range will such as a sensor array show this value to denote how far can the module reach with its capabilities.|
|»»»» name|string|true|none|Name of this module.|
|»»»» description|string|true|none|Description of this module.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» mounts|[[ShipMount](#schemashipmount)]|true|none|Mounts installed in this ship.|
|»»»» symbol|string|true|none|Symbo of this mount.|
|»»»» name|string|true|none|Name of this mount.|
|»»»» description|string|false|none|Description of this mount.|
|»»»» strength|integer|false|none|Mounts that have this value, such as mining lasers, denote how powerful this mount's capabilities are.|
|»»»» deposits|[string]|false|none|Mounts that have this value denote what goods can be produced from using the mount.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»»» name|string|true|none|The name of the cargo item type.|
|»»»»» description|string|true|none|The description of the cargo item type.|
|»»»»» units|integer|true|none|The number of units of the cargo item.|
|»»» fuel|[ShipFuel](#schemashipfuel)|true|none|Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.|
|»»»» current|integer|true|none|The current amount of fuel in the ship's tanks.|
|»»»» capacity|integer|true|none|The maximum amount of fuel the ship's tanks can hold.|
|»»»» consumed|object|false|none|An object that only shows up when an action has consumed fuel in the process. Shows the fuel consumption data.|
|»»»»» amount|integer|true|none|The amount of fuel consumed by the most recent transit or action.|
|»»»»» timestamp|string(date-time)|true|none|The time at which the fuel was consumed.|
|»» transaction|[ShipyardTransaction](#schemashipyardtransaction)|true|none|Results of a transaction with a shipyard.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» shipSymbol|string|true|none|The symbol of the ship that was the subject of the transaction.|
|»»» shipType|string|true|none|The symbol of the ship that was the subject of the transaction.|
|»»» price|integer|true|none|The price of the transaction.|
|»»» agentSymbol|string|true|none|The symbol of the agent that made the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|

#### Enumerated Values

|Property|Value|
|---|---|
|role|FABRICATOR|
|role|HARVESTER|
|role|HAULER|
|role|INTERCEPTOR|
|role|EXCAVATOR|
|role|TRANSPORT|
|role|REPAIR|
|role|SURVEYOR|
|role|COMMAND|
|role|CARRIER|
|role|PATROL|
|role|SATELLITE|
|role|EXPLORER|
|role|REFINERY|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|
|rotation|STRICT|
|rotation|RELAXED|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## get-my-ship

<a id="opIdget-my-ship"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('https://api.spacetraders.io/v2/my/ships/{shipSymbol}', headers = headers)

print(r.json())

```

`GET /my/ships/{shipSymbol}`

*Get Ship*

Retrieve the details of a ship under your agent's ownership.

<h3 id="get-my-ship-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The symbol of the ship.|

> Example responses

> 200 Response

```json
{
  "data": {
    "symbol": "string",
    "registration": {
      "name": "string",
      "factionSymbol": "string",
      "role": "FABRICATOR"
    },
    "nav": {
      "systemSymbol": "string",
      "waypointSymbol": "string",
      "route": {
        "destination": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0
        },
        "origin": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0
        },
        "departureTime": "2019-08-24T14:15:22Z",
        "arrival": "2019-08-24T14:15:22Z"
      },
      "status": "IN_TRANSIT",
      "flightMode": "DRIFT"
    },
    "crew": {
      "current": 0,
      "required": 0,
      "capacity": 0,
      "rotation": "STRICT",
      "morale": 100,
      "wages": 0
    },
    "frame": {
      "symbol": "FRAME_PROBE",
      "name": "string",
      "description": "string",
      "condition": 1,
      "integrity": 1,
      "moduleSlots": 0,
      "mountingPoints": 0,
      "fuelCapacity": 0,
      "requirements": {
        "power": 0,
        "crew": 0,
        "slots": 0
      }
    },
    "reactor": {
      "symbol": "REACTOR_SOLAR_I",
      "name": "string",
      "description": "string",
      "condition": 1,
      "integrity": 1,
      "powerOutput": 1,
      "requirements": {
        "power": 0,
        "crew": 0,
        "slots": 0
      }
    },
    "engine": {
      "symbol": "ENGINE_IMPULSE_DRIVE_I",
      "name": "string",
      "description": "string",
      "condition": 1,
      "integrity": 1,
      "speed": 1,
      "requirements": {
        "power": 0,
        "crew": 0,
        "slots": 0
      }
    },
    "cooldown": {
      "shipSymbol": "string",
      "totalSeconds": 0,
      "remainingSeconds": 0,
      "expiration": "2019-08-24T14:15:22Z"
    },
    "modules": [
      {
        "symbol": "MODULE_MINERAL_PROCESSOR_I",
        "capacity": 0,
        "range": 0,
        "name": "string",
        "description": "string",
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      }
    ],
    "mounts": [
      {
        "symbol": "MOUNT_GAS_SIPHON_I",
        "name": "string",
        "description": "string",
        "strength": 0,
        "deposits": [
          "QUARTZ_SAND"
        ],
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      }
    ],
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    },
    "fuel": {
      "current": 0,
      "capacity": 0,
      "consumed": {
        "amount": 0,
        "timestamp": "2019-08-24T14:15:22Z"
      }
    }
  }
}
```

<h3 id="get-my-ship-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched ship.|Inline|

<h3 id="get-my-ship-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[Ship](#schemaship)|true|none|Ship details.|
|»» symbol|string|true|none|The globally unique identifier of the ship in the following format: `[AGENT_SYMBOL]-[HEX_ID]`|
|»» registration|[ShipRegistration](#schemashipregistration)|true|none|The public registration information of the ship|
|»»» name|string|true|none|The agent's registered name of the ship|
|»»» factionSymbol|string|true|none|The symbol of the faction the ship is registered with|
|»»» role|[ShipRole](#schemashiprole)|true|none|The registered role of the ship|
|»» nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|
|»» crew|[ShipCrew](#schemashipcrew)|true|none|The ship's crew service and maintain the ship's systems and equipment.|
|»»» current|integer|true|none|The current number of crew members on the ship.|
|»»» required|integer|true|none|The minimum number of crew members required to maintain the ship.|
|»»» capacity|integer|true|none|The maximum number of crew members the ship can support.|
|»»» rotation|string|true|none|The rotation of crew shifts. A stricter shift improves the ship's performance. A more relaxed shift improves the crew's morale.|
|»»» morale|integer|true|none|A rough measure of the crew's morale. A higher morale means the crew is happier and more productive. A lower morale means the ship is more prone to accidents.|
|»»» wages|integer|true|none|The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint.|
|»» frame|[ShipFrame](#schemashipframe)|true|none|The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.|
|»»» symbol|string|true|none|Symbol of the frame.|
|»»» name|string|true|none|Name of the frame.|
|»»» description|string|true|none|Description of the frame.|
|»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»» moduleSlots|integer|true|none|The amount of slots that can be dedicated to modules installed in the ship. Each installed module take up a number of slots, and once there are no more slots, no new modules can be installed.|
|»»» mountingPoints|integer|true|none|The amount of slots that can be dedicated to mounts installed in the ship. Each installed mount takes up a number of points, and once there are no more points remaining, no new mounts can be installed.|
|»»» fuelCapacity|integer|true|none|The maximum amount of fuel that can be stored in this ship. When refueling, the ship will be refueled to this amount.|
|»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»»» power|integer|false|none|The amount of power required from the reactor.|
|»»»» crew|integer|false|none|The number of crew required for operation.|
|»»»» slots|integer|false|none|The number of module slots required for installation.|
|»» reactor|[ShipReactor](#schemashipreactor)|true|none|The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.|
|»»» symbol|string|true|none|Symbol of the reactor.|
|»»» name|string|true|none|Name of the reactor.|
|»»» description|string|true|none|Description of the reactor.|
|»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»» powerOutput|integer|true|none|The amount of power provided by this reactor. The more power a reactor provides to the ship, the lower the cooldown it gets when using a module or mount that taxes the ship's power.|
|»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»» engine|[ShipEngine](#schemashipengine)|true|none|The engine determines how quickly a ship travels between waypoints.|
|»»» symbol|string|true|none|The symbol of the engine.|
|»»» name|string|true|none|The name of the engine.|
|»»» description|string|true|none|The description of the engine.|
|»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»» speed|integer|true|none|The speed stat of this engine. The higher the speed, the faster a ship can travel from one point to another. Reduces the time of arrival when navigating the ship.|
|»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»» modules|[[ShipModule](#schemashipmodule)]|true|none|Modules installed in this ship.|
|»»» symbol|string|true|none|The symbol of the module.|
|»»» capacity|integer|false|none|Modules that provide capacity, such as cargo hold or crew quarters will show this value to denote how much of a bonus the module grants.|
|»»» range|integer|false|none|Modules that have a range will such as a sensor array show this value to denote how far can the module reach with its capabilities.|
|»»» name|string|true|none|Name of this module.|
|»»» description|string|true|none|Description of this module.|
|»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»» mounts|[[ShipMount](#schemashipmount)]|true|none|Mounts installed in this ship.|
|»»» symbol|string|true|none|Symbo of this mount.|
|»»» name|string|true|none|Name of this mount.|
|»»» description|string|false|none|Description of this mount.|
|»»» strength|integer|false|none|Mounts that have this value, such as mining lasers, denote how powerful this mount's capabilities are.|
|»»» deposits|[string]|false|none|Mounts that have this value denote what goods can be produced from using the mount.|
|»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|
|»» fuel|[ShipFuel](#schemashipfuel)|true|none|Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.|
|»»» current|integer|true|none|The current amount of fuel in the ship's tanks.|
|»»» capacity|integer|true|none|The maximum amount of fuel the ship's tanks can hold.|
|»»» consumed|object|false|none|An object that only shows up when an action has consumed fuel in the process. Shows the fuel consumption data.|
|»»»» amount|integer|true|none|The amount of fuel consumed by the most recent transit or action.|
|»»»» timestamp|string(date-time)|true|none|The time at which the fuel was consumed.|

#### Enumerated Values

|Property|Value|
|---|---|
|role|FABRICATOR|
|role|HARVESTER|
|role|HAULER|
|role|INTERCEPTOR|
|role|EXCAVATOR|
|role|TRANSPORT|
|role|REPAIR|
|role|SURVEYOR|
|role|COMMAND|
|role|CARRIER|
|role|PATROL|
|role|SATELLITE|
|role|EXPLORER|
|role|REFINERY|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|
|rotation|STRICT|
|rotation|RELAXED|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## get-my-ship-cargo

<a id="opIdget-my-ship-cargo"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/cargo', headers = headers)

print(r.json())

```

`GET /my/ships/{shipSymbol}/cargo`

*Get Ship Cargo*

Retrieve the cargo of a ship under your agent's ownership.

<h3 id="get-my-ship-cargo-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The symbol of the ship.|

> Example responses

> 200 Response

```json
{
  "data": {
    "capacity": 0,
    "units": 0,
    "inventory": [
      {
        "symbol": "PRECIOUS_STONES",
        "name": "string",
        "description": "string",
        "units": 1
      }
    ]
  }
}
```

<h3 id="get-my-ship-cargo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched ship's cargo.|Inline|

<h3 id="get-my-ship-cargo-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»» name|string|true|none|The name of the cargo item type.|
|»»» description|string|true|none|The description of the cargo item type.|
|»»» units|integer|true|none|The number of units of the cargo item.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## orbit-ship

<a id="opIdorbit-ship"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/orbit', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/orbit`

*Orbit Ship*

Attempt to move your ship into orbit at its current location. The request will only succeed if your ship is capable of moving into orbit at the time of the request.

Orbiting ships are able to do actions that require the ship to be above surface such as navigating or extracting, but cannot access elements in their current waypoint, such as the market or a shipyard.

The endpoint is idempotent - successive calls will succeed even if the ship is already in orbit.

<h3 id="orbit-ship-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The symbol of the ship.|

> Example responses

> 200 Response

```json
{
  "data": {
    "nav": {
      "systemSymbol": "string",
      "waypointSymbol": "string",
      "route": {
        "destination": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0
        },
        "origin": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0
        },
        "departureTime": "2019-08-24T14:15:22Z",
        "arrival": "2019-08-24T14:15:22Z"
      },
      "status": "IN_TRANSIT",
      "flightMode": "DRIFT"
    }
  }
}
```

<h3 id="orbit-ship-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The ship has successfully moved into orbit at its current location.|Inline|

<h3 id="orbit-ship-responseschema">Response Schema</h3>

Status Code **200**

*Orbit Ship 200 Response*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## ship-refine

<a id="opIdship-refine"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/refine', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/refine`

*Ship Refine*

Attempt to refine the raw materials on your ship. The request will only succeed if your ship is capable of refining at the time of the request. In order to be able to refine, a ship must have goods that can be refined and have installed a `Refinery` module that can refine it.

When refining, 30 basic goods will be converted into 10 processed goods.

> Body parameter

```json
{
  "produce": "IRON"
}
```

<h3 id="ship-refine-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» produce|body|string|true|The type of good to produce out of the refining process.|
|shipSymbol|path|string|true|The symbol of the ship.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» produce|IRON|
|» produce|COPPER|
|» produce|SILVER|
|» produce|GOLD|
|» produce|ALUMINUM|
|» produce|PLATINUM|
|» produce|URANITE|
|» produce|MERITIUM|
|» produce|FUEL|

> Example responses

> 201 Response

```json
{
  "data": {
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    },
    "cooldown": {
      "shipSymbol": "string",
      "totalSeconds": 0,
      "remainingSeconds": 0,
      "expiration": "2019-08-24T14:15:22Z"
    },
    "produced": [
      {
        "tradeSymbol": "string",
        "units": 0
      }
    ],
    "consumed": [
      {
        "tradeSymbol": "string",
        "units": 0
      }
    ]
  }
}
```

<h3 id="ship-refine-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|The ship has successfully refined goods.|Inline|

<h3 id="ship-refine-responseschema">Response Schema</h3>

Status Code **201**

*Ship Refine 201 Response*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|
|»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»» produced|[object]|true|none|Goods that were produced by this refining process.|
|»»» tradeSymbol|string|true|none|Symbol of the good.|
|»»» units|integer|true|none|Amount of units of the good.|
|»» consumed|[object]|true|none|Goods that were consumed during this refining process.|
|»»» tradeSymbol|string|true|none|Symbol of the good.|
|»»» units|integer|true|none|Amount of units of the good.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## create-chart

<a id="opIdcreate-chart"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/chart', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/chart`

*Create Chart*

Command a ship to chart the waypoint at its current location.

Most waypoints in the universe are uncharted by default. These waypoints have their traits hidden until they have been charted by a ship.

Charting a waypoint will record your agent as the one who created the chart, and all other agents would also be able to see the waypoint's traits.

<h3 id="create-chart-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The symbol of the ship.|

> Example responses

> 201 Response

```json
{
  "data": {
    "chart": {
      "waypointSymbol": "string",
      "submittedBy": "string",
      "submittedOn": "2019-08-24T14:15:22Z"
    },
    "waypoint": {
      "symbol": "string",
      "type": "PLANET",
      "systemSymbol": "string",
      "x": 0,
      "y": 0,
      "orbitals": [
        {
          "symbol": "string"
        }
      ],
      "orbits": "string",
      "faction": {
        "symbol": "COSMIC"
      },
      "traits": [
        {
          "symbol": "UNCHARTED",
          "name": "string",
          "description": "string"
        }
      ],
      "modifiers": [
        {
          "symbol": "STRIPPED",
          "name": "string",
          "description": "string"
        }
      ],
      "chart": {
        "waypointSymbol": "string",
        "submittedBy": "string",
        "submittedOn": "2019-08-24T14:15:22Z"
      },
      "isUnderConstruction": true
    }
  }
}
```

<h3 id="create-chart-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|Inline|

<h3 id="create-chart-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» chart|[Chart](#schemachart)|true|none|The chart of a system or waypoint, which makes the location visible to other agents.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|false|none|The symbol of the waypoint.|
|»»» submittedBy|string|false|none|The agent that submitted the chart for this waypoint.|
|»»» submittedOn|string(date-time)|false|none|The time the chart for this waypoint was submitted.|
|»» waypoint|[Waypoint](#schemawaypoint)|true|none|A waypoint is a location that ships can travel to such as a Planet, Moon or Space Station.|
|»»» symbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»» x|integer|true|none|Relative position of the waypoint on the system's x axis. This is not an absolute position in the universe.|
|»»» y|integer|true|none|Relative position of the waypoint on the system's y axis. This is not an absolute position in the universe.|
|»»» orbitals|[[WaypointOrbital](#schemawaypointorbital)]|true|none|Waypoints that orbit this waypoint.|
|»»»» symbol|string|true|none|The symbol of the orbiting waypoint.|
|»»» orbits|string|false|none|The symbol of the parent waypoint, if this waypoint is in orbit around another waypoint. Otherwise this value is undefined.|
|»»» faction|[WaypointFaction](#schemawaypointfaction)|false|none|The faction that controls the waypoint.|
|»»»» symbol|[FactionSymbol](#schemafactionsymbol)|true|none|The symbol of the faction.|
|»»» traits|[[WaypointTrait](#schemawaypointtrait)]|true|none|The traits of the waypoint.|
|»»»» symbol|[WaypointTraitSymbol](#schemawaypointtraitsymbol)|true|none|The unique identifier of the trait.|
|»»»» name|string|true|none|The name of the trait.|
|»»»» description|string|true|none|A description of the trait.|
|»»» modifiers|[[WaypointModifier](#schemawaypointmodifier)]|false|none|The modifiers of the waypoint.|
|»»»» symbol|[WaypointModifierSymbol](#schemawaypointmodifiersymbol)|true|none|The unique identifier of the modifier.|
|»»»» name|string|true|none|The name of the trait.|
|»»»» description|string|true|none|A description of the trait.|
|»»» chart|[Chart](#schemachart)|false|none|The chart of a system or waypoint, which makes the location visible to other agents.|
|»»» isUnderConstruction|boolean|true|none|True if the waypoint is under construction.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|symbol|COSMIC|
|symbol|VOID|
|symbol|GALACTIC|
|symbol|QUANTUM|
|symbol|DOMINION|
|symbol|ASTRO|
|symbol|CORSAIRS|
|symbol|OBSIDIAN|
|symbol|AEGIS|
|symbol|UNITED|
|symbol|SOLITARY|
|symbol|COBALT|
|symbol|OMEGA|
|symbol|ECHO|
|symbol|LORDS|
|symbol|CULT|
|symbol|ANCIENTS|
|symbol|SHADOW|
|symbol|ETHEREAL|
|symbol|UNCHARTED|
|symbol|UNDER_CONSTRUCTION|
|symbol|MARKETPLACE|
|symbol|SHIPYARD|
|symbol|OUTPOST|
|symbol|SCATTERED_SETTLEMENTS|
|symbol|SPRAWLING_CITIES|
|symbol|MEGA_STRUCTURES|
|symbol|PIRATE_BASE|
|symbol|OVERCROWDED|
|symbol|HIGH_TECH|
|symbol|CORRUPT|
|symbol|BUREAUCRATIC|
|symbol|TRADING_HUB|
|symbol|INDUSTRIAL|
|symbol|BLACK_MARKET|
|symbol|RESEARCH_FACILITY|
|symbol|MILITARY_BASE|
|symbol|SURVEILLANCE_OUTPOST|
|symbol|EXPLORATION_OUTPOST|
|symbol|MINERAL_DEPOSITS|
|symbol|COMMON_METAL_DEPOSITS|
|symbol|PRECIOUS_METAL_DEPOSITS|
|symbol|RARE_METAL_DEPOSITS|
|symbol|METHANE_POOLS|
|symbol|ICE_CRYSTALS|
|symbol|EXPLOSIVE_GASES|
|symbol|STRONG_MAGNETOSPHERE|
|symbol|VIBRANT_AURORAS|
|symbol|SALT_FLATS|
|symbol|CANYONS|
|symbol|PERPETUAL_DAYLIGHT|
|symbol|PERPETUAL_OVERCAST|
|symbol|DRY_SEABEDS|
|symbol|MAGMA_SEAS|
|symbol|SUPERVOLCANOES|
|symbol|ASH_CLOUDS|
|symbol|VAST_RUINS|
|symbol|MUTATED_FLORA|
|symbol|TERRAFORMED|
|symbol|EXTREME_TEMPERATURES|
|symbol|EXTREME_PRESSURE|
|symbol|DIVERSE_LIFE|
|symbol|SCARCE_LIFE|
|symbol|FOSSILS|
|symbol|WEAK_GRAVITY|
|symbol|STRONG_GRAVITY|
|symbol|CRUSHING_GRAVITY|
|symbol|TOXIC_ATMOSPHERE|
|symbol|CORROSIVE_ATMOSPHERE|
|symbol|BREATHABLE_ATMOSPHERE|
|symbol|THIN_ATMOSPHERE|
|symbol|JOVIAN|
|symbol|ROCKY|
|symbol|VOLCANIC|
|symbol|FROZEN|
|symbol|SWAMP|
|symbol|BARREN|
|symbol|TEMPERATE|
|symbol|JUNGLE|
|symbol|OCEAN|
|symbol|RADIOACTIVE|
|symbol|MICRO_GRAVITY_ANOMALIES|
|symbol|DEBRIS_CLUSTER|
|symbol|DEEP_CRATERS|
|symbol|SHALLOW_CRATERS|
|symbol|UNSTABLE_COMPOSITION|
|symbol|HOLLOWED_INTERIOR|
|symbol|STRIPPED|
|symbol|STRIPPED|
|symbol|UNSTABLE|
|symbol|RADIATION_LEAK|
|symbol|CRITICAL_LIMIT|
|symbol|CIVIL_UNREST|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## get-ship-cooldown

<a id="opIdget-ship-cooldown"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/cooldown', headers = headers)

print(r.json())

```

`GET /my/ships/{shipSymbol}/cooldown`

*Get Ship Cooldown*

Retrieve the details of your ship's reactor cooldown. Some actions such as activating your jump drive, scanning, or extracting resources taxes your reactor and results in a cooldown.

Your ship cannot perform additional actions until your cooldown has expired. The duration of your cooldown is relative to the power consumption of the related modules or mounts for the action taken.

Response returns a 204 status code (no-content) when the ship has no cooldown.

<h3 id="get-ship-cooldown-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The symbol of the ship.|

> Example responses

> 200 Response

```json
{
  "data": {
    "shipSymbol": "string",
    "totalSeconds": 0,
    "remainingSeconds": 0,
    "expiration": "2019-08-24T14:15:22Z"
  }
}
```

<h3 id="get-ship-cooldown-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Succesfully fetched ship's cooldown.|Inline|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No cooldown.|None|

<h3 id="get-ship-cooldown-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## dock-ship

<a id="opIddock-ship"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/dock', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/dock`

*Dock Ship*

Attempt to dock your ship at its current location. Docking will only succeed if your ship is capable of docking at the time of the request.

Docked ships can access elements in their current location, such as the market or a shipyard, but cannot do actions that require the ship to be above surface such as navigating or extracting.

The endpoint is idempotent - successive calls will succeed even if the ship is already docked.

<h3 id="dock-ship-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The symbol of the ship.|

> Example responses

> 200 Response

```json
{
  "data": {
    "nav": {
      "systemSymbol": "string",
      "waypointSymbol": "string",
      "route": {
        "destination": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0
        },
        "origin": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0
        },
        "departureTime": "2019-08-24T14:15:22Z",
        "arrival": "2019-08-24T14:15:22Z"
      },
      "status": "IN_TRANSIT",
      "flightMode": "DRIFT"
    }
  }
}
```

<h3 id="dock-ship-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The ship has successfully docked at its current location.|Inline|

<h3 id="dock-ship-responseschema">Response Schema</h3>

Status Code **200**

*Dock Ship 200 Response*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## create-survey

<a id="opIdcreate-survey"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/survey', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/survey`

*Create Survey*

Create surveys on a waypoint that can be extracted such as asteroid fields. A survey focuses on specific types of deposits from the extracted location. When ships extract using this survey, they are guaranteed to procure a high amount of one of the goods in the survey.

In order to use a survey, send the entire survey details in the body of the extract request.

Each survey may have multiple deposits, and if a symbol shows up more than once, that indicates a higher chance of extracting that resource.

Your ship will enter a cooldown after surveying in which it is unable to perform certain actions. Surveys will eventually expire after a period of time or will be exhausted after being extracted several times based on the survey's size. Multiple ships can use the same survey for extraction.

A ship must have the `Surveyor` mount installed in order to use this function.

<h3 id="create-survey-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The symbol of the ship.|

> Example responses

> 201 Response

```json
{
  "data": {
    "cooldown": {
      "shipSymbol": "string",
      "totalSeconds": 0,
      "remainingSeconds": 0,
      "expiration": "2019-08-24T14:15:22Z"
    },
    "surveys": [
      {
        "signature": "string",
        "symbol": "string",
        "deposits": [
          {
            "symbol": "string"
          }
        ],
        "expiration": "2019-08-24T14:15:22Z",
        "size": "SMALL"
      }
    ]
  }
}
```

<h3 id="create-survey-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Surveys has been created.|Inline|

<h3 id="create-survey-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»» surveys|[[Survey](#schemasurvey)]|true|none|Surveys created by this action.|
|»»» signature|string|true|none|A unique signature for the location of this survey. This signature is verified when attempting an extraction using this survey.|
|»»» symbol|string|true|none|The symbol of the waypoint that this survey is for.|
|»»» deposits|[[SurveyDeposit](#schemasurveydeposit)]|true|none|A list of deposits that can be found at this location. A ship will extract one of these deposits when using this survey in an extraction request. If multiple deposits of the same type are present, the chance of extracting that deposit is increased.|
|»»»» symbol|string|true|none|The symbol of the deposit.|
|»»» expiration|string(date-time)|true|none|The date and time when the survey expires. After this date and time, the survey will no longer be available for extraction.|
|»»» size|string|true|none|The size of the deposit. This value indicates how much can be extracted from the survey before it is exhausted.|

#### Enumerated Values

|Property|Value|
|---|---|
|size|SMALL|
|size|MODERATE|
|size|LARGE|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## extract-resources

<a id="opIdextract-resources"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/extract', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/extract`

*Extract Resources*

Extract resources from a waypoint that can be extracted, such as asteroid fields, into your ship. Send an optional survey as the payload to target specific yields.

The ship must be in orbit to be able to extract and must have mining equipments installed that can extract goods, such as the `Gas Siphon` mount for gas-based goods or `Mining Laser` mount for ore-based goods.

The survey property is now deprecated. See the `extract/survey` endpoint for more details.

> Body parameter

```json
{
  "survey": {
    "signature": "string",
    "symbol": "string",
    "deposits": [
      {
        "symbol": "string"
      }
    ],
    "expiration": "2019-08-24T14:15:22Z",
    "size": "SMALL"
  }
}
```

<h3 id="extract-resources-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» survey|body|[Survey](#schemasurvey)|false|A resource survey of a waypoint, detailing a specific extraction location and the types of resources that can be found there.|
|»» signature|body|string|true|A unique signature for the location of this survey. This signature is verified when attempting an extraction using this survey.|
|»» symbol|body|string|true|The symbol of the waypoint that this survey is for.|
|»» deposits|body|[[SurveyDeposit](#schemasurveydeposit)]|true|A list of deposits that can be found at this location. A ship will extract one of these deposits when using this survey in an extraction request. If multiple deposits of the same type are present, the chance of extracting that deposit is increased.|
|»»» symbol|body|string|true|The symbol of the deposit.|
|»» expiration|body|string(date-time)|true|The date and time when the survey expires. After this date and time, the survey will no longer be available for extraction.|
|»» size|body|string|true|The size of the deposit. This value indicates how much can be extracted from the survey before it is exhausted.|
|shipSymbol|path|string|true|The ship symbol.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|»» size|SMALL|
|»» size|MODERATE|
|»» size|LARGE|

> Example responses

> 201 Response

```json
{
  "data": {
    "cooldown": {
      "shipSymbol": "string",
      "totalSeconds": 0,
      "remainingSeconds": 0,
      "expiration": "2019-08-24T14:15:22Z"
    },
    "extraction": {
      "shipSymbol": "string",
      "yield": {
        "symbol": "PRECIOUS_STONES",
        "units": 0
      }
    },
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    },
    "events": [
      {
        "symbol": "REACTOR_OVERLOAD",
        "component": "FRAME",
        "name": "string",
        "description": "string"
      }
    ]
  }
}
```

<h3 id="extract-resources-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Extracted successfully.|Inline|

<h3 id="extract-resources-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»» extraction|[Extraction](#schemaextraction)|true|none|Extraction details.|
|»»» shipSymbol|string|true|none|Symbol of the ship that executed the extraction.|
|»»» yield|[ExtractionYield](#schemaextractionyield)|true|none|A yield from the extraction operation.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» units|integer|true|none|The number of units extracted that were placed into the ship's cargo hold.|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|
|»» events|[oneOf]|true|none|none|
|»»» symbol|string|true|none|none|
|»»» component|string|true|none|none|
|»»» name|string|true|none|The name of the event.|
|»»» description|string|true|none|A description of the event.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|
|symbol|REACTOR_OVERLOAD|
|symbol|ENERGY_SPIKE_FROM_MINERAL|
|symbol|SOLAR_FLARE_INTERFERENCE|
|symbol|COOLANT_LEAK|
|symbol|POWER_DISTRIBUTION_FLUCTUATION|
|symbol|MAGNETIC_FIELD_DISRUPTION|
|symbol|HULL_MICROMETEORITE_STRIKES|
|symbol|STRUCTURAL_STRESS_FRACTURES|
|symbol|CORROSIVE_MINERAL_CONTAMINATION|
|symbol|THERMAL_EXPANSION_MISMATCH|
|symbol|VIBRATION_DAMAGE_FROM_DRILLING|
|symbol|ELECTROMAGNETIC_FIELD_INTERFERENCE|
|symbol|IMPACT_WITH_EXTRACTED_DEBRIS|
|symbol|FUEL_EFFICIENCY_DEGRADATION|
|symbol|COOLANT_SYSTEM_AGEING|
|symbol|DUST_MICROABRASIONS|
|symbol|THRUSTER_NOZZLE_WEAR|
|symbol|EXHAUST_PORT_CLOGGING|
|symbol|BEARING_LUBRICATION_FADE|
|symbol|SENSOR_CALIBRATION_DRIFT|
|symbol|HULL_MICROMETEORITE_DAMAGE|
|symbol|SPACE_DEBRIS_COLLISION|
|symbol|THERMAL_STRESS|
|symbol|VIBRATION_OVERLOAD|
|symbol|PRESSURE_DIFFERENTIAL_STRESS|
|symbol|ELECTROMAGNETIC_SURGE_EFFECTS|
|symbol|ATMOSPHERIC_ENTRY_HEAT|
|component|FRAME|
|component|REACTOR|
|component|ENGINE|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## siphon-resources

<a id="opIdsiphon-resources"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/siphon', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/siphon`

*Siphon Resources*

Siphon gases, such as hydrocarbon, from gas giants.

The ship must be in orbit to be able to siphon and must have siphon mounts and a gas processor installed.

<h3 id="siphon-resources-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 201 Response

```json
{
  "data": {
    "cooldown": {
      "shipSymbol": "string",
      "totalSeconds": 0,
      "remainingSeconds": 0,
      "expiration": "2019-08-24T14:15:22Z"
    },
    "siphon": {
      "shipSymbol": "string",
      "yield": {
        "symbol": "PRECIOUS_STONES",
        "units": 0
      }
    },
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    },
    "events": [
      {
        "symbol": "REACTOR_OVERLOAD",
        "component": "FRAME",
        "name": "string",
        "description": "string"
      }
    ]
  }
}
```

<h3 id="siphon-resources-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Siphon successful.|Inline|

<h3 id="siphon-resources-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»» siphon|[Siphon](#schemasiphon)|true|none|Siphon details.|
|»»» shipSymbol|string|true|none|Symbol of the ship that executed the siphon.|
|»»» yield|[SiphonYield](#schemasiphonyield)|true|none|A yield from the siphon operation.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» units|integer|true|none|The number of units siphoned that were placed into the ship's cargo hold.|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|
|»» events|[oneOf]|true|none|none|
|»»» symbol|string|true|none|none|
|»»» component|string|true|none|none|
|»»» name|string|true|none|The name of the event.|
|»»» description|string|true|none|A description of the event.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|
|symbol|REACTOR_OVERLOAD|
|symbol|ENERGY_SPIKE_FROM_MINERAL|
|symbol|SOLAR_FLARE_INTERFERENCE|
|symbol|COOLANT_LEAK|
|symbol|POWER_DISTRIBUTION_FLUCTUATION|
|symbol|MAGNETIC_FIELD_DISRUPTION|
|symbol|HULL_MICROMETEORITE_STRIKES|
|symbol|STRUCTURAL_STRESS_FRACTURES|
|symbol|CORROSIVE_MINERAL_CONTAMINATION|
|symbol|THERMAL_EXPANSION_MISMATCH|
|symbol|VIBRATION_DAMAGE_FROM_DRILLING|
|symbol|ELECTROMAGNETIC_FIELD_INTERFERENCE|
|symbol|IMPACT_WITH_EXTRACTED_DEBRIS|
|symbol|FUEL_EFFICIENCY_DEGRADATION|
|symbol|COOLANT_SYSTEM_AGEING|
|symbol|DUST_MICROABRASIONS|
|symbol|THRUSTER_NOZZLE_WEAR|
|symbol|EXHAUST_PORT_CLOGGING|
|symbol|BEARING_LUBRICATION_FADE|
|symbol|SENSOR_CALIBRATION_DRIFT|
|symbol|HULL_MICROMETEORITE_DAMAGE|
|symbol|SPACE_DEBRIS_COLLISION|
|symbol|THERMAL_STRESS|
|symbol|VIBRATION_OVERLOAD|
|symbol|PRESSURE_DIFFERENTIAL_STRESS|
|symbol|ELECTROMAGNETIC_SURGE_EFFECTS|
|symbol|ATMOSPHERIC_ENTRY_HEAT|
|component|FRAME|
|component|REACTOR|
|component|ENGINE|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## extract-resources-with-survey

<a id="opIdextract-resources-with-survey"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/extract/survey', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/extract/survey`

*Extract Resources with Survey*

Use a survey when extracting resources from a waypoint. This endpoint requires a survey as the payload, which allows your ship to extract specific yields.

Send the full survey object as the payload which will be validated according to the signature. If the signature is invalid, or any properties of the survey are changed, the request will fail.

> Body parameter

```json
{
  "signature": "string",
  "symbol": "string",
  "deposits": [
    {
      "symbol": "string"
    }
  ],
  "expiration": "2019-08-24T14:15:22Z",
  "size": "SMALL"
}
```

<h3 id="extract-resources-with-survey-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Survey](#schemasurvey)|false|none|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 201 Response

```json
{
  "data": {
    "cooldown": {
      "shipSymbol": "string",
      "totalSeconds": 0,
      "remainingSeconds": 0,
      "expiration": "2019-08-24T14:15:22Z"
    },
    "extraction": {
      "shipSymbol": "string",
      "yield": {
        "symbol": "PRECIOUS_STONES",
        "units": 0
      }
    },
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    },
    "events": [
      {
        "symbol": "REACTOR_OVERLOAD",
        "component": "FRAME",
        "name": "string",
        "description": "string"
      }
    ]
  }
}
```

<h3 id="extract-resources-with-survey-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Extracted successfully.|Inline|

<h3 id="extract-resources-with-survey-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»» extraction|[Extraction](#schemaextraction)|true|none|Extraction details.|
|»»» shipSymbol|string|true|none|Symbol of the ship that executed the extraction.|
|»»» yield|[ExtractionYield](#schemaextractionyield)|true|none|A yield from the extraction operation.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» units|integer|true|none|The number of units extracted that were placed into the ship's cargo hold.|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|
|»» events|[oneOf]|true|none|none|
|»»» symbol|string|true|none|none|
|»»» component|string|true|none|none|
|»»» name|string|true|none|The name of the event.|
|»»» description|string|true|none|A description of the event.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|
|symbol|REACTOR_OVERLOAD|
|symbol|ENERGY_SPIKE_FROM_MINERAL|
|symbol|SOLAR_FLARE_INTERFERENCE|
|symbol|COOLANT_LEAK|
|symbol|POWER_DISTRIBUTION_FLUCTUATION|
|symbol|MAGNETIC_FIELD_DISRUPTION|
|symbol|HULL_MICROMETEORITE_STRIKES|
|symbol|STRUCTURAL_STRESS_FRACTURES|
|symbol|CORROSIVE_MINERAL_CONTAMINATION|
|symbol|THERMAL_EXPANSION_MISMATCH|
|symbol|VIBRATION_DAMAGE_FROM_DRILLING|
|symbol|ELECTROMAGNETIC_FIELD_INTERFERENCE|
|symbol|IMPACT_WITH_EXTRACTED_DEBRIS|
|symbol|FUEL_EFFICIENCY_DEGRADATION|
|symbol|COOLANT_SYSTEM_AGEING|
|symbol|DUST_MICROABRASIONS|
|symbol|THRUSTER_NOZZLE_WEAR|
|symbol|EXHAUST_PORT_CLOGGING|
|symbol|BEARING_LUBRICATION_FADE|
|symbol|SENSOR_CALIBRATION_DRIFT|
|symbol|HULL_MICROMETEORITE_DAMAGE|
|symbol|SPACE_DEBRIS_COLLISION|
|symbol|THERMAL_STRESS|
|symbol|VIBRATION_OVERLOAD|
|symbol|PRESSURE_DIFFERENTIAL_STRESS|
|symbol|ELECTROMAGNETIC_SURGE_EFFECTS|
|symbol|ATMOSPHERIC_ENTRY_HEAT|
|component|FRAME|
|component|REACTOR|
|component|ENGINE|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## jettison

<a id="opIdjettison"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/jettison', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/jettison`

*Jettison Cargo*

Jettison cargo from your ship's cargo hold.

> Body parameter

```json
{
  "symbol": "PRECIOUS_STONES",
  "units": 1
}
```

<h3 id="jettison-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» symbol|body|[TradeSymbol](#schematradesymbol)|true|The good's symbol.|
|» units|body|integer|true|Amount of units to jettison of this good.|
|shipSymbol|path|string|true|The ship symbol.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» symbol|PRECIOUS_STONES|
|» symbol|QUARTZ_SAND|
|» symbol|SILICON_CRYSTALS|
|» symbol|AMMONIA_ICE|
|» symbol|LIQUID_HYDROGEN|
|» symbol|LIQUID_NITROGEN|
|» symbol|ICE_WATER|
|» symbol|EXOTIC_MATTER|
|» symbol|ADVANCED_CIRCUITRY|
|» symbol|GRAVITON_EMITTERS|
|» symbol|IRON|
|» symbol|IRON_ORE|
|» symbol|COPPER|
|» symbol|COPPER_ORE|
|» symbol|ALUMINUM|
|» symbol|ALUMINUM_ORE|
|» symbol|SILVER|
|» symbol|SILVER_ORE|
|» symbol|GOLD|
|» symbol|GOLD_ORE|
|» symbol|PLATINUM|
|» symbol|PLATINUM_ORE|
|» symbol|DIAMONDS|
|» symbol|URANITE|
|» symbol|URANITE_ORE|
|» symbol|MERITIUM|
|» symbol|MERITIUM_ORE|
|» symbol|HYDROCARBON|
|» symbol|ANTIMATTER|
|» symbol|FAB_MATS|
|» symbol|FERTILIZERS|
|» symbol|FABRICS|
|» symbol|FOOD|
|» symbol|JEWELRY|
|» symbol|MACHINERY|
|» symbol|FIREARMS|
|» symbol|ASSAULT_RIFLES|
|» symbol|MILITARY_EQUIPMENT|
|» symbol|EXPLOSIVES|
|» symbol|LAB_INSTRUMENTS|
|» symbol|AMMUNITION|
|» symbol|ELECTRONICS|
|» symbol|SHIP_PLATING|
|» symbol|SHIP_PARTS|
|» symbol|EQUIPMENT|
|» symbol|FUEL|
|» symbol|MEDICINE|
|» symbol|DRUGS|
|» symbol|CLOTHING|
|» symbol|MICROPROCESSORS|
|» symbol|PLASTICS|
|» symbol|POLYNUCLEOTIDES|
|» symbol|BIOCOMPOSITES|
|» symbol|QUANTUM_STABILIZERS|
|» symbol|NANOBOTS|
|» symbol|AI_MAINFRAMES|
|» symbol|QUANTUM_DRIVES|
|» symbol|ROBOTIC_DRONES|
|» symbol|CYBER_IMPLANTS|
|» symbol|GENE_THERAPEUTICS|
|» symbol|NEURAL_CHIPS|
|» symbol|MOOD_REGULATORS|
|» symbol|VIRAL_AGENTS|
|» symbol|MICRO_FUSION_GENERATORS|
|» symbol|SUPERGRAINS|
|» symbol|LASER_RIFLES|
|» symbol|HOLOGRAPHICS|
|» symbol|SHIP_SALVAGE|
|» symbol|RELIC_TECH|
|» symbol|NOVEL_LIFEFORMS|
|» symbol|BOTANICAL_SPECIMENS|
|» symbol|CULTURAL_ARTIFACTS|
|» symbol|FRAME_PROBE|
|» symbol|FRAME_DRONE|
|» symbol|FRAME_INTERCEPTOR|
|» symbol|FRAME_RACER|
|» symbol|FRAME_FIGHTER|
|» symbol|FRAME_FRIGATE|
|» symbol|FRAME_SHUTTLE|
|» symbol|FRAME_EXPLORER|
|» symbol|FRAME_MINER|
|» symbol|FRAME_LIGHT_FREIGHTER|
|» symbol|FRAME_HEAVY_FREIGHTER|
|» symbol|FRAME_TRANSPORT|
|» symbol|FRAME_DESTROYER|
|» symbol|FRAME_CRUISER|
|» symbol|FRAME_CARRIER|
|» symbol|REACTOR_SOLAR_I|
|» symbol|REACTOR_FUSION_I|
|» symbol|REACTOR_FISSION_I|
|» symbol|REACTOR_CHEMICAL_I|
|» symbol|REACTOR_ANTIMATTER_I|
|» symbol|ENGINE_IMPULSE_DRIVE_I|
|» symbol|ENGINE_ION_DRIVE_I|
|» symbol|ENGINE_ION_DRIVE_II|
|» symbol|ENGINE_HYPER_DRIVE_I|
|» symbol|MODULE_MINERAL_PROCESSOR_I|
|» symbol|MODULE_GAS_PROCESSOR_I|
|» symbol|MODULE_CARGO_HOLD_I|
|» symbol|MODULE_CARGO_HOLD_II|
|» symbol|MODULE_CARGO_HOLD_III|
|» symbol|MODULE_CREW_QUARTERS_I|
|» symbol|MODULE_ENVOY_QUARTERS_I|
|» symbol|MODULE_PASSENGER_CABIN_I|
|» symbol|MODULE_MICRO_REFINERY_I|
|» symbol|MODULE_SCIENCE_LAB_I|
|» symbol|MODULE_JUMP_DRIVE_I|
|» symbol|MODULE_JUMP_DRIVE_II|
|» symbol|MODULE_JUMP_DRIVE_III|
|» symbol|MODULE_WARP_DRIVE_I|
|» symbol|MODULE_WARP_DRIVE_II|
|» symbol|MODULE_WARP_DRIVE_III|
|» symbol|MODULE_SHIELD_GENERATOR_I|
|» symbol|MODULE_SHIELD_GENERATOR_II|
|» symbol|MODULE_ORE_REFINERY_I|
|» symbol|MODULE_FUEL_REFINERY_I|
|» symbol|MOUNT_GAS_SIPHON_I|
|» symbol|MOUNT_GAS_SIPHON_II|
|» symbol|MOUNT_GAS_SIPHON_III|
|» symbol|MOUNT_SURVEYOR_I|
|» symbol|MOUNT_SURVEYOR_II|
|» symbol|MOUNT_SURVEYOR_III|
|» symbol|MOUNT_SENSOR_ARRAY_I|
|» symbol|MOUNT_SENSOR_ARRAY_II|
|» symbol|MOUNT_SENSOR_ARRAY_III|
|» symbol|MOUNT_MINING_LASER_I|
|» symbol|MOUNT_MINING_LASER_II|
|» symbol|MOUNT_MINING_LASER_III|
|» symbol|MOUNT_LASER_CANNON_I|
|» symbol|MOUNT_MISSILE_LAUNCHER_I|
|» symbol|MOUNT_TURRET_I|
|» symbol|SHIP_PROBE|
|» symbol|SHIP_MINING_DRONE|
|» symbol|SHIP_SIPHON_DRONE|
|» symbol|SHIP_INTERCEPTOR|
|» symbol|SHIP_LIGHT_HAULER|
|» symbol|SHIP_COMMAND_FRIGATE|
|» symbol|SHIP_EXPLORER|
|» symbol|SHIP_HEAVY_FREIGHTER|
|» symbol|SHIP_LIGHT_SHUTTLE|
|» symbol|SHIP_ORE_HOUND|
|» symbol|SHIP_REFINING_FREIGHTER|
|» symbol|SHIP_SURVEYOR|

> Example responses

> 200 Response

```json
{
  "data": {
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    }
  }
}
```

<h3 id="jettison-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Jettison successful.|Inline|

<h3 id="jettison-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## jump-ship

<a id="opIdjump-ship"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/jump', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/jump`

*Jump Ship*

Jump your ship instantly to a target connected waypoint. The ship must be in orbit to execute a jump.

A unit of antimatter is purchased and consumed from the market when jumping. The price of antimatter is determined by the market and is subject to change. A ship can only jump to connected waypoints

> Body parameter

```json
{
  "waypointSymbol": "string"
}
```

<h3 id="jump-ship-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» waypointSymbol|body|string|true|The symbol of the waypoint to jump to. The destination must be a connected waypoint.|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 200 Response

```json
{
  "data": {
    "nav": {
      "systemSymbol": "string",
      "waypointSymbol": "string",
      "route": {
        "destination": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0
        },
        "origin": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0
        },
        "departureTime": "2019-08-24T14:15:22Z",
        "arrival": "2019-08-24T14:15:22Z"
      },
      "status": "IN_TRANSIT",
      "flightMode": "DRIFT"
    },
    "cooldown": {
      "shipSymbol": "string",
      "totalSeconds": 0,
      "remainingSeconds": 0,
      "expiration": "2019-08-24T14:15:22Z"
    },
    "transaction": {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "tradeSymbol": "string",
      "type": "PURCHASE",
      "units": 0,
      "pricePerUnit": 0,
      "totalPrice": 0,
      "timestamp": "2019-08-24T14:15:22Z"
    },
    "agent": {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    }
  }
}
```

<h3 id="jump-ship-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Jump successful.|Inline|

<h3 id="jump-ship-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|
|»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»» transaction|[MarketTransaction](#schemamarkettransaction)|true|none|Result of a transaction with a market.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» shipSymbol|string|true|none|The symbol of the ship that made the transaction.|
|»»» tradeSymbol|string|true|none|The symbol of the trade good.|
|»»» type|string|true|none|The type of transaction.|
|»»» units|integer|true|none|The number of units of the transaction.|
|»»» pricePerUnit|integer|true|none|The price per unit of the transaction.|
|»»» totalPrice|integer|true|none|The total price of the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|
|»» agent|[Agent](#schemaagent)|true|none|Agent details.|
|»»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»»» symbol|string|true|none|Symbol of the agent.|
|»»» headquarters|string|true|none|The headquarters of the agent.|
|»»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»»» startingFaction|string|true|none|The faction the agent started with.|
|»»» shipCount|integer|true|none|How many ships are owned by the agent.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|
|type|PURCHASE|
|type|SELL|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## navigate-ship

<a id="opIdnavigate-ship"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/navigate', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/navigate`

*Navigate Ship*

Navigate to a target destination. The ship must be in orbit to use this function. The destination waypoint must be within the same system as the ship's current location. Navigating will consume the necessary fuel from the ship's manifest based on the distance to the target waypoint.

The returned response will detail the route information including the expected time of arrival. Most ship actions are unavailable until the ship has arrived at it's destination.

To travel between systems, see the ship's Warp or Jump actions.

> Body parameter

```json
{
  "waypointSymbol": "string"
}
```

<h3 id="navigate-ship-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» waypointSymbol|body|string|true|The target destination.|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 200 Response

```json
{
  "data": {
    "fuel": {
      "current": 0,
      "capacity": 0,
      "consumed": {
        "amount": 0,
        "timestamp": "2019-08-24T14:15:22Z"
      }
    },
    "nav": {
      "systemSymbol": "string",
      "waypointSymbol": "string",
      "route": {
        "destination": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0
        },
        "origin": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0
        },
        "departureTime": "2019-08-24T14:15:22Z",
        "arrival": "2019-08-24T14:15:22Z"
      },
      "status": "IN_TRANSIT",
      "flightMode": "DRIFT"
    },
    "events": [
      {
        "symbol": "REACTOR_OVERLOAD",
        "component": "FRAME",
        "name": "string",
        "description": "string"
      }
    ]
  }
}
```

<h3 id="navigate-ship-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The successful transit information including the route details and changes to ship fuel. The route includes the expected time of arrival.|Inline|

<h3 id="navigate-ship-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» fuel|[ShipFuel](#schemashipfuel)|true|none|Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.|
|»»» current|integer|true|none|The current amount of fuel in the ship's tanks.|
|»»» capacity|integer|true|none|The maximum amount of fuel the ship's tanks can hold.|
|»»» consumed|object|false|none|An object that only shows up when an action has consumed fuel in the process. Shows the fuel consumption data.|
|»»»» amount|integer|true|none|The amount of fuel consumed by the most recent transit or action.|
|»»»» timestamp|string(date-time)|true|none|The time at which the fuel was consumed.|
|»» nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|
|»» events|[oneOf]|true|none|none|
|»»» symbol|string|true|none|none|
|»»» component|string|true|none|none|
|»»» name|string|true|none|The name of the event.|
|»»» description|string|true|none|A description of the event.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|
|symbol|REACTOR_OVERLOAD|
|symbol|ENERGY_SPIKE_FROM_MINERAL|
|symbol|SOLAR_FLARE_INTERFERENCE|
|symbol|COOLANT_LEAK|
|symbol|POWER_DISTRIBUTION_FLUCTUATION|
|symbol|MAGNETIC_FIELD_DISRUPTION|
|symbol|HULL_MICROMETEORITE_STRIKES|
|symbol|STRUCTURAL_STRESS_FRACTURES|
|symbol|CORROSIVE_MINERAL_CONTAMINATION|
|symbol|THERMAL_EXPANSION_MISMATCH|
|symbol|VIBRATION_DAMAGE_FROM_DRILLING|
|symbol|ELECTROMAGNETIC_FIELD_INTERFERENCE|
|symbol|IMPACT_WITH_EXTRACTED_DEBRIS|
|symbol|FUEL_EFFICIENCY_DEGRADATION|
|symbol|COOLANT_SYSTEM_AGEING|
|symbol|DUST_MICROABRASIONS|
|symbol|THRUSTER_NOZZLE_WEAR|
|symbol|EXHAUST_PORT_CLOGGING|
|symbol|BEARING_LUBRICATION_FADE|
|symbol|SENSOR_CALIBRATION_DRIFT|
|symbol|HULL_MICROMETEORITE_DAMAGE|
|symbol|SPACE_DEBRIS_COLLISION|
|symbol|THERMAL_STRESS|
|symbol|VIBRATION_OVERLOAD|
|symbol|PRESSURE_DIFFERENTIAL_STRESS|
|symbol|ELECTROMAGNETIC_SURGE_EFFECTS|
|symbol|ATMOSPHERIC_ENTRY_HEAT|
|component|FRAME|
|component|REACTOR|
|component|ENGINE|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## patch-ship-nav

<a id="opIdpatch-ship-nav"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.patch('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/nav', headers = headers)

print(r.json())

```

`PATCH /my/ships/{shipSymbol}/nav`

*Patch Ship Nav*

Update the nav configuration of a ship.

Currently only supports configuring the Flight Mode of the ship, which affects its speed and fuel consumption.

> Body parameter

```json
{
  "flightMode": "DRIFT"
}
```

<h3 id="patch-ship-nav-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» flightMode|body|[ShipNavFlightMode](#schemashipnavflightmode)|false|The ship's set speed when traveling between waypoints or systems.|
|shipSymbol|path|string|true|The ship symbol.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» flightMode|DRIFT|
|» flightMode|STEALTH|
|» flightMode|CRUISE|
|» flightMode|BURN|

> Example responses

> 200 Response

```json
{
  "data": {
    "systemSymbol": "string",
    "waypointSymbol": "string",
    "route": {
      "destination": {
        "symbol": "string",
        "type": "PLANET",
        "systemSymbol": "string",
        "x": 0,
        "y": 0
      },
      "origin": {
        "symbol": "string",
        "type": "PLANET",
        "systemSymbol": "string",
        "x": 0,
        "y": 0
      },
      "departureTime": "2019-08-24T14:15:22Z",
      "arrival": "2019-08-24T14:15:22Z"
    },
    "status": "IN_TRANSIT",
    "flightMode": "DRIFT"
  }
}
```

<h3 id="patch-ship-nav-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The updated nav data of the ship.|Inline|

<h3 id="patch-ship-nav-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## get-ship-nav

<a id="opIdget-ship-nav"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/nav', headers = headers)

print(r.json())

```

`GET /my/ships/{shipSymbol}/nav`

*Get Ship Nav*

Get the current nav status of a ship.

<h3 id="get-ship-nav-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 200 Response

```json
{
  "data": {
    "systemSymbol": "string",
    "waypointSymbol": "string",
    "route": {
      "destination": {
        "symbol": "string",
        "type": "PLANET",
        "systemSymbol": "string",
        "x": 0,
        "y": 0
      },
      "origin": {
        "symbol": "string",
        "type": "PLANET",
        "systemSymbol": "string",
        "x": 0,
        "y": 0
      },
      "departureTime": "2019-08-24T14:15:22Z",
      "arrival": "2019-08-24T14:15:22Z"
    },
    "status": "IN_TRANSIT",
    "flightMode": "DRIFT"
  }
}
```

<h3 id="get-ship-nav-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The current nav status of the ship.|Inline|

<h3 id="get-ship-nav-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## warp-ship

<a id="opIdwarp-ship"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/warp', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/warp`

*Warp Ship*

Warp your ship to a target destination in another system. The ship must be in orbit to use this function and must have the `Warp Drive` module installed. Warping will consume the necessary fuel from the ship's manifest.

The returned response will detail the route information including the expected time of arrival. Most ship actions are unavailable until the ship has arrived at its destination.

> Body parameter

```json
{
  "waypointSymbol": "string"
}
```

<h3 id="warp-ship-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» waypointSymbol|body|string|true|The target destination.|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 200 Response

```json
{
  "data": {
    "fuel": {
      "current": 0,
      "capacity": 0,
      "consumed": {
        "amount": 0,
        "timestamp": "2019-08-24T14:15:22Z"
      }
    },
    "nav": {
      "systemSymbol": "string",
      "waypointSymbol": "string",
      "route": {
        "destination": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0
        },
        "origin": {
          "symbol": "string",
          "type": "PLANET",
          "systemSymbol": "string",
          "x": 0,
          "y": 0
        },
        "departureTime": "2019-08-24T14:15:22Z",
        "arrival": "2019-08-24T14:15:22Z"
      },
      "status": "IN_TRANSIT",
      "flightMode": "DRIFT"
    }
  }
}
```

<h3 id="warp-ship-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|The successful transit information including the route details and changes to ship fuel. The route includes the expected time of arrival.|Inline|

<h3 id="warp-ship-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» fuel|[ShipFuel](#schemashipfuel)|true|none|Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.|
|»»» current|integer|true|none|The current amount of fuel in the ship's tanks.|
|»»» capacity|integer|true|none|The maximum amount of fuel the ship's tanks can hold.|
|»»» consumed|object|false|none|An object that only shows up when an action has consumed fuel in the process. Shows the fuel consumption data.|
|»»»» amount|integer|true|none|The amount of fuel consumed by the most recent transit or action.|
|»»»» timestamp|string(date-time)|true|none|The time at which the fuel was consumed.|
|»» nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## sell-cargo

<a id="opIdsell-cargo"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/sell', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/sell`

*Sell Cargo*

Sell cargo in your ship to a market that trades this cargo. The ship must be docked in a waypoint that has the `Marketplace` trait in order to use this function.

> Body parameter

```json
{
  "symbol": "PRECIOUS_STONES",
  "units": 0
}
```

<h3 id="sell-cargo-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» symbol|body|[TradeSymbol](#schematradesymbol)|true|The good's symbol.|
|» units|body|integer|true|Amounts of units to sell of the selected good.|
|shipSymbol|path|string|true|Symbol of a ship.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» symbol|PRECIOUS_STONES|
|» symbol|QUARTZ_SAND|
|» symbol|SILICON_CRYSTALS|
|» symbol|AMMONIA_ICE|
|» symbol|LIQUID_HYDROGEN|
|» symbol|LIQUID_NITROGEN|
|» symbol|ICE_WATER|
|» symbol|EXOTIC_MATTER|
|» symbol|ADVANCED_CIRCUITRY|
|» symbol|GRAVITON_EMITTERS|
|» symbol|IRON|
|» symbol|IRON_ORE|
|» symbol|COPPER|
|» symbol|COPPER_ORE|
|» symbol|ALUMINUM|
|» symbol|ALUMINUM_ORE|
|» symbol|SILVER|
|» symbol|SILVER_ORE|
|» symbol|GOLD|
|» symbol|GOLD_ORE|
|» symbol|PLATINUM|
|» symbol|PLATINUM_ORE|
|» symbol|DIAMONDS|
|» symbol|URANITE|
|» symbol|URANITE_ORE|
|» symbol|MERITIUM|
|» symbol|MERITIUM_ORE|
|» symbol|HYDROCARBON|
|» symbol|ANTIMATTER|
|» symbol|FAB_MATS|
|» symbol|FERTILIZERS|
|» symbol|FABRICS|
|» symbol|FOOD|
|» symbol|JEWELRY|
|» symbol|MACHINERY|
|» symbol|FIREARMS|
|» symbol|ASSAULT_RIFLES|
|» symbol|MILITARY_EQUIPMENT|
|» symbol|EXPLOSIVES|
|» symbol|LAB_INSTRUMENTS|
|» symbol|AMMUNITION|
|» symbol|ELECTRONICS|
|» symbol|SHIP_PLATING|
|» symbol|SHIP_PARTS|
|» symbol|EQUIPMENT|
|» symbol|FUEL|
|» symbol|MEDICINE|
|» symbol|DRUGS|
|» symbol|CLOTHING|
|» symbol|MICROPROCESSORS|
|» symbol|PLASTICS|
|» symbol|POLYNUCLEOTIDES|
|» symbol|BIOCOMPOSITES|
|» symbol|QUANTUM_STABILIZERS|
|» symbol|NANOBOTS|
|» symbol|AI_MAINFRAMES|
|» symbol|QUANTUM_DRIVES|
|» symbol|ROBOTIC_DRONES|
|» symbol|CYBER_IMPLANTS|
|» symbol|GENE_THERAPEUTICS|
|» symbol|NEURAL_CHIPS|
|» symbol|MOOD_REGULATORS|
|» symbol|VIRAL_AGENTS|
|» symbol|MICRO_FUSION_GENERATORS|
|» symbol|SUPERGRAINS|
|» symbol|LASER_RIFLES|
|» symbol|HOLOGRAPHICS|
|» symbol|SHIP_SALVAGE|
|» symbol|RELIC_TECH|
|» symbol|NOVEL_LIFEFORMS|
|» symbol|BOTANICAL_SPECIMENS|
|» symbol|CULTURAL_ARTIFACTS|
|» symbol|FRAME_PROBE|
|» symbol|FRAME_DRONE|
|» symbol|FRAME_INTERCEPTOR|
|» symbol|FRAME_RACER|
|» symbol|FRAME_FIGHTER|
|» symbol|FRAME_FRIGATE|
|» symbol|FRAME_SHUTTLE|
|» symbol|FRAME_EXPLORER|
|» symbol|FRAME_MINER|
|» symbol|FRAME_LIGHT_FREIGHTER|
|» symbol|FRAME_HEAVY_FREIGHTER|
|» symbol|FRAME_TRANSPORT|
|» symbol|FRAME_DESTROYER|
|» symbol|FRAME_CRUISER|
|» symbol|FRAME_CARRIER|
|» symbol|REACTOR_SOLAR_I|
|» symbol|REACTOR_FUSION_I|
|» symbol|REACTOR_FISSION_I|
|» symbol|REACTOR_CHEMICAL_I|
|» symbol|REACTOR_ANTIMATTER_I|
|» symbol|ENGINE_IMPULSE_DRIVE_I|
|» symbol|ENGINE_ION_DRIVE_I|
|» symbol|ENGINE_ION_DRIVE_II|
|» symbol|ENGINE_HYPER_DRIVE_I|
|» symbol|MODULE_MINERAL_PROCESSOR_I|
|» symbol|MODULE_GAS_PROCESSOR_I|
|» symbol|MODULE_CARGO_HOLD_I|
|» symbol|MODULE_CARGO_HOLD_II|
|» symbol|MODULE_CARGO_HOLD_III|
|» symbol|MODULE_CREW_QUARTERS_I|
|» symbol|MODULE_ENVOY_QUARTERS_I|
|» symbol|MODULE_PASSENGER_CABIN_I|
|» symbol|MODULE_MICRO_REFINERY_I|
|» symbol|MODULE_SCIENCE_LAB_I|
|» symbol|MODULE_JUMP_DRIVE_I|
|» symbol|MODULE_JUMP_DRIVE_II|
|» symbol|MODULE_JUMP_DRIVE_III|
|» symbol|MODULE_WARP_DRIVE_I|
|» symbol|MODULE_WARP_DRIVE_II|
|» symbol|MODULE_WARP_DRIVE_III|
|» symbol|MODULE_SHIELD_GENERATOR_I|
|» symbol|MODULE_SHIELD_GENERATOR_II|
|» symbol|MODULE_ORE_REFINERY_I|
|» symbol|MODULE_FUEL_REFINERY_I|
|» symbol|MOUNT_GAS_SIPHON_I|
|» symbol|MOUNT_GAS_SIPHON_II|
|» symbol|MOUNT_GAS_SIPHON_III|
|» symbol|MOUNT_SURVEYOR_I|
|» symbol|MOUNT_SURVEYOR_II|
|» symbol|MOUNT_SURVEYOR_III|
|» symbol|MOUNT_SENSOR_ARRAY_I|
|» symbol|MOUNT_SENSOR_ARRAY_II|
|» symbol|MOUNT_SENSOR_ARRAY_III|
|» symbol|MOUNT_MINING_LASER_I|
|» symbol|MOUNT_MINING_LASER_II|
|» symbol|MOUNT_MINING_LASER_III|
|» symbol|MOUNT_LASER_CANNON_I|
|» symbol|MOUNT_MISSILE_LAUNCHER_I|
|» symbol|MOUNT_TURRET_I|
|» symbol|SHIP_PROBE|
|» symbol|SHIP_MINING_DRONE|
|» symbol|SHIP_SIPHON_DRONE|
|» symbol|SHIP_INTERCEPTOR|
|» symbol|SHIP_LIGHT_HAULER|
|» symbol|SHIP_COMMAND_FRIGATE|
|» symbol|SHIP_EXPLORER|
|» symbol|SHIP_HEAVY_FREIGHTER|
|» symbol|SHIP_LIGHT_SHUTTLE|
|» symbol|SHIP_ORE_HOUND|
|» symbol|SHIP_REFINING_FREIGHTER|
|» symbol|SHIP_SURVEYOR|

> Example responses

> 201 Response

```json
{
  "data": {
    "agent": {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    },
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    },
    "transaction": {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "tradeSymbol": "string",
      "type": "PURCHASE",
      "units": 0,
      "pricePerUnit": 0,
      "totalPrice": 0,
      "timestamp": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="sell-cargo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Cargo was successfully sold.|Inline|

<h3 id="sell-cargo-responseschema">Response Schema</h3>

Status Code **201**

*Sell Cargo 201 Response*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» agent|[Agent](#schemaagent)|true|none|Agent details.|
|»»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»»» symbol|string|true|none|Symbol of the agent.|
|»»» headquarters|string|true|none|The headquarters of the agent.|
|»»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»»» startingFaction|string|true|none|The faction the agent started with.|
|»»» shipCount|integer|true|none|How many ships are owned by the agent.|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|
|»» transaction|[MarketTransaction](#schemamarkettransaction)|true|none|Result of a transaction with a market.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» shipSymbol|string|true|none|The symbol of the ship that made the transaction.|
|»»» tradeSymbol|string|true|none|The symbol of the trade good.|
|»»» type|string|true|none|The type of transaction.|
|»»» units|integer|true|none|The number of units of the transaction.|
|»»» pricePerUnit|integer|true|none|The price per unit of the transaction.|
|»»» totalPrice|integer|true|none|The total price of the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|
|type|PURCHASE|
|type|SELL|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## create-ship-system-scan

<a id="opIdcreate-ship-system-scan"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/scan/systems', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/scan/systems`

*Scan Systems*

Scan for nearby systems, retrieving information on the systems' distance from the ship and their waypoints. Requires a ship to have the `Sensor Array` mount installed to use.

The ship will enter a cooldown after using this function, during which it cannot execute certain actions.

<h3 id="create-ship-system-scan-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 201 Response

```json
{
  "data": {
    "cooldown": {
      "shipSymbol": "string",
      "totalSeconds": 0,
      "remainingSeconds": 0,
      "expiration": "2019-08-24T14:15:22Z"
    },
    "systems": [
      {
        "symbol": "string",
        "sectorSymbol": "string",
        "type": "NEUTRON_STAR",
        "x": 0,
        "y": 0,
        "distance": 0
      }
    ]
  }
}
```

<h3 id="create-ship-system-scan-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successfully scanned for nearby systems.|Inline|

<h3 id="create-ship-system-scan-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»» systems|[[ScannedSystem](#schemascannedsystem)]|true|none|List of scanned systems.|
|»»» symbol|string|true|none|Symbol of the system.|
|»»» sectorSymbol|string|true|none|Symbol of the system's sector.|
|»»» type|[SystemType](#schemasystemtype)|true|none|The type of system.|
|»»» x|integer|true|none|Position in the universe in the x axis.|
|»»» y|integer|true|none|Position in the universe in the y axis.|
|»»» distance|integer|true|none|The system's distance from the scanning ship.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|NEUTRON_STAR|
|type|RED_STAR|
|type|ORANGE_STAR|
|type|BLUE_STAR|
|type|YOUNG_STAR|
|type|WHITE_DWARF|
|type|BLACK_HOLE|
|type|HYPERGIANT|
|type|NEBULA|
|type|UNSTABLE|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## create-ship-waypoint-scan

<a id="opIdcreate-ship-waypoint-scan"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/scan/waypoints', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/scan/waypoints`

*Scan Waypoints*

Scan for nearby waypoints, retrieving detailed information on each waypoint in range. Scanning uncharted waypoints will allow you to ignore their uncharted state and will list the waypoints' traits.

Requires a ship to have the `Sensor Array` mount installed to use.

The ship will enter a cooldown after using this function, during which it cannot execute certain actions.

<h3 id="create-ship-waypoint-scan-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 201 Response

```json
{
  "data": {
    "cooldown": {
      "shipSymbol": "string",
      "totalSeconds": 0,
      "remainingSeconds": 0,
      "expiration": "2019-08-24T14:15:22Z"
    },
    "waypoints": [
      {
        "symbol": "string",
        "type": "PLANET",
        "systemSymbol": "string",
        "x": 0,
        "y": 0,
        "orbitals": [
          {
            "symbol": "string"
          }
        ],
        "faction": {
          "symbol": "COSMIC"
        },
        "traits": [
          {
            "symbol": "UNCHARTED",
            "name": "string",
            "description": "string"
          }
        ],
        "chart": {
          "waypointSymbol": "string",
          "submittedBy": "string",
          "submittedOn": "2019-08-24T14:15:22Z"
        }
      }
    ]
  }
}
```

<h3 id="create-ship-waypoint-scan-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successfully scanned for nearby waypoints.|Inline|

<h3 id="create-ship-waypoint-scan-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»» waypoints|[[ScannedWaypoint](#schemascannedwaypoint)]|true|none|List of scanned waypoints.|
|»»» symbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»» x|integer|true|none|Position in the universe in the x axis.|
|»»» y|integer|true|none|Position in the universe in the y axis.|
|»»» orbitals|[[WaypointOrbital](#schemawaypointorbital)]|true|none|List of waypoints that orbit this waypoint.|
|»»»» symbol|string|true|none|The symbol of the orbiting waypoint.|
|»»» faction|[WaypointFaction](#schemawaypointfaction)|false|none|The faction that controls the waypoint.|
|»»»» symbol|[FactionSymbol](#schemafactionsymbol)|true|none|The symbol of the faction.|
|»»» traits|[[WaypointTrait](#schemawaypointtrait)]|true|none|The traits of the waypoint.|
|»»»» symbol|[WaypointTraitSymbol](#schemawaypointtraitsymbol)|true|none|The unique identifier of the trait.|
|»»»» name|string|true|none|The name of the trait.|
|»»»» description|string|true|none|A description of the trait.|
|»»» chart|[Chart](#schemachart)|false|none|The chart of a system or waypoint, which makes the location visible to other agents.|
|»»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|false|none|The symbol of the waypoint.|
|»»»» submittedBy|string|false|none|The agent that submitted the chart for this waypoint.|
|»»»» submittedOn|string(date-time)|false|none|The time the chart for this waypoint was submitted.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|symbol|COSMIC|
|symbol|VOID|
|symbol|GALACTIC|
|symbol|QUANTUM|
|symbol|DOMINION|
|symbol|ASTRO|
|symbol|CORSAIRS|
|symbol|OBSIDIAN|
|symbol|AEGIS|
|symbol|UNITED|
|symbol|SOLITARY|
|symbol|COBALT|
|symbol|OMEGA|
|symbol|ECHO|
|symbol|LORDS|
|symbol|CULT|
|symbol|ANCIENTS|
|symbol|SHADOW|
|symbol|ETHEREAL|
|symbol|UNCHARTED|
|symbol|UNDER_CONSTRUCTION|
|symbol|MARKETPLACE|
|symbol|SHIPYARD|
|symbol|OUTPOST|
|symbol|SCATTERED_SETTLEMENTS|
|symbol|SPRAWLING_CITIES|
|symbol|MEGA_STRUCTURES|
|symbol|PIRATE_BASE|
|symbol|OVERCROWDED|
|symbol|HIGH_TECH|
|symbol|CORRUPT|
|symbol|BUREAUCRATIC|
|symbol|TRADING_HUB|
|symbol|INDUSTRIAL|
|symbol|BLACK_MARKET|
|symbol|RESEARCH_FACILITY|
|symbol|MILITARY_BASE|
|symbol|SURVEILLANCE_OUTPOST|
|symbol|EXPLORATION_OUTPOST|
|symbol|MINERAL_DEPOSITS|
|symbol|COMMON_METAL_DEPOSITS|
|symbol|PRECIOUS_METAL_DEPOSITS|
|symbol|RARE_METAL_DEPOSITS|
|symbol|METHANE_POOLS|
|symbol|ICE_CRYSTALS|
|symbol|EXPLOSIVE_GASES|
|symbol|STRONG_MAGNETOSPHERE|
|symbol|VIBRANT_AURORAS|
|symbol|SALT_FLATS|
|symbol|CANYONS|
|symbol|PERPETUAL_DAYLIGHT|
|symbol|PERPETUAL_OVERCAST|
|symbol|DRY_SEABEDS|
|symbol|MAGMA_SEAS|
|symbol|SUPERVOLCANOES|
|symbol|ASH_CLOUDS|
|symbol|VAST_RUINS|
|symbol|MUTATED_FLORA|
|symbol|TERRAFORMED|
|symbol|EXTREME_TEMPERATURES|
|symbol|EXTREME_PRESSURE|
|symbol|DIVERSE_LIFE|
|symbol|SCARCE_LIFE|
|symbol|FOSSILS|
|symbol|WEAK_GRAVITY|
|symbol|STRONG_GRAVITY|
|symbol|CRUSHING_GRAVITY|
|symbol|TOXIC_ATMOSPHERE|
|symbol|CORROSIVE_ATMOSPHERE|
|symbol|BREATHABLE_ATMOSPHERE|
|symbol|THIN_ATMOSPHERE|
|symbol|JOVIAN|
|symbol|ROCKY|
|symbol|VOLCANIC|
|symbol|FROZEN|
|symbol|SWAMP|
|symbol|BARREN|
|symbol|TEMPERATE|
|symbol|JUNGLE|
|symbol|OCEAN|
|symbol|RADIOACTIVE|
|symbol|MICRO_GRAVITY_ANOMALIES|
|symbol|DEBRIS_CLUSTER|
|symbol|DEEP_CRATERS|
|symbol|SHALLOW_CRATERS|
|symbol|UNSTABLE_COMPOSITION|
|symbol|HOLLOWED_INTERIOR|
|symbol|STRIPPED|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## create-ship-ship-scan

<a id="opIdcreate-ship-ship-scan"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/scan/ships', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/scan/ships`

*Scan Ships*

Scan for nearby ships, retrieving information for all ships in range.

Requires a ship to have the `Sensor Array` mount installed to use.

The ship will enter a cooldown after using this function, during which it cannot execute certain actions.

<h3 id="create-ship-ship-scan-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 201 Response

```json
{
  "data": {
    "cooldown": {
      "shipSymbol": "string",
      "totalSeconds": 0,
      "remainingSeconds": 0,
      "expiration": "2019-08-24T14:15:22Z"
    },
    "ships": [
      {
        "symbol": "string",
        "registration": {
          "name": "string",
          "factionSymbol": "string",
          "role": "FABRICATOR"
        },
        "nav": {
          "systemSymbol": "string",
          "waypointSymbol": "string",
          "route": {
            "destination": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "origin": {
              "symbol": "string",
              "type": "PLANET",
              "systemSymbol": "string",
              "x": 0,
              "y": 0
            },
            "departureTime": "2019-08-24T14:15:22Z",
            "arrival": "2019-08-24T14:15:22Z"
          },
          "status": "IN_TRANSIT",
          "flightMode": "DRIFT"
        },
        "frame": {
          "symbol": "string"
        },
        "reactor": {
          "symbol": "string"
        },
        "engine": {
          "symbol": "string"
        },
        "mounts": [
          {
            "symbol": "string"
          }
        ]
      }
    ]
  }
}
```

<h3 id="create-ship-ship-scan-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successfully scanned for nearby ships.|Inline|

<h3 id="create-ship-ship-scan-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»» ships|[[ScannedShip](#schemascannedship)]|true|none|List of scanned ships.|
|»»» symbol|string|true|none|The globally unique identifier of the ship.|
|»»» registration|[ShipRegistration](#schemashipregistration)|true|none|The public registration information of the ship|
|»»»» name|string|true|none|The agent's registered name of the ship|
|»»»» factionSymbol|string|true|none|The symbol of the faction the ship is registered with|
|»»»» role|[ShipRole](#schemashiprole)|true|none|The registered role of the ship|
|»»» nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»»»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»»»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|
|»»» frame|object|false|none|The frame of the ship.|
|»»»» symbol|string|true|none|The symbol of the frame.|
|»»» reactor|object|false|none|The reactor of the ship.|
|»»»» symbol|string|true|none|The symbol of the reactor.|
|»»» engine|object|true|none|The engine of the ship.|
|»»»» symbol|string|true|none|The symbol of the engine.|
|»»» mounts|[object]|false|none|List of mounts installed in the ship.|
|»»»» symbol|string|true|none|The symbol of the mount.|

#### Enumerated Values

|Property|Value|
|---|---|
|role|FABRICATOR|
|role|HARVESTER|
|role|HAULER|
|role|INTERCEPTOR|
|role|EXCAVATOR|
|role|TRANSPORT|
|role|REPAIR|
|role|SURVEYOR|
|role|COMMAND|
|role|CARRIER|
|role|PATROL|
|role|SATELLITE|
|role|EXPLORER|
|role|REFINERY|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## refuel-ship

<a id="opIdrefuel-ship"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/refuel', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/refuel`

*Refuel Ship*

Refuel your ship by buying fuel from the local market.

Requires the ship to be docked in a waypoint that has the `Marketplace` trait, and the market must be selling fuel in order to refuel.

Each fuel bought from the market replenishes 100 units in your ship's fuel.

Ships will always be refuel to their frame's maximum fuel capacity when using this action.

> Body parameter

```json
{
  "units": "100",
  "fromCargo": false
}
```

<h3 id="refuel-ship-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» units|body|integer|false|The amount of fuel to fill in the ship's tanks. When not specified, the ship will be refueled to its maximum fuel capacity. If the amount specified is greater than the ship's remaining capacity, the ship will only be refueled to its maximum fuel capacity. The amount specified is not in market units but in ship fuel units.|
|» fromCargo|body|boolean|false|Wether to use the FUEL thats in your cargo or not. Default: false|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 200 Response

```json
{
  "data": {
    "agent": {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    },
    "fuel": {
      "current": 0,
      "capacity": 0,
      "consumed": {
        "amount": 0,
        "timestamp": "2019-08-24T14:15:22Z"
      }
    },
    "transaction": {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "tradeSymbol": "string",
      "type": "PURCHASE",
      "units": 0,
      "pricePerUnit": 0,
      "totalPrice": 0,
      "timestamp": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="refuel-ship-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Refueled successfully.|Inline|

<h3 id="refuel-ship-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» agent|[Agent](#schemaagent)|true|none|Agent details.|
|»»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»»» symbol|string|true|none|Symbol of the agent.|
|»»» headquarters|string|true|none|The headquarters of the agent.|
|»»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»»» startingFaction|string|true|none|The faction the agent started with.|
|»»» shipCount|integer|true|none|How many ships are owned by the agent.|
|»» fuel|[ShipFuel](#schemashipfuel)|true|none|Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.|
|»»» current|integer|true|none|The current amount of fuel in the ship's tanks.|
|»»» capacity|integer|true|none|The maximum amount of fuel the ship's tanks can hold.|
|»»» consumed|object|false|none|An object that only shows up when an action has consumed fuel in the process. Shows the fuel consumption data.|
|»»»» amount|integer|true|none|The amount of fuel consumed by the most recent transit or action.|
|»»»» timestamp|string(date-time)|true|none|The time at which the fuel was consumed.|
|»» transaction|[MarketTransaction](#schemamarkettransaction)|true|none|Result of a transaction with a market.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» shipSymbol|string|true|none|The symbol of the ship that made the transaction.|
|»»» tradeSymbol|string|true|none|The symbol of the trade good.|
|»»» type|string|true|none|The type of transaction.|
|»»» units|integer|true|none|The number of units of the transaction.|
|»»» pricePerUnit|integer|true|none|The price per unit of the transaction.|
|»»» totalPrice|integer|true|none|The total price of the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PURCHASE|
|type|SELL|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## purchase-cargo

<a id="opIdpurchase-cargo"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/purchase', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/purchase`

*Purchase Cargo*

Purchase cargo from a market.

The ship must be docked in a waypoint that has `Marketplace` trait, and the market must be selling a good to be able to purchase it.

The maximum amount of units of a good that can be purchased in each transaction are denoted by the `tradeVolume` value of the good, which can be viewed by using the Get Market action.

Purchased goods are added to the ship's cargo hold.

> Body parameter

```json
{
  "symbol": "PRECIOUS_STONES",
  "units": 0
}
```

<h3 id="purchase-cargo-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» symbol|body|[TradeSymbol](#schematradesymbol)|true|The good's symbol.|
|» units|body|integer|true|Amounts of units to purchase.|
|shipSymbol|path|string|true|The ship's symbol.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» symbol|PRECIOUS_STONES|
|» symbol|QUARTZ_SAND|
|» symbol|SILICON_CRYSTALS|
|» symbol|AMMONIA_ICE|
|» symbol|LIQUID_HYDROGEN|
|» symbol|LIQUID_NITROGEN|
|» symbol|ICE_WATER|
|» symbol|EXOTIC_MATTER|
|» symbol|ADVANCED_CIRCUITRY|
|» symbol|GRAVITON_EMITTERS|
|» symbol|IRON|
|» symbol|IRON_ORE|
|» symbol|COPPER|
|» symbol|COPPER_ORE|
|» symbol|ALUMINUM|
|» symbol|ALUMINUM_ORE|
|» symbol|SILVER|
|» symbol|SILVER_ORE|
|» symbol|GOLD|
|» symbol|GOLD_ORE|
|» symbol|PLATINUM|
|» symbol|PLATINUM_ORE|
|» symbol|DIAMONDS|
|» symbol|URANITE|
|» symbol|URANITE_ORE|
|» symbol|MERITIUM|
|» symbol|MERITIUM_ORE|
|» symbol|HYDROCARBON|
|» symbol|ANTIMATTER|
|» symbol|FAB_MATS|
|» symbol|FERTILIZERS|
|» symbol|FABRICS|
|» symbol|FOOD|
|» symbol|JEWELRY|
|» symbol|MACHINERY|
|» symbol|FIREARMS|
|» symbol|ASSAULT_RIFLES|
|» symbol|MILITARY_EQUIPMENT|
|» symbol|EXPLOSIVES|
|» symbol|LAB_INSTRUMENTS|
|» symbol|AMMUNITION|
|» symbol|ELECTRONICS|
|» symbol|SHIP_PLATING|
|» symbol|SHIP_PARTS|
|» symbol|EQUIPMENT|
|» symbol|FUEL|
|» symbol|MEDICINE|
|» symbol|DRUGS|
|» symbol|CLOTHING|
|» symbol|MICROPROCESSORS|
|» symbol|PLASTICS|
|» symbol|POLYNUCLEOTIDES|
|» symbol|BIOCOMPOSITES|
|» symbol|QUANTUM_STABILIZERS|
|» symbol|NANOBOTS|
|» symbol|AI_MAINFRAMES|
|» symbol|QUANTUM_DRIVES|
|» symbol|ROBOTIC_DRONES|
|» symbol|CYBER_IMPLANTS|
|» symbol|GENE_THERAPEUTICS|
|» symbol|NEURAL_CHIPS|
|» symbol|MOOD_REGULATORS|
|» symbol|VIRAL_AGENTS|
|» symbol|MICRO_FUSION_GENERATORS|
|» symbol|SUPERGRAINS|
|» symbol|LASER_RIFLES|
|» symbol|HOLOGRAPHICS|
|» symbol|SHIP_SALVAGE|
|» symbol|RELIC_TECH|
|» symbol|NOVEL_LIFEFORMS|
|» symbol|BOTANICAL_SPECIMENS|
|» symbol|CULTURAL_ARTIFACTS|
|» symbol|FRAME_PROBE|
|» symbol|FRAME_DRONE|
|» symbol|FRAME_INTERCEPTOR|
|» symbol|FRAME_RACER|
|» symbol|FRAME_FIGHTER|
|» symbol|FRAME_FRIGATE|
|» symbol|FRAME_SHUTTLE|
|» symbol|FRAME_EXPLORER|
|» symbol|FRAME_MINER|
|» symbol|FRAME_LIGHT_FREIGHTER|
|» symbol|FRAME_HEAVY_FREIGHTER|
|» symbol|FRAME_TRANSPORT|
|» symbol|FRAME_DESTROYER|
|» symbol|FRAME_CRUISER|
|» symbol|FRAME_CARRIER|
|» symbol|REACTOR_SOLAR_I|
|» symbol|REACTOR_FUSION_I|
|» symbol|REACTOR_FISSION_I|
|» symbol|REACTOR_CHEMICAL_I|
|» symbol|REACTOR_ANTIMATTER_I|
|» symbol|ENGINE_IMPULSE_DRIVE_I|
|» symbol|ENGINE_ION_DRIVE_I|
|» symbol|ENGINE_ION_DRIVE_II|
|» symbol|ENGINE_HYPER_DRIVE_I|
|» symbol|MODULE_MINERAL_PROCESSOR_I|
|» symbol|MODULE_GAS_PROCESSOR_I|
|» symbol|MODULE_CARGO_HOLD_I|
|» symbol|MODULE_CARGO_HOLD_II|
|» symbol|MODULE_CARGO_HOLD_III|
|» symbol|MODULE_CREW_QUARTERS_I|
|» symbol|MODULE_ENVOY_QUARTERS_I|
|» symbol|MODULE_PASSENGER_CABIN_I|
|» symbol|MODULE_MICRO_REFINERY_I|
|» symbol|MODULE_SCIENCE_LAB_I|
|» symbol|MODULE_JUMP_DRIVE_I|
|» symbol|MODULE_JUMP_DRIVE_II|
|» symbol|MODULE_JUMP_DRIVE_III|
|» symbol|MODULE_WARP_DRIVE_I|
|» symbol|MODULE_WARP_DRIVE_II|
|» symbol|MODULE_WARP_DRIVE_III|
|» symbol|MODULE_SHIELD_GENERATOR_I|
|» symbol|MODULE_SHIELD_GENERATOR_II|
|» symbol|MODULE_ORE_REFINERY_I|
|» symbol|MODULE_FUEL_REFINERY_I|
|» symbol|MOUNT_GAS_SIPHON_I|
|» symbol|MOUNT_GAS_SIPHON_II|
|» symbol|MOUNT_GAS_SIPHON_III|
|» symbol|MOUNT_SURVEYOR_I|
|» symbol|MOUNT_SURVEYOR_II|
|» symbol|MOUNT_SURVEYOR_III|
|» symbol|MOUNT_SENSOR_ARRAY_I|
|» symbol|MOUNT_SENSOR_ARRAY_II|
|» symbol|MOUNT_SENSOR_ARRAY_III|
|» symbol|MOUNT_MINING_LASER_I|
|» symbol|MOUNT_MINING_LASER_II|
|» symbol|MOUNT_MINING_LASER_III|
|» symbol|MOUNT_LASER_CANNON_I|
|» symbol|MOUNT_MISSILE_LAUNCHER_I|
|» symbol|MOUNT_TURRET_I|
|» symbol|SHIP_PROBE|
|» symbol|SHIP_MINING_DRONE|
|» symbol|SHIP_SIPHON_DRONE|
|» symbol|SHIP_INTERCEPTOR|
|» symbol|SHIP_LIGHT_HAULER|
|» symbol|SHIP_COMMAND_FRIGATE|
|» symbol|SHIP_EXPLORER|
|» symbol|SHIP_HEAVY_FREIGHTER|
|» symbol|SHIP_LIGHT_SHUTTLE|
|» symbol|SHIP_ORE_HOUND|
|» symbol|SHIP_REFINING_FREIGHTER|
|» symbol|SHIP_SURVEYOR|

> Example responses

> 201 Response

```json
{
  "data": {
    "agent": {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    },
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    },
    "transaction": {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "tradeSymbol": "string",
      "type": "PURCHASE",
      "units": 0,
      "pricePerUnit": 0,
      "totalPrice": 0,
      "timestamp": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="purchase-cargo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Purchased goods successfully.|Inline|

<h3 id="purchase-cargo-responseschema">Response Schema</h3>

Status Code **201**

*Purchase Cargo 201 Response*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» agent|[Agent](#schemaagent)|true|none|Agent details.|
|»»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»»» symbol|string|true|none|Symbol of the agent.|
|»»» headquarters|string|true|none|The headquarters of the agent.|
|»»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»»» startingFaction|string|true|none|The faction the agent started with.|
|»»» shipCount|integer|true|none|How many ships are owned by the agent.|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|
|»» transaction|[MarketTransaction](#schemamarkettransaction)|true|none|Result of a transaction with a market.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» shipSymbol|string|true|none|The symbol of the ship that made the transaction.|
|»»» tradeSymbol|string|true|none|The symbol of the trade good.|
|»»» type|string|true|none|The type of transaction.|
|»»» units|integer|true|none|The number of units of the transaction.|
|»»» pricePerUnit|integer|true|none|The price per unit of the transaction.|
|»»» totalPrice|integer|true|none|The total price of the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|
|type|PURCHASE|
|type|SELL|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## transfer-cargo

<a id="opIdtransfer-cargo"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/transfer', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/transfer`

*Transfer Cargo*

Transfer cargo between ships.

The receiving ship must be in the same waypoint as the transferring ship, and it must able to hold the additional cargo after the transfer is complete. Both ships also must be in the same state, either both are docked or both are orbiting.

The response body's cargo shows the cargo of the transferring ship after the transfer is complete.

> Body parameter

```json
{
  "tradeSymbol": "PRECIOUS_STONES",
  "units": 0,
  "shipSymbol": "string"
}
```

<h3 id="transfer-cargo-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» tradeSymbol|body|[TradeSymbol](#schematradesymbol)|true|The good's symbol.|
|» units|body|integer|true|Amount of units to transfer.|
|» shipSymbol|body|string|true|The symbol of the ship to transfer to.|
|shipSymbol|path|string|true|The transferring ship's symbol.|

#### Enumerated Values

|Parameter|Value|
|---|---|
|» tradeSymbol|PRECIOUS_STONES|
|» tradeSymbol|QUARTZ_SAND|
|» tradeSymbol|SILICON_CRYSTALS|
|» tradeSymbol|AMMONIA_ICE|
|» tradeSymbol|LIQUID_HYDROGEN|
|» tradeSymbol|LIQUID_NITROGEN|
|» tradeSymbol|ICE_WATER|
|» tradeSymbol|EXOTIC_MATTER|
|» tradeSymbol|ADVANCED_CIRCUITRY|
|» tradeSymbol|GRAVITON_EMITTERS|
|» tradeSymbol|IRON|
|» tradeSymbol|IRON_ORE|
|» tradeSymbol|COPPER|
|» tradeSymbol|COPPER_ORE|
|» tradeSymbol|ALUMINUM|
|» tradeSymbol|ALUMINUM_ORE|
|» tradeSymbol|SILVER|
|» tradeSymbol|SILVER_ORE|
|» tradeSymbol|GOLD|
|» tradeSymbol|GOLD_ORE|
|» tradeSymbol|PLATINUM|
|» tradeSymbol|PLATINUM_ORE|
|» tradeSymbol|DIAMONDS|
|» tradeSymbol|URANITE|
|» tradeSymbol|URANITE_ORE|
|» tradeSymbol|MERITIUM|
|» tradeSymbol|MERITIUM_ORE|
|» tradeSymbol|HYDROCARBON|
|» tradeSymbol|ANTIMATTER|
|» tradeSymbol|FAB_MATS|
|» tradeSymbol|FERTILIZERS|
|» tradeSymbol|FABRICS|
|» tradeSymbol|FOOD|
|» tradeSymbol|JEWELRY|
|» tradeSymbol|MACHINERY|
|» tradeSymbol|FIREARMS|
|» tradeSymbol|ASSAULT_RIFLES|
|» tradeSymbol|MILITARY_EQUIPMENT|
|» tradeSymbol|EXPLOSIVES|
|» tradeSymbol|LAB_INSTRUMENTS|
|» tradeSymbol|AMMUNITION|
|» tradeSymbol|ELECTRONICS|
|» tradeSymbol|SHIP_PLATING|
|» tradeSymbol|SHIP_PARTS|
|» tradeSymbol|EQUIPMENT|
|» tradeSymbol|FUEL|
|» tradeSymbol|MEDICINE|
|» tradeSymbol|DRUGS|
|» tradeSymbol|CLOTHING|
|» tradeSymbol|MICROPROCESSORS|
|» tradeSymbol|PLASTICS|
|» tradeSymbol|POLYNUCLEOTIDES|
|» tradeSymbol|BIOCOMPOSITES|
|» tradeSymbol|QUANTUM_STABILIZERS|
|» tradeSymbol|NANOBOTS|
|» tradeSymbol|AI_MAINFRAMES|
|» tradeSymbol|QUANTUM_DRIVES|
|» tradeSymbol|ROBOTIC_DRONES|
|» tradeSymbol|CYBER_IMPLANTS|
|» tradeSymbol|GENE_THERAPEUTICS|
|» tradeSymbol|NEURAL_CHIPS|
|» tradeSymbol|MOOD_REGULATORS|
|» tradeSymbol|VIRAL_AGENTS|
|» tradeSymbol|MICRO_FUSION_GENERATORS|
|» tradeSymbol|SUPERGRAINS|
|» tradeSymbol|LASER_RIFLES|
|» tradeSymbol|HOLOGRAPHICS|
|» tradeSymbol|SHIP_SALVAGE|
|» tradeSymbol|RELIC_TECH|
|» tradeSymbol|NOVEL_LIFEFORMS|
|» tradeSymbol|BOTANICAL_SPECIMENS|
|» tradeSymbol|CULTURAL_ARTIFACTS|
|» tradeSymbol|FRAME_PROBE|
|» tradeSymbol|FRAME_DRONE|
|» tradeSymbol|FRAME_INTERCEPTOR|
|» tradeSymbol|FRAME_RACER|
|» tradeSymbol|FRAME_FIGHTER|
|» tradeSymbol|FRAME_FRIGATE|
|» tradeSymbol|FRAME_SHUTTLE|
|» tradeSymbol|FRAME_EXPLORER|
|» tradeSymbol|FRAME_MINER|
|» tradeSymbol|FRAME_LIGHT_FREIGHTER|
|» tradeSymbol|FRAME_HEAVY_FREIGHTER|
|» tradeSymbol|FRAME_TRANSPORT|
|» tradeSymbol|FRAME_DESTROYER|
|» tradeSymbol|FRAME_CRUISER|
|» tradeSymbol|FRAME_CARRIER|
|» tradeSymbol|REACTOR_SOLAR_I|
|» tradeSymbol|REACTOR_FUSION_I|
|» tradeSymbol|REACTOR_FISSION_I|
|» tradeSymbol|REACTOR_CHEMICAL_I|
|» tradeSymbol|REACTOR_ANTIMATTER_I|
|» tradeSymbol|ENGINE_IMPULSE_DRIVE_I|
|» tradeSymbol|ENGINE_ION_DRIVE_I|
|» tradeSymbol|ENGINE_ION_DRIVE_II|
|» tradeSymbol|ENGINE_HYPER_DRIVE_I|
|» tradeSymbol|MODULE_MINERAL_PROCESSOR_I|
|» tradeSymbol|MODULE_GAS_PROCESSOR_I|
|» tradeSymbol|MODULE_CARGO_HOLD_I|
|» tradeSymbol|MODULE_CARGO_HOLD_II|
|» tradeSymbol|MODULE_CARGO_HOLD_III|
|» tradeSymbol|MODULE_CREW_QUARTERS_I|
|» tradeSymbol|MODULE_ENVOY_QUARTERS_I|
|» tradeSymbol|MODULE_PASSENGER_CABIN_I|
|» tradeSymbol|MODULE_MICRO_REFINERY_I|
|» tradeSymbol|MODULE_SCIENCE_LAB_I|
|» tradeSymbol|MODULE_JUMP_DRIVE_I|
|» tradeSymbol|MODULE_JUMP_DRIVE_II|
|» tradeSymbol|MODULE_JUMP_DRIVE_III|
|» tradeSymbol|MODULE_WARP_DRIVE_I|
|» tradeSymbol|MODULE_WARP_DRIVE_II|
|» tradeSymbol|MODULE_WARP_DRIVE_III|
|» tradeSymbol|MODULE_SHIELD_GENERATOR_I|
|» tradeSymbol|MODULE_SHIELD_GENERATOR_II|
|» tradeSymbol|MODULE_ORE_REFINERY_I|
|» tradeSymbol|MODULE_FUEL_REFINERY_I|
|» tradeSymbol|MOUNT_GAS_SIPHON_I|
|» tradeSymbol|MOUNT_GAS_SIPHON_II|
|» tradeSymbol|MOUNT_GAS_SIPHON_III|
|» tradeSymbol|MOUNT_SURVEYOR_I|
|» tradeSymbol|MOUNT_SURVEYOR_II|
|» tradeSymbol|MOUNT_SURVEYOR_III|
|» tradeSymbol|MOUNT_SENSOR_ARRAY_I|
|» tradeSymbol|MOUNT_SENSOR_ARRAY_II|
|» tradeSymbol|MOUNT_SENSOR_ARRAY_III|
|» tradeSymbol|MOUNT_MINING_LASER_I|
|» tradeSymbol|MOUNT_MINING_LASER_II|
|» tradeSymbol|MOUNT_MINING_LASER_III|
|» tradeSymbol|MOUNT_LASER_CANNON_I|
|» tradeSymbol|MOUNT_MISSILE_LAUNCHER_I|
|» tradeSymbol|MOUNT_TURRET_I|
|» tradeSymbol|SHIP_PROBE|
|» tradeSymbol|SHIP_MINING_DRONE|
|» tradeSymbol|SHIP_SIPHON_DRONE|
|» tradeSymbol|SHIP_INTERCEPTOR|
|» tradeSymbol|SHIP_LIGHT_HAULER|
|» tradeSymbol|SHIP_COMMAND_FRIGATE|
|» tradeSymbol|SHIP_EXPLORER|
|» tradeSymbol|SHIP_HEAVY_FREIGHTER|
|» tradeSymbol|SHIP_LIGHT_SHUTTLE|
|» tradeSymbol|SHIP_ORE_HOUND|
|» tradeSymbol|SHIP_REFINING_FREIGHTER|
|» tradeSymbol|SHIP_SURVEYOR|

> Example responses

> 200 Response

```json
{
  "data": {
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    }
  }
}
```

<h3 id="transfer-cargo-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Transfer successful.|Inline|

<h3 id="transfer-cargo-responseschema">Response Schema</h3>

Status Code **200**

*Transfer Cargo 200 Response*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## negotiateContract

<a id="opIdnegotiateContract"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/negotiate/contract', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/negotiate/contract`

*Negotiate Contract*

Negotiate a new contract with the HQ.

In order to negotiate a new contract, an agent must not have ongoing or offered contracts over the allowed maximum amount. Currently the maximum contracts an agent can have at a time is 1.

Once a contract is negotiated, it is added to the list of contracts offered to the agent, which the agent can then accept. 

The ship must be present at any waypoint with a faction present to negotiate a contract with that faction.

<h3 id="negotiatecontract-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The ship's symbol.|

> Example responses

> 201 Response

```json
{
  "data": {
    "contract": {
      "id": "string",
      "factionSymbol": "string",
      "type": "PROCUREMENT",
      "terms": {
        "deadline": "2019-08-24T14:15:22Z",
        "payment": {
          "onAccepted": 0,
          "onFulfilled": 0
        },
        "deliver": [
          {
            "tradeSymbol": "string",
            "destinationSymbol": "string",
            "unitsRequired": 0,
            "unitsFulfilled": 0
          }
        ]
      },
      "accepted": false,
      "fulfilled": false,
      "expiration": "2019-08-24T14:15:22Z",
      "deadlineToAccept": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="negotiatecontract-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successfully negotiated a new contract.|Inline|

<h3 id="negotiatecontract-responseschema">Response Schema</h3>

Status Code **201**

*Negotiate Contract 200 Response*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» contract|[Contract](#schemacontract)|true|none|Contract details.|
|»»» id|string|true|none|ID of the contract.|
|»»» factionSymbol|string|true|none|The symbol of the faction that this contract is for.|
|»»» type|string|true|none|Type of contract.|
|»»» terms|[ContractTerms](#schemacontractterms)|true|none|The terms to fulfill the contract.|
|»»»» deadline|string(date-time)|true|none|The deadline for the contract.|
|»»»» payment|[ContractPayment](#schemacontractpayment)|true|none|Payments for the contract.|
|»»»»» onAccepted|integer|true|none|The amount of credits received up front for accepting the contract.|
|»»»»» onFulfilled|integer|true|none|The amount of credits received when the contract is fulfilled.|
|»»»» deliver|[[ContractDeliverGood](#schemacontractdelivergood)]|false|none|The cargo that needs to be delivered to fulfill the contract.|
|»»»»» tradeSymbol|string|true|none|The symbol of the trade good to deliver.|
|»»»»» destinationSymbol|string|true|none|The destination where goods need to be delivered.|
|»»»»» unitsRequired|integer|true|none|The number of units that need to be delivered on this contract.|
|»»»»» unitsFulfilled|integer|true|none|The number of units fulfilled on this contract.|
|»»» accepted|boolean|true|none|Whether the contract has been accepted by the agent|
|»»» fulfilled|boolean|true|none|Whether the contract has been fulfilled|
|»»» expiration|string(date-time)|true|none|Deprecated in favor of deadlineToAccept|
|»»» deadlineToAccept|string(date-time)|false|none|The time at which the contract is no longer available to be accepted|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PROCUREMENT|
|type|TRANSPORT|
|type|SHUTTLE|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## get-mounts

<a id="opIdget-mounts"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/mounts', headers = headers)

print(r.json())

```

`GET /my/ships/{shipSymbol}/mounts`

*Get Mounts*

Get the mounts installed on a ship.

<h3 id="get-mounts-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The ship's symbol.|

> Example responses

> 200 Response

```json
{
  "data": [
    {
      "symbol": "MOUNT_GAS_SIPHON_I",
      "name": "string",
      "description": "string",
      "strength": 0,
      "deposits": [
        "QUARTZ_SAND"
      ],
      "requirements": {
        "power": 0,
        "crew": 0,
        "slots": 0
      }
    }
  ]
}
```

<h3 id="get-mounts-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Got installed mounts.|Inline|

<h3 id="get-mounts-responseschema">Response Schema</h3>

Status Code **200**

*Get Mounts 200 Response*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[[ShipMount](#schemashipmount)]|true|none|[A mount is installed on the exterier of a ship.]|
|»» symbol|string|true|none|Symbo of this mount.|
|»» name|string|true|none|Name of this mount.|
|»» description|string|false|none|Description of this mount.|
|»» strength|integer|false|none|Mounts that have this value, such as mining lasers, denote how powerful this mount's capabilities are.|
|»» deposits|[string]|false|none|Mounts that have this value denote what goods can be produced from using the mount.|
|»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» power|integer|false|none|The amount of power required from the reactor.|
|»»» crew|integer|false|none|The number of crew required for operation.|
|»»» slots|integer|false|none|The number of module slots required for installation.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## install-mount

<a id="opIdinstall-mount"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/mounts/install', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/mounts/install`

*Install Mount*

Install a mount on a ship.

In order to install a mount, the ship must be docked and located in a waypoint that has a `Shipyard` trait. The ship also must have the mount to install in its cargo hold.

An installation fee will be deduced by the Shipyard for installing the mount on the ship. 

> Body parameter

```json
{
  "symbol": "string"
}
```

<h3 id="install-mount-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» symbol|body|string|true|none|
|shipSymbol|path|string|true|The ship's symbol.|

> Example responses

> 201 Response

```json
{
  "data": {
    "agent": {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    },
    "mounts": [
      {
        "symbol": "MOUNT_GAS_SIPHON_I",
        "name": "string",
        "description": "string",
        "strength": 0,
        "deposits": [
          "QUARTZ_SAND"
        ],
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      }
    ],
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    },
    "transaction": {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "tradeSymbol": "string",
      "totalPrice": 0,
      "timestamp": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="install-mount-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successfully installed the mount.|Inline|

<h3 id="install-mount-responseschema">Response Schema</h3>

Status Code **201**

*Install Mount 201 Response*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» agent|[Agent](#schemaagent)|true|none|Agent details.|
|»»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»»» symbol|string|true|none|Symbol of the agent.|
|»»» headquarters|string|true|none|The headquarters of the agent.|
|»»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»»» startingFaction|string|true|none|The faction the agent started with.|
|»»» shipCount|integer|true|none|How many ships are owned by the agent.|
|»» mounts|[[ShipMount](#schemashipmount)]|true|none|List of installed mounts after the installation of the new mount.|
|»»» symbol|string|true|none|Symbo of this mount.|
|»»» name|string|true|none|Name of this mount.|
|»»» description|string|false|none|Description of this mount.|
|»»» strength|integer|false|none|Mounts that have this value, such as mining lasers, denote how powerful this mount's capabilities are.|
|»»» deposits|[string]|false|none|Mounts that have this value denote what goods can be produced from using the mount.|
|»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»»» power|integer|false|none|The amount of power required from the reactor.|
|»»»» crew|integer|false|none|The number of crew required for operation.|
|»»»» slots|integer|false|none|The number of module slots required for installation.|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|
|»» transaction|[ShipModificationTransaction](#schemashipmodificationtransaction)|true|none|Result of a transaction for a ship modification, such as installing a mount or a module.|
|»»» waypointSymbol|string|true|none|The symbol of the waypoint where the transaction took place.|
|»»» shipSymbol|string|true|none|The symbol of the ship that made the transaction.|
|»»» tradeSymbol|string|true|none|The symbol of the trade good.|
|»»» totalPrice|integer|true|none|The total price of the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## remove-mount

<a id="opIdremove-mount"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/mounts/remove', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/mounts/remove`

*Remove Mount*

Remove a mount from a ship.

The ship must be docked in a waypoint that has the `Shipyard` trait, and must have the desired mount that it wish to remove installed.

A removal fee will be deduced from the agent by the Shipyard.

> Body parameter

```json
{
  "symbol": "string"
}
```

<h3 id="remove-mount-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» symbol|body|string|true|The symbol of the mount to remove.|
|shipSymbol|path|string|true|The ship's symbol.|

> Example responses

> 201 Response

```json
{
  "data": {
    "agent": {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    },
    "mounts": [
      {
        "symbol": "MOUNT_GAS_SIPHON_I",
        "name": "string",
        "description": "string",
        "strength": 0,
        "deposits": [
          "QUARTZ_SAND"
        ],
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      }
    ],
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    },
    "transaction": {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "tradeSymbol": "string",
      "totalPrice": 0,
      "timestamp": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="remove-mount-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successfully removed the mount.|Inline|

<h3 id="remove-mount-responseschema">Response Schema</h3>

Status Code **201**

*Remove Mount 201 Response*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» agent|[Agent](#schemaagent)|true|none|Agent details.|
|»»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»»» symbol|string|true|none|Symbol of the agent.|
|»»» headquarters|string|true|none|The headquarters of the agent.|
|»»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»»» startingFaction|string|true|none|The faction the agent started with.|
|»»» shipCount|integer|true|none|How many ships are owned by the agent.|
|»» mounts|[[ShipMount](#schemashipmount)]|true|none|List of installed mounts after the removal of the selected mount.|
|»»» symbol|string|true|none|Symbo of this mount.|
|»»» name|string|true|none|Name of this mount.|
|»»» description|string|false|none|Description of this mount.|
|»»» strength|integer|false|none|Mounts that have this value, such as mining lasers, denote how powerful this mount's capabilities are.|
|»»» deposits|[string]|false|none|Mounts that have this value denote what goods can be produced from using the mount.|
|»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»»» power|integer|false|none|The amount of power required from the reactor.|
|»»»» crew|integer|false|none|The number of crew required for operation.|
|»»»» slots|integer|false|none|The number of module slots required for installation.|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|
|»» transaction|[ShipModificationTransaction](#schemashipmodificationtransaction)|true|none|Result of a transaction for a ship modification, such as installing a mount or a module.|
|»»» waypointSymbol|string|true|none|The symbol of the waypoint where the transaction took place.|
|»»» shipSymbol|string|true|none|The symbol of the ship that made the transaction.|
|»»» tradeSymbol|string|true|none|The symbol of the trade good.|
|»»» totalPrice|integer|true|none|The total price of the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## get-scrap-ship

<a id="opIdget-scrap-ship"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/scrap', headers = headers)

print(r.json())

```

`GET /my/ships/{shipSymbol}/scrap`

*Get Scrap Ship*

Get the amount of value that will be returned when scrapping a ship.

<h3 id="get-scrap-ship-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 200 Response

```json
{
  "data": {
    "transaction": {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "totalPrice": 0,
      "timestamp": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="get-scrap-ship-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully retrieved the amount of value that will be returned when scrapping a ship.|Inline|

<h3 id="get-scrap-ship-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» transaction|[ScrapTransaction](#schemascraptransaction)|true|none|Result of a scrap transaction.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» shipSymbol|string|true|none|The symbol of the ship.|
|»»» totalPrice|integer|true|none|The total price of the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## scrap-ship

<a id="opIdscrap-ship"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/scrap', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/scrap`

*Scrap Ship*

Scrap a ship, removing it from the game and returning a portion of the ship's value to the agent. The ship must be docked in a waypoint that has the `Shipyard` trait in order to use this function. To preview the amount of value that will be returned, use the Get Ship action.

<h3 id="scrap-ship-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 200 Response

```json
{
  "data": {
    "agent": {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    },
    "transaction": {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "totalPrice": 0,
      "timestamp": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="scrap-ship-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ship scrapped successfully.|Inline|

<h3 id="scrap-ship-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» agent|[Agent](#schemaagent)|true|none|Agent details.|
|»»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»»» symbol|string|true|none|Symbol of the agent.|
|»»» headquarters|string|true|none|The headquarters of the agent.|
|»»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»»» startingFaction|string|true|none|The faction the agent started with.|
|»»» shipCount|integer|true|none|How many ships are owned by the agent.|
|»» transaction|[ScrapTransaction](#schemascraptransaction)|true|none|Result of a scrap transaction.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» shipSymbol|string|true|none|The symbol of the ship.|
|»»» totalPrice|integer|true|none|The total price of the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## get-repair-ship

<a id="opIdget-repair-ship"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/repair', headers = headers)

print(r.json())

```

`GET /my/ships/{shipSymbol}/repair`

*Get Repair Ship*

Get the cost of repairing a ship.

<h3 id="get-repair-ship-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 200 Response

```json
{
  "data": {
    "transaction": {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "totalPrice": 0,
      "timestamp": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="get-repair-ship-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully retrieved the cost of repairing a ship.|Inline|

<h3 id="get-repair-ship-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» transaction|[RepairTransaction](#schemarepairtransaction)|true|none|Result of a repair transaction.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» shipSymbol|string|true|none|The symbol of the ship.|
|»»» totalPrice|integer|true|none|The total price of the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

## repair-ship

<a id="opIdrepair-ship"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/my/ships/{shipSymbol}/repair', headers = headers)

print(r.json())

```

`POST /my/ships/{shipSymbol}/repair`

*Repair Ship*

Repair a ship, restoring the ship to maximum condition. The ship must be docked at a waypoint that has the `Shipyard` trait in order to use this function. To preview the cost of repairing the ship, use the Get action.

<h3 id="repair-ship-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|shipSymbol|path|string|true|The ship symbol.|

> Example responses

> 200 Response

```json
{
  "data": {
    "agent": {
      "accountId": "string",
      "symbol": "string",
      "headquarters": "string",
      "credits": 0,
      "startingFaction": "string",
      "shipCount": 0
    },
    "ship": {
      "symbol": "string",
      "registration": {
        "name": "string",
        "factionSymbol": "string",
        "role": "FABRICATOR"
      },
      "nav": {
        "systemSymbol": "string",
        "waypointSymbol": "string",
        "route": {
          "destination": {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0
          },
          "origin": {
            "symbol": "string",
            "type": "PLANET",
            "systemSymbol": "string",
            "x": 0,
            "y": 0
          },
          "departureTime": "2019-08-24T14:15:22Z",
          "arrival": "2019-08-24T14:15:22Z"
        },
        "status": "IN_TRANSIT",
        "flightMode": "DRIFT"
      },
      "crew": {
        "current": 0,
        "required": 0,
        "capacity": 0,
        "rotation": "STRICT",
        "morale": 100,
        "wages": 0
      },
      "frame": {
        "symbol": "FRAME_PROBE",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "moduleSlots": 0,
        "mountingPoints": 0,
        "fuelCapacity": 0,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "reactor": {
        "symbol": "REACTOR_SOLAR_I",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "powerOutput": 1,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "engine": {
        "symbol": "ENGINE_IMPULSE_DRIVE_I",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "speed": 1,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "cooldown": {
        "shipSymbol": "string",
        "totalSeconds": 0,
        "remainingSeconds": 0,
        "expiration": "2019-08-24T14:15:22Z"
      },
      "modules": [
        {
          "symbol": "MODULE_MINERAL_PROCESSOR_I",
          "capacity": 0,
          "range": 0,
          "name": "string",
          "description": "string",
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        }
      ],
      "mounts": [
        {
          "symbol": "MOUNT_GAS_SIPHON_I",
          "name": "string",
          "description": "string",
          "strength": 0,
          "deposits": [
            "QUARTZ_SAND"
          ],
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        }
      ],
      "cargo": {
        "capacity": 0,
        "units": 0,
        "inventory": [
          {
            "symbol": "PRECIOUS_STONES",
            "name": "string",
            "description": "string",
            "units": 1
          }
        ]
      },
      "fuel": {
        "current": 0,
        "capacity": 0,
        "consumed": {
          "amount": 0,
          "timestamp": "2019-08-24T14:15:22Z"
        }
      }
    },
    "transaction": {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "totalPrice": 0,
      "timestamp": "2019-08-24T14:15:22Z"
    }
  }
}
```

<h3 id="repair-ship-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ship repaired successfully.|Inline|

<h3 id="repair-ship-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» agent|[Agent](#schemaagent)|true|none|Agent details.|
|»»» accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|»»» symbol|string|true|none|Symbol of the agent.|
|»»» headquarters|string|true|none|The headquarters of the agent.|
|»»» credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|»»» startingFaction|string|true|none|The faction the agent started with.|
|»»» shipCount|integer|true|none|How many ships are owned by the agent.|
|»» ship|[Ship](#schemaship)|true|none|Ship details.|
|»»» symbol|string|true|none|The globally unique identifier of the ship in the following format: `[AGENT_SYMBOL]-[HEX_ID]`|
|»»» registration|[ShipRegistration](#schemashipregistration)|true|none|The public registration information of the ship|
|»»»» name|string|true|none|The agent's registered name of the ship|
|»»»» factionSymbol|string|true|none|The symbol of the faction the ship is registered with|
|»»»» role|[ShipRole](#schemashiprole)|true|none|The registered role of the ship|
|»»» nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»»» route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|»»»»» destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»»» symbol|string|true|none|The symbol of the waypoint.|
|»»»»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»»»»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»»»»»» x|integer|true|none|Position in the universe in the x axis.|
|»»»»»» y|integer|true|none|Position in the universe in the y axis.|
|»»»»» origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|»»»»» departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|»»»»» arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|
|»»»» status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|»»»» flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|
|»»» crew|[ShipCrew](#schemashipcrew)|true|none|The ship's crew service and maintain the ship's systems and equipment.|
|»»»» current|integer|true|none|The current number of crew members on the ship.|
|»»»» required|integer|true|none|The minimum number of crew members required to maintain the ship.|
|»»»» capacity|integer|true|none|The maximum number of crew members the ship can support.|
|»»»» rotation|string|true|none|The rotation of crew shifts. A stricter shift improves the ship's performance. A more relaxed shift improves the crew's morale.|
|»»»» morale|integer|true|none|A rough measure of the crew's morale. A higher morale means the crew is happier and more productive. A lower morale means the ship is more prone to accidents.|
|»»»» wages|integer|true|none|The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint.|
|»»» frame|[ShipFrame](#schemashipframe)|true|none|The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.|
|»»»» symbol|string|true|none|Symbol of the frame.|
|»»»» name|string|true|none|Name of the frame.|
|»»»» description|string|true|none|Description of the frame.|
|»»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»»» moduleSlots|integer|true|none|The amount of slots that can be dedicated to modules installed in the ship. Each installed module take up a number of slots, and once there are no more slots, no new modules can be installed.|
|»»»» mountingPoints|integer|true|none|The amount of slots that can be dedicated to mounts installed in the ship. Each installed mount takes up a number of points, and once there are no more points remaining, no new mounts can be installed.|
|»»»» fuelCapacity|integer|true|none|The maximum amount of fuel that can be stored in this ship. When refueling, the ship will be refueled to this amount.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»»»» power|integer|false|none|The amount of power required from the reactor.|
|»»»»» crew|integer|false|none|The number of crew required for operation.|
|»»»»» slots|integer|false|none|The number of module slots required for installation.|
|»»» reactor|[ShipReactor](#schemashipreactor)|true|none|The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.|
|»»»» symbol|string|true|none|Symbol of the reactor.|
|»»»» name|string|true|none|Name of the reactor.|
|»»»» description|string|true|none|Description of the reactor.|
|»»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»»» powerOutput|integer|true|none|The amount of power provided by this reactor. The more power a reactor provides to the ship, the lower the cooldown it gets when using a module or mount that taxes the ship's power.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» engine|[ShipEngine](#schemashipengine)|true|none|The engine determines how quickly a ship travels between waypoints.|
|»»»» symbol|string|true|none|The symbol of the engine.|
|»»»» name|string|true|none|The name of the engine.|
|»»»» description|string|true|none|The description of the engine.|
|»»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»»» speed|integer|true|none|The speed stat of this engine. The higher the speed, the faster a ship can travel from one point to another. Reduces the time of arrival when navigating the ship.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|»»»» shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|»»»» totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|»»»» remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|»»»» expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|
|»»» modules|[[ShipModule](#schemashipmodule)]|true|none|Modules installed in this ship.|
|»»»» symbol|string|true|none|The symbol of the module.|
|»»»» capacity|integer|false|none|Modules that provide capacity, such as cargo hold or crew quarters will show this value to denote how much of a bonus the module grants.|
|»»»» range|integer|false|none|Modules that have a range will such as a sensor array show this value to denote how far can the module reach with its capabilities.|
|»»»» name|string|true|none|Name of this module.|
|»»»» description|string|true|none|Description of this module.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» mounts|[[ShipMount](#schemashipmount)]|true|none|Mounts installed in this ship.|
|»»»» symbol|string|true|none|Symbo of this mount.|
|»»»» name|string|true|none|Name of this mount.|
|»»»» description|string|false|none|Description of this mount.|
|»»»» strength|integer|false|none|Mounts that have this value, such as mining lasers, denote how powerful this mount's capabilities are.|
|»»»» deposits|[string]|false|none|Mounts that have this value denote what goods can be produced from using the mount.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»»» name|string|true|none|The name of the cargo item type.|
|»»»»» description|string|true|none|The description of the cargo item type.|
|»»»»» units|integer|true|none|The number of units of the cargo item.|
|»»» fuel|[ShipFuel](#schemashipfuel)|true|none|Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.|
|»»»» current|integer|true|none|The current amount of fuel in the ship's tanks.|
|»»»» capacity|integer|true|none|The maximum amount of fuel the ship's tanks can hold.|
|»»»» consumed|object|false|none|An object that only shows up when an action has consumed fuel in the process. Shows the fuel consumption data.|
|»»»»» amount|integer|true|none|The amount of fuel consumed by the most recent transit or action.|
|»»»»» timestamp|string(date-time)|true|none|The time at which the fuel was consumed.|
|»» transaction|[RepairTransaction](#schemarepairtransaction)|true|none|Result of a repair transaction.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» shipSymbol|string|true|none|The symbol of the ship.|
|»»» totalPrice|integer|true|none|The total price of the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|

#### Enumerated Values

|Property|Value|
|---|---|
|role|FABRICATOR|
|role|HARVESTER|
|role|HAULER|
|role|INTERCEPTOR|
|role|EXCAVATOR|
|role|TRANSPORT|
|role|REPAIR|
|role|SURVEYOR|
|role|COMMAND|
|role|CARRIER|
|role|PATROL|
|role|SATELLITE|
|role|EXPLORER|
|role|REFINERY|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|status|IN_TRANSIT|
|status|IN_ORBIT|
|status|DOCKED|
|flightMode|DRIFT|
|flightMode|STEALTH|
|flightMode|CRUISE|
|flightMode|BURN|
|rotation|STRICT|
|rotation|RELAXED|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

<h1 id="spacetraders-api-systems">Systems</h1>

Systems

## get-systems

<a id="opIdget-systems"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.spacetraders.io/v2/systems', headers = headers)

print(r.json())

```

`GET /systems`

*List Systems*

Return a paginated list of all systems.

<h3 id="get-systems-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|What entry offset to request|
|limit|query|integer|false|How many entries to return per page|

> Example responses

> 200 Response

```json
{
  "data": [
    {
      "symbol": "string",
      "sectorSymbol": "string",
      "type": "NEUTRON_STAR",
      "x": 0,
      "y": 0,
      "waypoints": [
        {
          "symbol": "string",
          "type": "PLANET",
          "x": 0,
          "y": 0,
          "orbitals": [
            {
              "symbol": "string"
            }
          ],
          "orbits": "string"
        }
      ],
      "factions": [
        {
          "symbol": "COSMIC"
        }
      ]
    }
  ],
  "meta": {
    "total": 0,
    "page": 1,
    "limit": 10
  }
}
```

<h3 id="get-systems-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully listed systems.|Inline|

<h3 id="get-systems-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[[System](#schemasystem)]|true|none|none|
|»» symbol|string|true|none|The symbol of the system.|
|»» sectorSymbol|string|true|none|The symbol of the sector.|
|»» type|[SystemType](#schemasystemtype)|true|none|The type of system.|
|»» x|integer|true|none|Relative position of the system in the sector in the x axis.|
|»» y|integer|true|none|Relative position of the system in the sector in the y axis.|
|»» waypoints|[[SystemWaypoint](#schemasystemwaypoint)]|true|none|Waypoints in this system.|
|»»» symbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»» x|integer|true|none|Relative position of the waypoint on the system's x axis. This is not an absolute position in the universe.|
|»»» y|integer|true|none|Relative position of the waypoint on the system's y axis. This is not an absolute position in the universe.|
|»»» orbitals|[[WaypointOrbital](#schemawaypointorbital)]|true|none|Waypoints that orbit this waypoint.|
|»»»» symbol|string|true|none|The symbol of the orbiting waypoint.|
|»»» orbits|string|false|none|The symbol of the parent waypoint, if this waypoint is in orbit around another waypoint. Otherwise this value is undefined.|
|»» factions|[[SystemFaction](#schemasystemfaction)]|true|none|Factions that control this system.|
|»»» symbol|[FactionSymbol](#schemafactionsymbol)|true|none|The symbol of the faction.|
|» meta|[Meta](#schemameta)|true|none|Meta details for pagination.|
|»» total|integer|true|none|Shows the total amount of items of this kind that exist.|
|»» page|integer|true|none|A page denotes an amount of items, offset from the first item. Each page holds an amount of items equal to the `limit`.|
|»» limit|integer|true|none|The amount of items in each page. Limits how many items can be fetched at once.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|NEUTRON_STAR|
|type|RED_STAR|
|type|ORANGE_STAR|
|type|BLUE_STAR|
|type|YOUNG_STAR|
|type|WHITE_DWARF|
|type|BLACK_HOLE|
|type|HYPERGIANT|
|type|NEBULA|
|type|UNSTABLE|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|symbol|COSMIC|
|symbol|VOID|
|symbol|GALACTIC|
|symbol|QUANTUM|
|symbol|DOMINION|
|symbol|ASTRO|
|symbol|CORSAIRS|
|symbol|OBSIDIAN|
|symbol|AEGIS|
|symbol|UNITED|
|symbol|SOLITARY|
|symbol|COBALT|
|symbol|OMEGA|
|symbol|ECHO|
|symbol|LORDS|
|symbol|CULT|
|symbol|ANCIENTS|
|symbol|SHADOW|
|symbol|ETHEREAL|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, AgentToken
</aside>

## get-system

<a id="opIdget-system"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.spacetraders.io/v2/systems/{systemSymbol}', headers = headers)

print(r.json())

```

`GET /systems/{systemSymbol}`

*Get System*

Get the details of a system.

<h3 id="get-system-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|systemSymbol|path|string|true|The system symbol|

> Example responses

> 200 Response

```json
{
  "data": {
    "symbol": "string",
    "sectorSymbol": "string",
    "type": "NEUTRON_STAR",
    "x": 0,
    "y": 0,
    "waypoints": [
      {
        "symbol": "string",
        "type": "PLANET",
        "x": 0,
        "y": 0,
        "orbitals": [
          {
            "symbol": "string"
          }
        ],
        "orbits": "string"
      }
    ],
    "factions": [
      {
        "symbol": "COSMIC"
      }
    ]
  }
}
```

<h3 id="get-system-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched the system.|Inline|

<h3 id="get-system-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[System](#schemasystem)|true|none|none|
|»» symbol|string|true|none|The symbol of the system.|
|»» sectorSymbol|string|true|none|The symbol of the sector.|
|»» type|[SystemType](#schemasystemtype)|true|none|The type of system.|
|»» x|integer|true|none|Relative position of the system in the sector in the x axis.|
|»» y|integer|true|none|Relative position of the system in the sector in the y axis.|
|»» waypoints|[[SystemWaypoint](#schemasystemwaypoint)]|true|none|Waypoints in this system.|
|»»» symbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»»» x|integer|true|none|Relative position of the waypoint on the system's x axis. This is not an absolute position in the universe.|
|»»» y|integer|true|none|Relative position of the waypoint on the system's y axis. This is not an absolute position in the universe.|
|»»» orbitals|[[WaypointOrbital](#schemawaypointorbital)]|true|none|Waypoints that orbit this waypoint.|
|»»»» symbol|string|true|none|The symbol of the orbiting waypoint.|
|»»» orbits|string|false|none|The symbol of the parent waypoint, if this waypoint is in orbit around another waypoint. Otherwise this value is undefined.|
|»» factions|[[SystemFaction](#schemasystemfaction)]|true|none|Factions that control this system.|
|»»» symbol|[FactionSymbol](#schemafactionsymbol)|true|none|The symbol of the faction.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|NEUTRON_STAR|
|type|RED_STAR|
|type|ORANGE_STAR|
|type|BLUE_STAR|
|type|YOUNG_STAR|
|type|WHITE_DWARF|
|type|BLACK_HOLE|
|type|HYPERGIANT|
|type|NEBULA|
|type|UNSTABLE|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|symbol|COSMIC|
|symbol|VOID|
|symbol|GALACTIC|
|symbol|QUANTUM|
|symbol|DOMINION|
|symbol|ASTRO|
|symbol|CORSAIRS|
|symbol|OBSIDIAN|
|symbol|AEGIS|
|symbol|UNITED|
|symbol|SOLITARY|
|symbol|COBALT|
|symbol|OMEGA|
|symbol|ECHO|
|symbol|LORDS|
|symbol|CULT|
|symbol|ANCIENTS|
|symbol|SHADOW|
|symbol|ETHEREAL|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, AgentToken
</aside>

## get-system-waypoints

<a id="opIdget-system-waypoints"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.spacetraders.io/v2/systems/{systemSymbol}/waypoints', headers = headers)

print(r.json())

```

`GET /systems/{systemSymbol}/waypoints`

*List Waypoints in System*

Return a paginated list of all of the waypoints for a given system.

If a waypoint is uncharted, it will return the `Uncharted` trait instead of its actual traits.

<h3 id="get-system-waypoints-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|What entry offset to request|
|limit|query|integer|false|How many entries to return per page|
|type|query|[WaypointType](#schemawaypointtype)|false|Filter waypoints by type.|
|traits|query|any|false|Filter waypoints by one or more traits.|
|systemSymbol|path|string|true|The system symbol|

#### Enumerated Values

|Parameter|Value|
|---|---|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|

> Example responses

> 200 Response

```json
{
  "data": [
    {
      "symbol": "string",
      "type": "PLANET",
      "systemSymbol": "string",
      "x": 0,
      "y": 0,
      "orbitals": [
        {
          "symbol": "string"
        }
      ],
      "orbits": "string",
      "faction": {
        "symbol": "COSMIC"
      },
      "traits": [
        {
          "symbol": "UNCHARTED",
          "name": "string",
          "description": "string"
        }
      ],
      "modifiers": [
        {
          "symbol": "STRIPPED",
          "name": "string",
          "description": "string"
        }
      ],
      "chart": {
        "waypointSymbol": "string",
        "submittedBy": "string",
        "submittedOn": "2019-08-24T14:15:22Z"
      },
      "isUnderConstruction": true
    }
  ],
  "meta": {
    "total": 0,
    "page": 1,
    "limit": 10
  }
}
```

<h3 id="get-system-waypoints-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched all waypoints in the system.|Inline|

<h3 id="get-system-waypoints-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[[Waypoint](#schemawaypoint)]|true|none|[A waypoint is a location that ships can travel to such as a Planet, Moon or Space Station.]|
|»» symbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»» x|integer|true|none|Relative position of the waypoint on the system's x axis. This is not an absolute position in the universe.|
|»» y|integer|true|none|Relative position of the waypoint on the system's y axis. This is not an absolute position in the universe.|
|»» orbitals|[[WaypointOrbital](#schemawaypointorbital)]|true|none|Waypoints that orbit this waypoint.|
|»»» symbol|string|true|none|The symbol of the orbiting waypoint.|
|»» orbits|string|false|none|The symbol of the parent waypoint, if this waypoint is in orbit around another waypoint. Otherwise this value is undefined.|
|»» faction|[WaypointFaction](#schemawaypointfaction)|false|none|The faction that controls the waypoint.|
|»»» symbol|[FactionSymbol](#schemafactionsymbol)|true|none|The symbol of the faction.|
|»» traits|[[WaypointTrait](#schemawaypointtrait)]|true|none|The traits of the waypoint.|
|»»» symbol|[WaypointTraitSymbol](#schemawaypointtraitsymbol)|true|none|The unique identifier of the trait.|
|»»» name|string|true|none|The name of the trait.|
|»»» description|string|true|none|A description of the trait.|
|»» modifiers|[[WaypointModifier](#schemawaypointmodifier)]|false|none|The modifiers of the waypoint.|
|»»» symbol|[WaypointModifierSymbol](#schemawaypointmodifiersymbol)|true|none|The unique identifier of the modifier.|
|»»» name|string|true|none|The name of the trait.|
|»»» description|string|true|none|A description of the trait.|
|»» chart|[Chart](#schemachart)|false|none|The chart of a system or waypoint, which makes the location visible to other agents.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|false|none|The symbol of the waypoint.|
|»»» submittedBy|string|false|none|The agent that submitted the chart for this waypoint.|
|»»» submittedOn|string(date-time)|false|none|The time the chart for this waypoint was submitted.|
|»» isUnderConstruction|boolean|true|none|True if the waypoint is under construction.|
|» meta|[Meta](#schemameta)|true|none|Meta details for pagination.|
|»» total|integer|true|none|Shows the total amount of items of this kind that exist.|
|»» page|integer|true|none|A page denotes an amount of items, offset from the first item. Each page holds an amount of items equal to the `limit`.|
|»» limit|integer|true|none|The amount of items in each page. Limits how many items can be fetched at once.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|symbol|COSMIC|
|symbol|VOID|
|symbol|GALACTIC|
|symbol|QUANTUM|
|symbol|DOMINION|
|symbol|ASTRO|
|symbol|CORSAIRS|
|symbol|OBSIDIAN|
|symbol|AEGIS|
|symbol|UNITED|
|symbol|SOLITARY|
|symbol|COBALT|
|symbol|OMEGA|
|symbol|ECHO|
|symbol|LORDS|
|symbol|CULT|
|symbol|ANCIENTS|
|symbol|SHADOW|
|symbol|ETHEREAL|
|symbol|UNCHARTED|
|symbol|UNDER_CONSTRUCTION|
|symbol|MARKETPLACE|
|symbol|SHIPYARD|
|symbol|OUTPOST|
|symbol|SCATTERED_SETTLEMENTS|
|symbol|SPRAWLING_CITIES|
|symbol|MEGA_STRUCTURES|
|symbol|PIRATE_BASE|
|symbol|OVERCROWDED|
|symbol|HIGH_TECH|
|symbol|CORRUPT|
|symbol|BUREAUCRATIC|
|symbol|TRADING_HUB|
|symbol|INDUSTRIAL|
|symbol|BLACK_MARKET|
|symbol|RESEARCH_FACILITY|
|symbol|MILITARY_BASE|
|symbol|SURVEILLANCE_OUTPOST|
|symbol|EXPLORATION_OUTPOST|
|symbol|MINERAL_DEPOSITS|
|symbol|COMMON_METAL_DEPOSITS|
|symbol|PRECIOUS_METAL_DEPOSITS|
|symbol|RARE_METAL_DEPOSITS|
|symbol|METHANE_POOLS|
|symbol|ICE_CRYSTALS|
|symbol|EXPLOSIVE_GASES|
|symbol|STRONG_MAGNETOSPHERE|
|symbol|VIBRANT_AURORAS|
|symbol|SALT_FLATS|
|symbol|CANYONS|
|symbol|PERPETUAL_DAYLIGHT|
|symbol|PERPETUAL_OVERCAST|
|symbol|DRY_SEABEDS|
|symbol|MAGMA_SEAS|
|symbol|SUPERVOLCANOES|
|symbol|ASH_CLOUDS|
|symbol|VAST_RUINS|
|symbol|MUTATED_FLORA|
|symbol|TERRAFORMED|
|symbol|EXTREME_TEMPERATURES|
|symbol|EXTREME_PRESSURE|
|symbol|DIVERSE_LIFE|
|symbol|SCARCE_LIFE|
|symbol|FOSSILS|
|symbol|WEAK_GRAVITY|
|symbol|STRONG_GRAVITY|
|symbol|CRUSHING_GRAVITY|
|symbol|TOXIC_ATMOSPHERE|
|symbol|CORROSIVE_ATMOSPHERE|
|symbol|BREATHABLE_ATMOSPHERE|
|symbol|THIN_ATMOSPHERE|
|symbol|JOVIAN|
|symbol|ROCKY|
|symbol|VOLCANIC|
|symbol|FROZEN|
|symbol|SWAMP|
|symbol|BARREN|
|symbol|TEMPERATE|
|symbol|JUNGLE|
|symbol|OCEAN|
|symbol|RADIOACTIVE|
|symbol|MICRO_GRAVITY_ANOMALIES|
|symbol|DEBRIS_CLUSTER|
|symbol|DEEP_CRATERS|
|symbol|SHALLOW_CRATERS|
|symbol|UNSTABLE_COMPOSITION|
|symbol|HOLLOWED_INTERIOR|
|symbol|STRIPPED|
|symbol|STRIPPED|
|symbol|UNSTABLE|
|symbol|RADIATION_LEAK|
|symbol|CRITICAL_LIMIT|
|symbol|CIVIL_UNREST|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, AgentToken
</aside>

## get-waypoint

<a id="opIdget-waypoint"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.spacetraders.io/v2/systems/{systemSymbol}/waypoints/{waypointSymbol}', headers = headers)

print(r.json())

```

`GET /systems/{systemSymbol}/waypoints/{waypointSymbol}`

*Get Waypoint*

View the details of a waypoint.

If the waypoint is uncharted, it will return the 'Uncharted' trait instead of its actual traits.

<h3 id="get-waypoint-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|systemSymbol|path|string|true|The system symbol|
|waypointSymbol|path|string|true|The waypoint symbol|

> Example responses

> 200 Response

```json
{
  "data": {
    "symbol": "string",
    "type": "PLANET",
    "systemSymbol": "string",
    "x": 0,
    "y": 0,
    "orbitals": [
      {
        "symbol": "string"
      }
    ],
    "orbits": "string",
    "faction": {
      "symbol": "COSMIC"
    },
    "traits": [
      {
        "symbol": "UNCHARTED",
        "name": "string",
        "description": "string"
      }
    ],
    "modifiers": [
      {
        "symbol": "STRIPPED",
        "name": "string",
        "description": "string"
      }
    ],
    "chart": {
      "waypointSymbol": "string",
      "submittedBy": "string",
      "submittedOn": "2019-08-24T14:15:22Z"
    },
    "isUnderConstruction": true
  }
}
```

<h3 id="get-waypoint-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched waypoint.|Inline|

<h3 id="get-waypoint-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[Waypoint](#schemawaypoint)|true|none|A waypoint is a location that ships can travel to such as a Planet, Moon or Space Station.|
|»» symbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»» type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|»» systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|»» x|integer|true|none|Relative position of the waypoint on the system's x axis. This is not an absolute position in the universe.|
|»» y|integer|true|none|Relative position of the waypoint on the system's y axis. This is not an absolute position in the universe.|
|»» orbitals|[[WaypointOrbital](#schemawaypointorbital)]|true|none|Waypoints that orbit this waypoint.|
|»»» symbol|string|true|none|The symbol of the orbiting waypoint.|
|»» orbits|string|false|none|The symbol of the parent waypoint, if this waypoint is in orbit around another waypoint. Otherwise this value is undefined.|
|»» faction|[WaypointFaction](#schemawaypointfaction)|false|none|The faction that controls the waypoint.|
|»»» symbol|[FactionSymbol](#schemafactionsymbol)|true|none|The symbol of the faction.|
|»» traits|[[WaypointTrait](#schemawaypointtrait)]|true|none|The traits of the waypoint.|
|»»» symbol|[WaypointTraitSymbol](#schemawaypointtraitsymbol)|true|none|The unique identifier of the trait.|
|»»» name|string|true|none|The name of the trait.|
|»»» description|string|true|none|A description of the trait.|
|»» modifiers|[[WaypointModifier](#schemawaypointmodifier)]|false|none|The modifiers of the waypoint.|
|»»» symbol|[WaypointModifierSymbol](#schemawaypointmodifiersymbol)|true|none|The unique identifier of the modifier.|
|»»» name|string|true|none|The name of the trait.|
|»»» description|string|true|none|A description of the trait.|
|»» chart|[Chart](#schemachart)|false|none|The chart of a system or waypoint, which makes the location visible to other agents.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|false|none|The symbol of the waypoint.|
|»»» submittedBy|string|false|none|The agent that submitted the chart for this waypoint.|
|»»» submittedOn|string(date-time)|false|none|The time the chart for this waypoint was submitted.|
|»» isUnderConstruction|boolean|true|none|True if the waypoint is under construction.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PLANET|
|type|GAS_GIANT|
|type|MOON|
|type|ORBITAL_STATION|
|type|JUMP_GATE|
|type|ASTEROID_FIELD|
|type|ASTEROID|
|type|ENGINEERED_ASTEROID|
|type|ASTEROID_BASE|
|type|NEBULA|
|type|DEBRIS_FIELD|
|type|GRAVITY_WELL|
|type|ARTIFICIAL_GRAVITY_WELL|
|type|FUEL_STATION|
|symbol|COSMIC|
|symbol|VOID|
|symbol|GALACTIC|
|symbol|QUANTUM|
|symbol|DOMINION|
|symbol|ASTRO|
|symbol|CORSAIRS|
|symbol|OBSIDIAN|
|symbol|AEGIS|
|symbol|UNITED|
|symbol|SOLITARY|
|symbol|COBALT|
|symbol|OMEGA|
|symbol|ECHO|
|symbol|LORDS|
|symbol|CULT|
|symbol|ANCIENTS|
|symbol|SHADOW|
|symbol|ETHEREAL|
|symbol|UNCHARTED|
|symbol|UNDER_CONSTRUCTION|
|symbol|MARKETPLACE|
|symbol|SHIPYARD|
|symbol|OUTPOST|
|symbol|SCATTERED_SETTLEMENTS|
|symbol|SPRAWLING_CITIES|
|symbol|MEGA_STRUCTURES|
|symbol|PIRATE_BASE|
|symbol|OVERCROWDED|
|symbol|HIGH_TECH|
|symbol|CORRUPT|
|symbol|BUREAUCRATIC|
|symbol|TRADING_HUB|
|symbol|INDUSTRIAL|
|symbol|BLACK_MARKET|
|symbol|RESEARCH_FACILITY|
|symbol|MILITARY_BASE|
|symbol|SURVEILLANCE_OUTPOST|
|symbol|EXPLORATION_OUTPOST|
|symbol|MINERAL_DEPOSITS|
|symbol|COMMON_METAL_DEPOSITS|
|symbol|PRECIOUS_METAL_DEPOSITS|
|symbol|RARE_METAL_DEPOSITS|
|symbol|METHANE_POOLS|
|symbol|ICE_CRYSTALS|
|symbol|EXPLOSIVE_GASES|
|symbol|STRONG_MAGNETOSPHERE|
|symbol|VIBRANT_AURORAS|
|symbol|SALT_FLATS|
|symbol|CANYONS|
|symbol|PERPETUAL_DAYLIGHT|
|symbol|PERPETUAL_OVERCAST|
|symbol|DRY_SEABEDS|
|symbol|MAGMA_SEAS|
|symbol|SUPERVOLCANOES|
|symbol|ASH_CLOUDS|
|symbol|VAST_RUINS|
|symbol|MUTATED_FLORA|
|symbol|TERRAFORMED|
|symbol|EXTREME_TEMPERATURES|
|symbol|EXTREME_PRESSURE|
|symbol|DIVERSE_LIFE|
|symbol|SCARCE_LIFE|
|symbol|FOSSILS|
|symbol|WEAK_GRAVITY|
|symbol|STRONG_GRAVITY|
|symbol|CRUSHING_GRAVITY|
|symbol|TOXIC_ATMOSPHERE|
|symbol|CORROSIVE_ATMOSPHERE|
|symbol|BREATHABLE_ATMOSPHERE|
|symbol|THIN_ATMOSPHERE|
|symbol|JOVIAN|
|symbol|ROCKY|
|symbol|VOLCANIC|
|symbol|FROZEN|
|symbol|SWAMP|
|symbol|BARREN|
|symbol|TEMPERATE|
|symbol|JUNGLE|
|symbol|OCEAN|
|symbol|RADIOACTIVE|
|symbol|MICRO_GRAVITY_ANOMALIES|
|symbol|DEBRIS_CLUSTER|
|symbol|DEEP_CRATERS|
|symbol|SHALLOW_CRATERS|
|symbol|UNSTABLE_COMPOSITION|
|symbol|HOLLOWED_INTERIOR|
|symbol|STRIPPED|
|symbol|STRIPPED|
|symbol|UNSTABLE|
|symbol|RADIATION_LEAK|
|symbol|CRITICAL_LIMIT|
|symbol|CIVIL_UNREST|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, AgentToken
</aside>

## get-market

<a id="opIdget-market"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.spacetraders.io/v2/systems/{systemSymbol}/waypoints/{waypointSymbol}/market', headers = headers)

print(r.json())

```

`GET /systems/{systemSymbol}/waypoints/{waypointSymbol}/market`

*Get Market*

Retrieve imports, exports and exchange data from a marketplace. Requires a waypoint that has the `Marketplace` trait to use.

Send a ship to the waypoint to access trade good prices and recent transactions. Refer to the [Market Overview page](https://docs.spacetraders.io/game-concepts/markets) to gain better a understanding of the market in the game.

<h3 id="get-market-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|systemSymbol|path|string|true|The system symbol|
|waypointSymbol|path|string|true|The waypoint symbol|

> Example responses

> 200 Response

```json
{
  "data": {
    "symbol": "string",
    "exports": [
      {
        "symbol": "PRECIOUS_STONES",
        "name": "string",
        "description": "string"
      }
    ],
    "imports": [
      {
        "symbol": "PRECIOUS_STONES",
        "name": "string",
        "description": "string"
      }
    ],
    "exchange": [
      {
        "symbol": "PRECIOUS_STONES",
        "name": "string",
        "description": "string"
      }
    ],
    "transactions": [
      {
        "waypointSymbol": "string",
        "shipSymbol": "string",
        "tradeSymbol": "string",
        "type": "PURCHASE",
        "units": 0,
        "pricePerUnit": 0,
        "totalPrice": 0,
        "timestamp": "2019-08-24T14:15:22Z"
      }
    ],
    "tradeGoods": [
      {
        "symbol": "PRECIOUS_STONES",
        "type": "EXPORT",
        "tradeVolume": 1,
        "supply": "SCARCE",
        "activity": "WEAK",
        "purchasePrice": 0,
        "sellPrice": 0
      }
    ]
  }
}
```

<h3 id="get-market-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched the market.|Inline|

<h3 id="get-market-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[Market](#schemamarket)|true|none|none|
|»» symbol|string|true|none|The symbol of the market. The symbol is the same as the waypoint where the market is located.|
|»» exports|[[TradeGood](#schematradegood)]|true|none|The list of goods that are exported from this market.|
|»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»» name|string|true|none|The name of the good.|
|»»» description|string|true|none|The description of the good.|
|»» imports|[[TradeGood](#schematradegood)]|true|none|The list of goods that are sought as imports in this market.|
|»» exchange|[[TradeGood](#schematradegood)]|true|none|The list of goods that are bought and sold between agents at this market.|
|»» transactions|[[MarketTransaction](#schemamarkettransaction)]|false|none|The list of recent transactions at this market. Visible only when a ship is present at the market.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» shipSymbol|string|true|none|The symbol of the ship that made the transaction.|
|»»» tradeSymbol|string|true|none|The symbol of the trade good.|
|»»» type|string|true|none|The type of transaction.|
|»»» units|integer|true|none|The number of units of the transaction.|
|»»» pricePerUnit|integer|true|none|The price per unit of the transaction.|
|»»» totalPrice|integer|true|none|The total price of the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|
|»» tradeGoods|[[MarketTradeGood](#schemamarkettradegood)]|false|none|The list of goods that are traded at this market. Visible only when a ship is present at the market.|
|»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»» type|string|true|none|The type of trade good (export, import, or exchange).|
|»»» tradeVolume|integer|true|none|This is the maximum number of units that can be purchased or sold at this market in a single trade for this good. Trade volume also gives an indication of price volatility. A market with a low trade volume will have large price swings, while high trade volume will be more resilient to price changes.|
|»»» supply|[SupplyLevel](#schemasupplylevel)|true|none|The supply level of a trade good.|
|»»» activity|[ActivityLevel](#schemaactivitylevel)|false|none|The activity level of a trade good. If the good is an import, this represents how strong consumption is. If the good is an export, this represents how strong the production is for the good. When activity is strong, consumption or production is near maximum capacity. When activity is weak, consumption or production is near minimum capacity.|
|»»» purchasePrice|integer|true|none|The price at which this good can be purchased from the market.|
|»»» sellPrice|integer|true|none|The price at which this good can be sold to the market.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|
|type|PURCHASE|
|type|SELL|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|
|type|EXPORT|
|type|IMPORT|
|type|EXCHANGE|
|supply|SCARCE|
|supply|LIMITED|
|supply|MODERATE|
|supply|HIGH|
|supply|ABUNDANT|
|activity|WEAK|
|activity|GROWING|
|activity|STRONG|
|activity|RESTRICTED|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, AgentToken
</aside>

## get-shipyard

<a id="opIdget-shipyard"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.spacetraders.io/v2/systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard', headers = headers)

print(r.json())

```

`GET /systems/{systemSymbol}/waypoints/{waypointSymbol}/shipyard`

*Get Shipyard*

Get the shipyard for a waypoint. Requires a waypoint that has the `Shipyard` trait to use. Send a ship to the waypoint to access data on ships that are currently available for purchase and recent transactions.

<h3 id="get-shipyard-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|systemSymbol|path|string|true|The system symbol|
|waypointSymbol|path|string|true|The waypoint symbol|

> Example responses

> 200 Response

```json
{
  "data": {
    "symbol": "string",
    "shipTypes": [
      {
        "type": "SHIP_PROBE"
      }
    ],
    "transactions": [
      {
        "waypointSymbol": "string",
        "shipSymbol": "string",
        "shipType": "string",
        "price": 0,
        "agentSymbol": "string",
        "timestamp": "2019-08-24T14:15:22Z"
      }
    ],
    "ships": [
      {
        "type": "SHIP_PROBE",
        "name": "string",
        "description": "string",
        "supply": "SCARCE",
        "activity": "WEAK",
        "purchasePrice": 0,
        "frame": {
          "symbol": "FRAME_PROBE",
          "name": "string",
          "description": "string",
          "condition": 1,
          "integrity": 1,
          "moduleSlots": 0,
          "mountingPoints": 0,
          "fuelCapacity": 0,
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        },
        "reactor": {
          "symbol": "REACTOR_SOLAR_I",
          "name": "string",
          "description": "string",
          "condition": 1,
          "integrity": 1,
          "powerOutput": 1,
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        },
        "engine": {
          "symbol": "ENGINE_IMPULSE_DRIVE_I",
          "name": "string",
          "description": "string",
          "condition": 1,
          "integrity": 1,
          "speed": 1,
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        },
        "modules": [
          {
            "symbol": "MODULE_MINERAL_PROCESSOR_I",
            "capacity": 0,
            "range": 0,
            "name": "string",
            "description": "string",
            "requirements": {
              "power": 0,
              "crew": 0,
              "slots": 0
            }
          }
        ],
        "mounts": [
          {
            "symbol": "MOUNT_GAS_SIPHON_I",
            "name": "string",
            "description": "string",
            "strength": 0,
            "deposits": [
              "QUARTZ_SAND"
            ],
            "requirements": {
              "power": 0,
              "crew": 0,
              "slots": 0
            }
          }
        ],
        "crew": {
          "required": 0,
          "capacity": 0
        }
      }
    ],
    "modificationsFee": 0
  }
}
```

<h3 id="get-shipyard-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched the shipyard.|Inline|

<h3 id="get-shipyard-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[Shipyard](#schemashipyard)|true|none|none|
|»» symbol|string|true|none|The symbol of the shipyard. The symbol is the same as the waypoint where the shipyard is located.|
|»» shipTypes|[object]|true|none|The list of ship types available for purchase at this shipyard.|
|»»» type|[ShipType](#schemashiptype)|true|none|Type of ship|
|»» transactions|[[ShipyardTransaction](#schemashipyardtransaction)]|false|none|The list of recent transactions at this shipyard.|
|»»» waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»»» shipSymbol|string|true|none|The symbol of the ship that was the subject of the transaction.|
|»»» shipType|string|true|none|The symbol of the ship that was the subject of the transaction.|
|»»» price|integer|true|none|The price of the transaction.|
|»»» agentSymbol|string|true|none|The symbol of the agent that made the transaction.|
|»»» timestamp|string(date-time)|true|none|The timestamp of the transaction.|
|»» ships|[[ShipyardShip](#schemashipyardship)]|false|none|The ships that are currently available for purchase at the shipyard.|
|»»» type|[ShipType](#schemashiptype)|true|none|Type of ship|
|»»» name|string|true|none|none|
|»»» description|string|true|none|none|
|»»» supply|[SupplyLevel](#schemasupplylevel)|true|none|The supply level of a trade good.|
|»»» activity|[ActivityLevel](#schemaactivitylevel)|false|none|The activity level of a trade good. If the good is an import, this represents how strong consumption is. If the good is an export, this represents how strong the production is for the good. When activity is strong, consumption or production is near maximum capacity. When activity is weak, consumption or production is near minimum capacity.|
|»»» purchasePrice|integer|true|none|none|
|»»» frame|[ShipFrame](#schemashipframe)|true|none|The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.|
|»»»» symbol|string|true|none|Symbol of the frame.|
|»»»» name|string|true|none|Name of the frame.|
|»»»» description|string|true|none|Description of the frame.|
|»»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»»» moduleSlots|integer|true|none|The amount of slots that can be dedicated to modules installed in the ship. Each installed module take up a number of slots, and once there are no more slots, no new modules can be installed.|
|»»»» mountingPoints|integer|true|none|The amount of slots that can be dedicated to mounts installed in the ship. Each installed mount takes up a number of points, and once there are no more points remaining, no new mounts can be installed.|
|»»»» fuelCapacity|integer|true|none|The maximum amount of fuel that can be stored in this ship. When refueling, the ship will be refueled to this amount.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»»»» power|integer|false|none|The amount of power required from the reactor.|
|»»»»» crew|integer|false|none|The number of crew required for operation.|
|»»»»» slots|integer|false|none|The number of module slots required for installation.|
|»»» reactor|[ShipReactor](#schemashipreactor)|true|none|The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.|
|»»»» symbol|string|true|none|Symbol of the reactor.|
|»»»» name|string|true|none|Name of the reactor.|
|»»»» description|string|true|none|Description of the reactor.|
|»»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»»» powerOutput|integer|true|none|The amount of power provided by this reactor. The more power a reactor provides to the ship, the lower the cooldown it gets when using a module or mount that taxes the ship's power.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» engine|[ShipEngine](#schemashipengine)|true|none|The engine determines how quickly a ship travels between waypoints.|
|»»»» symbol|string|true|none|The symbol of the engine.|
|»»»» name|string|true|none|The name of the engine.|
|»»»» description|string|true|none|The description of the engine.|
|»»»» condition|[ShipComponentCondition](#schemashipcomponentcondition)(double)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|»»»» integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)(double)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|»»»» speed|integer|true|none|The speed stat of this engine. The higher the speed, the faster a ship can travel from one point to another. Reduces the time of arrival when navigating the ship.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» modules|[[ShipModule](#schemashipmodule)]|true|none|[A module can be installed in a ship and provides a set of capabilities such as storage space or quarters for crew. Module installations are permanent.]|
|»»»» symbol|string|true|none|The symbol of the module.|
|»»»» capacity|integer|false|none|Modules that provide capacity, such as cargo hold or crew quarters will show this value to denote how much of a bonus the module grants.|
|»»»» range|integer|false|none|Modules that have a range will such as a sensor array show this value to denote how far can the module reach with its capabilities.|
|»»»» name|string|true|none|Name of this module.|
|»»»» description|string|true|none|Description of this module.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» mounts|[[ShipMount](#schemashipmount)]|true|none|[A mount is installed on the exterier of a ship.]|
|»»»» symbol|string|true|none|Symbo of this mount.|
|»»»» name|string|true|none|Name of this mount.|
|»»»» description|string|false|none|Description of this mount.|
|»»»» strength|integer|false|none|Mounts that have this value, such as mining lasers, denote how powerful this mount's capabilities are.|
|»»»» deposits|[string]|false|none|Mounts that have this value denote what goods can be produced from using the mount.|
|»»»» requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|
|»»» crew|object|true|none|none|
|»»»» required|integer|true|none|none|
|»»»» capacity|integer|true|none|none|
|»» modificationsFee|integer|true|none|The fee to modify a ship at this shipyard. This includes installing or removing modules and mounts on a ship. In the case of mounts, the fee is a flat rate per mount. In the case of modules, the fee is per slot the module occupies.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|SHIP_PROBE|
|type|SHIP_MINING_DRONE|
|type|SHIP_SIPHON_DRONE|
|type|SHIP_INTERCEPTOR|
|type|SHIP_LIGHT_HAULER|
|type|SHIP_COMMAND_FRIGATE|
|type|SHIP_EXPLORER|
|type|SHIP_HEAVY_FREIGHTER|
|type|SHIP_LIGHT_SHUTTLE|
|type|SHIP_ORE_HOUND|
|type|SHIP_REFINING_FREIGHTER|
|type|SHIP_SURVEYOR|
|type|SHIP_PROBE|
|type|SHIP_MINING_DRONE|
|type|SHIP_SIPHON_DRONE|
|type|SHIP_INTERCEPTOR|
|type|SHIP_LIGHT_HAULER|
|type|SHIP_COMMAND_FRIGATE|
|type|SHIP_EXPLORER|
|type|SHIP_HEAVY_FREIGHTER|
|type|SHIP_LIGHT_SHUTTLE|
|type|SHIP_ORE_HOUND|
|type|SHIP_REFINING_FREIGHTER|
|type|SHIP_SURVEYOR|
|supply|SCARCE|
|supply|LIMITED|
|supply|MODERATE|
|supply|HIGH|
|supply|ABUNDANT|
|activity|WEAK|
|activity|GROWING|
|activity|STRONG|
|activity|RESTRICTED|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, AgentToken
</aside>

## get-jump-gate

<a id="opIdget-jump-gate"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.spacetraders.io/v2/systems/{systemSymbol}/waypoints/{waypointSymbol}/jump-gate', headers = headers)

print(r.json())

```

`GET /systems/{systemSymbol}/waypoints/{waypointSymbol}/jump-gate`

*Get Jump Gate*

Get jump gate details for a waypoint. Requires a waypoint of type `JUMP_GATE` to use.

Waypoints connected to this jump gate can be 

<h3 id="get-jump-gate-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|systemSymbol|path|string|true|The system symbol|
|waypointSymbol|path|string|true|The waypoint symbol|

> Example responses

> 200 Response

```json
{
  "data": {
    "symbol": "string",
    "connections": [
      "string"
    ]
  }
}
```

<h3 id="get-jump-gate-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched jump gate.|Inline|

<h3 id="get-jump-gate-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[JumpGate](#schemajumpgate)|true|none|none|
|»» symbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|»» connections|[string]|true|none|All the gates that are connected to this waypoint.|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, AgentToken
</aside>

## get-construction

<a id="opIdget-construction"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.spacetraders.io/v2/systems/{systemSymbol}/waypoints/{waypointSymbol}/construction', headers = headers)

print(r.json())

```

`GET /systems/{systemSymbol}/waypoints/{waypointSymbol}/construction`

*Get Construction Site*

Get construction details for a waypoint. Requires a waypoint with a property of `isUnderConstruction` to be true.

<h3 id="get-construction-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|systemSymbol|path|string|true|The system symbol|
|waypointSymbol|path|string|true|The waypoint symbol|

> Example responses

> 200 Response

```json
{
  "data": {
    "symbol": "string",
    "materials": [
      {
        "tradeSymbol": "PRECIOUS_STONES",
        "required": 0,
        "fulfilled": 0
      }
    ],
    "isComplete": true
  }
}
```

<h3 id="get-construction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successfully fetched construction site.|Inline|

<h3 id="get-construction-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|[Construction](#schemaconstruction)|true|none|The construction details of a waypoint.|
|»» symbol|string|true|none|The symbol of the waypoint.|
|»» materials|[[ConstructionMaterial](#schemaconstructionmaterial)]|true|none|The materials required to construct the waypoint.|
|»»» tradeSymbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»» required|integer|true|none|The number of units required.|
|»»» fulfilled|integer|true|none|The number of units fulfilled toward the required amount.|
|»» isComplete|boolean|true|none|Whether the waypoint has been constructed.|

#### Enumerated Values

|Property|Value|
|---|---|
|tradeSymbol|PRECIOUS_STONES|
|tradeSymbol|QUARTZ_SAND|
|tradeSymbol|SILICON_CRYSTALS|
|tradeSymbol|AMMONIA_ICE|
|tradeSymbol|LIQUID_HYDROGEN|
|tradeSymbol|LIQUID_NITROGEN|
|tradeSymbol|ICE_WATER|
|tradeSymbol|EXOTIC_MATTER|
|tradeSymbol|ADVANCED_CIRCUITRY|
|tradeSymbol|GRAVITON_EMITTERS|
|tradeSymbol|IRON|
|tradeSymbol|IRON_ORE|
|tradeSymbol|COPPER|
|tradeSymbol|COPPER_ORE|
|tradeSymbol|ALUMINUM|
|tradeSymbol|ALUMINUM_ORE|
|tradeSymbol|SILVER|
|tradeSymbol|SILVER_ORE|
|tradeSymbol|GOLD|
|tradeSymbol|GOLD_ORE|
|tradeSymbol|PLATINUM|
|tradeSymbol|PLATINUM_ORE|
|tradeSymbol|DIAMONDS|
|tradeSymbol|URANITE|
|tradeSymbol|URANITE_ORE|
|tradeSymbol|MERITIUM|
|tradeSymbol|MERITIUM_ORE|
|tradeSymbol|HYDROCARBON|
|tradeSymbol|ANTIMATTER|
|tradeSymbol|FAB_MATS|
|tradeSymbol|FERTILIZERS|
|tradeSymbol|FABRICS|
|tradeSymbol|FOOD|
|tradeSymbol|JEWELRY|
|tradeSymbol|MACHINERY|
|tradeSymbol|FIREARMS|
|tradeSymbol|ASSAULT_RIFLES|
|tradeSymbol|MILITARY_EQUIPMENT|
|tradeSymbol|EXPLOSIVES|
|tradeSymbol|LAB_INSTRUMENTS|
|tradeSymbol|AMMUNITION|
|tradeSymbol|ELECTRONICS|
|tradeSymbol|SHIP_PLATING|
|tradeSymbol|SHIP_PARTS|
|tradeSymbol|EQUIPMENT|
|tradeSymbol|FUEL|
|tradeSymbol|MEDICINE|
|tradeSymbol|DRUGS|
|tradeSymbol|CLOTHING|
|tradeSymbol|MICROPROCESSORS|
|tradeSymbol|PLASTICS|
|tradeSymbol|POLYNUCLEOTIDES|
|tradeSymbol|BIOCOMPOSITES|
|tradeSymbol|QUANTUM_STABILIZERS|
|tradeSymbol|NANOBOTS|
|tradeSymbol|AI_MAINFRAMES|
|tradeSymbol|QUANTUM_DRIVES|
|tradeSymbol|ROBOTIC_DRONES|
|tradeSymbol|CYBER_IMPLANTS|
|tradeSymbol|GENE_THERAPEUTICS|
|tradeSymbol|NEURAL_CHIPS|
|tradeSymbol|MOOD_REGULATORS|
|tradeSymbol|VIRAL_AGENTS|
|tradeSymbol|MICRO_FUSION_GENERATORS|
|tradeSymbol|SUPERGRAINS|
|tradeSymbol|LASER_RIFLES|
|tradeSymbol|HOLOGRAPHICS|
|tradeSymbol|SHIP_SALVAGE|
|tradeSymbol|RELIC_TECH|
|tradeSymbol|NOVEL_LIFEFORMS|
|tradeSymbol|BOTANICAL_SPECIMENS|
|tradeSymbol|CULTURAL_ARTIFACTS|
|tradeSymbol|FRAME_PROBE|
|tradeSymbol|FRAME_DRONE|
|tradeSymbol|FRAME_INTERCEPTOR|
|tradeSymbol|FRAME_RACER|
|tradeSymbol|FRAME_FIGHTER|
|tradeSymbol|FRAME_FRIGATE|
|tradeSymbol|FRAME_SHUTTLE|
|tradeSymbol|FRAME_EXPLORER|
|tradeSymbol|FRAME_MINER|
|tradeSymbol|FRAME_LIGHT_FREIGHTER|
|tradeSymbol|FRAME_HEAVY_FREIGHTER|
|tradeSymbol|FRAME_TRANSPORT|
|tradeSymbol|FRAME_DESTROYER|
|tradeSymbol|FRAME_CRUISER|
|tradeSymbol|FRAME_CARRIER|
|tradeSymbol|REACTOR_SOLAR_I|
|tradeSymbol|REACTOR_FUSION_I|
|tradeSymbol|REACTOR_FISSION_I|
|tradeSymbol|REACTOR_CHEMICAL_I|
|tradeSymbol|REACTOR_ANTIMATTER_I|
|tradeSymbol|ENGINE_IMPULSE_DRIVE_I|
|tradeSymbol|ENGINE_ION_DRIVE_I|
|tradeSymbol|ENGINE_ION_DRIVE_II|
|tradeSymbol|ENGINE_HYPER_DRIVE_I|
|tradeSymbol|MODULE_MINERAL_PROCESSOR_I|
|tradeSymbol|MODULE_GAS_PROCESSOR_I|
|tradeSymbol|MODULE_CARGO_HOLD_I|
|tradeSymbol|MODULE_CARGO_HOLD_II|
|tradeSymbol|MODULE_CARGO_HOLD_III|
|tradeSymbol|MODULE_CREW_QUARTERS_I|
|tradeSymbol|MODULE_ENVOY_QUARTERS_I|
|tradeSymbol|MODULE_PASSENGER_CABIN_I|
|tradeSymbol|MODULE_MICRO_REFINERY_I|
|tradeSymbol|MODULE_SCIENCE_LAB_I|
|tradeSymbol|MODULE_JUMP_DRIVE_I|
|tradeSymbol|MODULE_JUMP_DRIVE_II|
|tradeSymbol|MODULE_JUMP_DRIVE_III|
|tradeSymbol|MODULE_WARP_DRIVE_I|
|tradeSymbol|MODULE_WARP_DRIVE_II|
|tradeSymbol|MODULE_WARP_DRIVE_III|
|tradeSymbol|MODULE_SHIELD_GENERATOR_I|
|tradeSymbol|MODULE_SHIELD_GENERATOR_II|
|tradeSymbol|MODULE_ORE_REFINERY_I|
|tradeSymbol|MODULE_FUEL_REFINERY_I|
|tradeSymbol|MOUNT_GAS_SIPHON_I|
|tradeSymbol|MOUNT_GAS_SIPHON_II|
|tradeSymbol|MOUNT_GAS_SIPHON_III|
|tradeSymbol|MOUNT_SURVEYOR_I|
|tradeSymbol|MOUNT_SURVEYOR_II|
|tradeSymbol|MOUNT_SURVEYOR_III|
|tradeSymbol|MOUNT_SENSOR_ARRAY_I|
|tradeSymbol|MOUNT_SENSOR_ARRAY_II|
|tradeSymbol|MOUNT_SENSOR_ARRAY_III|
|tradeSymbol|MOUNT_MINING_LASER_I|
|tradeSymbol|MOUNT_MINING_LASER_II|
|tradeSymbol|MOUNT_MINING_LASER_III|
|tradeSymbol|MOUNT_LASER_CANNON_I|
|tradeSymbol|MOUNT_MISSILE_LAUNCHER_I|
|tradeSymbol|MOUNT_TURRET_I|
|tradeSymbol|SHIP_PROBE|
|tradeSymbol|SHIP_MINING_DRONE|
|tradeSymbol|SHIP_SIPHON_DRONE|
|tradeSymbol|SHIP_INTERCEPTOR|
|tradeSymbol|SHIP_LIGHT_HAULER|
|tradeSymbol|SHIP_COMMAND_FRIGATE|
|tradeSymbol|SHIP_EXPLORER|
|tradeSymbol|SHIP_HEAVY_FREIGHTER|
|tradeSymbol|SHIP_LIGHT_SHUTTLE|
|tradeSymbol|SHIP_ORE_HOUND|
|tradeSymbol|SHIP_REFINING_FREIGHTER|
|tradeSymbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
None, AgentToken
</aside>

## supply-construction

<a id="opIdsupply-construction"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('https://api.spacetraders.io/v2/systems/{systemSymbol}/waypoints/{waypointSymbol}/construction/supply', headers = headers)

print(r.json())

```

`POST /systems/{systemSymbol}/waypoints/{waypointSymbol}/construction/supply`

*Supply Construction Site*

Supply a construction site with the specified good. Requires a waypoint with a property of `isUnderConstruction` to be true.

The good must be in your ship's cargo. The good will be removed from your ship's cargo and added to the construction site's materials.

> Body parameter

```json
{
  "shipSymbol": "string",
  "tradeSymbol": "string",
  "units": 0
}
```

<h3 id="supply-construction-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» shipSymbol|body|string|true|Symbol of the ship to use.|
|» tradeSymbol|body|string|true|The symbol of the good to supply.|
|» units|body|integer|true|Amount of units to supply.|
|systemSymbol|path|string|true|The system symbol|
|waypointSymbol|path|string|true|The waypoint symbol|

> Example responses

> 201 Response

```json
{
  "data": {
    "construction": {
      "symbol": "string",
      "materials": [
        {
          "tradeSymbol": "PRECIOUS_STONES",
          "required": 0,
          "fulfilled": 0
        }
      ],
      "isComplete": true
    },
    "cargo": {
      "capacity": 0,
      "units": 0,
      "inventory": [
        {
          "symbol": "PRECIOUS_STONES",
          "name": "string",
          "description": "string",
          "units": 1
        }
      ]
    }
  }
}
```

<h3 id="supply-construction-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Successfully supplied construction site.|Inline|

<h3 id="supply-construction-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» data|object|true|none|none|
|»» construction|[Construction](#schemaconstruction)|true|none|The construction details of a waypoint.|
|»»» symbol|string|true|none|The symbol of the waypoint.|
|»»» materials|[[ConstructionMaterial](#schemaconstructionmaterial)]|true|none|The materials required to construct the waypoint.|
|»»»» tradeSymbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» required|integer|true|none|The number of units required.|
|»»»» fulfilled|integer|true|none|The number of units fulfilled toward the required amount.|
|»»» isComplete|boolean|true|none|Whether the waypoint has been constructed.|
|»» cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|»»» capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|»»» units|integer|true|none|The number of items currently stored in the cargo hold.|
|»»» inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|
|»»»» symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|»»»» name|string|true|none|The name of the cargo item type.|
|»»»» description|string|true|none|The description of the cargo item type.|
|»»»» units|integer|true|none|The number of units of the cargo item.|

#### Enumerated Values

|Property|Value|
|---|---|
|tradeSymbol|PRECIOUS_STONES|
|tradeSymbol|QUARTZ_SAND|
|tradeSymbol|SILICON_CRYSTALS|
|tradeSymbol|AMMONIA_ICE|
|tradeSymbol|LIQUID_HYDROGEN|
|tradeSymbol|LIQUID_NITROGEN|
|tradeSymbol|ICE_WATER|
|tradeSymbol|EXOTIC_MATTER|
|tradeSymbol|ADVANCED_CIRCUITRY|
|tradeSymbol|GRAVITON_EMITTERS|
|tradeSymbol|IRON|
|tradeSymbol|IRON_ORE|
|tradeSymbol|COPPER|
|tradeSymbol|COPPER_ORE|
|tradeSymbol|ALUMINUM|
|tradeSymbol|ALUMINUM_ORE|
|tradeSymbol|SILVER|
|tradeSymbol|SILVER_ORE|
|tradeSymbol|GOLD|
|tradeSymbol|GOLD_ORE|
|tradeSymbol|PLATINUM|
|tradeSymbol|PLATINUM_ORE|
|tradeSymbol|DIAMONDS|
|tradeSymbol|URANITE|
|tradeSymbol|URANITE_ORE|
|tradeSymbol|MERITIUM|
|tradeSymbol|MERITIUM_ORE|
|tradeSymbol|HYDROCARBON|
|tradeSymbol|ANTIMATTER|
|tradeSymbol|FAB_MATS|
|tradeSymbol|FERTILIZERS|
|tradeSymbol|FABRICS|
|tradeSymbol|FOOD|
|tradeSymbol|JEWELRY|
|tradeSymbol|MACHINERY|
|tradeSymbol|FIREARMS|
|tradeSymbol|ASSAULT_RIFLES|
|tradeSymbol|MILITARY_EQUIPMENT|
|tradeSymbol|EXPLOSIVES|
|tradeSymbol|LAB_INSTRUMENTS|
|tradeSymbol|AMMUNITION|
|tradeSymbol|ELECTRONICS|
|tradeSymbol|SHIP_PLATING|
|tradeSymbol|SHIP_PARTS|
|tradeSymbol|EQUIPMENT|
|tradeSymbol|FUEL|
|tradeSymbol|MEDICINE|
|tradeSymbol|DRUGS|
|tradeSymbol|CLOTHING|
|tradeSymbol|MICROPROCESSORS|
|tradeSymbol|PLASTICS|
|tradeSymbol|POLYNUCLEOTIDES|
|tradeSymbol|BIOCOMPOSITES|
|tradeSymbol|QUANTUM_STABILIZERS|
|tradeSymbol|NANOBOTS|
|tradeSymbol|AI_MAINFRAMES|
|tradeSymbol|QUANTUM_DRIVES|
|tradeSymbol|ROBOTIC_DRONES|
|tradeSymbol|CYBER_IMPLANTS|
|tradeSymbol|GENE_THERAPEUTICS|
|tradeSymbol|NEURAL_CHIPS|
|tradeSymbol|MOOD_REGULATORS|
|tradeSymbol|VIRAL_AGENTS|
|tradeSymbol|MICRO_FUSION_GENERATORS|
|tradeSymbol|SUPERGRAINS|
|tradeSymbol|LASER_RIFLES|
|tradeSymbol|HOLOGRAPHICS|
|tradeSymbol|SHIP_SALVAGE|
|tradeSymbol|RELIC_TECH|
|tradeSymbol|NOVEL_LIFEFORMS|
|tradeSymbol|BOTANICAL_SPECIMENS|
|tradeSymbol|CULTURAL_ARTIFACTS|
|tradeSymbol|FRAME_PROBE|
|tradeSymbol|FRAME_DRONE|
|tradeSymbol|FRAME_INTERCEPTOR|
|tradeSymbol|FRAME_RACER|
|tradeSymbol|FRAME_FIGHTER|
|tradeSymbol|FRAME_FRIGATE|
|tradeSymbol|FRAME_SHUTTLE|
|tradeSymbol|FRAME_EXPLORER|
|tradeSymbol|FRAME_MINER|
|tradeSymbol|FRAME_LIGHT_FREIGHTER|
|tradeSymbol|FRAME_HEAVY_FREIGHTER|
|tradeSymbol|FRAME_TRANSPORT|
|tradeSymbol|FRAME_DESTROYER|
|tradeSymbol|FRAME_CRUISER|
|tradeSymbol|FRAME_CARRIER|
|tradeSymbol|REACTOR_SOLAR_I|
|tradeSymbol|REACTOR_FUSION_I|
|tradeSymbol|REACTOR_FISSION_I|
|tradeSymbol|REACTOR_CHEMICAL_I|
|tradeSymbol|REACTOR_ANTIMATTER_I|
|tradeSymbol|ENGINE_IMPULSE_DRIVE_I|
|tradeSymbol|ENGINE_ION_DRIVE_I|
|tradeSymbol|ENGINE_ION_DRIVE_II|
|tradeSymbol|ENGINE_HYPER_DRIVE_I|
|tradeSymbol|MODULE_MINERAL_PROCESSOR_I|
|tradeSymbol|MODULE_GAS_PROCESSOR_I|
|tradeSymbol|MODULE_CARGO_HOLD_I|
|tradeSymbol|MODULE_CARGO_HOLD_II|
|tradeSymbol|MODULE_CARGO_HOLD_III|
|tradeSymbol|MODULE_CREW_QUARTERS_I|
|tradeSymbol|MODULE_ENVOY_QUARTERS_I|
|tradeSymbol|MODULE_PASSENGER_CABIN_I|
|tradeSymbol|MODULE_MICRO_REFINERY_I|
|tradeSymbol|MODULE_SCIENCE_LAB_I|
|tradeSymbol|MODULE_JUMP_DRIVE_I|
|tradeSymbol|MODULE_JUMP_DRIVE_II|
|tradeSymbol|MODULE_JUMP_DRIVE_III|
|tradeSymbol|MODULE_WARP_DRIVE_I|
|tradeSymbol|MODULE_WARP_DRIVE_II|
|tradeSymbol|MODULE_WARP_DRIVE_III|
|tradeSymbol|MODULE_SHIELD_GENERATOR_I|
|tradeSymbol|MODULE_SHIELD_GENERATOR_II|
|tradeSymbol|MODULE_ORE_REFINERY_I|
|tradeSymbol|MODULE_FUEL_REFINERY_I|
|tradeSymbol|MOUNT_GAS_SIPHON_I|
|tradeSymbol|MOUNT_GAS_SIPHON_II|
|tradeSymbol|MOUNT_GAS_SIPHON_III|
|tradeSymbol|MOUNT_SURVEYOR_I|
|tradeSymbol|MOUNT_SURVEYOR_II|
|tradeSymbol|MOUNT_SURVEYOR_III|
|tradeSymbol|MOUNT_SENSOR_ARRAY_I|
|tradeSymbol|MOUNT_SENSOR_ARRAY_II|
|tradeSymbol|MOUNT_SENSOR_ARRAY_III|
|tradeSymbol|MOUNT_MINING_LASER_I|
|tradeSymbol|MOUNT_MINING_LASER_II|
|tradeSymbol|MOUNT_MINING_LASER_III|
|tradeSymbol|MOUNT_LASER_CANNON_I|
|tradeSymbol|MOUNT_MISSILE_LAUNCHER_I|
|tradeSymbol|MOUNT_TURRET_I|
|tradeSymbol|SHIP_PROBE|
|tradeSymbol|SHIP_MINING_DRONE|
|tradeSymbol|SHIP_SIPHON_DRONE|
|tradeSymbol|SHIP_INTERCEPTOR|
|tradeSymbol|SHIP_LIGHT_HAULER|
|tradeSymbol|SHIP_COMMAND_FRIGATE|
|tradeSymbol|SHIP_EXPLORER|
|tradeSymbol|SHIP_HEAVY_FREIGHTER|
|tradeSymbol|SHIP_LIGHT_SHUTTLE|
|tradeSymbol|SHIP_ORE_HOUND|
|tradeSymbol|SHIP_REFINING_FREIGHTER|
|tradeSymbol|SHIP_SURVEYOR|
|symbol|PRECIOUS_STONES|
|symbol|QUARTZ_SAND|
|symbol|SILICON_CRYSTALS|
|symbol|AMMONIA_ICE|
|symbol|LIQUID_HYDROGEN|
|symbol|LIQUID_NITROGEN|
|symbol|ICE_WATER|
|symbol|EXOTIC_MATTER|
|symbol|ADVANCED_CIRCUITRY|
|symbol|GRAVITON_EMITTERS|
|symbol|IRON|
|symbol|IRON_ORE|
|symbol|COPPER|
|symbol|COPPER_ORE|
|symbol|ALUMINUM|
|symbol|ALUMINUM_ORE|
|symbol|SILVER|
|symbol|SILVER_ORE|
|symbol|GOLD|
|symbol|GOLD_ORE|
|symbol|PLATINUM|
|symbol|PLATINUM_ORE|
|symbol|DIAMONDS|
|symbol|URANITE|
|symbol|URANITE_ORE|
|symbol|MERITIUM|
|symbol|MERITIUM_ORE|
|symbol|HYDROCARBON|
|symbol|ANTIMATTER|
|symbol|FAB_MATS|
|symbol|FERTILIZERS|
|symbol|FABRICS|
|symbol|FOOD|
|symbol|JEWELRY|
|symbol|MACHINERY|
|symbol|FIREARMS|
|symbol|ASSAULT_RIFLES|
|symbol|MILITARY_EQUIPMENT|
|symbol|EXPLOSIVES|
|symbol|LAB_INSTRUMENTS|
|symbol|AMMUNITION|
|symbol|ELECTRONICS|
|symbol|SHIP_PLATING|
|symbol|SHIP_PARTS|
|symbol|EQUIPMENT|
|symbol|FUEL|
|symbol|MEDICINE|
|symbol|DRUGS|
|symbol|CLOTHING|
|symbol|MICROPROCESSORS|
|symbol|PLASTICS|
|symbol|POLYNUCLEOTIDES|
|symbol|BIOCOMPOSITES|
|symbol|QUANTUM_STABILIZERS|
|symbol|NANOBOTS|
|symbol|AI_MAINFRAMES|
|symbol|QUANTUM_DRIVES|
|symbol|ROBOTIC_DRONES|
|symbol|CYBER_IMPLANTS|
|symbol|GENE_THERAPEUTICS|
|symbol|NEURAL_CHIPS|
|symbol|MOOD_REGULATORS|
|symbol|VIRAL_AGENTS|
|symbol|MICRO_FUSION_GENERATORS|
|symbol|SUPERGRAINS|
|symbol|LASER_RIFLES|
|symbol|HOLOGRAPHICS|
|symbol|SHIP_SALVAGE|
|symbol|RELIC_TECH|
|symbol|NOVEL_LIFEFORMS|
|symbol|BOTANICAL_SPECIMENS|
|symbol|CULTURAL_ARTIFACTS|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|
|symbol|SHIP_PROBE|
|symbol|SHIP_MINING_DRONE|
|symbol|SHIP_SIPHON_DRONE|
|symbol|SHIP_INTERCEPTOR|
|symbol|SHIP_LIGHT_HAULER|
|symbol|SHIP_COMMAND_FRIGATE|
|symbol|SHIP_EXPLORER|
|symbol|SHIP_HEAVY_FREIGHTER|
|symbol|SHIP_LIGHT_SHUTTLE|
|symbol|SHIP_ORE_HOUND|
|symbol|SHIP_REFINING_FREIGHTER|
|symbol|SHIP_SURVEYOR|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
AgentToken
</aside>

# Schemas

<h2 id="tocS_ActivityLevel">ActivityLevel</h2>
<!-- backwards compatibility -->
<a id="schemaactivitylevel"></a>
<a id="schema_ActivityLevel"></a>
<a id="tocSactivitylevel"></a>
<a id="tocsactivitylevel"></a>

```json
"WEAK"

```

The activity level of a trade good. If the good is an import, this represents how strong consumption is. If the good is an export, this represents how strong the production is for the good. When activity is strong, consumption or production is near maximum capacity. When activity is weak, consumption or production is near minimum capacity.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The activity level of a trade good. If the good is an import, this represents how strong consumption is. If the good is an export, this represents how strong the production is for the good. When activity is strong, consumption or production is near maximum capacity. When activity is weak, consumption or production is near minimum capacity.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|WEAK|
|*anonymous*|GROWING|
|*anonymous*|STRONG|
|*anonymous*|RESTRICTED|

<h2 id="tocS_Agent">Agent</h2>
<!-- backwards compatibility -->
<a id="schemaagent"></a>
<a id="schema_Agent"></a>
<a id="tocSagent"></a>
<a id="tocsagent"></a>

```json
{
  "accountId": "string",
  "symbol": "string",
  "headquarters": "string",
  "credits": 0,
  "startingFaction": "string",
  "shipCount": 0
}

```

Agent details.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|accountId|string|false|none|Account ID that is tied to this agent. Only included on your own agent.|
|symbol|string|true|none|Symbol of the agent.|
|headquarters|string|true|none|The headquarters of the agent.|
|credits|integer(int64)|true|none|The number of credits the agent has available. Credits can be negative if funds have been overdrawn.|
|startingFaction|string|true|none|The faction the agent started with.|
|shipCount|integer|true|none|How many ships are owned by the agent.|

<h2 id="tocS_Chart">Chart</h2>
<!-- backwards compatibility -->
<a id="schemachart"></a>
<a id="schema_Chart"></a>
<a id="tocSchart"></a>
<a id="tocschart"></a>

```json
{
  "waypointSymbol": "string",
  "submittedBy": "string",
  "submittedOn": "2019-08-24T14:15:22Z"
}

```

The chart of a system or waypoint, which makes the location visible to other agents.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|false|none|The symbol of the waypoint.|
|submittedBy|string|false|none|The agent that submitted the chart for this waypoint.|
|submittedOn|string(date-time)|false|none|The time the chart for this waypoint was submitted.|

<h2 id="tocS_Construction">Construction</h2>
<!-- backwards compatibility -->
<a id="schemaconstruction"></a>
<a id="schema_Construction"></a>
<a id="tocSconstruction"></a>
<a id="tocsconstruction"></a>

```json
{
  "symbol": "string",
  "materials": [
    {
      "tradeSymbol": "PRECIOUS_STONES",
      "required": 0,
      "fulfilled": 0
    }
  ],
  "isComplete": true
}

```

The construction details of a waypoint.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|The symbol of the waypoint.|
|materials|[[ConstructionMaterial](#schemaconstructionmaterial)]|true|none|The materials required to construct the waypoint.|
|isComplete|boolean|true|none|Whether the waypoint has been constructed.|

<h2 id="tocS_ConstructionMaterial">ConstructionMaterial</h2>
<!-- backwards compatibility -->
<a id="schemaconstructionmaterial"></a>
<a id="schema_ConstructionMaterial"></a>
<a id="tocSconstructionmaterial"></a>
<a id="tocsconstructionmaterial"></a>

```json
{
  "tradeSymbol": "PRECIOUS_STONES",
  "required": 0,
  "fulfilled": 0
}

```

The details of the required construction materials for a given waypoint under construction.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tradeSymbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|required|integer|true|none|The number of units required.|
|fulfilled|integer|true|none|The number of units fulfilled toward the required amount.|

<h2 id="tocS_Contract">Contract</h2>
<!-- backwards compatibility -->
<a id="schemacontract"></a>
<a id="schema_Contract"></a>
<a id="tocScontract"></a>
<a id="tocscontract"></a>

```json
{
  "id": "string",
  "factionSymbol": "string",
  "type": "PROCUREMENT",
  "terms": {
    "deadline": "2019-08-24T14:15:22Z",
    "payment": {
      "onAccepted": 0,
      "onFulfilled": 0
    },
    "deliver": [
      {
        "tradeSymbol": "string",
        "destinationSymbol": "string",
        "unitsRequired": 0,
        "unitsFulfilled": 0
      }
    ]
  },
  "accepted": false,
  "fulfilled": false,
  "expiration": "2019-08-24T14:15:22Z",
  "deadlineToAccept": "2019-08-24T14:15:22Z"
}

```

Contract details.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|ID of the contract.|
|factionSymbol|string|true|none|The symbol of the faction that this contract is for.|
|type|string|true|none|Type of contract.|
|terms|[ContractTerms](#schemacontractterms)|true|none|The terms to fulfill the contract.|
|accepted|boolean|true|none|Whether the contract has been accepted by the agent|
|fulfilled|boolean|true|none|Whether the contract has been fulfilled|
|expiration|string(date-time)|true|none|Deprecated in favor of deadlineToAccept|
|deadlineToAccept|string(date-time)|false|none|The time at which the contract is no longer available to be accepted|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PROCUREMENT|
|type|TRANSPORT|
|type|SHUTTLE|

<h2 id="tocS_ContractDeliverGood">ContractDeliverGood</h2>
<!-- backwards compatibility -->
<a id="schemacontractdelivergood"></a>
<a id="schema_ContractDeliverGood"></a>
<a id="tocScontractdelivergood"></a>
<a id="tocscontractdelivergood"></a>

```json
{
  "tradeSymbol": "string",
  "destinationSymbol": "string",
  "unitsRequired": 0,
  "unitsFulfilled": 0
}

```

The details of a delivery contract. Includes the type of good, units needed, and the destination.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tradeSymbol|string|true|none|The symbol of the trade good to deliver.|
|destinationSymbol|string|true|none|The destination where goods need to be delivered.|
|unitsRequired|integer|true|none|The number of units that need to be delivered on this contract.|
|unitsFulfilled|integer|true|none|The number of units fulfilled on this contract.|

<h2 id="tocS_ContractPayment">ContractPayment</h2>
<!-- backwards compatibility -->
<a id="schemacontractpayment"></a>
<a id="schema_ContractPayment"></a>
<a id="tocScontractpayment"></a>
<a id="tocscontractpayment"></a>

```json
{
  "onAccepted": 0,
  "onFulfilled": 0
}

```

Payments for the contract.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|onAccepted|integer|true|none|The amount of credits received up front for accepting the contract.|
|onFulfilled|integer|true|none|The amount of credits received when the contract is fulfilled.|

<h2 id="tocS_ContractTerms">ContractTerms</h2>
<!-- backwards compatibility -->
<a id="schemacontractterms"></a>
<a id="schema_ContractTerms"></a>
<a id="tocScontractterms"></a>
<a id="tocscontractterms"></a>

```json
{
  "deadline": "2019-08-24T14:15:22Z",
  "payment": {
    "onAccepted": 0,
    "onFulfilled": 0
  },
  "deliver": [
    {
      "tradeSymbol": "string",
      "destinationSymbol": "string",
      "unitsRequired": 0,
      "unitsFulfilled": 0
    }
  ]
}

```

The terms to fulfill the contract.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|deadline|string(date-time)|true|none|The deadline for the contract.|
|payment|[ContractPayment](#schemacontractpayment)|true|none|Payments for the contract.|
|deliver|[[ContractDeliverGood](#schemacontractdelivergood)]|false|none|The cargo that needs to be delivered to fulfill the contract.|

<h2 id="tocS_Cooldown">Cooldown</h2>
<!-- backwards compatibility -->
<a id="schemacooldown"></a>
<a id="schema_Cooldown"></a>
<a id="tocScooldown"></a>
<a id="tocscooldown"></a>

```json
{
  "shipSymbol": "string",
  "totalSeconds": 0,
  "remainingSeconds": 0,
  "expiration": "2019-08-24T14:15:22Z"
}

```

A cooldown is a period of time in which a ship cannot perform certain actions.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|shipSymbol|string|true|none|The symbol of the ship that is on cooldown|
|totalSeconds|integer|true|none|The total duration of the cooldown in seconds|
|remainingSeconds|integer|true|none|The remaining duration of the cooldown in seconds|
|expiration|string(date-time)|false|none|The date and time when the cooldown expires in ISO 8601 format|

<h2 id="tocS_Extraction">Extraction</h2>
<!-- backwards compatibility -->
<a id="schemaextraction"></a>
<a id="schema_Extraction"></a>
<a id="tocSextraction"></a>
<a id="tocsextraction"></a>

```json
{
  "shipSymbol": "string",
  "yield": {
    "symbol": "PRECIOUS_STONES",
    "units": 0
  }
}

```

Extraction details.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|shipSymbol|string|true|none|Symbol of the ship that executed the extraction.|
|yield|[ExtractionYield](#schemaextractionyield)|true|none|A yield from the extraction operation.|

<h2 id="tocS_ExtractionYield">ExtractionYield</h2>
<!-- backwards compatibility -->
<a id="schemaextractionyield"></a>
<a id="schema_ExtractionYield"></a>
<a id="tocSextractionyield"></a>
<a id="tocsextractionyield"></a>

```json
{
  "symbol": "PRECIOUS_STONES",
  "units": 0
}

```

A yield from the extraction operation.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|units|integer|true|none|The number of units extracted that were placed into the ship's cargo hold.|

<h2 id="tocS_Faction">Faction</h2>
<!-- backwards compatibility -->
<a id="schemafaction"></a>
<a id="schema_Faction"></a>
<a id="tocSfaction"></a>
<a id="tocsfaction"></a>

```json
{
  "symbol": "COSMIC",
  "name": "string",
  "description": "string",
  "headquarters": "string",
  "traits": [
    {
      "symbol": "BUREAUCRATIC",
      "name": "string",
      "description": "string"
    }
  ],
  "isRecruiting": true
}

```

Faction details.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[FactionSymbol](#schemafactionsymbol)|true|none|The symbol of the faction.|
|name|string|true|none|Name of the faction.|
|description|string|true|none|Description of the faction.|
|headquarters|string|true|none|The waypoint in which the faction's HQ is located in.|
|traits|[[FactionTrait](#schemafactiontrait)]|true|none|List of traits that define this faction.|
|isRecruiting|boolean|true|none|Whether or not the faction is currently recruiting new agents.|

<h2 id="tocS_FactionSymbol">FactionSymbol</h2>
<!-- backwards compatibility -->
<a id="schemafactionsymbol"></a>
<a id="schema_FactionSymbol"></a>
<a id="tocSfactionsymbol"></a>
<a id="tocsfactionsymbol"></a>

```json
"COSMIC"

```

The symbol of the faction.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The symbol of the faction.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|COSMIC|
|*anonymous*|VOID|
|*anonymous*|GALACTIC|
|*anonymous*|QUANTUM|
|*anonymous*|DOMINION|
|*anonymous*|ASTRO|
|*anonymous*|CORSAIRS|
|*anonymous*|OBSIDIAN|
|*anonymous*|AEGIS|
|*anonymous*|UNITED|
|*anonymous*|SOLITARY|
|*anonymous*|COBALT|
|*anonymous*|OMEGA|
|*anonymous*|ECHO|
|*anonymous*|LORDS|
|*anonymous*|CULT|
|*anonymous*|ANCIENTS|
|*anonymous*|SHADOW|
|*anonymous*|ETHEREAL|

<h2 id="tocS_FactionTrait">FactionTrait</h2>
<!-- backwards compatibility -->
<a id="schemafactiontrait"></a>
<a id="schema_FactionTrait"></a>
<a id="tocSfactiontrait"></a>
<a id="tocsfactiontrait"></a>

```json
{
  "symbol": "BUREAUCRATIC",
  "name": "string",
  "description": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[FactionTraitSymbol](#schemafactiontraitsymbol)|true|none|The unique identifier of the trait.|
|name|string|true|none|The name of the trait.|
|description|string|true|none|A description of the trait.|

<h2 id="tocS_FactionTraitSymbol">FactionTraitSymbol</h2>
<!-- backwards compatibility -->
<a id="schemafactiontraitsymbol"></a>
<a id="schema_FactionTraitSymbol"></a>
<a id="tocSfactiontraitsymbol"></a>
<a id="tocsfactiontraitsymbol"></a>

```json
"BUREAUCRATIC"

```

The unique identifier of the trait.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The unique identifier of the trait.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|BUREAUCRATIC|
|*anonymous*|SECRETIVE|
|*anonymous*|CAPITALISTIC|
|*anonymous*|INDUSTRIOUS|
|*anonymous*|PEACEFUL|
|*anonymous*|DISTRUSTFUL|
|*anonymous*|WELCOMING|
|*anonymous*|SMUGGLERS|
|*anonymous*|SCAVENGERS|
|*anonymous*|REBELLIOUS|
|*anonymous*|EXILES|
|*anonymous*|PIRATES|
|*anonymous*|RAIDERS|
|*anonymous*|CLAN|
|*anonymous*|GUILD|
|*anonymous*|DOMINION|
|*anonymous*|FRINGE|
|*anonymous*|FORSAKEN|
|*anonymous*|ISOLATED|
|*anonymous*|LOCALIZED|
|*anonymous*|ESTABLISHED|
|*anonymous*|NOTABLE|
|*anonymous*|DOMINANT|
|*anonymous*|INESCAPABLE|
|*anonymous*|INNOVATIVE|
|*anonymous*|BOLD|
|*anonymous*|VISIONARY|
|*anonymous*|CURIOUS|
|*anonymous*|DARING|
|*anonymous*|EXPLORATORY|
|*anonymous*|RESOURCEFUL|
|*anonymous*|FLEXIBLE|
|*anonymous*|COOPERATIVE|
|*anonymous*|UNITED|
|*anonymous*|STRATEGIC|
|*anonymous*|INTELLIGENT|
|*anonymous*|RESEARCH_FOCUSED|
|*anonymous*|COLLABORATIVE|
|*anonymous*|PROGRESSIVE|
|*anonymous*|MILITARISTIC|
|*anonymous*|TECHNOLOGICALLY_ADVANCED|
|*anonymous*|AGGRESSIVE|
|*anonymous*|IMPERIALISTIC|
|*anonymous*|TREASURE_HUNTERS|
|*anonymous*|DEXTEROUS|
|*anonymous*|UNPREDICTABLE|
|*anonymous*|BRUTAL|
|*anonymous*|FLEETING|
|*anonymous*|ADAPTABLE|
|*anonymous*|SELF_SUFFICIENT|
|*anonymous*|DEFENSIVE|
|*anonymous*|PROUD|
|*anonymous*|DIVERSE|
|*anonymous*|INDEPENDENT|
|*anonymous*|SELF_INTERESTED|
|*anonymous*|FRAGMENTED|
|*anonymous*|COMMERCIAL|
|*anonymous*|FREE_MARKETS|
|*anonymous*|ENTREPRENEURIAL|

<h2 id="tocS_JumpGate">JumpGate</h2>
<!-- backwards compatibility -->
<a id="schemajumpgate"></a>
<a id="schema_JumpGate"></a>
<a id="tocSjumpgate"></a>
<a id="tocsjumpgate"></a>

```json
{
  "symbol": "string",
  "connections": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|connections|[string]|true|none|All the gates that are connected to this waypoint.|

<h2 id="tocS_Market">Market</h2>
<!-- backwards compatibility -->
<a id="schemamarket"></a>
<a id="schema_Market"></a>
<a id="tocSmarket"></a>
<a id="tocsmarket"></a>

```json
{
  "symbol": "string",
  "exports": [
    {
      "symbol": "PRECIOUS_STONES",
      "name": "string",
      "description": "string"
    }
  ],
  "imports": [
    {
      "symbol": "PRECIOUS_STONES",
      "name": "string",
      "description": "string"
    }
  ],
  "exchange": [
    {
      "symbol": "PRECIOUS_STONES",
      "name": "string",
      "description": "string"
    }
  ],
  "transactions": [
    {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "tradeSymbol": "string",
      "type": "PURCHASE",
      "units": 0,
      "pricePerUnit": 0,
      "totalPrice": 0,
      "timestamp": "2019-08-24T14:15:22Z"
    }
  ],
  "tradeGoods": [
    {
      "symbol": "PRECIOUS_STONES",
      "type": "EXPORT",
      "tradeVolume": 1,
      "supply": "SCARCE",
      "activity": "WEAK",
      "purchasePrice": 0,
      "sellPrice": 0
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|The symbol of the market. The symbol is the same as the waypoint where the market is located.|
|exports|[[TradeGood](#schematradegood)]|true|none|The list of goods that are exported from this market.|
|imports|[[TradeGood](#schematradegood)]|true|none|The list of goods that are sought as imports in this market.|
|exchange|[[TradeGood](#schematradegood)]|true|none|The list of goods that are bought and sold between agents at this market.|
|transactions|[[MarketTransaction](#schemamarkettransaction)]|false|none|The list of recent transactions at this market. Visible only when a ship is present at the market.|
|tradeGoods|[[MarketTradeGood](#schemamarkettradegood)]|false|none|The list of goods that are traded at this market. Visible only when a ship is present at the market.|

<h2 id="tocS_MarketTradeGood">MarketTradeGood</h2>
<!-- backwards compatibility -->
<a id="schemamarkettradegood"></a>
<a id="schema_MarketTradeGood"></a>
<a id="tocSmarkettradegood"></a>
<a id="tocsmarkettradegood"></a>

```json
{
  "symbol": "PRECIOUS_STONES",
  "type": "EXPORT",
  "tradeVolume": 1,
  "supply": "SCARCE",
  "activity": "WEAK",
  "purchasePrice": 0,
  "sellPrice": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|type|string|true|none|The type of trade good (export, import, or exchange).|
|tradeVolume|integer|true|none|This is the maximum number of units that can be purchased or sold at this market in a single trade for this good. Trade volume also gives an indication of price volatility. A market with a low trade volume will have large price swings, while high trade volume will be more resilient to price changes.|
|supply|[SupplyLevel](#schemasupplylevel)|true|none|The supply level of a trade good.|
|activity|[ActivityLevel](#schemaactivitylevel)|false|none|The activity level of a trade good. If the good is an import, this represents how strong consumption is. If the good is an export, this represents how strong the production is for the good. When activity is strong, consumption or production is near maximum capacity. When activity is weak, consumption or production is near minimum capacity.|
|purchasePrice|integer|true|none|The price at which this good can be purchased from the market.|
|sellPrice|integer|true|none|The price at which this good can be sold to the market.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|EXPORT|
|type|IMPORT|
|type|EXCHANGE|

<h2 id="tocS_MarketTransaction">MarketTransaction</h2>
<!-- backwards compatibility -->
<a id="schemamarkettransaction"></a>
<a id="schema_MarketTransaction"></a>
<a id="tocSmarkettransaction"></a>
<a id="tocsmarkettransaction"></a>

```json
{
  "waypointSymbol": "string",
  "shipSymbol": "string",
  "tradeSymbol": "string",
  "type": "PURCHASE",
  "units": 0,
  "pricePerUnit": 0,
  "totalPrice": 0,
  "timestamp": "2019-08-24T14:15:22Z"
}

```

Result of a transaction with a market.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|shipSymbol|string|true|none|The symbol of the ship that made the transaction.|
|tradeSymbol|string|true|none|The symbol of the trade good.|
|type|string|true|none|The type of transaction.|
|units|integer|true|none|The number of units of the transaction.|
|pricePerUnit|integer|true|none|The price per unit of the transaction.|
|totalPrice|integer|true|none|The total price of the transaction.|
|timestamp|string(date-time)|true|none|The timestamp of the transaction.|

#### Enumerated Values

|Property|Value|
|---|---|
|type|PURCHASE|
|type|SELL|

<h2 id="tocS_Meta">Meta</h2>
<!-- backwards compatibility -->
<a id="schemameta"></a>
<a id="schema_Meta"></a>
<a id="tocSmeta"></a>
<a id="tocsmeta"></a>

```json
{
  "total": 0,
  "page": 1,
  "limit": 10
}

```

Meta details for pagination.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|total|integer|true|none|Shows the total amount of items of this kind that exist.|
|page|integer|true|none|A page denotes an amount of items, offset from the first item. Each page holds an amount of items equal to the `limit`.|
|limit|integer|true|none|The amount of items in each page. Limits how many items can be fetched at once.|

<h2 id="tocS_RepairTransaction">RepairTransaction</h2>
<!-- backwards compatibility -->
<a id="schemarepairtransaction"></a>
<a id="schema_RepairTransaction"></a>
<a id="tocSrepairtransaction"></a>
<a id="tocsrepairtransaction"></a>

```json
{
  "waypointSymbol": "string",
  "shipSymbol": "string",
  "totalPrice": 0,
  "timestamp": "2019-08-24T14:15:22Z"
}

```

Result of a repair transaction.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|shipSymbol|string|true|none|The symbol of the ship.|
|totalPrice|integer|true|none|The total price of the transaction.|
|timestamp|string(date-time)|true|none|The timestamp of the transaction.|

<h2 id="tocS_ScannedShip">ScannedShip</h2>
<!-- backwards compatibility -->
<a id="schemascannedship"></a>
<a id="schema_ScannedShip"></a>
<a id="tocSscannedship"></a>
<a id="tocsscannedship"></a>

```json
{
  "symbol": "string",
  "registration": {
    "name": "string",
    "factionSymbol": "string",
    "role": "FABRICATOR"
  },
  "nav": {
    "systemSymbol": "string",
    "waypointSymbol": "string",
    "route": {
      "destination": {
        "symbol": "string",
        "type": "PLANET",
        "systemSymbol": "string",
        "x": 0,
        "y": 0
      },
      "origin": {
        "symbol": "string",
        "type": "PLANET",
        "systemSymbol": "string",
        "x": 0,
        "y": 0
      },
      "departureTime": "2019-08-24T14:15:22Z",
      "arrival": "2019-08-24T14:15:22Z"
    },
    "status": "IN_TRANSIT",
    "flightMode": "DRIFT"
  },
  "frame": {
    "symbol": "string"
  },
  "reactor": {
    "symbol": "string"
  },
  "engine": {
    "symbol": "string"
  },
  "mounts": [
    {
      "symbol": "string"
    }
  ]
}

```

The ship that was scanned. Details include information about the ship that could be detected by the scanner.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|The globally unique identifier of the ship.|
|registration|[ShipRegistration](#schemashipregistration)|true|none|The public registration information of the ship|
|nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|frame|object|false|none|The frame of the ship.|
|» symbol|string|true|none|The symbol of the frame.|
|reactor|object|false|none|The reactor of the ship.|
|» symbol|string|true|none|The symbol of the reactor.|
|engine|object|true|none|The engine of the ship.|
|» symbol|string|true|none|The symbol of the engine.|
|mounts|[object]|false|none|List of mounts installed in the ship.|
|» symbol|string|true|none|The symbol of the mount.|

<h2 id="tocS_ScannedSystem">ScannedSystem</h2>
<!-- backwards compatibility -->
<a id="schemascannedsystem"></a>
<a id="schema_ScannedSystem"></a>
<a id="tocSscannedsystem"></a>
<a id="tocsscannedsystem"></a>

```json
{
  "symbol": "string",
  "sectorSymbol": "string",
  "type": "NEUTRON_STAR",
  "x": 0,
  "y": 0,
  "distance": 0
}

```

Details of a system was that scanned.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|Symbol of the system.|
|sectorSymbol|string|true|none|Symbol of the system's sector.|
|type|[SystemType](#schemasystemtype)|true|none|The type of system.|
|x|integer|true|none|Position in the universe in the x axis.|
|y|integer|true|none|Position in the universe in the y axis.|
|distance|integer|true|none|The system's distance from the scanning ship.|

<h2 id="tocS_ScannedWaypoint">ScannedWaypoint</h2>
<!-- backwards compatibility -->
<a id="schemascannedwaypoint"></a>
<a id="schema_ScannedWaypoint"></a>
<a id="tocSscannedwaypoint"></a>
<a id="tocsscannedwaypoint"></a>

```json
{
  "symbol": "string",
  "type": "PLANET",
  "systemSymbol": "string",
  "x": 0,
  "y": 0,
  "orbitals": [
    {
      "symbol": "string"
    }
  ],
  "faction": {
    "symbol": "COSMIC"
  },
  "traits": [
    {
      "symbol": "UNCHARTED",
      "name": "string",
      "description": "string"
    }
  ],
  "chart": {
    "waypointSymbol": "string",
    "submittedBy": "string",
    "submittedOn": "2019-08-24T14:15:22Z"
  }
}

```

A waypoint that was scanned by a ship.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|x|integer|true|none|Position in the universe in the x axis.|
|y|integer|true|none|Position in the universe in the y axis.|
|orbitals|[[WaypointOrbital](#schemawaypointorbital)]|true|none|List of waypoints that orbit this waypoint.|
|faction|[WaypointFaction](#schemawaypointfaction)|false|none|The faction that controls the waypoint.|
|traits|[[WaypointTrait](#schemawaypointtrait)]|true|none|The traits of the waypoint.|
|chart|[Chart](#schemachart)|false|none|The chart of a system or waypoint, which makes the location visible to other agents.|

<h2 id="tocS_ScrapTransaction">ScrapTransaction</h2>
<!-- backwards compatibility -->
<a id="schemascraptransaction"></a>
<a id="schema_ScrapTransaction"></a>
<a id="tocSscraptransaction"></a>
<a id="tocsscraptransaction"></a>

```json
{
  "waypointSymbol": "string",
  "shipSymbol": "string",
  "totalPrice": 0,
  "timestamp": "2019-08-24T14:15:22Z"
}

```

Result of a scrap transaction.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|shipSymbol|string|true|none|The symbol of the ship.|
|totalPrice|integer|true|none|The total price of the transaction.|
|timestamp|string(date-time)|true|none|The timestamp of the transaction.|

<h2 id="tocS_Ship">Ship</h2>
<!-- backwards compatibility -->
<a id="schemaship"></a>
<a id="schema_Ship"></a>
<a id="tocSship"></a>
<a id="tocsship"></a>

```json
{
  "symbol": "string",
  "registration": {
    "name": "string",
    "factionSymbol": "string",
    "role": "FABRICATOR"
  },
  "nav": {
    "systemSymbol": "string",
    "waypointSymbol": "string",
    "route": {
      "destination": {
        "symbol": "string",
        "type": "PLANET",
        "systemSymbol": "string",
        "x": 0,
        "y": 0
      },
      "origin": {
        "symbol": "string",
        "type": "PLANET",
        "systemSymbol": "string",
        "x": 0,
        "y": 0
      },
      "departureTime": "2019-08-24T14:15:22Z",
      "arrival": "2019-08-24T14:15:22Z"
    },
    "status": "IN_TRANSIT",
    "flightMode": "DRIFT"
  },
  "crew": {
    "current": 0,
    "required": 0,
    "capacity": 0,
    "rotation": "STRICT",
    "morale": 100,
    "wages": 0
  },
  "frame": {
    "symbol": "FRAME_PROBE",
    "name": "string",
    "description": "string",
    "condition": 1,
    "integrity": 1,
    "moduleSlots": 0,
    "mountingPoints": 0,
    "fuelCapacity": 0,
    "requirements": {
      "power": 0,
      "crew": 0,
      "slots": 0
    }
  },
  "reactor": {
    "symbol": "REACTOR_SOLAR_I",
    "name": "string",
    "description": "string",
    "condition": 1,
    "integrity": 1,
    "powerOutput": 1,
    "requirements": {
      "power": 0,
      "crew": 0,
      "slots": 0
    }
  },
  "engine": {
    "symbol": "ENGINE_IMPULSE_DRIVE_I",
    "name": "string",
    "description": "string",
    "condition": 1,
    "integrity": 1,
    "speed": 1,
    "requirements": {
      "power": 0,
      "crew": 0,
      "slots": 0
    }
  },
  "cooldown": {
    "shipSymbol": "string",
    "totalSeconds": 0,
    "remainingSeconds": 0,
    "expiration": "2019-08-24T14:15:22Z"
  },
  "modules": [
    {
      "symbol": "MODULE_MINERAL_PROCESSOR_I",
      "capacity": 0,
      "range": 0,
      "name": "string",
      "description": "string",
      "requirements": {
        "power": 0,
        "crew": 0,
        "slots": 0
      }
    }
  ],
  "mounts": [
    {
      "symbol": "MOUNT_GAS_SIPHON_I",
      "name": "string",
      "description": "string",
      "strength": 0,
      "deposits": [
        "QUARTZ_SAND"
      ],
      "requirements": {
        "power": 0,
        "crew": 0,
        "slots": 0
      }
    }
  ],
  "cargo": {
    "capacity": 0,
    "units": 0,
    "inventory": [
      {
        "symbol": "PRECIOUS_STONES",
        "name": "string",
        "description": "string",
        "units": 1
      }
    ]
  },
  "fuel": {
    "current": 0,
    "capacity": 0,
    "consumed": {
      "amount": 0,
      "timestamp": "2019-08-24T14:15:22Z"
    }
  }
}

```

Ship details.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|The globally unique identifier of the ship in the following format: `[AGENT_SYMBOL]-[HEX_ID]`|
|registration|[ShipRegistration](#schemashipregistration)|true|none|The public registration information of the ship|
|nav|[ShipNav](#schemashipnav)|true|none|The navigation information of the ship.|
|crew|[ShipCrew](#schemashipcrew)|true|none|The ship's crew service and maintain the ship's systems and equipment.|
|frame|[ShipFrame](#schemashipframe)|true|none|The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.|
|reactor|[ShipReactor](#schemashipreactor)|true|none|The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.|
|engine|[ShipEngine](#schemashipengine)|true|none|The engine determines how quickly a ship travels between waypoints.|
|cooldown|[Cooldown](#schemacooldown)|true|none|A cooldown is a period of time in which a ship cannot perform certain actions.|
|modules|[[ShipModule](#schemashipmodule)]|true|none|Modules installed in this ship.|
|mounts|[[ShipMount](#schemashipmount)]|true|none|Mounts installed in this ship.|
|cargo|[ShipCargo](#schemashipcargo)|true|none|Ship cargo details.|
|fuel|[ShipFuel](#schemashipfuel)|true|none|Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.|

<h2 id="tocS_ShipCargo">ShipCargo</h2>
<!-- backwards compatibility -->
<a id="schemashipcargo"></a>
<a id="schema_ShipCargo"></a>
<a id="tocSshipcargo"></a>
<a id="tocsshipcargo"></a>

```json
{
  "capacity": 0,
  "units": 0,
  "inventory": [
    {
      "symbol": "PRECIOUS_STONES",
      "name": "string",
      "description": "string",
      "units": 1
    }
  ]
}

```

Ship cargo details.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|capacity|integer|true|none|The max number of items that can be stored in the cargo hold.|
|units|integer|true|none|The number of items currently stored in the cargo hold.|
|inventory|[[ShipCargoItem](#schemashipcargoitem)]|true|none|The items currently in the cargo hold.|

<h2 id="tocS_ShipCargoItem">ShipCargoItem</h2>
<!-- backwards compatibility -->
<a id="schemashipcargoitem"></a>
<a id="schema_ShipCargoItem"></a>
<a id="tocSshipcargoitem"></a>
<a id="tocsshipcargoitem"></a>

```json
{
  "symbol": "PRECIOUS_STONES",
  "name": "string",
  "description": "string",
  "units": 1
}

```

The type of cargo item and the number of units.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|name|string|true|none|The name of the cargo item type.|
|description|string|true|none|The description of the cargo item type.|
|units|integer|true|none|The number of units of the cargo item.|

<h2 id="tocS_ShipComponentCondition">ShipComponentCondition</h2>
<!-- backwards compatibility -->
<a id="schemashipcomponentcondition"></a>
<a id="schema_ShipComponentCondition"></a>
<a id="tocSshipcomponentcondition"></a>
<a id="tocsshipcomponentcondition"></a>

```json
1

```

The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|number(double)|false|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|

<h2 id="tocS_ShipComponentIntegrity">ShipComponentIntegrity</h2>
<!-- backwards compatibility -->
<a id="schemashipcomponentintegrity"></a>
<a id="schema_ShipComponentIntegrity"></a>
<a id="tocSshipcomponentintegrity"></a>
<a id="tocsshipcomponentintegrity"></a>

```json
1

```

The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|number(double)|false|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|

<h2 id="tocS_ShipConditionEvent">ShipConditionEvent</h2>
<!-- backwards compatibility -->
<a id="schemashipconditionevent"></a>
<a id="schema_ShipConditionEvent"></a>
<a id="tocSshipconditionevent"></a>
<a id="tocsshipconditionevent"></a>

```json
{
  "symbol": "REACTOR_OVERLOAD",
  "component": "FRAME",
  "name": "string",
  "description": "string"
}

```

An event that represents damage or wear to a ship's reactor, frame, or engine, reducing the condition of the ship.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|none|
|component|string|true|none|none|
|name|string|true|none|The name of the event.|
|description|string|true|none|A description of the event.|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|REACTOR_OVERLOAD|
|symbol|ENERGY_SPIKE_FROM_MINERAL|
|symbol|SOLAR_FLARE_INTERFERENCE|
|symbol|COOLANT_LEAK|
|symbol|POWER_DISTRIBUTION_FLUCTUATION|
|symbol|MAGNETIC_FIELD_DISRUPTION|
|symbol|HULL_MICROMETEORITE_STRIKES|
|symbol|STRUCTURAL_STRESS_FRACTURES|
|symbol|CORROSIVE_MINERAL_CONTAMINATION|
|symbol|THERMAL_EXPANSION_MISMATCH|
|symbol|VIBRATION_DAMAGE_FROM_DRILLING|
|symbol|ELECTROMAGNETIC_FIELD_INTERFERENCE|
|symbol|IMPACT_WITH_EXTRACTED_DEBRIS|
|symbol|FUEL_EFFICIENCY_DEGRADATION|
|symbol|COOLANT_SYSTEM_AGEING|
|symbol|DUST_MICROABRASIONS|
|symbol|THRUSTER_NOZZLE_WEAR|
|symbol|EXHAUST_PORT_CLOGGING|
|symbol|BEARING_LUBRICATION_FADE|
|symbol|SENSOR_CALIBRATION_DRIFT|
|symbol|HULL_MICROMETEORITE_DAMAGE|
|symbol|SPACE_DEBRIS_COLLISION|
|symbol|THERMAL_STRESS|
|symbol|VIBRATION_OVERLOAD|
|symbol|PRESSURE_DIFFERENTIAL_STRESS|
|symbol|ELECTROMAGNETIC_SURGE_EFFECTS|
|symbol|ATMOSPHERIC_ENTRY_HEAT|
|component|FRAME|
|component|REACTOR|
|component|ENGINE|

<h2 id="tocS_ShipCrew">ShipCrew</h2>
<!-- backwards compatibility -->
<a id="schemashipcrew"></a>
<a id="schema_ShipCrew"></a>
<a id="tocSshipcrew"></a>
<a id="tocsshipcrew"></a>

```json
{
  "current": 0,
  "required": 0,
  "capacity": 0,
  "rotation": "STRICT",
  "morale": 100,
  "wages": 0
}

```

The ship's crew service and maintain the ship's systems and equipment.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|current|integer|true|none|The current number of crew members on the ship.|
|required|integer|true|none|The minimum number of crew members required to maintain the ship.|
|capacity|integer|true|none|The maximum number of crew members the ship can support.|
|rotation|string|true|none|The rotation of crew shifts. A stricter shift improves the ship's performance. A more relaxed shift improves the crew's morale.|
|morale|integer|true|none|A rough measure of the crew's morale. A higher morale means the crew is happier and more productive. A lower morale means the ship is more prone to accidents.|
|wages|integer|true|none|The amount of credits per crew member paid per hour. Wages are paid when a ship docks at a civilized waypoint.|

#### Enumerated Values

|Property|Value|
|---|---|
|rotation|STRICT|
|rotation|RELAXED|

<h2 id="tocS_ShipEngine">ShipEngine</h2>
<!-- backwards compatibility -->
<a id="schemashipengine"></a>
<a id="schema_ShipEngine"></a>
<a id="tocSshipengine"></a>
<a id="tocsshipengine"></a>

```json
{
  "symbol": "ENGINE_IMPULSE_DRIVE_I",
  "name": "string",
  "description": "string",
  "condition": 1,
  "integrity": 1,
  "speed": 1,
  "requirements": {
    "power": 0,
    "crew": 0,
    "slots": 0
  }
}

```

The engine determines how quickly a ship travels between waypoints.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|The symbol of the engine.|
|name|string|true|none|The name of the engine.|
|description|string|true|none|The description of the engine.|
|condition|[ShipComponentCondition](#schemashipcomponentcondition)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|speed|integer|true|none|The speed stat of this engine. The higher the speed, the faster a ship can travel from one point to another. Reduces the time of arrival when navigating the ship.|
|requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|ENGINE_IMPULSE_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_I|
|symbol|ENGINE_ION_DRIVE_II|
|symbol|ENGINE_HYPER_DRIVE_I|

<h2 id="tocS_ShipFrame">ShipFrame</h2>
<!-- backwards compatibility -->
<a id="schemashipframe"></a>
<a id="schema_ShipFrame"></a>
<a id="tocSshipframe"></a>
<a id="tocsshipframe"></a>

```json
{
  "symbol": "FRAME_PROBE",
  "name": "string",
  "description": "string",
  "condition": 1,
  "integrity": 1,
  "moduleSlots": 0,
  "mountingPoints": 0,
  "fuelCapacity": 0,
  "requirements": {
    "power": 0,
    "crew": 0,
    "slots": 0
  }
}

```

The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|Symbol of the frame.|
|name|string|true|none|Name of the frame.|
|description|string|true|none|Description of the frame.|
|condition|[ShipComponentCondition](#schemashipcomponentcondition)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|moduleSlots|integer|true|none|The amount of slots that can be dedicated to modules installed in the ship. Each installed module take up a number of slots, and once there are no more slots, no new modules can be installed.|
|mountingPoints|integer|true|none|The amount of slots that can be dedicated to mounts installed in the ship. Each installed mount takes up a number of points, and once there are no more points remaining, no new mounts can be installed.|
|fuelCapacity|integer|true|none|The maximum amount of fuel that can be stored in this ship. When refueling, the ship will be refueled to this amount.|
|requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|FRAME_PROBE|
|symbol|FRAME_DRONE|
|symbol|FRAME_INTERCEPTOR|
|symbol|FRAME_RACER|
|symbol|FRAME_FIGHTER|
|symbol|FRAME_FRIGATE|
|symbol|FRAME_SHUTTLE|
|symbol|FRAME_EXPLORER|
|symbol|FRAME_MINER|
|symbol|FRAME_LIGHT_FREIGHTER|
|symbol|FRAME_HEAVY_FREIGHTER|
|symbol|FRAME_TRANSPORT|
|symbol|FRAME_DESTROYER|
|symbol|FRAME_CRUISER|
|symbol|FRAME_CARRIER|

<h2 id="tocS_ShipFuel">ShipFuel</h2>
<!-- backwards compatibility -->
<a id="schemashipfuel"></a>
<a id="schema_ShipFuel"></a>
<a id="tocSshipfuel"></a>
<a id="tocsshipfuel"></a>

```json
{
  "current": 0,
  "capacity": 0,
  "consumed": {
    "amount": 0,
    "timestamp": "2019-08-24T14:15:22Z"
  }
}

```

Details of the ship's fuel tanks including how much fuel was consumed during the last transit or action.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|current|integer|true|none|The current amount of fuel in the ship's tanks.|
|capacity|integer|true|none|The maximum amount of fuel the ship's tanks can hold.|
|consumed|object|false|none|An object that only shows up when an action has consumed fuel in the process. Shows the fuel consumption data.|
|» amount|integer|true|none|The amount of fuel consumed by the most recent transit or action.|
|» timestamp|string(date-time)|true|none|The time at which the fuel was consumed.|

<h2 id="tocS_ShipModificationTransaction">ShipModificationTransaction</h2>
<!-- backwards compatibility -->
<a id="schemashipmodificationtransaction"></a>
<a id="schema_ShipModificationTransaction"></a>
<a id="tocSshipmodificationtransaction"></a>
<a id="tocsshipmodificationtransaction"></a>

```json
{
  "waypointSymbol": "string",
  "shipSymbol": "string",
  "tradeSymbol": "string",
  "totalPrice": 0,
  "timestamp": "2019-08-24T14:15:22Z"
}

```

Result of a transaction for a ship modification, such as installing a mount or a module.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|waypointSymbol|string|true|none|The symbol of the waypoint where the transaction took place.|
|shipSymbol|string|true|none|The symbol of the ship that made the transaction.|
|tradeSymbol|string|true|none|The symbol of the trade good.|
|totalPrice|integer|true|none|The total price of the transaction.|
|timestamp|string(date-time)|true|none|The timestamp of the transaction.|

<h2 id="tocS_ShipModule">ShipModule</h2>
<!-- backwards compatibility -->
<a id="schemashipmodule"></a>
<a id="schema_ShipModule"></a>
<a id="tocSshipmodule"></a>
<a id="tocsshipmodule"></a>

```json
{
  "symbol": "MODULE_MINERAL_PROCESSOR_I",
  "capacity": 0,
  "range": 0,
  "name": "string",
  "description": "string",
  "requirements": {
    "power": 0,
    "crew": 0,
    "slots": 0
  }
}

```

A module can be installed in a ship and provides a set of capabilities such as storage space or quarters for crew. Module installations are permanent.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|The symbol of the module.|
|capacity|integer|false|none|Modules that provide capacity, such as cargo hold or crew quarters will show this value to denote how much of a bonus the module grants.|
|range|integer|false|none|Modules that have a range will such as a sensor array show this value to denote how far can the module reach with its capabilities.|
|name|string|true|none|Name of this module.|
|description|string|true|none|Description of this module.|
|requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|MODULE_MINERAL_PROCESSOR_I|
|symbol|MODULE_GAS_PROCESSOR_I|
|symbol|MODULE_CARGO_HOLD_I|
|symbol|MODULE_CARGO_HOLD_II|
|symbol|MODULE_CARGO_HOLD_III|
|symbol|MODULE_CREW_QUARTERS_I|
|symbol|MODULE_ENVOY_QUARTERS_I|
|symbol|MODULE_PASSENGER_CABIN_I|
|symbol|MODULE_MICRO_REFINERY_I|
|symbol|MODULE_ORE_REFINERY_I|
|symbol|MODULE_FUEL_REFINERY_I|
|symbol|MODULE_SCIENCE_LAB_I|
|symbol|MODULE_JUMP_DRIVE_I|
|symbol|MODULE_JUMP_DRIVE_II|
|symbol|MODULE_JUMP_DRIVE_III|
|symbol|MODULE_WARP_DRIVE_I|
|symbol|MODULE_WARP_DRIVE_II|
|symbol|MODULE_WARP_DRIVE_III|
|symbol|MODULE_SHIELD_GENERATOR_I|
|symbol|MODULE_SHIELD_GENERATOR_II|

<h2 id="tocS_ShipMount">ShipMount</h2>
<!-- backwards compatibility -->
<a id="schemashipmount"></a>
<a id="schema_ShipMount"></a>
<a id="tocSshipmount"></a>
<a id="tocsshipmount"></a>

```json
{
  "symbol": "MOUNT_GAS_SIPHON_I",
  "name": "string",
  "description": "string",
  "strength": 0,
  "deposits": [
    "QUARTZ_SAND"
  ],
  "requirements": {
    "power": 0,
    "crew": 0,
    "slots": 0
  }
}

```

A mount is installed on the exterier of a ship.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|Symbo of this mount.|
|name|string|true|none|Name of this mount.|
|description|string|false|none|Description of this mount.|
|strength|integer|false|none|Mounts that have this value, such as mining lasers, denote how powerful this mount's capabilities are.|
|deposits|[string]|false|none|Mounts that have this value denote what goods can be produced from using the mount.|
|requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|MOUNT_GAS_SIPHON_I|
|symbol|MOUNT_GAS_SIPHON_II|
|symbol|MOUNT_GAS_SIPHON_III|
|symbol|MOUNT_SURVEYOR_I|
|symbol|MOUNT_SURVEYOR_II|
|symbol|MOUNT_SURVEYOR_III|
|symbol|MOUNT_SENSOR_ARRAY_I|
|symbol|MOUNT_SENSOR_ARRAY_II|
|symbol|MOUNT_SENSOR_ARRAY_III|
|symbol|MOUNT_MINING_LASER_I|
|symbol|MOUNT_MINING_LASER_II|
|symbol|MOUNT_MINING_LASER_III|
|symbol|MOUNT_LASER_CANNON_I|
|symbol|MOUNT_MISSILE_LAUNCHER_I|
|symbol|MOUNT_TURRET_I|

<h2 id="tocS_ShipNav">ShipNav</h2>
<!-- backwards compatibility -->
<a id="schemashipnav"></a>
<a id="schema_ShipNav"></a>
<a id="tocSshipnav"></a>
<a id="tocsshipnav"></a>

```json
{
  "systemSymbol": "string",
  "waypointSymbol": "string",
  "route": {
    "destination": {
      "symbol": "string",
      "type": "PLANET",
      "systemSymbol": "string",
      "x": 0,
      "y": 0
    },
    "origin": {
      "symbol": "string",
      "type": "PLANET",
      "systemSymbol": "string",
      "x": 0,
      "y": 0
    },
    "departureTime": "2019-08-24T14:15:22Z",
    "arrival": "2019-08-24T14:15:22Z"
  },
  "status": "IN_TRANSIT",
  "flightMode": "DRIFT"
}

```

The navigation information of the ship.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|route|[ShipNavRoute](#schemashipnavroute)|true|none|The routing information for the ship's most recent transit or current location.|
|status|[ShipNavStatus](#schemashipnavstatus)|true|none|The current status of the ship|
|flightMode|[ShipNavFlightMode](#schemashipnavflightmode)|true|none|The ship's set speed when traveling between waypoints or systems.|

<h2 id="tocS_ShipNavFlightMode">ShipNavFlightMode</h2>
<!-- backwards compatibility -->
<a id="schemashipnavflightmode"></a>
<a id="schema_ShipNavFlightMode"></a>
<a id="tocSshipnavflightmode"></a>
<a id="tocsshipnavflightmode"></a>

```json
"DRIFT"

```

The ship's set speed when traveling between waypoints or systems.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The ship's set speed when traveling between waypoints or systems.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|DRIFT|
|*anonymous*|STEALTH|
|*anonymous*|CRUISE|
|*anonymous*|BURN|

<h2 id="tocS_ShipNavRoute">ShipNavRoute</h2>
<!-- backwards compatibility -->
<a id="schemashipnavroute"></a>
<a id="schema_ShipNavRoute"></a>
<a id="tocSshipnavroute"></a>
<a id="tocsshipnavroute"></a>

```json
{
  "destination": {
    "symbol": "string",
    "type": "PLANET",
    "systemSymbol": "string",
    "x": 0,
    "y": 0
  },
  "origin": {
    "symbol": "string",
    "type": "PLANET",
    "systemSymbol": "string",
    "x": 0,
    "y": 0
  },
  "departureTime": "2019-08-24T14:15:22Z",
  "arrival": "2019-08-24T14:15:22Z"
}

```

The routing information for the ship's most recent transit or current location.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|destination|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|origin|[ShipNavRouteWaypoint](#schemashipnavroutewaypoint)|true|none|The destination or departure of a ships nav route.|
|departureTime|string(date-time)|true|none|The date time of the ship's departure.|
|arrival|string(date-time)|true|none|The date time of the ship's arrival. If the ship is in-transit, this is the expected time of arrival.|

<h2 id="tocS_ShipNavRouteWaypoint">ShipNavRouteWaypoint</h2>
<!-- backwards compatibility -->
<a id="schemashipnavroutewaypoint"></a>
<a id="schema_ShipNavRouteWaypoint"></a>
<a id="tocSshipnavroutewaypoint"></a>
<a id="tocsshipnavroutewaypoint"></a>

```json
{
  "symbol": "string",
  "type": "PLANET",
  "systemSymbol": "string",
  "x": 0,
  "y": 0
}

```

The destination or departure of a ships nav route.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|The symbol of the waypoint.|
|type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|x|integer|true|none|Position in the universe in the x axis.|
|y|integer|true|none|Position in the universe in the y axis.|

<h2 id="tocS_ShipNavStatus">ShipNavStatus</h2>
<!-- backwards compatibility -->
<a id="schemashipnavstatus"></a>
<a id="schema_ShipNavStatus"></a>
<a id="tocSshipnavstatus"></a>
<a id="tocsshipnavstatus"></a>

```json
"IN_TRANSIT"

```

The current status of the ship

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The current status of the ship|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|IN_TRANSIT|
|*anonymous*|IN_ORBIT|
|*anonymous*|DOCKED|

<h2 id="tocS_ShipReactor">ShipReactor</h2>
<!-- backwards compatibility -->
<a id="schemashipreactor"></a>
<a id="schema_ShipReactor"></a>
<a id="tocSshipreactor"></a>
<a id="tocsshipreactor"></a>

```json
{
  "symbol": "REACTOR_SOLAR_I",
  "name": "string",
  "description": "string",
  "condition": 1,
  "integrity": 1,
  "powerOutput": 1,
  "requirements": {
    "power": 0,
    "crew": 0,
    "slots": 0
  }
}

```

The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|Symbol of the reactor.|
|name|string|true|none|Name of the reactor.|
|description|string|true|none|Description of the reactor.|
|condition|[ShipComponentCondition](#schemashipcomponentcondition)|true|none|The repairable condition of a component. A value of 0 indicates the component needs significant repairs, while a value of 1 indicates the component is in near perfect condition. As the condition of a component is repaired, the overall integrity of the component decreases.|
|integrity|[ShipComponentIntegrity](#schemashipcomponentintegrity)|true|none|The overall integrity of the component, which determines the performance of the component. A value of 0 indicates that the component is almost completely degraded, while a value of 1 indicates that the component is in near perfect condition. The integrity of the component is non-repairable, and represents permanent wear over time.|
|powerOutput|integer|true|none|The amount of power provided by this reactor. The more power a reactor provides to the ship, the lower the cooldown it gets when using a module or mount that taxes the ship's power.|
|requirements|[ShipRequirements](#schemashiprequirements)|true|none|The requirements for installation on a ship|

#### Enumerated Values

|Property|Value|
|---|---|
|symbol|REACTOR_SOLAR_I|
|symbol|REACTOR_FUSION_I|
|symbol|REACTOR_FISSION_I|
|symbol|REACTOR_CHEMICAL_I|
|symbol|REACTOR_ANTIMATTER_I|

<h2 id="tocS_ShipRegistration">ShipRegistration</h2>
<!-- backwards compatibility -->
<a id="schemashipregistration"></a>
<a id="schema_ShipRegistration"></a>
<a id="tocSshipregistration"></a>
<a id="tocsshipregistration"></a>

```json
{
  "name": "string",
  "factionSymbol": "string",
  "role": "FABRICATOR"
}

```

The public registration information of the ship

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|The agent's registered name of the ship|
|factionSymbol|string|true|none|The symbol of the faction the ship is registered with|
|role|[ShipRole](#schemashiprole)|true|none|The registered role of the ship|

<h2 id="tocS_ShipRequirements">ShipRequirements</h2>
<!-- backwards compatibility -->
<a id="schemashiprequirements"></a>
<a id="schema_ShipRequirements"></a>
<a id="tocSshiprequirements"></a>
<a id="tocsshiprequirements"></a>

```json
{
  "power": 0,
  "crew": 0,
  "slots": 0
}

```

The requirements for installation on a ship

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|power|integer|false|none|The amount of power required from the reactor.|
|crew|integer|false|none|The number of crew required for operation.|
|slots|integer|false|none|The number of module slots required for installation.|

<h2 id="tocS_ShipRole">ShipRole</h2>
<!-- backwards compatibility -->
<a id="schemashiprole"></a>
<a id="schema_ShipRole"></a>
<a id="tocSshiprole"></a>
<a id="tocsshiprole"></a>

```json
"FABRICATOR"

```

The registered role of the ship

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The registered role of the ship|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|FABRICATOR|
|*anonymous*|HARVESTER|
|*anonymous*|HAULER|
|*anonymous*|INTERCEPTOR|
|*anonymous*|EXCAVATOR|
|*anonymous*|TRANSPORT|
|*anonymous*|REPAIR|
|*anonymous*|SURVEYOR|
|*anonymous*|COMMAND|
|*anonymous*|CARRIER|
|*anonymous*|PATROL|
|*anonymous*|SATELLITE|
|*anonymous*|EXPLORER|
|*anonymous*|REFINERY|

<h2 id="tocS_ShipType">ShipType</h2>
<!-- backwards compatibility -->
<a id="schemashiptype"></a>
<a id="schema_ShipType"></a>
<a id="tocSshiptype"></a>
<a id="tocsshiptype"></a>

```json
"SHIP_PROBE"

```

Type of ship

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|Type of ship|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|SHIP_PROBE|
|*anonymous*|SHIP_MINING_DRONE|
|*anonymous*|SHIP_SIPHON_DRONE|
|*anonymous*|SHIP_INTERCEPTOR|
|*anonymous*|SHIP_LIGHT_HAULER|
|*anonymous*|SHIP_COMMAND_FRIGATE|
|*anonymous*|SHIP_EXPLORER|
|*anonymous*|SHIP_HEAVY_FREIGHTER|
|*anonymous*|SHIP_LIGHT_SHUTTLE|
|*anonymous*|SHIP_ORE_HOUND|
|*anonymous*|SHIP_REFINING_FREIGHTER|
|*anonymous*|SHIP_SURVEYOR|

<h2 id="tocS_Shipyard">Shipyard</h2>
<!-- backwards compatibility -->
<a id="schemashipyard"></a>
<a id="schema_Shipyard"></a>
<a id="tocSshipyard"></a>
<a id="tocsshipyard"></a>

```json
{
  "symbol": "string",
  "shipTypes": [
    {
      "type": "SHIP_PROBE"
    }
  ],
  "transactions": [
    {
      "waypointSymbol": "string",
      "shipSymbol": "string",
      "shipType": "string",
      "price": 0,
      "agentSymbol": "string",
      "timestamp": "2019-08-24T14:15:22Z"
    }
  ],
  "ships": [
    {
      "type": "SHIP_PROBE",
      "name": "string",
      "description": "string",
      "supply": "SCARCE",
      "activity": "WEAK",
      "purchasePrice": 0,
      "frame": {
        "symbol": "FRAME_PROBE",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "moduleSlots": 0,
        "mountingPoints": 0,
        "fuelCapacity": 0,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "reactor": {
        "symbol": "REACTOR_SOLAR_I",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "powerOutput": 1,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "engine": {
        "symbol": "ENGINE_IMPULSE_DRIVE_I",
        "name": "string",
        "description": "string",
        "condition": 1,
        "integrity": 1,
        "speed": 1,
        "requirements": {
          "power": 0,
          "crew": 0,
          "slots": 0
        }
      },
      "modules": [
        {
          "symbol": "MODULE_MINERAL_PROCESSOR_I",
          "capacity": 0,
          "range": 0,
          "name": "string",
          "description": "string",
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        }
      ],
      "mounts": [
        {
          "symbol": "MOUNT_GAS_SIPHON_I",
          "name": "string",
          "description": "string",
          "strength": 0,
          "deposits": [
            "QUARTZ_SAND"
          ],
          "requirements": {
            "power": 0,
            "crew": 0,
            "slots": 0
          }
        }
      ],
      "crew": {
        "required": 0,
        "capacity": 0
      }
    }
  ],
  "modificationsFee": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|The symbol of the shipyard. The symbol is the same as the waypoint where the shipyard is located.|
|shipTypes|[object]|true|none|The list of ship types available for purchase at this shipyard.|
|» type|[ShipType](#schemashiptype)|true|none|Type of ship|
|transactions|[[ShipyardTransaction](#schemashipyardtransaction)]|false|none|The list of recent transactions at this shipyard.|
|ships|[[ShipyardShip](#schemashipyardship)]|false|none|The ships that are currently available for purchase at the shipyard.|
|modificationsFee|integer|true|none|The fee to modify a ship at this shipyard. This includes installing or removing modules and mounts on a ship. In the case of mounts, the fee is a flat rate per mount. In the case of modules, the fee is per slot the module occupies.|

<h2 id="tocS_ShipyardShip">ShipyardShip</h2>
<!-- backwards compatibility -->
<a id="schemashipyardship"></a>
<a id="schema_ShipyardShip"></a>
<a id="tocSshipyardship"></a>
<a id="tocsshipyardship"></a>

```json
{
  "type": "SHIP_PROBE",
  "name": "string",
  "description": "string",
  "supply": "SCARCE",
  "activity": "WEAK",
  "purchasePrice": 0,
  "frame": {
    "symbol": "FRAME_PROBE",
    "name": "string",
    "description": "string",
    "condition": 1,
    "integrity": 1,
    "moduleSlots": 0,
    "mountingPoints": 0,
    "fuelCapacity": 0,
    "requirements": {
      "power": 0,
      "crew": 0,
      "slots": 0
    }
  },
  "reactor": {
    "symbol": "REACTOR_SOLAR_I",
    "name": "string",
    "description": "string",
    "condition": 1,
    "integrity": 1,
    "powerOutput": 1,
    "requirements": {
      "power": 0,
      "crew": 0,
      "slots": 0
    }
  },
  "engine": {
    "symbol": "ENGINE_IMPULSE_DRIVE_I",
    "name": "string",
    "description": "string",
    "condition": 1,
    "integrity": 1,
    "speed": 1,
    "requirements": {
      "power": 0,
      "crew": 0,
      "slots": 0
    }
  },
  "modules": [
    {
      "symbol": "MODULE_MINERAL_PROCESSOR_I",
      "capacity": 0,
      "range": 0,
      "name": "string",
      "description": "string",
      "requirements": {
        "power": 0,
        "crew": 0,
        "slots": 0
      }
    }
  ],
  "mounts": [
    {
      "symbol": "MOUNT_GAS_SIPHON_I",
      "name": "string",
      "description": "string",
      "strength": 0,
      "deposits": [
        "QUARTZ_SAND"
      ],
      "requirements": {
        "power": 0,
        "crew": 0,
        "slots": 0
      }
    }
  ],
  "crew": {
    "required": 0,
    "capacity": 0
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|[ShipType](#schemashiptype)|true|none|Type of ship|
|name|string|true|none|none|
|description|string|true|none|none|
|supply|[SupplyLevel](#schemasupplylevel)|true|none|The supply level of a trade good.|
|activity|[ActivityLevel](#schemaactivitylevel)|false|none|The activity level of a trade good. If the good is an import, this represents how strong consumption is. If the good is an export, this represents how strong the production is for the good. When activity is strong, consumption or production is near maximum capacity. When activity is weak, consumption or production is near minimum capacity.|
|purchasePrice|integer|true|none|none|
|frame|[ShipFrame](#schemashipframe)|true|none|The frame of the ship. The frame determines the number of modules and mounting points of the ship, as well as base fuel capacity. As the condition of the frame takes more wear, the ship will become more sluggish and less maneuverable.|
|reactor|[ShipReactor](#schemashipreactor)|true|none|The reactor of the ship. The reactor is responsible for powering the ship's systems and weapons.|
|engine|[ShipEngine](#schemashipengine)|true|none|The engine determines how quickly a ship travels between waypoints.|
|modules|[[ShipModule](#schemashipmodule)]|true|none|[A module can be installed in a ship and provides a set of capabilities such as storage space or quarters for crew. Module installations are permanent.]|
|mounts|[[ShipMount](#schemashipmount)]|true|none|[A mount is installed on the exterier of a ship.]|
|crew|object|true|none|none|
|» required|integer|true|none|none|
|» capacity|integer|true|none|none|

<h2 id="tocS_ShipyardTransaction">ShipyardTransaction</h2>
<!-- backwards compatibility -->
<a id="schemashipyardtransaction"></a>
<a id="schema_ShipyardTransaction"></a>
<a id="tocSshipyardtransaction"></a>
<a id="tocsshipyardtransaction"></a>

```json
{
  "waypointSymbol": "string",
  "shipSymbol": "string",
  "shipType": "string",
  "price": 0,
  "agentSymbol": "string",
  "timestamp": "2019-08-24T14:15:22Z"
}

```

Results of a transaction with a shipyard.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|waypointSymbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|shipSymbol|string|true|none|The symbol of the ship that was the subject of the transaction.|
|shipType|string|true|none|The symbol of the ship that was the subject of the transaction.|
|price|integer|true|none|The price of the transaction.|
|agentSymbol|string|true|none|The symbol of the agent that made the transaction.|
|timestamp|string(date-time)|true|none|The timestamp of the transaction.|

<h2 id="tocS_Siphon">Siphon</h2>
<!-- backwards compatibility -->
<a id="schemasiphon"></a>
<a id="schema_Siphon"></a>
<a id="tocSsiphon"></a>
<a id="tocssiphon"></a>

```json
{
  "shipSymbol": "string",
  "yield": {
    "symbol": "PRECIOUS_STONES",
    "units": 0
  }
}

```

Siphon details.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|shipSymbol|string|true|none|Symbol of the ship that executed the siphon.|
|yield|[SiphonYield](#schemasiphonyield)|true|none|A yield from the siphon operation.|

<h2 id="tocS_SiphonYield">SiphonYield</h2>
<!-- backwards compatibility -->
<a id="schemasiphonyield"></a>
<a id="schema_SiphonYield"></a>
<a id="tocSsiphonyield"></a>
<a id="tocssiphonyield"></a>

```json
{
  "symbol": "PRECIOUS_STONES",
  "units": 0
}

```

A yield from the siphon operation.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|units|integer|true|none|The number of units siphoned that were placed into the ship's cargo hold.|

<h2 id="tocS_SupplyLevel">SupplyLevel</h2>
<!-- backwards compatibility -->
<a id="schemasupplylevel"></a>
<a id="schema_SupplyLevel"></a>
<a id="tocSsupplylevel"></a>
<a id="tocssupplylevel"></a>

```json
"SCARCE"

```

The supply level of a trade good.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The supply level of a trade good.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|SCARCE|
|*anonymous*|LIMITED|
|*anonymous*|MODERATE|
|*anonymous*|HIGH|
|*anonymous*|ABUNDANT|

<h2 id="tocS_Survey">Survey</h2>
<!-- backwards compatibility -->
<a id="schemasurvey"></a>
<a id="schema_Survey"></a>
<a id="tocSsurvey"></a>
<a id="tocssurvey"></a>

```json
{
  "signature": "string",
  "symbol": "string",
  "deposits": [
    {
      "symbol": "string"
    }
  ],
  "expiration": "2019-08-24T14:15:22Z",
  "size": "SMALL"
}

```

A resource survey of a waypoint, detailing a specific extraction location and the types of resources that can be found there.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|signature|string|true|none|A unique signature for the location of this survey. This signature is verified when attempting an extraction using this survey.|
|symbol|string|true|none|The symbol of the waypoint that this survey is for.|
|deposits|[[SurveyDeposit](#schemasurveydeposit)]|true|none|A list of deposits that can be found at this location. A ship will extract one of these deposits when using this survey in an extraction request. If multiple deposits of the same type are present, the chance of extracting that deposit is increased.|
|expiration|string(date-time)|true|none|The date and time when the survey expires. After this date and time, the survey will no longer be available for extraction.|
|size|string|true|none|The size of the deposit. This value indicates how much can be extracted from the survey before it is exhausted.|

#### Enumerated Values

|Property|Value|
|---|---|
|size|SMALL|
|size|MODERATE|
|size|LARGE|

<h2 id="tocS_SurveyDeposit">SurveyDeposit</h2>
<!-- backwards compatibility -->
<a id="schemasurveydeposit"></a>
<a id="schema_SurveyDeposit"></a>
<a id="tocSsurveydeposit"></a>
<a id="tocssurveydeposit"></a>

```json
{
  "symbol": "string"
}

```

A surveyed deposit of a mineral or resource available for extraction.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|The symbol of the deposit.|

<h2 id="tocS_System">System</h2>
<!-- backwards compatibility -->
<a id="schemasystem"></a>
<a id="schema_System"></a>
<a id="tocSsystem"></a>
<a id="tocssystem"></a>

```json
{
  "symbol": "string",
  "sectorSymbol": "string",
  "type": "NEUTRON_STAR",
  "x": 0,
  "y": 0,
  "waypoints": [
    {
      "symbol": "string",
      "type": "PLANET",
      "x": 0,
      "y": 0,
      "orbitals": [
        {
          "symbol": "string"
        }
      ],
      "orbits": "string"
    }
  ],
  "factions": [
    {
      "symbol": "COSMIC"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|The symbol of the system.|
|sectorSymbol|string|true|none|The symbol of the sector.|
|type|[SystemType](#schemasystemtype)|true|none|The type of system.|
|x|integer|true|none|Relative position of the system in the sector in the x axis.|
|y|integer|true|none|Relative position of the system in the sector in the y axis.|
|waypoints|[[SystemWaypoint](#schemasystemwaypoint)]|true|none|Waypoints in this system.|
|factions|[[SystemFaction](#schemasystemfaction)]|true|none|Factions that control this system.|

<h2 id="tocS_SystemFaction">SystemFaction</h2>
<!-- backwards compatibility -->
<a id="schemasystemfaction"></a>
<a id="schema_SystemFaction"></a>
<a id="tocSsystemfaction"></a>
<a id="tocssystemfaction"></a>

```json
{
  "symbol": "COSMIC"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[FactionSymbol](#schemafactionsymbol)|true|none|The symbol of the faction.|

<h2 id="tocS_SystemSymbol">SystemSymbol</h2>
<!-- backwards compatibility -->
<a id="schemasystemsymbol"></a>
<a id="schema_SystemSymbol"></a>
<a id="tocSsystemsymbol"></a>
<a id="tocssystemsymbol"></a>

```json
"string"

```

The symbol of the system.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The symbol of the system.|

<h2 id="tocS_SystemType">SystemType</h2>
<!-- backwards compatibility -->
<a id="schemasystemtype"></a>
<a id="schema_SystemType"></a>
<a id="tocSsystemtype"></a>
<a id="tocssystemtype"></a>

```json
"NEUTRON_STAR"

```

The type of system.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The type of system.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|NEUTRON_STAR|
|*anonymous*|RED_STAR|
|*anonymous*|ORANGE_STAR|
|*anonymous*|BLUE_STAR|
|*anonymous*|YOUNG_STAR|
|*anonymous*|WHITE_DWARF|
|*anonymous*|BLACK_HOLE|
|*anonymous*|HYPERGIANT|
|*anonymous*|NEBULA|
|*anonymous*|UNSTABLE|

<h2 id="tocS_SystemWaypoint">SystemWaypoint</h2>
<!-- backwards compatibility -->
<a id="schemasystemwaypoint"></a>
<a id="schema_SystemWaypoint"></a>
<a id="tocSsystemwaypoint"></a>
<a id="tocssystemwaypoint"></a>

```json
{
  "symbol": "string",
  "type": "PLANET",
  "x": 0,
  "y": 0,
  "orbitals": [
    {
      "symbol": "string"
    }
  ],
  "orbits": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|x|integer|true|none|Relative position of the waypoint on the system's x axis. This is not an absolute position in the universe.|
|y|integer|true|none|Relative position of the waypoint on the system's y axis. This is not an absolute position in the universe.|
|orbitals|[[WaypointOrbital](#schemawaypointorbital)]|true|none|Waypoints that orbit this waypoint.|
|orbits|string|false|none|The symbol of the parent waypoint, if this waypoint is in orbit around another waypoint. Otherwise this value is undefined.|

<h2 id="tocS_TradeGood">TradeGood</h2>
<!-- backwards compatibility -->
<a id="schematradegood"></a>
<a id="schema_TradeGood"></a>
<a id="tocStradegood"></a>
<a id="tocstradegood"></a>

```json
{
  "symbol": "PRECIOUS_STONES",
  "name": "string",
  "description": "string"
}

```

A good that can be traded for other goods or currency.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[TradeSymbol](#schematradesymbol)|true|none|The good's symbol.|
|name|string|true|none|The name of the good.|
|description|string|true|none|The description of the good.|

<h2 id="tocS_TradeSymbol">TradeSymbol</h2>
<!-- backwards compatibility -->
<a id="schematradesymbol"></a>
<a id="schema_TradeSymbol"></a>
<a id="tocStradesymbol"></a>
<a id="tocstradesymbol"></a>

```json
"PRECIOUS_STONES"

```

The good's symbol.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The good's symbol.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|PRECIOUS_STONES|
|*anonymous*|QUARTZ_SAND|
|*anonymous*|SILICON_CRYSTALS|
|*anonymous*|AMMONIA_ICE|
|*anonymous*|LIQUID_HYDROGEN|
|*anonymous*|LIQUID_NITROGEN|
|*anonymous*|ICE_WATER|
|*anonymous*|EXOTIC_MATTER|
|*anonymous*|ADVANCED_CIRCUITRY|
|*anonymous*|GRAVITON_EMITTERS|
|*anonymous*|IRON|
|*anonymous*|IRON_ORE|
|*anonymous*|COPPER|
|*anonymous*|COPPER_ORE|
|*anonymous*|ALUMINUM|
|*anonymous*|ALUMINUM_ORE|
|*anonymous*|SILVER|
|*anonymous*|SILVER_ORE|
|*anonymous*|GOLD|
|*anonymous*|GOLD_ORE|
|*anonymous*|PLATINUM|
|*anonymous*|PLATINUM_ORE|
|*anonymous*|DIAMONDS|
|*anonymous*|URANITE|
|*anonymous*|URANITE_ORE|
|*anonymous*|MERITIUM|
|*anonymous*|MERITIUM_ORE|
|*anonymous*|HYDROCARBON|
|*anonymous*|ANTIMATTER|
|*anonymous*|FAB_MATS|
|*anonymous*|FERTILIZERS|
|*anonymous*|FABRICS|
|*anonymous*|FOOD|
|*anonymous*|JEWELRY|
|*anonymous*|MACHINERY|
|*anonymous*|FIREARMS|
|*anonymous*|ASSAULT_RIFLES|
|*anonymous*|MILITARY_EQUIPMENT|
|*anonymous*|EXPLOSIVES|
|*anonymous*|LAB_INSTRUMENTS|
|*anonymous*|AMMUNITION|
|*anonymous*|ELECTRONICS|
|*anonymous*|SHIP_PLATING|
|*anonymous*|SHIP_PARTS|
|*anonymous*|EQUIPMENT|
|*anonymous*|FUEL|
|*anonymous*|MEDICINE|
|*anonymous*|DRUGS|
|*anonymous*|CLOTHING|
|*anonymous*|MICROPROCESSORS|
|*anonymous*|PLASTICS|
|*anonymous*|POLYNUCLEOTIDES|
|*anonymous*|BIOCOMPOSITES|
|*anonymous*|QUANTUM_STABILIZERS|
|*anonymous*|NANOBOTS|
|*anonymous*|AI_MAINFRAMES|
|*anonymous*|QUANTUM_DRIVES|
|*anonymous*|ROBOTIC_DRONES|
|*anonymous*|CYBER_IMPLANTS|
|*anonymous*|GENE_THERAPEUTICS|
|*anonymous*|NEURAL_CHIPS|
|*anonymous*|MOOD_REGULATORS|
|*anonymous*|VIRAL_AGENTS|
|*anonymous*|MICRO_FUSION_GENERATORS|
|*anonymous*|SUPERGRAINS|
|*anonymous*|LASER_RIFLES|
|*anonymous*|HOLOGRAPHICS|
|*anonymous*|SHIP_SALVAGE|
|*anonymous*|RELIC_TECH|
|*anonymous*|NOVEL_LIFEFORMS|
|*anonymous*|BOTANICAL_SPECIMENS|
|*anonymous*|CULTURAL_ARTIFACTS|
|*anonymous*|FRAME_PROBE|
|*anonymous*|FRAME_DRONE|
|*anonymous*|FRAME_INTERCEPTOR|
|*anonymous*|FRAME_RACER|
|*anonymous*|FRAME_FIGHTER|
|*anonymous*|FRAME_FRIGATE|
|*anonymous*|FRAME_SHUTTLE|
|*anonymous*|FRAME_EXPLORER|
|*anonymous*|FRAME_MINER|
|*anonymous*|FRAME_LIGHT_FREIGHTER|
|*anonymous*|FRAME_HEAVY_FREIGHTER|
|*anonymous*|FRAME_TRANSPORT|
|*anonymous*|FRAME_DESTROYER|
|*anonymous*|FRAME_CRUISER|
|*anonymous*|FRAME_CARRIER|
|*anonymous*|REACTOR_SOLAR_I|
|*anonymous*|REACTOR_FUSION_I|
|*anonymous*|REACTOR_FISSION_I|
|*anonymous*|REACTOR_CHEMICAL_I|
|*anonymous*|REACTOR_ANTIMATTER_I|
|*anonymous*|ENGINE_IMPULSE_DRIVE_I|
|*anonymous*|ENGINE_ION_DRIVE_I|
|*anonymous*|ENGINE_ION_DRIVE_II|
|*anonymous*|ENGINE_HYPER_DRIVE_I|
|*anonymous*|MODULE_MINERAL_PROCESSOR_I|
|*anonymous*|MODULE_GAS_PROCESSOR_I|
|*anonymous*|MODULE_CARGO_HOLD_I|
|*anonymous*|MODULE_CARGO_HOLD_II|
|*anonymous*|MODULE_CARGO_HOLD_III|
|*anonymous*|MODULE_CREW_QUARTERS_I|
|*anonymous*|MODULE_ENVOY_QUARTERS_I|
|*anonymous*|MODULE_PASSENGER_CABIN_I|
|*anonymous*|MODULE_MICRO_REFINERY_I|
|*anonymous*|MODULE_SCIENCE_LAB_I|
|*anonymous*|MODULE_JUMP_DRIVE_I|
|*anonymous*|MODULE_JUMP_DRIVE_II|
|*anonymous*|MODULE_JUMP_DRIVE_III|
|*anonymous*|MODULE_WARP_DRIVE_I|
|*anonymous*|MODULE_WARP_DRIVE_II|
|*anonymous*|MODULE_WARP_DRIVE_III|
|*anonymous*|MODULE_SHIELD_GENERATOR_I|
|*anonymous*|MODULE_SHIELD_GENERATOR_II|
|*anonymous*|MODULE_ORE_REFINERY_I|
|*anonymous*|MODULE_FUEL_REFINERY_I|
|*anonymous*|MOUNT_GAS_SIPHON_I|
|*anonymous*|MOUNT_GAS_SIPHON_II|
|*anonymous*|MOUNT_GAS_SIPHON_III|
|*anonymous*|MOUNT_SURVEYOR_I|
|*anonymous*|MOUNT_SURVEYOR_II|
|*anonymous*|MOUNT_SURVEYOR_III|
|*anonymous*|MOUNT_SENSOR_ARRAY_I|
|*anonymous*|MOUNT_SENSOR_ARRAY_II|
|*anonymous*|MOUNT_SENSOR_ARRAY_III|
|*anonymous*|MOUNT_MINING_LASER_I|
|*anonymous*|MOUNT_MINING_LASER_II|
|*anonymous*|MOUNT_MINING_LASER_III|
|*anonymous*|MOUNT_LASER_CANNON_I|
|*anonymous*|MOUNT_MISSILE_LAUNCHER_I|
|*anonymous*|MOUNT_TURRET_I|
|*anonymous*|SHIP_PROBE|
|*anonymous*|SHIP_MINING_DRONE|
|*anonymous*|SHIP_SIPHON_DRONE|
|*anonymous*|SHIP_INTERCEPTOR|
|*anonymous*|SHIP_LIGHT_HAULER|
|*anonymous*|SHIP_COMMAND_FRIGATE|
|*anonymous*|SHIP_EXPLORER|
|*anonymous*|SHIP_HEAVY_FREIGHTER|
|*anonymous*|SHIP_LIGHT_SHUTTLE|
|*anonymous*|SHIP_ORE_HOUND|
|*anonymous*|SHIP_REFINING_FREIGHTER|
|*anonymous*|SHIP_SURVEYOR|

<h2 id="tocS_Waypoint">Waypoint</h2>
<!-- backwards compatibility -->
<a id="schemawaypoint"></a>
<a id="schema_Waypoint"></a>
<a id="tocSwaypoint"></a>
<a id="tocswaypoint"></a>

```json
{
  "symbol": "string",
  "type": "PLANET",
  "systemSymbol": "string",
  "x": 0,
  "y": 0,
  "orbitals": [
    {
      "symbol": "string"
    }
  ],
  "orbits": "string",
  "faction": {
    "symbol": "COSMIC"
  },
  "traits": [
    {
      "symbol": "UNCHARTED",
      "name": "string",
      "description": "string"
    }
  ],
  "modifiers": [
    {
      "symbol": "STRIPPED",
      "name": "string",
      "description": "string"
    }
  ],
  "chart": {
    "waypointSymbol": "string",
    "submittedBy": "string",
    "submittedOn": "2019-08-24T14:15:22Z"
  },
  "isUnderConstruction": true
}

```

A waypoint is a location that ships can travel to such as a Planet, Moon or Space Station.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[WaypointSymbol](#schemawaypointsymbol)|true|none|The symbol of the waypoint.|
|type|[WaypointType](#schemawaypointtype)|true|none|The type of waypoint.|
|systemSymbol|[SystemSymbol](#schemasystemsymbol)|true|none|The symbol of the system.|
|x|integer|true|none|Relative position of the waypoint on the system's x axis. This is not an absolute position in the universe.|
|y|integer|true|none|Relative position of the waypoint on the system's y axis. This is not an absolute position in the universe.|
|orbitals|[[WaypointOrbital](#schemawaypointorbital)]|true|none|Waypoints that orbit this waypoint.|
|orbits|string|false|none|The symbol of the parent waypoint, if this waypoint is in orbit around another waypoint. Otherwise this value is undefined.|
|faction|[WaypointFaction](#schemawaypointfaction)|false|none|The faction that controls the waypoint.|
|traits|[[WaypointTrait](#schemawaypointtrait)]|true|none|The traits of the waypoint.|
|modifiers|[[WaypointModifier](#schemawaypointmodifier)]|false|none|The modifiers of the waypoint.|
|chart|[Chart](#schemachart)|false|none|The chart of a system or waypoint, which makes the location visible to other agents.|
|isUnderConstruction|boolean|true|none|True if the waypoint is under construction.|

<h2 id="tocS_WaypointFaction">WaypointFaction</h2>
<!-- backwards compatibility -->
<a id="schemawaypointfaction"></a>
<a id="schema_WaypointFaction"></a>
<a id="tocSwaypointfaction"></a>
<a id="tocswaypointfaction"></a>

```json
{
  "symbol": "COSMIC"
}

```

The faction that controls the waypoint.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[FactionSymbol](#schemafactionsymbol)|true|none|The symbol of the faction.|

<h2 id="tocS_WaypointModifier">WaypointModifier</h2>
<!-- backwards compatibility -->
<a id="schemawaypointmodifier"></a>
<a id="schema_WaypointModifier"></a>
<a id="tocSwaypointmodifier"></a>
<a id="tocswaypointmodifier"></a>

```json
{
  "symbol": "STRIPPED",
  "name": "string",
  "description": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[WaypointModifierSymbol](#schemawaypointmodifiersymbol)|true|none|The unique identifier of the modifier.|
|name|string|true|none|The name of the trait.|
|description|string|true|none|A description of the trait.|

<h2 id="tocS_WaypointModifierSymbol">WaypointModifierSymbol</h2>
<!-- backwards compatibility -->
<a id="schemawaypointmodifiersymbol"></a>
<a id="schema_WaypointModifierSymbol"></a>
<a id="tocSwaypointmodifiersymbol"></a>
<a id="tocswaypointmodifiersymbol"></a>

```json
"STRIPPED"

```

The unique identifier of the modifier.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The unique identifier of the modifier.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|STRIPPED|
|*anonymous*|UNSTABLE|
|*anonymous*|RADIATION_LEAK|
|*anonymous*|CRITICAL_LIMIT|
|*anonymous*|CIVIL_UNREST|

<h2 id="tocS_WaypointOrbital">WaypointOrbital</h2>
<!-- backwards compatibility -->
<a id="schemawaypointorbital"></a>
<a id="schema_WaypointOrbital"></a>
<a id="tocSwaypointorbital"></a>
<a id="tocswaypointorbital"></a>

```json
{
  "symbol": "string"
}

```

An orbital is another waypoint that orbits a parent waypoint.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|string|true|none|The symbol of the orbiting waypoint.|

<h2 id="tocS_WaypointSymbol">WaypointSymbol</h2>
<!-- backwards compatibility -->
<a id="schemawaypointsymbol"></a>
<a id="schema_WaypointSymbol"></a>
<a id="tocSwaypointsymbol"></a>
<a id="tocswaypointsymbol"></a>

```json
"string"

```

The symbol of the waypoint.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The symbol of the waypoint.|

<h2 id="tocS_WaypointTrait">WaypointTrait</h2>
<!-- backwards compatibility -->
<a id="schemawaypointtrait"></a>
<a id="schema_WaypointTrait"></a>
<a id="tocSwaypointtrait"></a>
<a id="tocswaypointtrait"></a>

```json
{
  "symbol": "UNCHARTED",
  "name": "string",
  "description": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|symbol|[WaypointTraitSymbol](#schemawaypointtraitsymbol)|true|none|The unique identifier of the trait.|
|name|string|true|none|The name of the trait.|
|description|string|true|none|A description of the trait.|

<h2 id="tocS_WaypointTraitSymbol">WaypointTraitSymbol</h2>
<!-- backwards compatibility -->
<a id="schemawaypointtraitsymbol"></a>
<a id="schema_WaypointTraitSymbol"></a>
<a id="tocSwaypointtraitsymbol"></a>
<a id="tocswaypointtraitsymbol"></a>

```json
"UNCHARTED"

```

The unique identifier of the trait.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The unique identifier of the trait.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|UNCHARTED|
|*anonymous*|UNDER_CONSTRUCTION|
|*anonymous*|MARKETPLACE|
|*anonymous*|SHIPYARD|
|*anonymous*|OUTPOST|
|*anonymous*|SCATTERED_SETTLEMENTS|
|*anonymous*|SPRAWLING_CITIES|
|*anonymous*|MEGA_STRUCTURES|
|*anonymous*|PIRATE_BASE|
|*anonymous*|OVERCROWDED|
|*anonymous*|HIGH_TECH|
|*anonymous*|CORRUPT|
|*anonymous*|BUREAUCRATIC|
|*anonymous*|TRADING_HUB|
|*anonymous*|INDUSTRIAL|
|*anonymous*|BLACK_MARKET|
|*anonymous*|RESEARCH_FACILITY|
|*anonymous*|MILITARY_BASE|
|*anonymous*|SURVEILLANCE_OUTPOST|
|*anonymous*|EXPLORATION_OUTPOST|
|*anonymous*|MINERAL_DEPOSITS|
|*anonymous*|COMMON_METAL_DEPOSITS|
|*anonymous*|PRECIOUS_METAL_DEPOSITS|
|*anonymous*|RARE_METAL_DEPOSITS|
|*anonymous*|METHANE_POOLS|
|*anonymous*|ICE_CRYSTALS|
|*anonymous*|EXPLOSIVE_GASES|
|*anonymous*|STRONG_MAGNETOSPHERE|
|*anonymous*|VIBRANT_AURORAS|
|*anonymous*|SALT_FLATS|
|*anonymous*|CANYONS|
|*anonymous*|PERPETUAL_DAYLIGHT|
|*anonymous*|PERPETUAL_OVERCAST|
|*anonymous*|DRY_SEABEDS|
|*anonymous*|MAGMA_SEAS|
|*anonymous*|SUPERVOLCANOES|
|*anonymous*|ASH_CLOUDS|
|*anonymous*|VAST_RUINS|
|*anonymous*|MUTATED_FLORA|
|*anonymous*|TERRAFORMED|
|*anonymous*|EXTREME_TEMPERATURES|
|*anonymous*|EXTREME_PRESSURE|
|*anonymous*|DIVERSE_LIFE|
|*anonymous*|SCARCE_LIFE|
|*anonymous*|FOSSILS|
|*anonymous*|WEAK_GRAVITY|
|*anonymous*|STRONG_GRAVITY|
|*anonymous*|CRUSHING_GRAVITY|
|*anonymous*|TOXIC_ATMOSPHERE|
|*anonymous*|CORROSIVE_ATMOSPHERE|
|*anonymous*|BREATHABLE_ATMOSPHERE|
|*anonymous*|THIN_ATMOSPHERE|
|*anonymous*|JOVIAN|
|*anonymous*|ROCKY|
|*anonymous*|VOLCANIC|
|*anonymous*|FROZEN|
|*anonymous*|SWAMP|
|*anonymous*|BARREN|
|*anonymous*|TEMPERATE|
|*anonymous*|JUNGLE|
|*anonymous*|OCEAN|
|*anonymous*|RADIOACTIVE|
|*anonymous*|MICRO_GRAVITY_ANOMALIES|
|*anonymous*|DEBRIS_CLUSTER|
|*anonymous*|DEEP_CRATERS|
|*anonymous*|SHALLOW_CRATERS|
|*anonymous*|UNSTABLE_COMPOSITION|
|*anonymous*|HOLLOWED_INTERIOR|
|*anonymous*|STRIPPED|

<h2 id="tocS_WaypointType">WaypointType</h2>
<!-- backwards compatibility -->
<a id="schemawaypointtype"></a>
<a id="schema_WaypointType"></a>
<a id="tocSwaypointtype"></a>
<a id="tocswaypointtype"></a>

```json
"PLANET"

```

The type of waypoint.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|string|false|none|The type of waypoint.|

#### Enumerated Values

|Property|Value|
|---|---|
|*anonymous*|PLANET|
|*anonymous*|GAS_GIANT|
|*anonymous*|MOON|
|*anonymous*|ORBITAL_STATION|
|*anonymous*|JUMP_GATE|
|*anonymous*|ASTEROID_FIELD|
|*anonymous*|ASTEROID|
|*anonymous*|ENGINEERED_ASTEROID|
|*anonymous*|ASTEROID_BASE|
|*anonymous*|NEBULA|
|*anonymous*|DEBRIS_FIELD|
|*anonymous*|GRAVITY_WELL|
|*anonymous*|ARTIFICIAL_GRAVITY_WELL|
|*anonymous*|FUEL_STATION|

