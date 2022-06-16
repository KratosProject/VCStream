"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int("14039017")
API_HASH = "68996f618f44f1a841f831419868b77a"
BOT_TOKEN = "5437746873:AAFf_C9uNN8sNz1pXCjXTCdPq7shbw1TouQ"
SESSION_STRING = "BQAo34C9ldBA2alpOtAsNMUY25ha3j0OXoTiGP03M-6nqRSuDn6CXhMSVmRA50esNsaTZ2nWb1xdhAwFAa2zG6ar8ZSPO6DJr6XEzHH_SyOStWy6mEVXXLwkgtAsdHSKsBbUNXXpiV_Zjzc5OM3nB8MKtWHkUtuP39PMsbEqiKxSyPjSl0-f9uDsA7VarQn-BO2UjC1iN5LCIhM06XkB7IYf1gELNvpNbO2ifJM2KNrfUWj2GCpPBcLsi-dNAdXw2pBJee4nyIxdImYE_1JL4XqumEZ9dQosr7u7wLVIHQPwxuxK-UNoIhgujI84OudaLHYBLX94LYU00hjtncHftfAAAAAUagWpUA"
SUPPORT_GROUP = "kratos_71"
UPDATES_CHANNEL = "KRATOS_PROJECT"
ASSISTANT_NAME = "KRATOS_71"
SUDO_USERS = int("1879939671")
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
