import boigacustom    

__structure__ = {
  "id": "websocat",
  "name": "WebSockets",
  "blocks": [
    {
      "opcode": "startUpConnection",
      "blockType": "REPORTER",
      "text": "Connect to WebSocket [URL]",
      "arguments": {
        "URL": {
          "type": "STRING",
          "defaultValue": "ws://127.0.0.1:8080"
        }
      }
    },
    {
      "opcode": "isConnected",
      "blockType": "BOOLEAN",
      "text": "Connected to WebSocket [ID]",
      "arguments": {
        "ID": {
          "type": "NUMBER"
        }
      }
    },
    {
      "opcode": "messageQueue",
      "blockType": "BOOLEAN",
      "text": "Messages in queue for [ID]",
      "arguments": {
        "ID": {
          "type": "NUMBER"
        }
      }
    },
    {
      "opcode": "nextMessageInQueueText",
      "blockType": "REPORTER",
      "text": "Get next message in queue for [ID] as text",
      "arguments": {
        "ID": {
          "type": "NUMBER"
        }
      }
    },
    {
      "opcode": "nextMessageInQueueArray",
      "blockType": "REPORTER",
      "text": "Get next message in queue for [ID] as raw",
      "arguments": {
        "ID": {
          "type": "NUMBER"
        }
      }
    },
    {
      "opcode": "sendMessageText",
      "blockType": "COMMAND",
      "text": "Send text message to [ID] with contents of [DATA]",
      "arguments": {
        "ID": {
          "type": "NUMBER"
        },
        "DATA": {
          "type": "STRING",
          "defaultValue": "{\"hi\":\"Hello there!\"}"
        }
      }
    },
    {
      "opcode": "sendMessageArray",
      "blockType": "COMMAND",
      "text": "Send raw message to [ID] with contents of [DATA]",
      "arguments": {
        "ID": {
          "type": "NUMBER"
        },
        "DATA": {
          "type": "STRING"
        }
      }
    }
  ]
}

__structure__ = boigacustom.ExtensionBlockStructure(__structure__, True)

def start_up_connection(url):
  return __structure__.expression("startUpConnection", URL=url)

def send_message_text(connection_id, msg):
  return __structure__.statement("sendMessageText", ID=connection_id, DATA=msg)

def send_message_raw(connection_id, msg):
  return __structure__.statement("sendMessageArray", ID=connection_id, DATA=msg)

def is_connected(connection_id):
  return __structure__.expression("isConnected", ID=connection_id)

def message_in_queue(connection_id):
  return __structure__.expression("messageQueue", ID=connection_id)

def get_next_message_text(connection_id):
  return __structure__.expression("nextMessageInQueueText", ID=connection_id)

def get_next_message_raw(connection_id):
  return __structure__.expression("nextMessageInQueueArray", ID=connection_id)