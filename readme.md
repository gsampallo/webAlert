# WebAlert

Monitor service for URL that send push notification is service is down

## Configuration file
```
{
	"lastCheck": "2023-07-19 10:51:13",
	"notificationCount": 1,
	"maxNotificationCount": 3,
	"lastStatus":"DOWN"
}
```

## How to use
Modify run.sh change:
- the APIKEY_PUSBULLET variable environment for your own
- CONFIGURATION_FILE with the path for configuration.json file.

