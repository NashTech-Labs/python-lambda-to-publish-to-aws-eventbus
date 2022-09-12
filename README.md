# Python Lambda Function For Publishing Events To AWS EventBridge Event Bus

This script uses the boto3 library. This script publishes to the default event bus. If you have your own event bus then you can update the name here:

```
"EventBusName": "default",
```

Make sure your event bus rules(if any) matches with the entries.

<b>Note</b>: This script was made for Python `3.7`. May or may not need modifications for earlier or newer versions.