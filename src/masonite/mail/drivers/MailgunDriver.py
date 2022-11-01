import requests
from typing import TYPE_CHECKING, List

from ..Recipient import Recipient

if TYPE_CHECKING:
    from ...foundation import Application
    from ..MessageAttachment import MessageAttachment


class MailgunDriver:
    """Mailgun driver used to send e-mails from Mailgun service."""

    def __init__(self, application: "Application"):
        self.application = application
        self.options: dict = {}

    def set_options(self, options: dict) -> "MailgunDriver":
        self.options = options
        return self

    def get_mime_message(self) -> dict:
        data = {
            "from": self.options.get("from"),
            "to": Recipient(self.options.get("to")).header(),
            "subject": self.options.get("subject"),
            "h:Reply-To": self.options.get("reply_to"),
            "html": self.options.get("html_content"),
            "text": self.options.get("text_content"),
        }

        if self.options.get("cc"):
            data.update({"cc", self.options.get("cc")})
        if self.options.get("bcc"):
            data.update({"bcc", self.options.get("bcc")})
        if self.options.get("priority"):
            data.update({"h:X-Priority", self.options.get("priority")})
        if self.options.get("headers"):
            for header, value in self.options.get("headers").items():
                data.update({f"h:{header}", value})

        return data

    def get_attachments(self) -> "List[MessageAttachment]":
        files = []
        for attachment in self.options.get("attachments", []):
            files.append(("attachment", open(attachment.path, "rb")))

        return files

    def send(self) -> "requests.Response":
        domain = self.options["domain"]
        region = self.options.get("region", "us")
        secret = self.options["secret"]
        attachments = self.get_attachments()

        BASE_URL_BY_REGION = {
            "us": "https://api.mailgun.net/v3",
            "eu": "https://api.eu.mailgun.net/v3",
        }

        endpoint = BASE_URL_BY_REGION.get(region.lower())

        return requests.post(
            f"{endpoint}/{domain}/messages",
            auth=("api", secret),
            data=self.get_mime_message(),
            files=attachments,
        )
