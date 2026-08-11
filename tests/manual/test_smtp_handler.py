import logging

from logging_extended_handlers import BufferingSMTPHandler


def test_buffering_smt_handler():
    logger = logging.getLogger()
    logger.setLevel("DEBUG")
    buffered_mail_handler = BufferingSMTPHandler(
        mailhost="...",
        fromaddr="...",
        toaddrs=["..."],
        subject="Test BufferingSMTPHandler",
    )
    buffered_mail_handler.setLevel(logging.INFO)
    logger.addHandler(buffered_mail_handler)

    logging.debug("debug")
    logging.warning("warning")
    logging.info("info")
    logging.error("error")


if __name__ == "__main__":
    test_buffering_smt_handler()
