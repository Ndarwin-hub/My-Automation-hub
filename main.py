import os
import time
import logging
from datetime import datetime, timezone

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

RUN_INTERVAL_SECONDS = int(
    os.getenv("RUN_INTERVAL_SECONDS", "60")
)

APP_NAME = "Darwin-Automation-Agent"
VERSION = "0.1.0"


# ---------------------------------------------------------
# LOGGING
# ---------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(APP_NAME)


# ---------------------------------------------------------
# AGENT
# ---------------------------------------------------------

class AutomationAgent:

    def __init__(self):
        self.running = True
        self.cycle = 0

    def startup(self):
        logger.info("=" * 60)
        logger.info("%s starting", APP_NAME)
        logger.info("Version: %s", VERSION)
        logger.info("Scheduler interval: %s seconds", RUN_INTERVAL_SECONDS)
        logger.info("Trading execution: DISABLED")
        logger.info("Composio actions: NOT CONNECTED YET")
        logger.info("Video automation: NOT CONNECTED YET")
        logger.info("Social publishing: NOT CONNECTED YET")
        logger.info("=" * 60)

    def run_cycle(self):
        """
        One complete automation cycle.

        Future modules will be called from here.
        """

        self.cycle += 1

        now = datetime.now(timezone.utc).isoformat()

        logger.info(
            "Automation cycle #%s started | %s",
            self.cycle,
            now,
        )

        # -------------------------------------------------
        # FUTURE MODULES
        # -------------------------------------------------

        self.run_system_check()

        # Future:
        # self.run_ai_tasks()
        # self.run_composio_tasks()
        # self.run_trading_tasks()
        # self.run_video_tasks()
        # self.run_content_tasks()
        # self.run_social_tasks()
        # self.run_notification_tasks()

        logger.info(
            "Automation cycle #%s completed",
            self.cycle,
        )

    def run_system_check(self):
        """
        Basic health check.
        """

        logger.info("System health check: OK")

    def stop(self):
        self.running = False
        logger.info("Agent stopping...")


# ---------------------------------------------------------
# MAIN LOOP
# ---------------------------------------------------------

def main():

    agent = AutomationAgent()

    agent.startup()

    try:

        while agent.running:

            try:
                agent.run_cycle()

            except Exception as error:

                logger.exception(
                    "Error during automation cycle: %s",
                    error,
                )

                # Don't kill the entire 24/7 agent because
                # one task failed.
                logger.info(
                    "Agent will continue after the error."
                )

            time.sleep(RUN_INTERVAL_SECONDS)

    except KeyboardInterrupt:

        logger.info(
            "Shutdown requested by operating system."
        )

    finally:

        agent.stop()


if __name__ == "__main__":
    main()
