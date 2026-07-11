import sys
import os

AGENT_ROOT = os.path.dirname(os.path.abspath(__file__))

CUSTOM_PATH = os.path.join(AGENT_ROOT, 'custom')
if os.path.exists(CUSTOM_PATH) and CUSTOM_PATH not in sys.path:
    sys.path.insert(0, CUSTOM_PATH)

print(f"[Agent Init] Root: {AGENT_ROOT}")
print(f"[Agent Init] Custom loaded: {os.path.exists(CUSTOM_PATH)}")

from maa.agent.agent_server import AgentServer
from maa.toolkit import Toolkit

import my_action
import my_reco


def main():
    Toolkit.init_option("./")

    if len(sys.argv) < 2:
        print("Usage: python main.py <socket_id>")
        print("socket_id is provided by AgentIdentifier.")
        sys.exit(1)
        
    socket_id = sys.argv[-1]

    AgentServer.start_up(socket_id)
    AgentServer.join()
    AgentServer.shut_down()


if __name__ == "__main__":
    main()
