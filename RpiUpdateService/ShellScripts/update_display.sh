#!/bin/bash
export FIREBASE_PRIVATE_KEY=/home/lovebox/.keys/amanda-message-board-firebase-adminsdk-m1ybg-49c6cc3473.json
( cd /home/lovebox/software/love-box/RpiUpdateService/src && python3 update_display.py )
